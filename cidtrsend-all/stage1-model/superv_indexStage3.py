#coding: latin-1

import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

import conn3
conn= conn3.conn_mx

import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT-STAGE1.SEMANTIC')


import thread
a_lock = thread.allocate_lock() 




class thread_cntl:
 def __init__(self):
  self.finished=False



ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 


cache_i=[]

usr2='igor.moraes'

def init_nums_i():
  global cache_i
  cache_i=[]
  cache_i2=[]
  try:
     sq="call web_cache3_idx_r2 ('"+usr2+"' ) "
     cursor = conn.sql (sq)
     for results in cursor:
        I=results[0]
        cache_i2.append(I)
        if len(cache_i2)>=1:
          cache_i.append(cache_i2)
          cache_i2=[]
     if len(cache_i2) >0:     
       cache_i.append(cache_i2)
       cache_i2=[]
           
  except Exception,e : 
   log.exception("INIT_NUMS")
   conn.rollback()
   return
  #==========================  
  conn.commit()  
  print 'Cache.len:',len(cache_i)  
          
def get_cache_s():
  s2=0
  a_lock.acquire()
  s2=len(cache_i)
  a_lock.release()
  return s2

def get_dist_u_next():
  a_lock.acquire()
  isd=[]
  try:
    for s2 in cache_i:
     isd=(s2)
     cache_i.remove(s2)
     break     
  except: pass
  a_lock.release()
  return isd

def get_dist_u_next2():
  a_lock.acquire()
  isd=[]
  closes=[]
  try:
    for s2 in cache_i:
     isd.append(s2)
     cache_i.remove(s2)
     if len(isd) >= 20: break     
  except Exception, err2: 
   print 'Error collect:',err2
  a_lock.release()
  return isd
  


def process_cmd2(arr):
  s=''
  for a in arr:
    if s != '':
       s+=','
    s+=str(a)
  get_feeds(s)  

def get_feeds( space1  ):
 if True:
    try: 
     print 'Start process....'
     #"igor.moraes" "Lucas santos interact-need-detector." "simple-search-ask-aswer" "1"
     cmd='python32 entry_SemaIndexerStage3.py \"igor.moraes\"   "'+space1+' interact-need-detector. "  "simple-search-ask-aswer"  "1"    '
     os.system(cmd)
     #print cmd
    except: pass 



def process_cmd(u,th ):
  process_cmd2(u)
  th.finished=True
    
def index_subs( ):
 have_before=len(cache_i)
 if True :   
  usrs=[]
  for u in get_dist_u_next2():
   usrs.append(u)
  #================================ 
  ths=[]
  for u in usrs:
    try:    
     #=============================
     ths.append(thread_cntl())
     thread.start_new_thread(process_cmd,(u,ths[len(ths)-1]) )
     #==  
    except:pass 
  first_time=True  
  while get_cache_s() or ( (have_before >0) and first_time ):
     first_time=False
     try:
       for ths1 in ths:    
        if ths1.finished: 
          u=get_dist_u_next()
          ths.remove(ths1)
          ths.append(thread_cntl())
          thread.start_new_thread(process_cmd,(u,ths[len(ths)-1] ) )
          #============================
     except: pass
     time.sleep(.5)    
    
    
if True:
 init_nums_i() 
 index_subs() 

 
 
 
     
     


