from pycassa.system_manager import *


sys = SystemManager('79.143.185.3:9160')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT','datach')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT', 'datach', BYTES_TYPE, index_name='datach_index')
sys.close()