import time
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=1000)

tab2 = pycassa.ColumnFamily(pool2, 'fcb_users')


import socket 
import thread               
s = socket.socket()          
host = socket.gethostname()  
port = 12345                 
 
 
print 'Server started!'
print 'Waiting for clients...'

atu_reg='Start...'

def serve_stats(dmu,dmu2):
 global atu_reg
 s.bind((host, port))        # Bind to the port
 s.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   msg = c.recv(1024)
   #print addr, ' >> ', msg
   msg = str(atu_reg)
   c.send(msg);

   
thread.start_new_thread(serve_stats,(0,0) ) 

def ge_first_10(): 
 count=0
 for key,columns in tab2.get_range():
    dt= columns[u'url']
    print 'DT:',dt
    count += 1
    if count > 10: break
 

def get_cnt() :
 count=0
 global atu_reg
 for key,columns in tab2.get_range():
    count += 1
    if count % 100000 == 0 : print 'CNT.PARCIAL:',count
    if count % 500 == 0: 
      #print 'CNT.PARCIAL',count
      atu_reg='CNT.PARCIAL:'+str(count)
      time.sleep(.5)
 print 'CNT:', count    
    

get_cnt()  

