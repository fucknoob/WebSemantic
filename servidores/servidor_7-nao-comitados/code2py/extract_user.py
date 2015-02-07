#
import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

import socket 
import thread               
s = socket.socket()          
host = socket.gethostname()  
port = 12345    

atu_reg=''

def serve_stats(dmu,dmu2):
 global atu_reg
 s.bind((host, port))        # Bind to the port
 s.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = s.accept()     # Establish connection with client.
   #atu_reg= 'Got connection from', addr
   msg = c.recv(1024)
   #print addr, ' >> ', msg
   msg = str(atu_reg)
   c.send(msg);
   

atu_reg= 'Connect to cassandra...'
pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=10000)
fcb = pycassa.ColumnFamily(pool2, 'fcb_users2')

fcb2 = pycassa.ColumnFamily(pool2, 'fcb_users3')


thread.start_new_thread(serve_stats,(0,0) )

ind_files=1

total_collected=0


import os.path


def file_exists(pt):
 

while True:
 collected=[]
 rg=fcb.get_range()
 atu_reg= 'collect...'
 ind=0
 found_rows=False
 for ky,cols in rg:
  found_rows=True
  total_collected+=1
  collected.append([ky,cols]) 
  if len(collected) >= 1000000: break
  if ind % 10000 == 0 : 
    atu_reg='collect.rows:'+str(ind)+',of:'+str(total_collected) 
  ind+=1 
 #====================
 if not found_rows:
   atu_reg= 'FINISH'
   break
 atu_reg= 'save...of total:'+str(total_collected) 
 while True :
  if os.path.exists("/bkp_users/00"+str(ind_files)):
    ind_files+=1
  break  
 
 f=open("/bkp_users/00"+str(ind_files),"wr")  
 ind_files+=1
 # {'user_name':  user_name ,'id':ky , 'u_name':u_name,'indexed':'N'}) 
 ccn=0
 for ds in collected: 
  [ky,cols]=ds
  try:
   f.write(ky+"|"+cols['user_name']+"|"+cols['id']+"|"+cols['u_name']+"|"+cols['indexed']+"\n")
   fcb2.insert(ky,cols)
   fcb.remove(ky)
  except:
    pass  
  atu_reg='process:'+str(ccn)+',ky:'+ky
  ccn+=1
 f.close() 

