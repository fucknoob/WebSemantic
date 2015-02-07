
import pymongo

MONGO_URL='mongodb://mdnet1:acc159753@127.0.0.1:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
web=dbM['web_cache']

import logging
import time
import umisc

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('DserviceC')


def get_pages():  
  res=[]
  cach=web.find({"processed":"N"})
  cach1=[]
  for rg in cach:
        id=rg['doc_id']
        p1=id
        if len(res) >= 10: 
         break
         time.sleep(5)
        #==============
        if rg != None: 
         try:
          rtc1=rg['pg']
          try:
           rtc2=rg[u'title'].encode('latin-1')           
          except: 
           rtc2=rg[u'title'] 
          res.append( [ rtc1,p1,rtc2 ] )
         except:
          print 'Error.get.pg:',rg
          log.exception("")
          try:
           res.append( [ rg[u'PG'].decode('latin-1'),p1,rg[u'TITLE'].decode('latin-1') ] )
          except:
           print 'Error.get.pg(2):',rg
           log.exception("")  
        rg['processed']='S'   
        web.update({'_id':rg['_id']},rg) # fecha o registro
  #===================================
  typ=[]
  for [ts,ids,ids2] in res:
    if ids2 == None: ids2= ''
    if umisc.trim(ids2) != '':
            ts=(ids2+': '+ts)
    typ.append([ts,ids])    
  #  
  return typ  
 

 