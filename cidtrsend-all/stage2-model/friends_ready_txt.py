
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

'''
import conn
conn=conn.conn_mx
''' 


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



ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 

pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

w_cache = pycassa.ColumnFamily(pool2, 'web_cache')
w_cache3 = pycassa.ColumnFamily(pool2, 'web_cache3')
proc_ds = pycassa.ColumnFamily(pool2,'proc_ds')


def tokeniz(dt):
  rts=[]
  tmp=''
  start_comm=False
  for e in dt:
    if e in ['"']:
      if not start_comm:
       start_comm=True
      else:
       start_comm=False  
    if e in ['!'] and start_comm:
     tmp+=e 
    elif e in [' ','.',';',',','(',')','[',']','{','}','?','!','"','\'',':','@','\\','/']:
     if tmp != '':
      rts.append(tmp)
     if e in ['.',';',',','(',')','[',']','{','}','?','!','"','\'',':','@','\\','/']   :
      rts.append(e)
     tmp=''
    else:
     tmp+=e
  if tmp != '' :
   rts.append(tmp)  
  return rts
 #============================================
  
 
def get_by_keyword(is2): # busca algumas palavras chave para extrair os 'samples', amostras de codigo para calibrar e treinar o processador fuzzy
  isd=[]
  cnc=False
  for ch in is2:
   try:
     cnc=False
     try:
      rows=w_cache.get(ch)
     except:
      cnc=True
     if cnc : continue 
     if True:
        #============================
        print 'Print pg:',ch
        #=================
        PG=rows[u'pg']
        PROCESSED=rows[u'processed']
        TERMO=rows[u'termo']
        USR=rows[u'usr']
        PURPOSE=rows[u'purpose']
        URL_ICON=rows[u'url_icon']
        URL_PICTURE=rows[u'url_picture']
        ID_USR=float(rows[u'id_usr'])
        NAME_USR=rows[u'name_usr']
        STORY=rows[u'story']
        TITLE=rows[u'title']
        DOC_ID=rows[u'doc_id']
        TP=rows[u'tp']
        PHONE=''
        STREET=''
        CITY=''
        COUNTRY=''
        ZIP=''
        LATITUDE=''
        LONGITUDE=''
        TPS=rows['tps']
        URL=rows['url']
        #==========
        if PG != None : 
          pass
        else:
          PG=''        
        if URL_ICON != None : 
          pass
        else: URL_ICON=''
        if URL_PICTURE != None : 
         pass
        else:
         URL_PICTURE=''         
        if STORY != None : 
          pass
        else:
          STORY=''        
        if TITLE != None : 
          pass
        else:
          TITLE=''        
        if URL != None : 
         pass
        else:
         URL=''  
        
                
        words=tokeniz(PG)         
        #fnd=False
        fnd=True
        fnd2=False
        if 'are now friends' in PG :
         fnd2=True
        elif 'is now friends with' in PG :
         fnd2=True
        elif PG[:7] =='http://'  :
         fnd2=True
        elif 'likes' in PG : 
         fnd2=True
        elif '{like}' in PG:           
         fnd2=True       
        #===   
        '''
        for w in words:
         if 'quer' in w:
           fnd=True
         elif 'precis' in w:
           fnd=True
         elif 'poderia' in w:
           fnd=True
         elif 'pode' in w:
           fnd=True
         elif 'podi' in w:
           fnd=True
         elif 'gostar' in w:
           fnd=True
         elif 'pensand' in w:
           fnd=True
         elif 'comprar' in w:
           fnd=True
         elif 'adquirir' in w:
           fnd=True          
         elif 'pens' in w:
           fnd=True         
         elif 'pegar' in w:
           fnd=True         
         elif 'encontr' in w:
           fnd=True         
         elif 'indicar' in w:
           fnd=True       
        '''   
        #================================
        if umisc.trim(PG) == '':
         fnd=False
        if fnd and not fnd2: 
         isd.append([PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL])
         #apagar o item, passando p tabela processados somente os I,DOC_ID para o processo de reprocessamento nao considerar mais esses documentos
        #===================================================================
        #I=0
        #conn.sqlX('insert into PROC_DS (ID,DOC_ID) values(?,?)',[I,ch])
        proc_ds.insert(ch,{'ch':ch})
        #======================================================================
        w_cache.remove(ch)
   except: 
    log.exception("")   
    #conn.rollback()
    return []
  #conn.commit()   
  return isd


def post_cnt3(its):
 for [PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL] in its:  
  w_cache3.insert(str(DOC_ID),{'PG':PG,'PROCESSED':PROCESSED,'TERM':TERM,'USR':USR,'PURPOSE':PURPOSE,'URL_ICON':URL_ICON,\
                          'URL_PICTURE':URL_PICTURE,'ID_USR':ID_USR,'NAME_USR':NAME_USR,'STORY':STORY,'TITLE':TITLE,\
                          'DOC_ID':DOC_ID,'TP':TP,'PHONE':PHONE,'STREET':STREET,'CITY':CITY,'COUNTRY':COUNTRY,'ZIP':ZIP,\
                          'LATITUDE':LATITUDE,'LONGITUDE':LONGITUDE,'TPS':TPS,'URL':URL}) 
 
 
def post_cn2(its):
 print 'POST.LEN:',len(its) 
 sql=' insert into web_cache3(PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
 #for [PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL] in its: 
 for [PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL] in its:  
     conn.sqlX (sql,[PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL]) 
 conn.commit()    
 
 
def post_cn(its):
 f=open("/Neural/txt_logs","w")
 print 'POST.LEN:',len(its) 
 for [PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL] in its:  
      c1=str(PG)
      if umisc.trim(c1) != '':      
       f.write( str(PG)+'|'+str(PROCESSED)+'|'+str(TERM)+'|'+str(USR)+'|'+str(PURPOSE)+'|'+str(URL_ICON)+'|'+str(URL_PICTURE)+'|'+str(ID_USR)+'|'+str(NAME_USR)+'|'+str(STORY)+'|'+str(TITLE)+'|'+str(DOC_ID)+'|'+str(TP)+'|'+str(PHONE)+'|'+str(STREET)+'|'+str(CITY)+'|'+str(COUNTRY)+'|'+str(ZIP)+'|'+str(LATITUDE)+'|'+str(LONGITUDE)+'|'+str(TPS)+'|'+str(URL)+'|'+'\n'   )
 f.close()     
  
def index_subs(j1,j2,processo):
#
 if True :   
  tks=get_by_keyword(processo)
  post_cn3(tks)
 

is2=sys.argv[1]       

i2c=is2.split(',')
 
 
index_subs(1,1,i2c) 
 
 