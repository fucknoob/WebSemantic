#create all indexes for cassandra 


from pycassa.system_manager import *

print 'Connect..'
sys = SystemManager('localhost:9160')
print 'DROP...'
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT','datach')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT','topico')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT','object')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT','LEV')
sys.drop_index('MINDNET','fuzzy_store','layout_onto')

sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3','datach')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3','topico')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3','object')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3','LEV')

sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3_1_4','datach')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3_1_4','topico')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3_1_4','object')
sys.drop_index('MINDNET','SEMANTIC_OBJECT_DT3_1_4','LEV')

sys.drop_index('MINDNET','SEMANTIC_OBJECT','objeto')
sys.drop_index('MINDNET','SEMANTIC_OBJECT3','objeto')
sys.drop_index('MINDNET','SEMANTIC_OBJECT3_1_4','objeto')

sys.drop_index('MINDNET','SEMANTIC_RELACTIONS','obj_orig')
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS','opcode')
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS','obj_dest')
#
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS3','obj_orig')
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS3','opcode')
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS3','obj_dest')
#
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS3_1_4','obj_orig')
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS3_1_4','opcode')
sys.drop_index('MINDNET','SEMANTIC_RELACTIONS3_1_4','obj_dest')



print 'create...'
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT', 'datach', BYTES_TYPE, index_name='datach_index')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT', 'topico', BYTES_TYPE, index_name='topico_index')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT', 'object', BYTES_TYPE, index_name='object_index')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT', 'LEV', BYTES_TYPE, index_name='object_LEV')

sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3', 'datach', BYTES_TYPE, index_name='datach_index3')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3', 'topico', BYTES_TYPE, index_name='topico_index3')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3', 'object', BYTES_TYPE, index_name='object_index3')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3', 'LEV', BYTES_TYPE, index_name='object_LEV3')

sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3_1_4', 'datach', BYTES_TYPE, index_name='datach_index3_1_4')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3_1_4', 'topico', BYTES_TYPE, index_name='topico_index3_1_4')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3_1_4', 'object', BYTES_TYPE, index_name='object_index3_1_4')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT_DT3_1_4', 'LEV', BYTES_TYPE, index_name='object_LEV3_1_4')

sys.create_index('MINDNET', 'SEMANTIC_OBJECT', 'objeto', BYTES_TYPE, index_name='object_objeto')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT3', 'objeto', BYTES_TYPE, index_name='object_objeto3')
sys.create_index('MINDNET', 'SEMANTIC_OBJECT3_1_4', 'objeto', BYTES_TYPE, index_name='object_objeto3_1_4')

sys.create_index('MINDNET', 'fuzzy_store', 'layout_onto', BYTES_TYPE, index_name='fuzzy_store_layout_onto')


sys.create_index('MINDNET','SEMANTIC_RELACTIONS','obj_orig',BYTES_TYPE, index_name='relaction_obj_orig')
sys.create_index('MINDNET','SEMANTIC_RELACTIONS','opcode',BYTES_TYPE, index_name='relaction_opcode')
sys.create_index('MINDNET','SEMANTIC_RELACTIONS','obj_dest',BYTES_TYPE, index_name='relaction_oobj_dest')
#
sys.create_index('MINDNET','SEMANTIC_RELACTIONS3','obj_orig',BYTES_TYPE, index_name='relaction3_obj_orig')
sys.create_index('MINDNET','SEMANTIC_RELACTIONS3','opcode',BYTES_TYPE, index_name='relaction3_opcode')
sys.create_index('MINDNET','SEMANTIC_RELACTIONS3','obj_dest',BYTES_TYPE, index_name='relaction3_obj_dest')
#
sys.create_index('MINDNET','SEMANTIC_RELACTIONS3_1_4','obj_orig',BYTES_TYPE, index_name='relaction3_1_4_obj_orig')
sys.create_index('MINDNET','SEMANTIC_RELACTIONS3_1_4','opcode',BYTES_TYPE, index_name='relaction3_1_4_opcode')
sys.create_index('MINDNET','SEMANTIC_RELACTIONS3_1_4','obj_dest',BYTES_TYPE, index_name='relaction3_1_4_obj_dest')



sys.close()

print 'OK'