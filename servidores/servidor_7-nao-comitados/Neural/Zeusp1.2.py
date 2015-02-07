#!/usr/bin/env python

#
#	The server that doesn't use the Name Server.
#

import sys, os
import time
 


import thread
a_lock = thread.allocate_lock() 


import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@127.0.0.1:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcbM=dbM['fcb_users1']

      
atu_reg='no.page'
print atu_reg
      
global_cnt=0   
restg=[]  

import socket 
import thread               
sr = socket.socket()          
hostr = socket.gethostname()  
portr = 12225

def serve_stats(dmu,dmu2):
 global atu_reg
 sr.bind((hostr, portr))        # Bind to the port
 sr.listen(20)                 # Now wait for client connection.
 while True:
   cr, addr = sr.accept()     # Establish connection with client.
   print 'Got connection from', addr
   msg = cr.recv(1024)
   #print addr, ' >> ', msg
   msg = str(atu_reg)
   cr.send(msg);
   
thread.start_new_thread(serve_stats,(0,0) )  
all_len=0


def init_cache():
 global global_cnt
 global restg
 global atu_reg
 global all_len
 global_cnt=0
 all_len=0
 restg=[]
 atu_reg='init.cache->global_cnt:'+str(global_cnt)+',len(restg):'+str(len(restg))
 print atu_reg
 #==================================================
 rest=fcbM.find({'indexed':'N'})
 atu_reg= 'Prepare cache:'
 print atu_reg
 indk1=1
 for cols in rest:
     if indk1 >= 1000000: break
     try:
        ids=cols['id']   
        kl=cols['_id']
        restg.append([kl,ids]) 
     except Exception,e:
         atu_reg= 'INFO:Error in ',e  
         print atu_reg         
     indk1+=1
     if indk1 % 1000 == 0: 
      print 'cnt:',indk1
     if indk1 % 1000 == 0: 
      atu_reg='cnt:'+str(indk1)
      print atu_reg
 atu_reg= 'restg:',len(restg),'->OK'
 print atu_reg
 
init_cache()


      
def get_dist_u_next():  
  isd=[]
  global all_len
  global global_cnt
  global restg
  atu_reg='next->restg:'+str(all_len)+',global_cnt:'+str(global_cnt)
  print atu_reg
  try:     
     try:
      if all_len == 0 : all_len=len(restg)
      if global_cnt >= all_len:
       # capturar mais cache
       init_cache()      
       return []
      [key,cols]=restg[global_cnt]
      global_cnt+=1
     except Exception,e:
      print 'null.get.next[',e,'].........................................................'
      atu_reg ='error.get.next['+str(e)+']'
      print atu_reg
      time.sleep(.5)
     if True:
        ids=cols   
        i=ids        
        isd=[ids,i]
  except Exception,e: 
   print 'error.get.next:',e
   atu_reg ='error.get.next2['+str(e)+']'  
   print atu_reg
  return isd

import simplejson as json 

contad=0

        
def get_pages(lname): 
        global atu_reg 
        global contad        
        atu_reg = 'acc.lock....' 
        print atu_reg        
        a_lock.acquire()
        contad+=1
        atu_reg = 'get.page.nxt.1  '+str(contad)        
        print atu_reg        
        c1=get_dist_u_next()  
        atu_reg = 'get.page.nxt.2  '+str(contad)        
        print atu_reg        
        c2=get_dist_u_next()  
        atu_reg = 'get.page.nxt.3  '+str(contad)        
        print atu_reg        
        c3=get_dist_u_next()  
        atu_reg = 'get.page.nxt.4  '+str(contad)        
        print atu_reg        
        c4=get_dist_u_next()  
        atu_reg = 'get.page.nxt.5  '+str(contad)        
        print atu_reg        
        c5=get_dist_u_next()  
        #         
        c=[c1,c2,c3,c4,c5]
        a_lock.release()
        return c
		
     
def process_request(socket,addrinfo):
   print 'Got connection from', addrinfo
   msg = socket.recv(1024)
   #print addr, ' >> ', msg
   pg=get_pages('')
   msg=json.dumps(pg)
   socket.send(msg);
 

            
s1 = socket.socket()          
host1 = socket.gethostname()  
port1 = 1019
# sr
def serve_pg():
 global atu_reg
 s1.bind((host1, port1))         # Bind to the port
 s1.listen(2000)                 # Now wait for client connection.
 while True:
   cr, addr = s1.accept()     # Establish connection with client.
   thread.start_new_thread(process_request,(cr,addr))


def set_exit_handler(func):
    if os.name == "nt":
        try:
            import win32api
            win32api.SetConsoleCtrlHandler(func, True)
        except ImportError:
            version = ".".join(map(str, sys.version_info[:2]))
            raise Exception("pywin32 not installed for Python " + version)
    else:
        import signal
        signal.signal(signal.SIGTERM, func)
        signal.signal(signal.SIGINT, func)
        Exit=True



def on_exit(a,b):
  global atu_reg 
  print '[Zeusp1.2]:Shutdown...'
  atu_reg='[Zeusp1.2]:Shutdown...'
  global Exit
  s1.close()
  sr.close()
  Exit=True


set_exit_handler(on_exit)
   
 
serve_pg() 
 
 
 
 
 
 
 
 
 
 
 

