import time

import socket 
import thread               
s = socket.socket()          
host = socket.gethostname()  
port = 91                 
 
s2 = socket.socket()          
host2 = socket.gethostname()  
port2 = 95
 
print 'Server started!'
print 'Waiting for clients...'

atu_reg='No-rec'
Exit=False

def serve_stats_r(dmu,dmu2):
 global atu_reg
 global Exit
 s2.bind((host2, port2))        # Bind to the port
 s2.listen(5)                 # Now wait for client connection.
 while not Exit:
   c2, addr2 = s2.accept()     # Establish connection with client.
   print 'Got connection from', addr2
   msg = c2.recv(10)
   #print addr, ' >> ', msg
   msg = str(atu_reg)
   c2.send(msg);


def serve_stats(dmu,dmu2):
 global atu_reg
 global Exit
 s.bind((host, port))            # Bind to the port
 s.listen(10000)                 # Now wait for client connection.
 while not Exit:
   try:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    msg = c.recv(10)
    #print addr, ' >> ', msg
    atu_reg='receive:'+msg+',from:'+str(addr)
    msg = 'Status'
    c.send(msg);
    print 'send response to:',addr
   except Exception,errc: 
     atu_reg='ERROR:'+str(errc)+',from:'+str(addr)
     pass      

   
thread.start_new_thread(serve_stats,(0,0) ) 
thread.start_new_thread(serve_stats_r,(0,0) ) 

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




def on_exit(a,b):
  print '[Zeus-ping]:Shutdown...'
  global Exit
  global s
  global s2
  s.close()
  s2.close()
  Exit=True


set_exit_handler(on_exit)
  
while not Exit:
  time.sleep(100)


