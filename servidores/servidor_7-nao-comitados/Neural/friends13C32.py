
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
 
def c_reopen():
 a_lock.acquire()
 try:
  cur=conn.sql("select i,ids from to_reopen where rowno <= 500")
  dels=[]
  for re in cur:
   i=re[0]
   dels.append(i)
   ids=re[1]   
   reopen2(ids)
  conn.commit()
  for c in dels:
   conn.sql("delete from to_reopen where i="+str(c) )
  conn.commit() 
 except: 
  log.exception("Exception c_reopen:")
 a_lock.release() 

def reopen2(ids):      
  print 're-open:',ids
  try:
        conn.sql("update fcb_users set indexed='N' where ID=\'"+str(ids) +'\'' )
        conn.commit()   
  except: 
   print 'Eror reopen:'
   log.exception("")
 
def reopen(ids):      
  a_lock.acquire()
  print 're-open:',ids
  try:
        conn.sql("update fcb_users set indexed='N' where ID=\'"+str(ids) +'\'' )
        conn.commit()   
  except: 
   print 'Eror reopen:'
   log.exception("")
  a_lock.release()
      
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

       
c_reopen()     
     
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
thread.start_new_thread(index_subs,(1,1,18) )
thread.start_new_thread(index_subs,(1,1,19) )
thread.start_new_thread(index_subs,(1,1,20) )
thread.start_new_thread(index_subs,(1,1,21) )
thread.start_new_thread(index_subs,(1,1,22) )
thread.start_new_thread(index_subs,(1,1,23) )
thread.start_new_thread(index_subs,(1,1,24) )
thread.start_new_thread(index_subs,(1,1,25) )
thread.start_new_thread(index_subs,(1,1,26) )
thread.start_new_thread(index_subs,(1,1,27) )
thread.start_new_thread(index_subs,(1,1,28) )
thread.start_new_thread(index_subs,(1,1,29) )
thread.start_new_thread(index_subs,(1,1,30) )
thread.start_new_thread(index_subs,(1,1,31) )
thread.start_new_thread(index_subs,(1,1,32) )
thread.start_new_thread(index_subs,(1,1,33) )
thread.start_new_thread(index_subs,(1,1,34) )
thread.start_new_thread(index_subs,(1,1,35) )
thread.start_new_thread(index_subs,(1,1,36) )
thread.start_new_thread(index_subs,(1,1,37) )
thread.start_new_thread(index_subs,(1,1,38) )
thread.start_new_thread(index_subs,(1,1,39) )
thread.start_new_thread(index_subs,(1,1,40) )
thread.start_new_thread(index_subs,(1,1,41) )
thread.start_new_thread(index_subs,(1,1,42) )
thread.start_new_thread(index_subs,(1,1,43) )
thread.start_new_thread(index_subs,(1,1,44) )
thread.start_new_thread(index_subs,(1,1,45) )
thread.start_new_thread(index_subs,(1,1,46) )
thread.start_new_thread(index_subs,(1,1,47) )
thread.start_new_thread(index_subs,(1,1,48) )
thread.start_new_thread(index_subs,(1,1,49) )
thread.start_new_thread(index_subs,(1,1,50) )

thread.start_new_thread(index_subs,(1,1,51) )
thread.start_new_thread(index_subs,(1,1,52) )
thread.start_new_thread(index_subs,(1,1,53) )
thread.start_new_thread(index_subs,(1,1,54) )
thread.start_new_thread(index_subs,(1,1,55) )
thread.start_new_thread(index_subs,(1,1,56) )
thread.start_new_thread(index_subs,(1,1,57) )
thread.start_new_thread(index_subs,(1,1,58) )
thread.start_new_thread(index_subs,(1,1,59) )
thread.start_new_thread(index_subs,(1,1,60) )
thread.start_new_thread(index_subs,(1,1,61) )
thread.start_new_thread(index_subs,(1,1,62) )
thread.start_new_thread(index_subs,(1,1,63) )
thread.start_new_thread(index_subs,(1,1,64) )
thread.start_new_thread(index_subs,(1,1,65) )
thread.start_new_thread(index_subs,(1,1,66) )

thread.start_new_thread(index_subs,(1,1,67) )
thread.start_new_thread(index_subs,(1,1,68) )
thread.start_new_thread(index_subs,(1,1,69) )
thread.start_new_thread(index_subs,(1,1,70) )
thread.start_new_thread(index_subs,(1,1,71) )
thread.start_new_thread(index_subs,(1,1,72) )
thread.start_new_thread(index_subs,(1,1,73) )
thread.start_new_thread(index_subs,(1,1,74) )
thread.start_new_thread(index_subs,(1,1,75) )

thread.start_new_thread(index_subs,(1,1,76) )
thread.start_new_thread(index_subs,(1,1,77) )
thread.start_new_thread(index_subs,(1,1,78) )
thread.start_new_thread(index_subs,(1,1,79) )
thread.start_new_thread(index_subs,(1,1,80) )
thread.start_new_thread(index_subs,(1,1,81) )
thread.start_new_thread(index_subs,(1,1,82) )

thread.start_new_thread(index_subs,(1,1,83) )
thread.start_new_thread(index_subs,(1,1,84) )
thread.start_new_thread(index_subs,(1,1,85) )
thread.start_new_thread(index_subs,(1,1,86) )
thread.start_new_thread(index_subs,(1,1,87) )
thread.start_new_thread(index_subs,(1,1,88) )
thread.start_new_thread(index_subs,(1,1,89) )
thread.start_new_thread(index_subs,(1,1,90) )







while True:
 time.sleep(100) 
 