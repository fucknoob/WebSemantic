
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time


import conn
connp=conn.conn_mx


import conn2
conn= conn2.conn_mx


import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


import thread
a_lock = thread.allocate_lock() 




class thread_cntl:
 def __init__(self):
  self.finished=False



ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 


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
  
 
def get_by_keyword(): # busca algumas palavras chave para extrair os 'samples', amostras de codigo para calibrar e treinar o processador fuzzy
  isd=[]
  try:
     cursor = conn.sql("SELECT PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL,i  from web_cache where rowno <= 50 ") 
     for results in cursor:
        I=results[22]
        #============================
        print 'Print pg:',I
        PG=results[0]
        PROCESSED=results[1]
        TERMO=results[2]
        USR=results[3]
        PURPOSE=results[4]
        URL_ICON=results[5]
        URL_PICTURE=results[6]
        ID_USR=results[7]
        NAME_USR=results[8]
        STORY=results[9]
        TITLE=results[10]
        DOC_ID=results[11]
        TP=results[12]
        PHONE=results[13]
        STREET=results[14]
        CITY=results[15]
        COUNTRY=results[16]
        ZIP=results[17]
        LATITUDE=results[18]
        LONGITUDE=results[19]
        TPS=results[20]
        URL=results[21]
        #==========
        if PG != None : 
          PG=PG.read()
        else:
          PG=''        
        if URL_ICON != None : 
          URL_ICON=URL_ICON.read()
        else: URL_ICON=''
        if URL_PICTURE != None : 
         URL_PICTURE=URL_PICTURE.read()
        else:
         URL_PICTURE=''         
        if STORY != None : 
          STORY=STORY.read()
        else:
          STORY=''        
        if TITLE != None : 
          TITLE=TITLE.read()
        else:
          TITLE=''        
        if URL != None : 
         URL=URL.read()
        else:
         URL=''  
        
                
        words=tokeniz(PG)         
        fnd=False
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
        #================================
        if fnd: 
         ids.append([PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL])
  except: log.exception("")      
  return isd

 
def post_cn(its):
 print 'POST.LEN:',len(its)
 sql=' insert into web_cache(PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
 for [PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL] in its:     
     connp.sqlX (sql,[PG,PROCESSED,TERM,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL]) 
 connp.commit()    
  
  
def index_subs(j1,j2,processo=1):
#
 if True :   
  tks=get_by_keyword()
  post_cn(tks)
 

       
     
     
index_subs(1,1,1) 
 
 