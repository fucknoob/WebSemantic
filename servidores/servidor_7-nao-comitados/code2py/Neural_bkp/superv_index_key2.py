
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
log = logging.getLogger('GET-FACEBOOK->COLLECT')


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

#import conn
#conn= conn.conn_mx
 
 
      
def get_dist_u_next():
  a_lock.acquire()
  isd=[]
  try:
     cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno < 2 ") 
     for results in cursor:
        ids=results[0]
        i=results[1]    
        isd=[ids,i]
        
        conn.sql("update fcb_users set indexed='S' where i= "+str(i))
        conn.commit()   
        print 'Close usr(1):',ids
        
        break
  except: pass
  a_lock.release()
  return isd

def get_dist_u_next2():
  a_lock.acquire()
  isd=[]
  closes=[]
  try:
     cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno <= 5 ") 
     isd=[]
     for results in cursor:
        ids=results[0]
        i=results[1]    
        isd.append([ids,i])
        closes.append([i,ids])
        #==============
        
     for [cl,u_nm] in closes:   
        conn.sql("update fcb_users set indexed='S' where i= "+str(cl))
        print 'Close usr(2):',u_nm
     conn.commit()   
     
     #==
  except Exception, err2: 
   print 'Error collect:',err2
  a_lock.release()
  return isd

def get_feeds(u,itsc,itsc2,th,arrc1,uip,u2,processo ):
 if True:
    try: 
     print 'Start process....'
     #get_feeds(sents[0],0,'',[],sents[1],sents[2],sents[3] )
     cmd='python32 friends13C321.py  '+str(u)+','+str(uip)+','+str(u2)+','+str(processo)+','
     os.system(cmd)
    except: pass 
    print 'Process:',' finished'   
    th.finished=True
  
  
def index_subs(j1,j2,processo=1):
 c=0
 if True :   
  indstr=1
  usrs=[]
  for u in get_dist_u_next2():
   usrs.append(u)
   indstr+=1
  #================================ 
  ths=[]
  for [u,uip] in usrs:
    print 'Process usr:',u
    try:    
     #=============================
     ths.append(thread_cntl())
     thread.start_new_thread(get_feeds,(u,0,'',ths[len(ths)-1],[],uip,u,processo ) )
     #==  
    except:pass 
  ind_col=0
  ikc=0
  while True:
     #print 'wait for pages...',len(ths)-ind_col
     try:
       fnds_t=False
       ind_col=0
       for ths1 in ths:    
        if not ths1.finished:
         fnds_t=True
        if ths1.finished: 
          [u,uip]=get_dist_u_next()
          ind_col+=1
          ths.remove(ths1)
          #============================
          if ikc > 50:
           ikc=0
           c_reopen()
          ikc+=1 
          print 'Process usr:',u
          ths.append(thread_cntl())
          thread.start_new_thread(get_feeds,(u,0,'',ths[len(ths)-1],[],uip,u,processo ) )
          #============================
     except: pass
     time.sleep(3)

       
     
     
thread.start_new_thread(index_subs,(1,1,1) )
thread.start_new_thread(index_subs,(1,1,2) )
thread.start_new_thread(index_subs,(1,1,3) )
thread.start_new_thread(index_subs,(1,1,4) )
thread.start_new_thread(index_subs,(1,1,5) )
thread.start_new_thread(index_subs,(1,1,6) )
thread.start_new_thread(index_subs,(1,1,7) )
thread.start_new_thread(index_subs,(1,1,8) )
thread.start_new_thread(index_subs,(1,1,9) )
thread.start_new_thread(index_subs,(1,1,10) )

thread.start_new_thread(index_subs,(1,1,11) )
thread.start_new_thread(index_subs,(1,1,12) )
thread.start_new_thread(index_subs,(1,1,13) )
thread.start_new_thread(index_subs,(1,1,14) )
thread.start_new_thread(index_subs,(1,1,15) )
thread.start_new_thread(index_subs,(1,1,16) )
thread.start_new_thread(index_subs,(1,1,17) )

while True:
 time.sleep(100) 
 