#captura web_know

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=10000)

pool1 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

tb_web1 = pycassa.ColumnFamily(pool1, 'web_know') 
tb_web2 = pycassa.ColumnFamily(pool2, 'web_know2') 
tb_web2 = pycassa.ColumnFamily(pool2, 'web_know') 
#===
tb_web1.truncate()

rg1=tb_web2.get_range()
ind=0
for k,r in rg1:
  tb_web1.insert(k,r)
  print r
  ind+=1
  if ind % 1000 == 0: 
     print 'ind:',ind
  
  



