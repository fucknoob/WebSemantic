#coding: latin-1
# insere usuarios avulsos


import os
import sys

sys.path.append('./pycassa')
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
    
     
arr_alpgs=[]     
 
tb_object_3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3')

rg=tb_object_3.get_range()
for ky,col in rg:
 if col['processed']=='E2':
  col['processed']='S2'
  tb_object_3.insert(ky,col) 
 
