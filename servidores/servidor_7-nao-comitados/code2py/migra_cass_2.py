
import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 


pool1 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000000)
pool2 = ConnectionPool('MINDNET', ['213.136.81.102:9160'],timeout=10000000)

def migr(tab1,tab2,tb):
 #r1=tab1.get_range()
 #tab2.truncate()
 ind=0
 while True:
  cach=[]
  r1=tab1.get_range()
  for ky,col in r1:
   cach.append([ky,col])
   if len(cach) %1000==0:
    print 'collect(',tb,'):',len(cach)
   if len(cach) >= 500000: 
     break
  if len(cach) == 0: break
  
  b1 = tab2.batch(55000)
  b2 = tab1.batch(55000)   
  indc=0
  for ky,col in cach:
   tab2.insert(ky,col)
   tab1.remove(ky)
   indc+=1
   if indc % 50000==0:
    b1.send() 
    b2.send() 
    b1 = tab2.batch(55000)
    b2 = tab1.batch(55000)   
    print tb,'->',ind
  b1.send() 
  b2.send() 
 print tb,'->',ind 
 
web_cache10_1 = pycassa.ColumnFamily(pool1, 'web_cache10')
web_cache10_2 = pycassa.ColumnFamily(pool2, 'web_cache10')
#migr(web_cache10_1,web_cache10_2,'web_cache10')

fz_store_sufix_1 = pycassa.ColumnFamily(pool1, 'fz_store_sufix')
fz_store_sufix_2 = pycassa.ColumnFamily(pool2, 'fz_store_sufix')
#migr(fz_store_sufix_1,fz_store_sufix_2,'fz_store_sufix')

SEMANTIC_RELACTIONS_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_RELACTIONS')
SEMANTIC_RELACTIONS_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS')
#migr(SEMANTIC_RELACTIONS_1,SEMANTIC_RELACTIONS_2,'semantic_relactions')

SEMANTIC_OBJECT_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_OBJECT')
SEMANTIC_OBJECT_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT')
#migr(SEMANTIC_OBJECT_1,SEMANTIC_OBJECT_2,'semantic_object')
#
fz_store_defs_1 = pycassa.ColumnFamily(pool1, 'fz_store_defs')
fz_store_defs_2 = pycassa.ColumnFamily(pool2, 'fz_store_defs')
#migr(fz_store_defs_1,fz_store_defs_2,'fz_store_defs')

SEMANTIC_RELACTIONS3_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_RELACTIONS3')
SEMANTIC_RELACTIONS3_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3')
#migr(SEMANTIC_RELACTIONS3_1,SEMANTIC_RELACTIONS3_2,'semantic_relactions3')

knowledge_manager_1 = pycassa.ColumnFamily(pool1, 'knowledge_manager')
knowledge_manager_2 = pycassa.ColumnFamily(pool2, 'knowledge_manager')
#migr(knowledge_manager_1,knowledge_manager_2,'kwnolegde_manager')

SEMANTIC_OBJECT3_1_4_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_OBJECT3_1_4')
SEMANTIC_OBJECT3_1_4_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4')
#migr(SEMANTIC_OBJECT3_1_4_1,SEMANTIC_OBJECT3_1_4_2,'semantic_object3_1_4')

web_cache3_1 = pycassa.ColumnFamily(pool1, 'web_cache3')
web_cache3_2 = pycassa.ColumnFamily(pool2, 'web_cache3')
#migr(web_cache3_1,web_cache3_2,'web_cache3')

fcb_users1_1 = pycassa.ColumnFamily(pool1, 'fcb_users1')
fcb_users1_2 = pycassa.ColumnFamily(pool2, 'fcb_users1')
#migr(fcb_users1_1,fcb_users1_2,'fcb_users1')

fz_store_refer_1 = pycassa.ColumnFamily(pool1, 'fz_store_refer')
fz_store_refer_2 = pycassa.ColumnFamily(pool2, 'fz_store_refer')
#migr(fz_store_refer_1,fz_store_refer_2,'fz_store_refer')

DATA_BEHAVIOUR_CODE_PY_1 = pycassa.ColumnFamily(pool1, 'DATA_BEHAVIOUR_CODE_PY')
DATA_BEHAVIOUR_CODE_PY_2 = pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_CODE_PY')
#migr(DATA_BEHAVIOUR_CODE_PY_1,DATA_BEHAVIOUR_CODE_PY_2,'data_behaviour_code_py')

SEMANTIC_OBJECT_DT_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_OBJECT_DT')
SEMANTIC_OBJECT_DT_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT')
#migr(SEMANTIC_OBJECT_DT_1,SEMANTIC_OBJECT_DT_2,'semantic_object_dt')

SEMANTIC_OBJECT3_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_OBJECT3')
SEMANTIC_OBJECT3_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3')
#migr(SEMANTIC_OBJECT3_1,SEMANTIC_OBJECT3_2,'semantic_object3')

to_posting_1 = pycassa.ColumnFamily(pool1, 'to_posting')
to_posting_2 = pycassa.ColumnFamily(pool2, 'to_posting')
#migr(to_posting_1,to_posting_2,'to_posting')

SEMANTIC_RELACTIONS3_1_4_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_RELACTIONS3_1_4')
SEMANTIC_RELACTIONS3_1_4_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4')
#migr(SEMANTIC_RELACTIONS3_1_4_1,SEMANTIC_RELACTIONS3_1_4_2,'semantic_relactions3_1_4')

SEMANTIC_OBJECT_DT3_1_4_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_OBJECT_DT3_1_4')
SEMANTIC_OBJECT_DT3_1_4_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4')
#migr(SEMANTIC_OBJECT_DT3_1_4_1,SEMANTIC_OBJECT_DT3_1_4_2,'semantic_object_dt3_1_4')

fuzzy_store_1 = pycassa.ColumnFamily(pool1, 'fuzzy_store')
fuzzy_store_2 = pycassa.ColumnFamily(pool2, 'fuzzy_store')
#migr(fuzzy_store_1,fuzzy_store_2,'fuzzy_store')

cache_products_1 = pycassa.ColumnFamily(pool1, 'cache_products')
cache_products_2 = pycassa.ColumnFamily(pool2, 'cache_products')
#migr(cache_products_1,cache_products_2,'cache_products')

cache_links_1 = pycassa.ColumnFamily(pool1, 'cache_links')
cache_links_2 = pycassa.ColumnFamily(pool2, 'cache_links')
#migr(cache_links_1,cache_links_2,'cache_links')

DATA_BEHAVIOUR_PY_1 = pycassa.ColumnFamily(pool1, 'DATA_BEHAVIOUR_PY')
DATA_BEHAVIOUR_PY_2 = pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_PY')
#migr(DATA_BEHAVIOUR_PY_1,DATA_BEHAVIOUR_PY_2,'data_behaviour_py')

SEMANTIC_OBJECT_DT3_1 = pycassa.ColumnFamily(pool1, 'SEMANTIC_OBJECT_DT3')
SEMANTIC_OBJECT_DT3_2 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3')
#migr(SEMANTIC_OBJECT_DT3_1,SEMANTIC_OBJECT_DT3_2,'semantic_object_dt3')

to_posting2_1 = pycassa.ColumnFamily(pool1, 'to_posting2')
to_posting2_2 = pycassa.ColumnFamily(pool2, 'to_posting2')
#migr(to_posting2_1,to_posting2_2,'to_posting2')

fz_store_pref_1 = pycassa.ColumnFamily(pool1, 'fz_store_pref')
fz_store_pref_2 = pycassa.ColumnFamily(pool2, 'fz_store_pref')
#migr(fz_store_pref_1,fz_store_pref_2,'fz_store_pref')

web_cache1_1 = pycassa.ColumnFamily(pool1, 'web_cache1')
web_cache1_2 = pycassa.ColumnFamily(pool2, 'web_cache1')
migr(web_cache1_1,web_cache1_2,'web_cache1')

fz_arround_points_1 = pycassa.ColumnFamily(pool1, 'fz_arround_points')
fz_arround_points_2 = pycassa.ColumnFamily(pool2, 'fz_arround_points')
#migr(fz_arround_points_1,fz_arround_points_2,'fz_arround_points')





