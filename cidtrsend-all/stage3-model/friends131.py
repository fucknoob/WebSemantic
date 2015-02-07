#coding: latin-1
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

#import conn
#conn= conn.conn_mx

import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 

import conn
conn= conn.conn_mx


sql_insert_p='insert into fcb_users(user_name,id,u_name) values(?,?,?)'

def insere_usr(user_name,id,u_name): 
 #print 'insert:',[user_name,id,u_name] 
 try:
  conn.sqlX(sql_insert_p,([user_name,id,u_name]))
 except: pass 
     
    
def get_usrs(uid):
    fql='SELECT uid2 FROM friend WHERE uid1 = '+uid
    args = {}
    args["query"], args["format"] , args['access_token'] = fql, "json" ,'392136580875840|rdRN2UGmcx_eJdJhRFvq_-F9O0Y'

    url='http://api.facebook.com/method/fql.query?'+ urllib.urlencode(args)
    file = urllib2.urlopen("https://api.facebook.com/method/fql.query?" + urllib.urlencode(args))
    
    rets=file.read ()
    print rets
    #
    #result = simplejson.load(file)
    #return result
    
    
def get_likes(ids):
    url='https://graph.facebook.com/'+ids+'/likes?access_token=392136580875840|rdRN2UGmcx_eJdJhRFvq_-F9O0Y'
    file = urllib2.urlopen(url)
    dts=file.read ()   
    
    print dts
 
to_ins=[]
 
err=False 
 
def get_feeds(id,cs=0,c_url=''):
    args = {}
    global to_ins
    global err
    args['access_token'],args['limit'] =  '392136580875840|rdRN2UGmcx_eJdJhRFvq_-F9O0Y','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    print 'Process pg:',id
    
    if c_url != '':
     url=c_url
    
    try:
    
     file = urllib2.urlopen(url)
    
    except Exception,err1:
     err=True
     print 'Error:',err1
     return
    #dts=file.read ()   
    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    pagin=result['paging']
    msg_i=1
    for ch in r2:
     
     try:
      id=ch[u'id']
     except: pass 
     try:
      _from=ch[u'from']
     except: pass 
     try:
      likes=ch[u'likes']
     except: 
      likes=None     
     try:
      message=ch[u'message']
     except: pass 
     try:
      link=ch[u'link']
     except: pass 
     try:
      icon=ch[u'icon']
     except: pass 
     try:
      type=ch[u'type']
     except: pass 
     try:
      status_type=ch[u'status_type']
     except: pass 
     try:
      object_id=ch[u'object_id']
     except: pass 
     try:
      created_time=ch[u'created_time']
     except: pass 
     try:
      updated_time=ch[u'updated_time']
     except: pass 
     try:
      shares=ch[u'shares']
     except: pass 
     try:
      comments=ch[u'comments']
     except: 
      comments=None
       
    
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         #print u_name,u_id
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
     
     
    if cs > 200: return 
    try:
     nova_pagina=pagin['next']     
     print 'get page:',(cs+1)
     get_feeds(id,(cs+1),nova_pagina)
    except: pass
    
    #=======================
    if cs == 0:
     print 'insert rows.id:',len(to_ins)
     for its in to_ins:
       [a,u_id,u_name]=its
       insere_usr('',u_id,u_name)
     to_ins=[]  
     time.sleep( 2 )
    
def obter_toke(id,pwd):
 url='https://graph.facebook.com/oauth/access_token?%20client_id=392136580875840&client_secret=a165cab020b8a99f4a12ef5d8aecdf91&grant_type=client_credentials' 
 
 
def alterat_token(id,pwd):
    url='https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id='+id+'&client_secret='+pwd+'&fb_exchange_token=SHORT_LIVED_ACCESS_TOKEN'
    print url
    file = urllib2.urlopen(url)
    rets=file.read ()
    print rets
        

def get_dist_u():
 cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno < 50 ") 
 p=[]
 isd=[]
 for results in cursor:
    ids=results[0]
    i=results[1]    
    p.append(ids)
    isd.append(i)
 
 return [p,isd]   

 
def index_subs():
 c=0
 while c < 100000 :   
  [usrs,fc]=get_dist_u()
  c2=0  
  for u in usrs:
    print 'Process usr:',u
    try:    
     get_feeds(u)
     print 'Close usr:',usrs[c2]
     if not err:
      conn.sql("update fcb_users set indexed='S' where i= "+str(fc[c2]))
      conn.commit()
     err=False 
    except: pass 
    c2+=1
  c+=1  
   
  
  
a=sys.argv[1]

 
try:
    get_feeds(a)
except: pass
conn.commit()
 


 
#get_usrs("100002272680690")

 