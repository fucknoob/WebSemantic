#coding: latin-1
# prepara os produtos para ser processados e gerar base de dados

import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa import index


pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'cache_products')
tab3 = pycassa.ColumnFamily(pool2, 'cache_links') # links temporarios
 
tab2.truncate()
tab3.truncate()