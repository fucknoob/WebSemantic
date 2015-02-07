
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
conn=conn.conn_mx


#import conn2
#conn= conn2.conn_mx


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
  
 
def get_by_keyword(is2): # busca algumas palavras chave para extrair os 'samples', amostras de codigo para calibrar e treinar o processador fuzzy
  isd=[]
  try:
     cursor = conn.sql("SELECT PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL,i  from web_cache where i in("+is2+")  ") 
     for results in cursor:
        I=results[22]
        #============================
        #print 'Print pg:',I
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
        #================================
        if umisc.trim(PG) == '':
         fnd=False
        if fnd and not fnd2: 
         isd.append([PG,PROCESSED,TERMO,USR,PURPOSE,URL_ICON,URL_PICTURE,ID_USR,NAME_USR,STORY,TITLE,DOC_ID,TP,PHONE,STREET,CITY,COUNTRY,ZIP,LATITUDE,LONGITUDE,TPS,URL])
         #apagar o item, passando p tabela processados somente os I,DOC_ID para o processo de reprocessamento nao considerar mais esses documentos
        conn.sqlX('insert into PROC_DS (ID,DOC_ID) values(?,?)',[I,DOC_ID])
        conn.sqlX('delete from web_cache where I=?',[I])
  except: 
   log.exception("")   
   conn.rollback()
   return []
  conn.commit()   
  return isd

 
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
  #post_cn(tks)
  post_cn2(tks)
 

is2=sys.argv[1]       
     
index_subs(1,1,is2) 
 
 