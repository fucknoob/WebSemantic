#!/usr/bin/env python

#
#	The server that doesn't use the Name Server.
#

import sys, os
import Pyro.core

import thread
import socket

from Pyro.errors import PyroError


a_lock = thread.allocate_lock() 


sst = socket.socket()          
sst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsst = socket.gethostname()  
portsst = 1295    
 
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
 

sst2 = socket.socket()          
sst2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsst2 = socket.gethostname()  
portsst2 = 1299    

ret_msg=''; 
 
def serve_stats2(dmu,dmu2):
 global ret_msg
 sst2.bind((hostsst2, portsst2))        # Bind to the port
 sst2.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = sst2.accept()     # Establish connection with client.
   #atu_reg= 'Got connection from', addr
   c.send(ret_msg)
 

thread.start_new_thread(serve_stats2,(0,0) )  

 
import PGrunCollect  
import PGrunCollectSt2
import PGrunCollectSt3
   
class layoutBean(Pyro.core.ObjBase):
   def __init__(self):
    	Pyro.core.ObjBase.__init__(self)
        
   def process_cmd(self,cmd,lname,userd):  
        global resets  
        global ret_msg        
        a_lock.acquire()
        if resets:
          print 'reset base......'
          PGrunCollect.clear()
          PGrunCollectSt2.global_start=0
          PGrunCollectSt3.global_start=0
          PGrunCollectSt2.arr_alpgs=[]
          PGrunCollectSt3.arr_alpgs=[]
          resets=False
        try:
            if cmd == 'get_page':
              cd= PGrunCollect.get_pages()
            if cmd == 'get_st1':
             cd = [] 
             if PGrunCollect.is_full():
              cd = PGrunCollectSt2.get_pgs()
            if cmd == 'get_st2':
             cd = [] 
             if PGrunCollectSt2.is_full():
              cd = PGrunCollectSt3.get_pgs()
        except:
          pass           
        ret_msg ='PGrunCollect:'+str(PGrunCollect.global_index)+',of:'+str(len(PGrunCollect.arr_alpgs))+'\n'
        ret_msg+='PGrunCollectSt2:'+str(PGrunCollectSt2.global_start)+',of:'+str(len(PGrunCollectSt2.arr_alpgs))+'\n'
        ret_msg+='PGrunCollectSt3:'+str(PGrunCollectSt3.global_start)+',of:'+str(len(PGrunCollectSt3.arr_alpgs))+'\n'
        a_lock.release()
        print 'prepare to return'
        return cd
        
   def get_layout(self,lname,userd):  
        c=self.process_cmd('get_layout',lname,userd)   	
        return c
	
Pyro.core.initServer()

daemon = Pyro.core.Daemon(port=28)
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

