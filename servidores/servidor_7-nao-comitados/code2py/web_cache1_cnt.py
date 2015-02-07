import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

import os
import sys

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
web = pycassa.ColumnFamily(pool2, 'web_cache1') 


rs=web.get_range()
c1=1
for k,cl in rs:
 c1+=1
 if c1 % 1000==0:
  print 'c1:',c1
print c1 


 
