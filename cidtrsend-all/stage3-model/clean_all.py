import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3') 
tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 
tb_object_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3') 


tb_object_dt3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
tb_object3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
tb_object_relaction3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 


tb_object.truncate()
tb_object3.truncate()

tb_object_dt.truncate()
tb_object_dt3.truncate()

tb_object_relaction.truncate()
tb_object_relaction3.truncate()



 