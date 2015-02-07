import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
tb_object_dt1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT') 

r=tb_object_dt1.get('cenario_objs_importantes_ecomm1|1')
print r
print 'datach:',r['datach']

cl4 = index.create_index_expression(column_name="datach", value="$rule-destination-for-objects")
cl5=index.create_index_expression(column_name="topico", value="purp-destin")

clausec = index.create_index_clause([cl4,cl5],count=1000000)

resultSetk=tb_object_dt1.get_indexed_slices(clausec) 

#=============================================================
for ky,cols in resultSetk:
    obj=cols[u'object'] 
    print obj
print 'done:-----------------'    
#=============================================================    