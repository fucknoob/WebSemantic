#create all indexes for cassandra 


import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

print  'connect to local....'
pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000)

print  'connect to remote....'
pool2r = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

w_cache1 = pycassa.ColumnFamily(pool2, 'web_cache3') 
w_cache2 = pycassa.ColumnFamily(pool2r, 'web_cache3') 


tb_object1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT') 
tb_object_dt1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT') 
tb_relaction1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS')


tb_object1r = pycassa.ColumnFamily(pool2r, 'SEMANTIC_OBJECT') 
tb_object_dt1r = pycassa.ColumnFamily(pool2r, 'SEMANTIC_OBJECT_DT') 
tb_relaction1r = pycassa.ColumnFamily(pool2r, 'SEMANTIC_RELACTIONS')


print 'clean.....'
tb_object1r.truncate()
tb_object_dt1r.truncate()
tb_relaction1r.truncate()

print 'posting objs.'
r1=tb_object1.get_range()
for ky1,cols1 in r1:
  tb_object1r.insert(ky1,cols1)   

print 'posting objs-dt.'
r1=tb_object_dt1.get_range()
for ky1,cols1 in r1:
  tb_object_dt1r.insert(ky1,cols1)   

print 'posting objs-rel.'
r1=tb_relaction1.get_range()
for ky1,cols1 in r1:
  tb_relaction1r.insert(ky1,cols1)   


print 'OK'