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
 

 
def get_feeds(u2,itsc,itsc2,th,arrc1,uip,u3 ):
 if True:
     lpar=''  
     for u in u2:
      #print 'get.feed:',u     
      for s in u:
       if lpar != '': 
        lpar+=(',')
       lpar+=(s)
      #=============== 
      cmd='\"igor.moraes\" \"coll-usr-need\" \"'+lpar+'\" '
      #print 'return.cmd:',cmd 
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
  
def is_full():
 if len(arr_alpgs)<100:
  return False
 return global_index >= len(arr_alpgs)  
  
def prepare_data():
  global global_index
  global arr_alpgs
  global_index=0
  cach=web.get_range()
  md=0
  for ky,ch in cach:   
   if ch['indexed'] == 'S' or ch['indexed'] == 's': continue
   #
   ch['indexed']='S'
   web.insert(ky,ch)
   #
   arr_alpgs.append(ky)
   md+=1
   if md % 100: print 'CNT.md:',md
  
def get_pages2(i,a):
 global arr_alpgs
 global global_index
 arrpg=[]
 print 'Getting pages...'
 cach1=[]
 rec=False
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
   if len(cach1) >= 50:
    arrpg.append([cach1,cach1])
    
    return arrpg
    
    cach1=[]
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

def clear():
 global arr_alpgs
 global global_index
 arr_alpgs=[]
 global_index=0
 prepare_data()
  
def process_p(arrpg1,dm):
 print 'pages ok. init process ...'
 thst=[]
 indc=0
 for pg in arrpg1:
   u=pg
   uip=0
   return get_feeds(u,0,'',None,[],uip,u)
 
def get_pages():  
 #
 a1=get_pages2(1,1)
 #
 return process_p(a1,0 )
 #

prepare_data()

 
 
 