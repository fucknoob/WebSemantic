#==========================================
from pycassa.system_manager import *

print 'Connect..'
#sys = SystemManager('localhost:9160') 
sys = SystemManager('79.143.185.3:9160')
############################
sys.create_keyspace('MINDNET', SIMPLE_STRATEGY, {'replication_factor': '1'})
#
sys.create_column_family('MINDNET', 'fz_store_sufix', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'fz_store_sufix', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_RELACTIONS', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_RELACTIONS', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_OBJECT', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_OBJECT', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'fz_store_defs', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'fz_store_defs', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_RELACTIONS3', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_RELACTIONS3', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_OBJECT3_1_4', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_OBJECT3_1_4', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'knowledge_manager', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'knowledge_manager', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'fz_store_refer', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'fz_store_refer', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'DATA_BEHAVIOUR_CODE_PY', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'DATA_BEHAVIOUR_CODE_PY', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_OBJECT_DT', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_OBJECT_DT', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_OBJECT3', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_OBJECT3', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_RELACTIONS3_1_4', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_RELACTIONS3_1_4', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_OBJECT_DT3_1_4', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_OBJECT_DT3_1_4', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'fuzzy_store', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'fuzzy_store', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'DATA_BEHAVIOUR_PY', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'DATA_BEHAVIOUR_PY', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'SEMANTIC_OBJECT_DT3', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'SEMANTIC_OBJECT_DT3', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'fz_store_pref', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'fz_store_pref', key_cache_size=42, gc_grace_seconds=1000)
#
sys.create_column_family('MINDNET', 'fz_arround_points', super=False,comparator_type=BYTES_TYPE)
sys.alter_column_family('MINDNET', 'fz_arround_points', key_cache_size=42, gc_grace_seconds=1000)
#
sys.close()

print 'OK' 