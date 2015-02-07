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
 
#python \wamp\www\neural\SemaIndexerStage3.py "igor.moraes" "Teste de usuario 285773736 interact-need-detector." "simple-search-ask-aswer2" "1" > kk.txt 
 
def get_feeds(u,itsc,itsc2,th,arrc1,uip,u2 ):
 if True:
     #=============== 
     cmd='\"igor.moraes\" \"'+u+'  interact-need-detector. \" \"simple-search-ask-aswer2\" \"1\" '
     return cmd

     

sys.path.append('./pycassa')
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
    
     
arr_alpgs=[]     
 
tb_object_3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 



def clear_tables():# limpar as tabelas para iniciar a indexacao 
 to_posting = pycassa.ColumnFamily(pool2, 'to_posting') 
 #======================
 to_posting.truncate()
 #======================
  
  
global_start=0
def get_pages(i,a):
 global arr_alpgs
 global global_start
 arrpg=[]
 print 'Getting pages...'
 cach1=[]
 rec=False
 if len(arr_alpgs)==0:
  cach=tb_object_3.get_range()
  for ky,ch in cach:
   arr_alpgs.append(ky)
   #===========
   #===========
   #if len(arr_alpgs)>50:  break
   #===========
   #===========
 idxkcnt=-1  
 for k in arr_alpgs:
  idxkcnt+=1
  if global_start > idxkcnt:
    continue
  global_start+=1 
  #################################
  id=k
  idu=0
  if id != '':
   if len(cach1) >= 50:
    arrpg.append([cach1,cach1])
    return arrpg 
    #cach1=[id]
   else:
    cach1.append(id)
  if len(arrpg) >= 5: 
   break
   rec=True
 if not rec: 
   if len(cach1)>0:
    arrpg.append([cach1,cach1])
  
 return arrpg
  
import time
from threading import Thread

class thread_cntl:
 def __init__(self):
  self.finished=False

import os  

def run_cmd(params,thr1):  
 cmd='python entry_SemaIndexerStage3.py ' + params
 print 'run:',cmd
 os.system(cmd)
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

  
clear_tables()  
 
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

 
 
 