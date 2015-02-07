from pycassa.system_manager import *

print 'Connect..'
#=============================
sys = SystemManager('79.143.185.3:9160')
###############################3
print 'DROP...'
sys.drop_index('MINDNET','cache_products','INDEXED')
print 'CREATE...'
sys.create_index('MINDNET', 'cache_products', 'INDEXED', BYTES_TYPE, index_name='cache_products_indexed')

sys.close()

print 'OK'