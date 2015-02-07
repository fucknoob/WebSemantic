import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

import os
import sys

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3') 
tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 
tb_object_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS') 


tb_object_dt3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
tb_object3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
tb_object_relaction3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 
to_publish = pycassa.ColumnFamily(pool2, 'to_posting2') 
to_publish2 = pycassa.ColumnFamily(pool2, 'to_posting') 


ts=input("1-Object3|2-Object3_1_4|3-object3_Dt|4-object3_1_4_dt|5-tb_object_relaction3|6-tb_object_relaction|7-to_posting:")
ts=str(ts)

if ts == "1":
 print 'get.SEMANTIC_OBJECT3...\n'
 rs=tb_object.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 
if ts == "2":
 print 'get.SEMANTIC_OBJECT3_1_4...\n'
 rs=tb_object3.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 
 
if ts == "3":
 print 'get.SEMANTIC_OBJECT_DT3...\n'
 rs=tb_object_dt.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 

if ts == "4":
 print 'get.SEMANTIC_OBJECT_DT3_1_4...\n'
 rs=tb_object_dt3.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 
 
if ts == "5":
 print 'get.tb_object_relaction3...\n'
 rs=tb_object_relaction3.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 
 
if ts == "6":
 print 'get.tb_object_relaction...\n'
 rs=tb_object_relaction.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 

if ts == "7":
 print 'get.to_publish...\n'
 rs=to_publish.get_range()
 c1=1
 for k,cl in rs:
  c1+=1
 print c1 


 