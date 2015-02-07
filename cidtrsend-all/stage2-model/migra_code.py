import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

print 'to connect.'

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

tb_py=pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_PY') 
tb_py_code=pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_CODE_PY') 

import conn

conn= conn.conn_mx

print 'Conected...'

def process_py():
 tb_py.truncate()
 tb_py_code.truncate()
 #
 r1=conn.sql("select OBJETO,USERNAME,TYP from DATA_BEHAVIOUR_PY") 
 for re in r1:
  obj=re[0]
  usr=re[1]
  TYP=re[2]
  params={"USERNAME":usr,"OBJETO":obj,"TYP":str(TYP)}
  tb_py.insert(obj,params)
 r1=conn.sql("select OBJETO,USERNAME,CODE from DATA_BEHAVIOUR_CODE_PY ")
 for re in r1:
  obj=re[0]
  usr=re[1]
  code=re[2].read()
  params={"USERNAME":usr,"OBJETO":obj,"CODE":code}
  tb_py_code.insert(obj,params)
  
  
process_py()  