import os
import sys
import time
sys.path.append('./pycassa')
 
 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

              


pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
w_cache3 = pycassa.ColumnFamily(pool2, 'web_cache3')

def ret(): 
 r=w_cache3.get_range(row_count=5)
 ind=0
 strt=''
 for k,r1 in r:
  strt+= '<br>'+k
  if ind > 10 : break
 return strt
 

r1=ret()
print r1
 

 
 
 
 