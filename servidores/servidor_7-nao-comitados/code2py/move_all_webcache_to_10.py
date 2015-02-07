import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
web=pycassa.ColumnFamily(pool2, 'web_cache1')
web10=pycassa.ColumnFamily(pool2, 'web_cache10')

idx=0
for ky,col in web.get_range():
	web10.insert(ky,col)
	web.remove(ky)
	idx+=1
	if idx % 10000 == 0: print 'idx:',idx

print 'Finished!!!'	