
import time
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


import sys


pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'fcb_users')

def existe_usr(ID):
 try:
  tab2.get(ID)
  return True
 except:
  return False
    

def list():
 for key, columns in tab2.get_range():
    dt= columns[u'u_name']
    id= columns[u'id']
    print 'd:',dt,id
    break    
    
#list()
c=existe_usr('100000442067734')
print c
 



