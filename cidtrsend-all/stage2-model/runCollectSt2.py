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
 
  
global_start=0
def get_pages(i,a):
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
     list=proxy.process_cmd('get_st1','','')
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
 cmd='python entry_SemaIndexerStage2.py ' + params
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

 
while True:  
 #
 a1=get_pages(1,1)
 #
 if len(a1) > 0 :
  process_p(a1,0 )
 else:
  print 'ZERO.TASK...' 
  time.sleep(30)
 #
 time.sleep(10)

 
 
 