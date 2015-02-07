import MySQLdb
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

'''
  create column family teste 
    with comparator = UTF8Type
    and default_validation_class = UTF8Type
    and column_metadata = [{
        column_name : url,
        validation_class : UTF8Type,
        index_name : url_idx,
        index_type : 0}
    ];
'''

total = 1

def get_urls(host, user, passwd, db, limit):
 def get_urls_to_index(connect,us):
  rts=[]
  global total
  try:
   print "------------> ", host
   cursor = connect.cursor()
   cursor.execute ('select count(*) from url') 
   resultSet = cursor.fetchall()
   print "--Total: ", resultSet
   total = resultSet
   cursor2 = connect.cursor()
   cursor2.execute ('select url from url limit '+str(limit)+', 5000') 
   resultSet2 = cursor2.fetchall()
   for results in resultSet2:     
     id= results[0]
     rts.append(id)
  except Exception,err:
   print 'Error get_pages:',err
  return rts

 conn3= MySQLdb.connect(host, user, passwd, db) 
 rt=get_urls_to_index(conn3, user)

 if len(rt) > 0 :
   return rt

pool = ConnectionPool('ubuntu13',['localhost:9160'])
col_fam = ColumnFamily(pool, 'teste')
count = 0;
while count <= total:
 #for results in get_urls('dbmy0031.whservidor.com', 'esyns1',   'acc159753', 'esyns1',   count):
 for results in get_urls('dbmy0035.whservidor.com', 'esyns1_2', 'acc159753', 'esyns1_2', count):
 #for results in get_urls('dbmy0053.whservidor.com', 'esyns1_1', 'acc159753', 'esyns1_1', count):
   col_fam.insert(unicode(results, errors="ignore"), {'url': unicode(results, errors="ignore")})
   count = count + 1;
   if count % 5000 == 0:
     print "Count: ", count

