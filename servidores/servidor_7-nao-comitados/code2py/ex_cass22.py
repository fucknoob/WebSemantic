import time
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=1000)

tab2 = pycassa.ColumnFamily(pool2, 'web_know')


 

def count_tot2(): 
 count=0
 for key,columns in tab2.get_range():
    dt= columns[u'url']
    print 'DT:',dt
    count += 1
    if count > 10: break
 
    

count_tot2()  

