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
 

 

sys.path.append('./pycassa')
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
    
     
arr_alpgs=[]     
 
tb_object_3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 

import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('SemanticIndexer-Stage3') 
  
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
   try:
      processed=ch['processed']
   except:
      continue
   if processed !='S2' : continue 
   #
   ch['processed']='E2'
   tb_object_3.insert(ky,ch)
   #
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
   if len(cach1) >= 2:
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
  
def get_pgs():
 return  get_pages(1,1)
 
 
 
 