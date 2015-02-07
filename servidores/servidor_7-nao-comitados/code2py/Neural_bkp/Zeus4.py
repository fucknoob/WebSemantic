
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
portsst = 12244    

atu_reg=''
atu_reg2=''

refreshed=[]
to_refresh=False

def refresh_code(qsock):
 if not to_refresh: return False
 if qsock in refreshed:
   return False
 else:
   refreshed.append(qsock)
   return True   

def serve_stats(dmu,dmu2):
 global atu_reg
 global atu_reg2
 sst.bind((hostsst, portsst))        # Bind to the port
 sst.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = sst.accept()     # Establish connection with client.
   #atu_reg= 'Got connection from', addr
   msg = c.recv(1024)
   if msg != 'G' and msg=='refresh': to_refresh=True
   if msg != 'G' and msg=='clear': 
     to_refresh=False
     refreshed=[]
   #print addr, ' >> ', msg
   msg = str(atu_reg+atu_reg2)
   c.send(msg);


thread.start_new_thread(serve_stats,(0,0) )   
        
s = socket.socket()  
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
host = socket.gethostname()  
port = 61    


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
  print '[Zeus4]:Job.registered...'
  atu_reg='[Zeus4]:Job.registered...'
 #unclock
 return jb

class cthread_group :
  def __init__(self):
    self.finished=False
    self.socket=None
    self.response=''
 
import time
 
 
def serve_socket(thread_group_item,job):
   global atu_reg
   csocket=thread_group_item.socket
   startTT = time.clock ()
   print 'Start SUB-socket:',csocket,'[',job,']'
   atu_reg='Start SUB-socket:'+str(csocket)+'['+str(job)+']'
   csocket.send(job)    
   response=csocket.recv(2048)
   print 'job.returned:',csocket,'[',job,']:',time.clock ()-startTT
   atu_reg='job.returned:'+str(csocket)+'['+str(job)+']:'+str(time.clock ()-startTT)
   thread_group_item.response=response
   thread_group_item.finished=True
  
 
 
#csocket -> in multi-acess have a array of sockets 
def serve_process(csockets,queue_job,occup,indj):
  global atu_reg
  print '[Zeus4]:Server.process.started....'
  atu_reg='[Zeus4]:Server.process.started....'
  sockets_stack=[]
  for csocket in csockets:
   #parse response
   sockets_stack.append(cthread_group())
   sockets_stack[len(sockets_stack)-1].socket=csocket   
   thread.start_new_thread(serve_socket,(sockets_stack[len(sockets_stack)-1],queue_job.ask) )
  #=========================================  
  queue_job.ask=''
  ind_sk=0
  #for sk in sockets_stack:  
  while ind_sk < len(sockets_stack):
   sk = sockets_stack[ind_sk]
   if not sk.finished: 
     time.sleep(.1)
     continue
   response=sk.response  
   queue_job.response=[]
   tmp=''
   for d in response:
    if d == '\n':
     queue_job.response.append(tmp)
    else:
     tmp+=d
   if tmp != '':
    queue_job.response.append(tmp)  
   ind_sk+=1 
  #=========================================  
  occup[0]=False
  queue_job.finished=True 
  atu_reg='[Zeus4]:end job:'+str(indj)
  print '[Zeus4]:end job:',indj
  
 
def serve_job(dumy1,dumy2): 
 global queue_sockets
 global atu_reg
 global atu_reg2
 print '[Zeus4]:Start serve_job...'
 atu_reg='[Zeus4]:Start serve_job...'
 while True:
     #lock
     with lock:
      atu_reg2= 'Loop.queue_jobs:'+str(len(queue_jobs))+''
      found_Service=False
      ind=0
      ind_jb=0        
      for jbs in queue_sockets:
        [ocupped,socket,group]=jbs 
        ind_jb+=1
        atu_reg2='jbs:'+str(jbs)+',occuped:'+str(ocupped)
        if ocupped : continue
        found_Service=True     
        for jb in queue_jobs:          
          queue_jobs.remove(jb)
          print '[Zeus4]:Dispach. queue_jobs...',ind_jb
          atu_reg='[Zeus4]:Dispach. queue_jobs...'+str(ind_jb)
          print '[Zeus4]:Alloc quee_jobs from heroku...',ind_jb
          atu_reg='[Zeus4]:Alloc quee_jobs from heroku...'+str(ind_jb)
          queue_sockets[ind][0]=True
          #
          print '[Zeus4]:quee_jobs from heroku.found!!Start Thread to serve it..',ind_jb
          atu_reg='[Zeus4]:quee_jobs from heroku.found!!Start Thread to serve it..'+str(ind_jb)
          qsocket=queue_sockets[ind][1]
          # test socket before delegate job
          acnt=False
          try:
           for q in qsocket:
            # check if have atualization 
            srefr=refresh_code(q)
            if srefr:
             q.send('$$refresh$$')
             rq=q.recv(1024)
             if rq != '$$OK$$':
               r=''
             else:  
              q.send('$$test$$')
              r=q.recv(1024)
            else:            
             q.send('$$test$$')
             r=q.recv(1024)
            if r == '$$test$$':
             print 'job_socket_ok....'
             atu_reg='job_socket_ok....'
            else:
             raise Exception("job_socket_ERROR")
          except:
           try:
             for q in qsocket:
              q.close()
           except:
             pass
           queue_sockets.remove(jbs)
           acnt=True
           queue_jobs.append(jb)
           print 'Error job_socket.. get another(1)..'
           atu_reg='Error job_socket.. get another(1)..'
           ind_jb-=1           
          if acnt: 
           atu_reg2=''
           continue
          #
          thread.start_new_thread(serve_process,(qsocket,jb,queue_sockets[ind],ind_jb) )
          #
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
   print '[Zeus4]:Accept heroku process..'
   atu_reg='[Zeus4]:Accept heroku process..'
   reg_serv=c.recv(50)
   print '[Zeus4]:Response for register:',reg_serv,''
   atu_reg='[Zeus4]:Response for register:'+str(reg_serv)+''
   for r in register_purposes:
    [addrs,lay]=r
    for a in addrs:
     if a==reg_serv:
       c.send(lay)
       break
   #-==     
   print '[Zeus4]:Register new process heroku....:',addr,''
   atu_reg='[Zeus4]:Register new process heroku....:'+str(addr)+''
   fnd_type=False
   ind_t=0
   for q in queue_sockets:
    if q[2] == reg_serv:
      fnd_type=True  
      break
    ind_t+=1
   if fnd_type:
    queue_sockets[ind_t][1].append(c) 
   else:   
    queue_sockets.append([False,[c],reg_serv])   
   
s2 = socket.socket()          
s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
host2 = socket.gethostname()  
port2 = 62    


def thread_serv_job(csocket,addr):
   global atu_reg
   print '[Zeus4]:Enter question from mind-net...'
   atu_reg='[Zeus4]:Enter question from mind-net...'
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
    csocket.close()
   except : pass 
   print '[Zeus4]:finish question from mind-net...'
   atu_reg='[Zeus4]:finish question from mind-net...'


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
  global Exit
  print '[Zeus4]:Shutdown...'
  atu_reg='[Zeus4]:Shutdown...'
  s.close()
  s2.close()
  sst.close()
  Exit=True


set_exit_handler(on_exit)
  
while not Exit:
  time.sleep(.5)


  