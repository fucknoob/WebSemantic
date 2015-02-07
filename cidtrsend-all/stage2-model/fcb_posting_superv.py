
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

import conn
conn= conn.conn_mx

import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT-STAGE2')


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

import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa import index

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)
to_posting = pycassa.ColumnFamily(pool2, 'to_posting') 

cache_i=[]


def init_nums_i():
  global cache_i
  cache_i=[]
  cache_i2=[]
  processoc=1
  try:
     cursor = to_posting.get_range() 
     for ky,results in cursor:
        msg=results['msg']
        link=results['link']
        idx=results['indexed']
        results['indexed']='S'
        to_posting.insert(ky,results) # fecha a msg
        if idx == 'S': continue
        id_msg_to_coment=ky
        cache_i2.append([msg,link,id_msg_to_comment])
        if len(cache_i2)>=50:
          cache_i.append([cache_i2,processoc])
          cache_i2=[]
          processoc+=1
     if len(cache_i2) > 0 :     
          cache_i.append([cache_i2,processoc])
  
  except Exception,e : 
   log.exception("INIT_NUMS")
          
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
    for s22 in cache_i:
     [s2,processoc]=s22
     isd=[s2,processoc]
     cache_i.remove(s22)
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
     if len(isd) >= 50: break     
  except Exception, err2: 
   print 'Error collect:',err2
  a_lock.release()
  return isd
  

def process_cmd2(arr,processoc):
  s=''
  for [msg,link,id_msg_to_comment] in arr:
    a=id_msg_to_comment
    if s != '':
       s+=','
    s+=str(a)
  get_feeds(s,processoc)  

def get_feeds( space1 ,processo ):
 if True:
    try: 
     print 'Start process....'
     cmd='python fcb_posting.py '+processo+'  \''+ space1 + '\'' 
     os.system(cmd)
     #print cmd,'\n'
    except: pass 



def process_cmd(u,th,processoc ):
  process_cmd2(u,processoc)
  th.finished=True
    
def index_subs( ):
 if True :   
  usrs=[]
  for u in get_dist_u_next2():
   usrs.append(u)
  #================================ 
  ths=[]
  for [u,processoc] in usrs:
    try:    
     #=============================
     ths.append(thread_cntl())
     thread.start_new_thread(process_cmd,(u,ths[len(ths)-1],processoc) )
     #==  
    except:pass 
  while get_cache_s():
     try:
       for ths1 in ths:    
        if ths1.finished: 
          [u,processoc]=get_dist_u_next()
          ths.remove(ths1)
          ths.append(thread_cntl())
          thread.start_new_thread(process_cmd,(u,ths[len(ths)-1],processoc ) )
          #============================
     except: pass
     time.sleep(.5)    
   

if True:
 init_nums_i()
 index_subs() 

 
 
 
