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
 
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('SemanticIndexer-Stage3') 
 
processo=1 
 

 
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
#altready_run=False
def get_pages(i,a):
 #global altready_run  
 #if altready_run:
 # return []
 #altready_run=True 
 try:
     Pyro.core.initClient()
     objectName = 'layoutBean'
     hostname = '79.143.185.3'
     port = '28'
     print 'Creating proxy for object',objectName,' on ',hostname+':'+port
     if port:
        URI='PYROLOC://'+hostname+':'+port+'/'+objectName
     else:	
        URI='PYROLOC://'+hostname+'/'+objectName
     print 'The URI is',URI
     proxy=Pyro.core.getProxyForURI(URI) 
     #==
     list=proxy.process_cmd('get_st2','','')
     print 'List.getted!!'
     return list
 except:
  log.exception("ERROR==============" )
  time.sleep(2)
  return [] 
  
  
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
    # test -> no thread, producao->thread
    t = Thread(target=run_cmd, args=(params,thst[len(thst)-1]))
    t.start()
    #run_cmd(params,thst[len(thst)-1])
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
 if len(a1)>0:
  process_p(a1,0 )
 else:
  print 'ZERO.TASK...' 
  time.sleep(30)
 #
 if len(a1)>0:
  time.sleep(5)
 else:
  break 

 
 
 