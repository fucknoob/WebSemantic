import MySQLdb
'''
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
'''

import conn

conn= conn.conn_mx

import sys
import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


conn3= MySQLdb.connect('dbmy0031.whservidor.com', 'esyns1', 'acc159753', 'esyns1') 

connect=conn3
 

def get_urls1():
 def get_urls_to_index():
  rts=[]
  try:
   cursor = connect.cursor ()   
   cursor.execute ('select CONVERT(url USING latin1),rec_id from url limit 0,1000') 
   resultSet = cursor.fetchall()
   for results in resultSet:     
     url= results[0]
     rec_id=results[1]
     rts.append([url,rec_id])
     #=================
     
  except Exception,err:
   print 'Error get_pages:',err  
  return rts
 
 
 rt=get_urls_to_index()
 return rt 
 
cursor2 = connect.cursor ()   
   
sql_insert_p='insert into web_cache5(url,pg,processed,termo,usr,purpose) values(?,\'\',\'N\',\'SYSTEM\',\'igor.moraes\',\'SYSTEM\')'   

def insert_cache(url):
 try:
   [url1,rec_id]=url
   conn.sqlX(sql_insert_p,[url1])
   #=========================
   cursor2.execute("delete from url where rec_id="+str(rec_id))
 except:
  log.exception('ERROR INSERT') 
   

   
ck=1
   
while  ck<=10:   
 print 'Cycle:',ck
 for ur in get_urls1():
    insert_cache(ur)
 conn.commit()
 ck+=1
   

'''   
for results in get_urls('dbmy0053.whservidor.com', 'esyns1_1', 'acc159753', 'esyns1_1'):
   insert_cache(ur)

for results in get_urls('dbmy0035.whservidor.com', 'esyns1_2', 'acc159753', 'esyns1_2'):
   insert_cache(ur)
'''

   
'''
pool = ConnectionPool('ubuntu13',['localhost:9160'])
col_fam = ColumnFamily(pool, 'teste')
for results in get_urls('dbmy0031.whservidor.com', 'esyns1',   'acc159753', 'esyns1'):
   col_fam.insert(results, {'url': results})
   
for results in get_urls('dbmy0053.whservidor.com', 'esyns1_1', 'acc159753', 'esyns1_1'):
   col_fam.insert(results, {'url': results})

for results in get_urls('dbmy0035.whservidor.com', 'esyns1_2', 'acc159753', 'esyns1_2'):
   col_fam.insert(results, {'url': results})
'''







   
