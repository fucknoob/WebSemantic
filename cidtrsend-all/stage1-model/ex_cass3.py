
import time
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


import sys

sys.path.append('/Neural')

import conn
conn= conn.conn_mx

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'fcb_users')


import socket 
import thread               
s = socket.socket()          
host = socket.gethostname()  
port = 12345                 
 
 
print 'Server started!'
print 'Waiting for clients...'

atu_reg=''

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



def get_rows(startc):
  cur=conn.sql("select user_name,id,u_name,i,indexed  from fcb_users where  i>= "+str(startc)+"  and rowno <= 50000 order by i")
  dels=[]
  count=1
  cs=0
  for re in cur:
   user_name=re[0]
   id=re[1]
   u_name=re[2]
   if u_name == None: u_name=''
   i=re[3]
   indexed=re[4]
   cs=i
   if count % 5000 == 0:   
    print 'read.row:',count
    atu_reg='read.row:'+str(count)
   #print  {'user_name':  user_name },{'id':id},{'u_name':u_name} 
   tab2.insert(str(i) , {'user_name':  user_name ,'id':id , 'u_name':u_name,'indexed':indexed})
   #if count >5 :  return 0
   count+=1
  return cs 
    

def list():
 for key, columns in tab2.get_range():
    dt= columns[u'u_name']
    id= columns[u'id']
    print 'd:',dt,id
    
    
thread.start_new_thread(serve_stats,(0,0) )

c2=1
while c2 > 0:
 print 'Next.step(50000)...{',c2,'}'
 atu_reg='Next.step(50000)...{',c2,'}'
 c22=get_rows(c2)
 c2=c22
 time.sleep(5)


#list()
 



