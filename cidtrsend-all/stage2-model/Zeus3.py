
import sys
import os
import socket 
import thread       
import time
import sys

import threading
import logging

lock = threading.Lock()
lock2 = threading.Lock()

sst = socket.socket()      
sst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     
hostsst = socket.gethostname()  
portsst = 12243    

atu_reg=''
atu_reg2=''

def serve_stats(dmu,dmu2):
 global atu_reg
 global atu_reg2
 sst.bind((hostsst, portsst))        # Bind to the port
 sst.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = sst.accept()     # Establish connection with client.
   try:
    #atu_reg= 'Got connection from', addr
    msg = c.recv(1024)
    #print addr, ' >> ', msg
    msg = str(atu_reg+atu_reg2)
    c.send(msg);
   except:pass 
   
   
thread.start_new_thread(serve_stats,(0,0) )   

        
s = socket.socket()          
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
host = socket.gethostname()  
port = 51    

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('SemanticIndexer-Stage2')

class cjob:
 def __init__(self):
  self.finished=False
  self.ask=''
  self.response=[]

queue_jobs=[] # request from mind-net
queue_sockets=[]
 
 
Exit=False

def register_job(ask1):
 #lock
 global atu_reg
 with lock:
  jb=cjob()
  jb.ask=ask1
  queue_jobs.append(jb)
  jb=queue_jobs[len(queue_jobs)-1]
  print '[Zeus3]:Job.registered...'
  atu_reg='[Zeus3]:Job.registered...'
 #unclock
 return jb

 
def serve_process(csocket,queue_job,occup,indj):
  global atu_reg 
  try:
   print '[Zeus3]:Server.process.started....'
   atu_reg='[Zeus3]:Server.process.started....'
   csocket.send(queue_job.ask) 
   queue_job.ask=''
   response=csocket.recv(2048)
   #parse response
   queue_job.response=[]
   tmp=''
   for d in response:
    if d == '\n':
     queue_job.response.append(tmp)
    else:
     tmp+=d
   if tmp != '':
    queue_job.response.append(tmp)  
  except: pass  
  occup[0]=False
  queue_job.finished=True 
  print '[Zeus3]:end job:',indj
  atu_reg='[Zeus3]:end job:'+str(indj)
  
 
def serve_job(dumy1,dumy2): 
 global atu_reg
 global atu_reg2
 global queue_sockets
 print '[Zeus3]:Start serve_job...'
 atu_reg='[Zeus3]:Start serve_job...'
 while True:
     #lock
     with lock:
      found_Service=False
      ind=0
      ind_jb=0        
      for jbs in queue_sockets:
        [ocupped,socket]=jbs
        atu_reg2='jbs['+str(ind)+']:'+str(jbs)+',occuped:'+str(ocupped)
        ind_jb+=1
        if ocupped : continue
        found_Service=True  
        acnt=False    
        acnt_count=0        
        for jb in queue_jobs:          
          queue_jobs.remove(jb)
          print '[Zeus3]:Dispach. queue_jobs...',ind_jb
          atu_reg='[Zeus3]:Dispach. queue_jobs...'+str(ind_jb)
          print '[Zeus3]:Alloc quee_jobs from heroku...',ind_jb
          atu_reg='[Zeus3]:Alloc quee_jobs from heroku...'+str(ind_jb)
          queue_sockets[ind][0]=True
          #
          print '[Zeus3]:quee_jobs from heroku.found!!Start Thread to serve it..',ind_jb
          atu_reg='[Zeus3]:quee_jobs from heroku.found!!Start Thread to serve it..'+str(ind_jb)
          qsocket=queue_sockets[ind][1]
          # test the socket before
          try:
            qsocket.send('$$test$$') 
            r=qsocket.recv(1024)
            if r == '$$test$$': # ok
             print 'job_socket_ok....'
             atu_reg='job_socket_ok....'
            else:
             print 'Error job_socket.. get another(1)..'
             atu_reg='Error job_socket.. get another(1)..'
             acnt=True
             acnt_count=len(queue_sockets)
             qsocket.close()
             queue_sockets[ind][0]=False
             #queue_sockets.remove(jbs)
             del queue_sockets[ind]
             queue_jobs.append(jb)
             ind_jb-=1
             break              
          except:   
           print 'Error job_socket.. get another(2)..'  
           atu_reg='Error job_socket.. get another(2)..'  
           acnt=True
           acnt_count=len(queue_sockets)
           qsocket.close()
           queue_sockets[ind][0]=False
           #queue_sockets.remove(jbs)
           del queue_sockets[ind]
           ind_jb-=1
           queue_jobs.append(jb)
           break
          #
          thread.start_new_thread(serve_process,(qsocket,jb,queue_sockets[ind],ind_jb) )
          #
        if acnt: 
         print 'Remove jbs.'
         atu_reg='Remove jbs.['+str(len(queue_sockets))+']-ant:['+str(acnt_count)+']'
         atu_reg2=''         
         continue
        ind+=1        
      #if not found_Service and len(queue_sockets)>0:
      #  print 'Not found services:',queue_sockets
     #unlock
     time.sleep(.1)
 
register_purposes=[ [ ['1','2','3','4','5'] ,'simple-search-ask-aswer' ] ]  
 
def serve_reads_request(dmu,dmu2): # request from heroku
 global atu_reg
 global Exit
 global queue_sockets
 try:
  s.bind((host, port))        # Bind to the port
 except:
   log.exception("")
   Exit=True
 s.listen(50000)                 # Now wait for client connection.
 while True:
   c, addr = s.accept()     # Establish connection with client.
   # enviar o purpose para o requisitante, de acordo com o numero de registro
   #
   print '[Zeus3]:Accept heroku process..'
   atu_reg='[Zeus3]:Accept heroku process..'
   reg_serv=c.recv(50)
   print '[Zeus3]:Response for register:',reg_serv,''
   atu_reg='[Zeus3]:Response for register:'+str(reg_serv)+''
   for r in register_purposes:
    [addrs,lay]=r
    for a in addrs:
     if a==reg_serv:
       try:
         c.send(lay)
       except: pass  
       break
   #-==     
   print '[Zeus3]:Register new process heroku....:',addr,''
   atu_reg='[Zeus3]:Register new process heroku....:'+str(addr)+''
   queue_sockets.append([False,c])   
   
s2 = socket.socket()          
s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
host2 = socket.gethostname()  
port2 = 52    


def thread_serv_job(csocket,addr):
   global atu_reg
   print '[Zeus3]:Enter question from mind-net...'
   atu_reg='[Zeus3]:Enter question from mind-net...'
   try:
    msg = csocket.recv(1024)
    ret=register_job(msg)
    # wait for ok
    while not ret.finished:
      time.sleep(.1)
    #
    msg = str(ret.response[0])
    #
    csocket.send(msg);
   except:pass 
   try:
    csocket.close()   
   except: pass 
   print '[Zeus3]:finish question from mind-net...'
   atu_reg='[Zeus3]:finish question from mind-net...'


def serve_http_request(dmu,dmu2): # request from mind-net
 global atu_reg
 global Exit
 try:
  s2.bind((host2, port2))        # Bind to the port
 except:
  log.exception("")
  Exit=True 
 s2.listen(500000)                 # Now wait for client connection.
 while True:
   c, addr = s2.accept()     # Establish connection with client.
   thread.start_new_thread(thread_serv_job,(c,addr))   
   
thread.start_new_thread(serve_reads_request,(0,0) )
thread.start_new_thread(serve_http_request,(0,0) )
thread.start_new_thread(serve_job,(0,0))
 
import os, sys

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
  print '[Zeus3]:Shutdown...'
  atu_reg='[Zeus3]:Shutdown...'
  global Exit
  s.close()
  s2.close()
  sst.close()
  Exit=True


set_exit_handler(on_exit)
  
while not Exit:
  time.sleep(.5)


  