
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time


import logging
from StringIO import StringIO
import datetime
import time, datetime
#from multiprocessing import Process
from threading import Thread


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


import thread
a_lock = thread.allocate_lock() 


import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily


#pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=10000)
pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000)

to_reopen = pycassa.ColumnFamily(pool2, 'to_reopen')
fcb = pycassa.ColumnFamily(pool2, 'fcb_users')


class thread_cntl:
 def __init__(self):
  self.finished=False



ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 

 
def c_reopen():
 a_lock.acquire()
 try:
  cur=to_reopen.get_range()
  dels=[]
  for key,columns in cur: #i,ids
   i=columns[u'ids']
   dels.append(i)
   ids=columns[u'ids']
   reopen2(ids)
  for c in dels:
   to_reopen.remove(c)
 except: 
  log.exception("Exception c_reopen:")
 a_lock.release() 

def reopen2(ids):      
  print 're-open:',ids
  try:
        gt=fcb.get(ids)
        gt[u'indexed'] = 'N'
        fcb.insert(ids,gt)
  except: 
   print 'Eror reopen:'
   log.exception("")
 
def reopen(ids):      
  a_lock.acquire()
  print 're-open:',ids
  try:
        #conn.sql("update fcb_users set indexed='N' where ID=\'"+str(ids) +'\'' )
        gt=fcb.get(ids)
        gt[u'indexed'] = 'N'
        fcb.insert(ids,gt)
  except: 
   print 'Eror reopen:'
   log.exception("")
  a_lock.release()
      
global_cnt=0   
restg=[]   
exprc = index.create_index_expression(column_name='indexed', value='N')
clausec = index.create_index_clause([exprc],count=1000)
print 'Prepare cache:'
indk1=1
rest=fcb.get_indexed_slices(clausec)
for kl,cols in rest:
     try:
        ids=cols['id']   
        restg.append([kl,ids]) 
     except Exception,e:
         print 'INFO:Error in ',e    
     indk1+=1
     if indk1 % 500 == 0: print 'cnt:',indk1


print 'restg:',len(restg),'->OK'
      
def get_dist_u_next():
  a_lock.acquire()
  isd=[]
  global global_cnt
  global restg
  try:     
     try:
      if len(restg) <= global_cnt: 
       a_lock.release()
       return []
      [key,cols]=restg[global_cnt]
      global_cnt+=1
     except Exception,e:
      print 'null.get.next[',e,'].........................................................'
      time.sleep(.5)
     if True:
        ids=cols   
        i=ids        
        isd=[ids,i]
  except Exception,e: 
   print 'error.get.next:',e
   pass
  a_lock.release()
  return isd

def get_feeds(u,itsc,itsc2,th,arrc1,uip,u2,processo ):
 if True:
    try: 
     print 'Start process....'
     #get_feeds(sents[0],0,'',[],sents[1],sents[2],sents[3] )
     cmd='python32 friends13C321_c.py  '+str(u)+','+str(uip)+','+str(u2)+','+str(processo)+','
     os.system(cmd)
    except: pass 
    print 'Process:',' finished'   
    th.finished=True
  
  
def index_subs(j1,j2,processo=1):
 c=0
 if True :   
  indstr=1
  usrs=[]
  for u in get_dist_u_next():
   usrs.append(u)
   indstr+=1
  #================================ 
  ths=[]
  if len(usrs) == 0: return
  [u,uip] = usrs
  if True:
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
       if len(ths) == 0 : break
       for ths1 in ths:    
        if not ths1.finished:
         fnds_t=True        
        if ths1.finished:           
          ths.remove(ths1)
          rt1=get_dist_u_next()
          if len(rt1) == 0: continue
          [u,uip]=rt1
          ind_col+=1
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
     #
     # 
     time.sleep(2)
  print 'End thtread'   

       
c_reopen()  



thrs=[]
ind=1
while ind <= 90:
 process = Thread(target=index_subs, args=(1,1,ind))
 process.start()
 thrs.append(process)
 ind+=1

'''
thread.start_new_thread(index_subs,(1,1,90) )
'''

for th in thrs:
  th.join()

 
