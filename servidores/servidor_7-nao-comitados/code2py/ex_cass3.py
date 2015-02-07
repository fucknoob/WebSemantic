
import time
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


import sys

sys.path.append('/Neural')

import conn3
conn= conn3.conn_mx

pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10)
tab2 = pycassa.ColumnFamily(pool2, 'fcb_users')


'''
  create column family fcb_users 
    with comparator = UTF8Type
    and default_validation_class = UTF8Type
    and column_metadata = [{
        column_name : user_name,
        validation_class : UTF8Type,
        index_name : user_name_idx1,
        index_type : 0},
        {
        column_name : id,
        validation_class : UTF8Type,
        index_name : id_idx1,
        index_type : 0},
        {
        column_name : u_name,
        validation_class : UTF8Type,
        index_name : u_name_idx1,
        index_type : 0}        
    ];
'''

'''
  create column family fcb_users 
    with comparator = UTF8Type
    and default_validation_class = UTF8Type
    and column_metadata = [{
        column_name : user_name,
        validation_class : UTF8Type,
        index_name : user_name_idx1,
        index_type : 0},
        {
        column_name : id,
        validation_class : UTF8Type,
        index_name : id_idx1,
        index_type : 0},
        {
        column_name : u_name,
        validation_class : UTF8Type,
        index_name : u_name_idx1,
        index_type : 0}        
    ];
'''

def get_rows(startc):
  cur=conn.sql("select user_name,id,u_name,i from fcb_users where  i>= "+str(startc)+"  and rowno <= 5000 order by i")
  dels=[]
  count=1
  cs=0
  for re in cur:
   user_name=re[0]
   id=re[1]
   u_name=re[2]
   if u_name == None: u_name=''
   i=re[3]
   cs=i
   if count % 50000 == 0:
     time.sleep(2)
   if count % 5000 == 0:   
    print 'read.row:',count
   print  {'user_name':  user_name },{'id':id},{'u_name':u_name} 
   tab2.insert(str(i) , {'user_name':  user_name ,'id':id , 'u_name':u_name})
   if count >5 :  return 0
   count+=1
  return cs 
    

def list():
 for key, columns in tab2.get_range():
    dt= columns[u'u_name']
    id= columns[u'id']
    print 'd:',dt,id
    
    
'''
c2=1
while c2 > 0:
 c22=get_rows(c2)
 c2=c22
'''

list()
 



