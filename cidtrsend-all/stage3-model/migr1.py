import os
import sys



import conn
conn=conn.conn_mx
 


import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


import thread
a_lock = thread.allocate_lock() 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily


class thread_cntl:
 def __init__(self):
  self.finished=False

 

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)


w_cache3 = pycassa.ColumnFamily(pool2, 'web_cache3')
 

 
  
 
def get_by_keyword(lopsq): # busca algumas palavras chave para extrair os 'samples', amostras de codigo para calibrar e treinar o processador fuzzy
  isd=[]
  cnc=False
  ch=0
  is2=conn.sql("select PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL,i from  web_cache ")
  for rows in is2:
        ch+=1
        #============================
        print 'Print pg:',ch
        #=================
        PG=rows[0].read()
        PROCESSED=rows[1]
        if PROCESSED == None:PROCESSED='N'
        TERMO=rows[2]
        if TERMO == None: TERMO=''
        USR=rows[3]
        PURPOSE=rows[4]
        if PURPOSE == None: PURPOSE=''
        if rows[5]!= None:
         URL_ICON=rows[5].read()
        else:
         URL_ICON=''
        if rows[6] != None: 
         URL_PICTURE=rows[6].read()
        else:
         URL_PICTURE='' 
        ID_USR=str(rows[7])
        NAME_USR=rows[8]
        if NAME_USR == None : NAME_USR=''
        if rows[9] != None:
         STORY=rows[9].read()
        else:
         STORY='' 
        if rows[10] != None: 
         TITLE=rows[10].read()
        else:
         TITLE='' 
        DOC_ID=rows[11]
        TP=str(rows[12])
        PHONE=''
        STREET=''
        CITY=''
        COUNTRY=''
        ZIP=''
        LATITUDE=''
        LONGITUDE=''
        TPS=str(rows[20])
        if rows[21]!= None:
         URL=rows[21].read()
        else:
         URL='' 
        II=str(rows[22])
        DOC_ID=II
        #==========
        post_cnt3([PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL])
 
        


def post_cnt3(its):
  [PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL] = its  
  w_cache3.insert(str(DOC_ID),{'PG':PG,'PROCESSED':PROCESSED,'TERM':TERM,'USR':USR,'PURPOSE':PURPOSE,'URL_ICON':URL_ICON,\
                          'URL_PICTURE':URL_PICTURE,'ID_USR':ID_USR,'NAME_USR':NAME_USR,'STORY':STORY,'TITLE':TITLE,\
                          'DOC_ID':DOC_ID,'TP':TP,'PHONE':PHONE,'STREET':STREET,'CITY':CITY,'COUNTRY':COUNTRY,'ZIP':ZIP,\
                          'LATITUDE':LATITUDE,'LONGITUDE':LONGITUDE,'TPS':TPS,'URL':URL}) 
   
  
def index_subs(j1,j2,processo):
 get_by_keyword(processo)
 
 
 
index_subs(1,1,1) 
 
 