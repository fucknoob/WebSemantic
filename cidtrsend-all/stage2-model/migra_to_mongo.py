import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

import bson

import pymongo

print 'Connect to mongo...'
MONGO_URL='mongodb://mdnet1:acc159753@ds037358.mongolab.com:37358/mdnet2_5'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet2_5
fcbM=dbM['fcb_users']


print 'Connect to cassandra...'
pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=10000)
fcb = pycassa.ColumnFamily(pool2, 'fcb_users')


print 'Prepare.....'
exprc = index.create_index_expression(column_name='indexed', value='S')
clausec = index.create_index_clause([exprc],count=200000)
rest=fcb.get_indexed_slices(clausec)
ind=0

cache=[]
print 'Start to collect.....'
for kl,cols in rest:
     if ind >= 200000:
       break
     if ind % 1000 == 0 : print 'Collect:',ind   
     cache.append([kl,cols])
     ind+=1    
     
ind=0
for ca in cache:
  [ky,cols]=ca  
  fcbM.insert({"id":cols[u'id'],"indexed":'N',"user_name":bson.Binary(cols[u'user_name']),"u_name":bson.Binary(cols[u'u_name'])}) 
  cols[u'indexed']='Z'
  fcb.insert(ky,{"id":cols[u'id'],"indexed":cols[u'indexed'],"user_name":cols[u'user_name'],"u_name":cols[u'u_name']})    
  if ind % 1000 == 0 : print 'Save:',ind   
  ind+=1

print 'total inserts:',fcbM.count()
  
     
