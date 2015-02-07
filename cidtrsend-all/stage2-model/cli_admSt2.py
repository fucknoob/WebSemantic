#!/usr/bin/env python

#
#	Client that doesn't use the Name Server. Uses PYROLOC:// URI.
#

import sys 
import Pyro.core
import threading
import time 


import thread
a_lock = thread.allocate_lock()  
 
 
 
import socket   
import simplejson as json
 
processo=1 
 
def get_feeds(u,itsc,itsc2,th,arrc1,uip,u2 ):
 if True:
     #=============== 
     cmd='\"igor.moraes\" \"'+u+'  interact-need-detector. \" \"client-ecomm-sugest-communic\" \"0\" '
     return cmd

     

sys.path.append('./pycassa')
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
web=pycassa.ColumnFamily(pool2, 'web_cache1')    
     
arr_alpgs=[]     
  
def clear():
 obj=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3')
 obj_dt=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3')
 #==
 obj3=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4')
 obj_dt3=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4')
 obj_rl3=pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4')
 obj_rl_3=pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3')
 #=
 obj_dt.truncate()
 obj.truncate()
 obj_dt3.truncate()
 obj3.truncate()
 obj_rl3.truncate()
 obj_rl_3.truncate()
  
def get_pages(i,a):
 global arr_alpgs
 arrpg=[]
 print 'Getting pages...'
 cach1=[]
 rec=False
 if len(arr_alpgs)==0:
  cach=web.get_range()
  for ky,ch in cach:
   arr_alpgs.append(ky)
   #===========
   #===========
   #if len(arr_alpgs)>2:  break
   #===========
   #===========
 for k in arr_alpgs:
  ch=web.get(k)
  id=ch['doc_id']
  idu=ch['id_usr']
  if id != '':
   if len(cach1) >= 5:
    arrpg.append([cach1,cach1])
    cach1=[id]
   else:
    cach1.append(id)
  if len(arrpg) >= 5: 
   break
   rec=True
 if not rec: 
   arrpg.append([cach1,cach1])
  
 return arrpg
  
import time
from threading import Thread

class thread_cntl:
 def __init__(self):
  self.finished=False

import os  

def run_cmd(params,thr1):  
 cmd='python entry_SemaIndexerStage2.py ' + params
 os.system(cmd)
 print 'run:',cmd
 thr1.finished=True
  
def process_p(arrpg1,dm):
 print 'pages ok. init process ...'
 thst=[]
 indc=0
 for pg in arrpg1:
   indc+=1
   [u,uip]=pg
   for su in u:
    thst.append(thread_cntl())
    params=get_feeds(su,0,'',None,[],uip,su)
    #==========================
    print 'Start process thread....',indc
    t = Thread(target=run_cmd, args=(params,thst[len(thst)-1]))
    t.start()

 while True:
  fndac=False
  for t in thst:
   if not t.finished: fndac=True
  time.sleep(.5)
  if not fndac: break  

 
while True:  
 #
 a1=get_pages(1,1)
 #
 process_p(a1,0 )
 #
 if len(a1)>0:
  time.sleep(.5)
 else:
  break 

 
 
 