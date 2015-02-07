#!/usr/bin/env python

#
#	The server that doesn't use the Name Server.
#

import sys, os
import Pyro.core
import DserviceC

import thread


from Pyro.errors import PyroError


a_lock = thread.allocate_lock() 

class layoutBean(Pyro.core.ObjBase):
   def __init__(self):
    	Pyro.core.ObjBase.__init__(self)
        
   def process_cmd(self,cmd,lname,userd):   
        a_lock.acquire()
        if cmd == 'get_pages':
         cd=c= DserviceC.get_pages() 
        a_lock.release()
        return cd        
    	
   def get_pages(self,lname,userd):  
        c=self.process_cmd('get_pages',lname,userd)   	
        return c
		
Pyro.core.initServer()

daemon = Pyro.core.Daemon(port=251)
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

