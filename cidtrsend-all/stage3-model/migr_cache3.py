#coding: latin-1

import base64
import calendar
import os
import rfc822
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse
import thread
 
import subprocess
import string

sys.path.append('/Neural')
sys.path.append('c:/python25/mxdb')

import maxdb
import umisc

 

arrno=[]


user = 'MIND'
pwd = 'MIND'

host = '91.205.172.85'
dbname = 'MINDNET'

print 'Connecting to knowledge cluster(3)....[',dbname,host,']'
conn_mx = maxdb.connect (user, pwd, dbname, host)
print 'Connected.'


import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool2 = ConnectionPool('MINDNET', ['91.205.172.85:9160'],timeout=100000)
tab2 = pycassa.ColumnFamily(pool2, 'web_cache3')

conn=conn_mx
#
def get_columns(tablem):
   rt=[]
   curs1=conn.sqlX("select columnname from columns where upper(tablename)= '"+tablem.upper()+"' order by pos ") 
   for c in curs1:
      nm=c[0]
      if nm.upper() != 'I':   
       rt.append(nm)
      
   return rt


colunas=get_columns("web_cache3")
sql='select '
for col in colunas:
      if sql!='select ':
         sql+=','
      sql+= col 
sql+=' from web_cache3 where DOC_ID <> \'-\' and rowno<=500'

curtb=conn.sql(sql)
for c in curtb:
 ind=0
 cols=[]
 ID=''
 ky=''
 for k in c:
   if colunas[ind].upper() == 'DOC_ID':
     ky=k
   else:
     if (type(k).__name__) == 'SapDB_LongReader':
      k=k.read()
     pr={colunas[ind]:k} 
     cols.append(pr) 
   ind+=1
 #=   
 tab2.insert(ky,cols)   
