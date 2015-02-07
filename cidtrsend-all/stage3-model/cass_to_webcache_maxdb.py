import os
import sys
import umisc

import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa import index

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10)
wb2 = pycassa.ColumnFamily(pool2, 'web_cache3') 

usr='igor.moraes'

 

print 'Process web.cache....'

itemsc=0

def get_rows(i_count):
 i=0;
 rt=[]
 r=wb2.get_range()
 for ky,s in r:
  i+=1
  if i > i_count: break
  rt.append([ky,s])
 
 return rt

 
 
def process_wb(itens,conn):
  conn.sql('delete from web_cache where tps=\'K\'') # tps = K -> importado para analize
  conn.commit()
  rns=[]
  doc_id=0
  for ky,s in itens:
      url=s['url']
      pg=s['pg']
      termo=s['termo']
      usr=s['usr']
      purpose=s['purpose']
      processed='N'
      url_icon=s['url_icon']
      url_picture=s['url_picture']
      id_usr=s['id_usr']
      name_usr=s['name_usr']
      story=s['story']
      title=s['t_title']
      doc_id=ky
      t_title=s['t_title']
      tp=s['tp']
      tps='K'
      indexed='N'
      if id_usr == '': 
        id_usr=0
      else:
        id_usr=float(id_usr)
      rns.append([url,pg,termo,usr,purpose,processed,id_usr,name_usr,title,str(doc_id),tps])
 
  i=0
  c=len(rns)
  while i < c:
   r=rns[i]
   i+=1
   try:
     conn.sqlX("insert into WEB_CACHE(url,pg,termo,usr,purpose,processed,id_usr,name_usr,title,doc_id,tps)values(?,?,?,?,?,?,?,?,?,?,?) ",r)
   except Exception,e:
    print 'Err....',str(e)
  conn.commit()  
    
tp=input('Number of rows:')

tp=str(tp)    
    
rc=get_rows(int(tp))   

import conn
conn2= conn.conn_mx

print 'Init.process....'  
process_wb(rc,conn2)

print 'OK!!!'
