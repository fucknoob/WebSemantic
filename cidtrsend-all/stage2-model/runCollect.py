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
 
import logging
 


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('runCollect')

 
sys.path.append('./pycassa')
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
web=pycassa.ColumnFamily(pool2, 'web_cache1')
    
import umisc    
    
arr_alpgs=[]     

global_index=0  
  
  
import time
from threading import Thread

class thread_cntl:
 def __init__(self):
  self.finished=False

import os  

def run_cmd(): 
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
     list=proxy.process_cmd('get_page','','')
     print 'List.getted!!'
     list=umisc.trim(list)
     if len(list)<5:
      return 
     params=list 
     cmd='python entry_SemaIndexerStage1.py ' + params
     print cmd
     os.system(cmd)
 except:
  log.exception("ERROR==============" )
  time.sleep(2)
  
 
while True:  
 #
 run_cmd()
 #
 time.sleep(5) 


 
 
 