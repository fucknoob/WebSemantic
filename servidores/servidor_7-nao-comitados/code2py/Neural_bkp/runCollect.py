#!/usr/bin/env python

#
#	Client that doesn't use the Name Server. Uses PYROLOC:// URI.
#

import sys
import Pyro.core
import threading
import time 
import umisc

import thread
a_lock = thread.allocate_lock() 
 
 
 
import socket   
import simplejson as json
 

 
def get_feeds(u,itsc,itsc2,th,arrc1,uip,u2 ):
 if True:
     lpar=''     
     for s in u:
      if lpar != '': 
       lpar+=(',')
      lpar+=(s)
     #=============== 
     cmd='\"igor.moraes\" \"coll-usr-need\" \"'+lpar+'\" '
     return cmd

 
sys.path.append('./pycassa')
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
web=pycassa.ColumnFamily(pool2, 'web_cache1')
    
arr_alpgs=[]     

global_index=0  
  
def get_pages(i,a):
 global arr_alpgs
 global global_index
 arrpg=[]
 print 'Getting pages...'
 cach1=[]
 rec=False
 if len(arr_alpgs)==0:
  cach=web.get_range()
  for ky,ch in cach:
   arr_alpgs.append(ky)
   ###################
   ###################
   #if len(arr_alpgs)>200: break
   ###################
   ###################
 kindice=-1 
 for k in arr_alpgs:
  kindice+=1
  if kindice < global_index: 
   continue
  global_index+=1
  ch=web.get(k)
  id=ch['doc_id']
  idu=ch['id_usr']
  if id != '':
   if len(cach1) >= 30:
    arrpg.append([cach1,cach1])
    
    return arrpg
    
    cach1=[id]
   else:
    cach1.append(id)
  #====================  
  if len(arrpg) >= 1: 
   break
   rec=True
 if not rec: 
   if len(cach1)> 0:
    arrpg.append([cach1,cach1])
  
 return arrpg
  
import time
from threading import Thread

class thread_cntl:
 def __init__(self):
  self.finished=False

import os  

def run_cmd(params,thr1):  
 cmd='apy entry_SemaIndexerStage1.py ' + params
 os.system(cmd)
 #print cmd
 thr1.finished=True
  
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
  
  
def process_p(arrpg1,dm):
 print 'pages ok. init process ...'
 thst=[]
 indc=0
 for pg in arrpg1:
   indc+=1
   [u,uip]=pg
   if umisc.trim(u)=='': continue
   thst.append(thread_cntl())
   params=get_feeds(u,0,'',None,[],uip,u)
   #==========================
   t = Thread(target=run_cmd, args=(params,thst[len(thst)-1]))
   t.start()
  
 
 while True:
  fndac=False
  for t in thst:
   if not t.finished: fndac=True
  time.sleep(1)
  if not fndac: break  
 
clear() 
 
while True:  
 #
 a1=get_pages(1,1)
 #
 process_p(a1,0 )
 #
 if len(a1) > 0:
  time.sleep(5) 
 else:
  break


 
 
 