
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily


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

cache_i=[]

pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000)

def init_nums_i(): 
  global cache_i
  cache_i=[]
  cache_i2=[]
  try:
     w_cache = pycassa.ColumnFamily(pool2, 'web_cache')
     cnt_ctr=0
     for key,cols in w_cache.get_range():
        cnt_ctr+=1
        if cnt_ctr > 50000 : break
        #if cnt_ctr > 200 : break
        cache_i2.append(key)
        if len(cache_i2)>=50:
          cache_i.append(cache_i2)
          cache_i2=[]
  
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
     if len(isd) >= 3: break     
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
     cmd='python32 friends_ready_txt.py  \''+ space1 + '\'' 
     os.system(cmd)
     #print cmd,'\n'
    except: pass 



def process_cmd(u,th ):
  process_cmd2(u)
  th.finished=True
    
def index_subs( ):
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
  while get_cache_s():
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

 
 
 
