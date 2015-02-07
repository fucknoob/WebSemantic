#coding: latin-1
# insere usuarios avulsos


import os
import sys

sys.path.append('./pymongo')  
sys.path.append('./pycassa')
import pymongo
import thread


import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT-STAGE2')


import socket

sst = socket.socket()          
sst.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostsst = socket.gethostname()  
portsst = 1302   
 
 
def serve_stats(dmu,dmu2):
 sst.bind((hostsst, portsst))        # Bind to the port
 sst.listen(5)                 # Now wait for client connection.
 while True:
   c, addr = sst.accept()     # Establish connection with client.
   try:
    msg2 = c.recv(1024)
    msg=cnt(msg2,c)
   except:
    log.exception("_____")
   c.send('TTTC2')   
 
thread.start_new_thread(serve_stats,(0,0) ) 


import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
web1=pycassa.ColumnFamily(pool2, 'web_cache1')


def cnt(incp,sock):
 c=sock
 if incp == '1':
  MONGO_URL='mongodb://mdnet1:acc159753@91.205.172.85:27017/mdnet'
  c.send('connect to mongo...\n')
  connM = pymongo.Connection(MONGO_URL) 
  dbM=connM.mdnet
  us=dbM['fcb_users1']
 #=========== 
 web=pycassa.ColumnFamily(pool2,'web_cache1')
 ob=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3')
 obdt=pycassa.ColumnFamily(pool2,'SEMANTIC_OBJECT_DT3')
 ob3=pycassa.ColumnFamily(pool2,'SEMANTIC_OBJECT3_1_4')
 obdt3=pycassa.ColumnFamily(pool2,'SEMANTIC_OBJECT_DT3_1_4')
 to_posting = pycassa.ColumnFamily(pool2, 'to_posting')
 c.send('run option ...'+str(incp)+'\n')
 if str(incp)=='1':
  r=web.get_range()
  r1=0
  rcount=0
  rc=0
  for k,cl in r:
   if cl["processed"]=="S":
    r1+=1
   if cl["indexed"]=="S":
    rc+=1
   rcount+=1 
  c.send( 'web->all:'+str(rcount)+',processed:'+str(r1)+'indexed:'+str(rc)+'\n' )
  #===================================
  r2=us.find({"indexed":"S"}).count()
  f2=us.find({"indexed":"F"}).count()
  r3=us.find({"indexed":"C"}).count()
  r4=us.find({"indexed":"H"}).count()
  #======================================
  c.send( 'all.usr:'+str(us.count())+'\n')
  c.send( 'f2:'+str(f2)+'\n')
  c.send( 'st1:'+str(r2)+'\n')
  c.send( 'st1-passive:'+str(r3)+'\n')
  c.send( 'st2:'+str(r4)+'\n' )

 ob_count=0
 obdt_count=0
 ob3_count=0
 obdt3_count=0
 c.send('run cassandra get_Range...'+'\n')
 for ky,col in ob.get_range():
  ob_count+=1

 c.send( 'objs3:'+str(ob_count)+'\n')

 if str(incp)=='1' or str(incp)=='2':  
  for ky,col in obdt.get_range():
   obdt_count+=1
  c.send( 'objs3.dt:'+str(obdt_count)+'\n' )
 
 for ky,col in ob3.get_range():
  ob3_count+=1

 c.send( 'objs3_1_4:'+str(ob3_count) +'\n')
  
 if str(incp)=='1' or str(incp)=='2':  
  for ky,col in obdt3.get_range():
   obdt3_count+=1
  c.send( 'objs3_1_4.dt:'+str(obdt3_count) +'\n')
 
 to_posting_cnt=0 
 for ky,col in to_posting.get_range(): 
  to_posting_cnt+=1
 
 c.send( 'to_posting:'+str(to_posting_cnt) )
 
 web=pycassa.ColumnFamily(pool2, 'web_cache1')
    
 cnt1=0
 r=web.get_range()
 for k,cols in r:
  cnt1+=1
 
 c.send( 'web_cache1.count:'+str(cnt1)+'\n' )
 
 
import time

while True:
 time.sleep(100) 
 
 
 
 
 