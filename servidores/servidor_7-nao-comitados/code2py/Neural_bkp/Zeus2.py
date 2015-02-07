#!/usr/bin/env python

#
#	The server that doesn't use the Name Server.
#

import sys, os
import Pyro.core
import Dservice2 as Dservice

import thread
import socket

from Pyro.errors import PyroError


a_lock = thread.allocate_lock() 


sst = socket.socket()          
sst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsst = socket.gethostname()  
portsst = 1294    
 
resets=False
 
def serve_stats(dmu,dmu2):
 global resets
 sst.bind((hostsst, portsst))        # Bind to the port
 sst.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = sst.accept()     # Establish connection with client.
   #atu_reg= 'Got connection from', addr
   resets=True


thread.start_new_thread(serve_stats,(0,0) )    
   
class layoutBean(Pyro.core.ObjBase):
   def __init__(self):
    	Pyro.core.ObjBase.__init__(self)
        
   def process_cmd(self,cmd,lname,userd):  
        global resets   
        a_lock.acquire()
        if resets:
          print 'reset base......'
          Dservice.init_base()
          resets=False
        if cmd == 'get_layout':
         #print 'get.layout...'
         cd=c= Dservice.get_fuzzy(lname,userd) 
        if cmd == 'get_pages':
         #cd=c= Dservice.get_pages(lname,userd) 
         pass
        a_lock.release()
        return cd
        
   def get_layout(self,lname,userd):  
        c=self.process_cmd('get_layout',lname,userd)   	
        return c
   ''' 	
   def get_pages(self,lname,userd):  
        c=self.process_cmd('get_pages',lname,userd)   	
        return c
   '''		
Pyro.core.initServer()

daemon = Pyro.core.Daemon(port=26)
print
print 'The Pyro Deamon is running on ',daemon.hostname+':'+str(daemon.port)
print '(you may need this info for the client to connect to)'
print

objectName='layoutBean'

#uri=daemon.connect(layoutBean(),objectName)

object=Pyro.core.ObjBase()  # delegate approach
object.delegateTo(layoutBean())

uri=daemon.connect(object,objectName)

# enter the service loop.
print 'layoutBean is ready for customers.'
print 'Object name is:',objectName
print 'The URI is: ',uri

daemon.requestLoop()

