
import os
import sys
import umisc

import conn

conn= conn.conn_mx

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

web=pycassa.ColumnFamily(pool2, 'web_cache3')


 
usr='igor.moraes'

 

print 'Process web.cache....'

itemsc=0


def process_wb():
 global itemsc
 web.truncate()
 #
 r1=conn.sql("select I,PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,\
 TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL from WEB_CACHE") 
 itemsc=0
 for re in r1:
  I=str(re[0])
  PG=re[1].read()
  PROCESSED=str(re[2])
  TERMO=str(re[3])
  USR=str(re[4])
  PURPOSE=re[5]
  if re[6] != None:
   URL_ICON=re[6].read()
  else:
   URL_ICON=''
  if re[7] != None:
   URL_PICTURE=re[7].read()
  else:
   URL_PICTURE='' 
  if re[8] == None:
    ID_USR='0'
  else:
   ID_USR=str(re[8])   
  NAME_USR=re[9]
  if NAME_USR == None:
    NAME_USR='{undef}'
  if re[10] != None:
   STORY=re[10].read()
  else:
    STORY=''
  if re[11] != None:  
   TITLE=re[11].read()
  else:
   TITLE='' 
  DOC_ID=str(re[12])
  #DOC_ID=str(I)
  TP=re[13]
  if TP == None:
    TP='status'
  PHONE=re[14]
  if PHONE == None :
    PHONE=''
  STREET=re[15]
  if STREET == None:
    STREET=''
  CITY=re[16]
  if CITY == None:
    CITY=''
  COUNTRY=re[17]
  if COUNTRY == None:
    COUNTRY=''
  ZIP=re[18]
  if ZIP == None:
    ZIP=''
  LATITUDE=re[19]
  if LATITUDE == None :
    LATITUDE= ''
  LONGITUDE=re[20]
  if LONGITUDE == None:
    LONGITUDE=''
  TPS=re[21]
  if TPS == None :
    TPS='W'
  URL=re[22]
  #====================
  if URL == None:
    URL=''
  else:
    URL=URL.read()
  if URL_ICON == None :
    URL_ICON=''
  if URL_PICTURE == None:
    URL_PICTURE=''
  if USR == None :
    USR='{undef}'
  if ZIP == None :
    ZIP=''
  #====================
  params={'CITY':CITY,'COUNTRY':COUNTRY,'DOC_ID':DOC_ID,'ID_USR':ID_USR,'LATITUDE':LATITUDE,'LONGITUDE':LONGITUDE,'NAME_USR':NAME_USR,'PG':PG,'PHONE':PHONE,'PROCESSED':PROCESSED,'PURPOSE':PURPOSE,'STORY':STORY,'STREET':STREET,'TERM':TERMO,'TITLE':TITLE,'TP':TP,'TPS':TPS,'URL':URL,'URL_ICON':URL_ICON,'URL_PICTURE':URL_PICTURE,'USR':USR,'ZIP':ZIP}
  web.insert(str(I),params)
  itemsc+=1

process_wb()
print 'Itens.updated:',itemsc
print 'OK' 
 