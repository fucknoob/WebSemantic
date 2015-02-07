
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

import conn
conn= conn.conn_mx


sql_insert_p='insert into fcb_users(user_name,id,u_name) values(?,?,?)'

def insere_usr(user_name,id,u_name): 
 #print 'insert:',[user_name,id,u_name] 
 try:
  conn.sqlX(sql_insert_p,([user_name,id,u_name]))
 except: pass 
     
  
 
 
def get_feeds(id,cs,c_url,th,to_ins,pg_id,user):
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '392136580875840|rdRN2UGmcx_eJdJhRFvq_-F9O0Y','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
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
     
    post_cmd(to_ins,pg_id,user)
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2):',err2
  if cs == 0 and th != None: 
      th.finished=True
    
 
def get_feeds2(id,cs,c_url,th,to_ins,pg_id,user):
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '301848573269756|fDJa-7eeto12npt2JpdDO4X7P6E','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
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
     
        
    post_cmd(to_ins,pg_id,user)
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2):',err2
  if cs == 0 and th != None: 
      th.finished=True

      
      
def get_feeds3(id,cs,c_url,th,to_ins,pg_id,user):
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '323755687729999|p-YAUWo1Sc-2hRYPqi9mHUu6_k0','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
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
     
     
    post_cmd(to_ins,pg_id,user)
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2):',err2
  if cs == 0 and th != None: 
      th.finished=True
      
def get_dist_u_next():
 cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno < 2 ") 
 isd=[]
 for results in cursor:
    ids=results[0]
    i=results[1]    
    isd=[ids,i]
    break
 return isd

def get_dist_u_next2():
 cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno <= 5 ") 
 isd=[]
 for results in cursor:
    ids=results[0]
    i=results[1]    
    isd.append([ids,i])
    
 return isd

 
def post_cmd(arr,usr,u_nm):   
  a_lock.acquire()
  try:
   print 'insert rows.id:',len(arr)
   for its in arr:
     [a,u_id,u_name]=its
     insere_usr('',u_id,u_name)
   
   if True   : 
    conn.sql("update fcb_users set indexed='S' where i= "+str(usr))
    conn.commit()   
    print 'Close usr:',u_nm
  except: pass
  a_lock.release()
 
 
def index_subs():
 c=0
 if True :   
  indstr=1
  usrs=[]
  for u in get_dist_u_next2():
   usrs.append(u)
   indstr+=1
  #================================ 
  ths=[]
  for [u,uip] in usrs:
    print 'Process usr:',u
    try:    
     #get_feeds(u)
     #=============================
     ths.append(thread_cntl())
     thread.start_new_thread(get_feeds,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
       print 'wait for pages...',len(ths)-ind_col
       fnds_t=False
       ind_col=0
       for ths1 in ths:    
        if not ths1.finished:
         fnds_t=True
        if ths1.finished: 
          [u,uip]=get_dist_u_next()
          ind_col+=1
          ths.remove(ths1)
          #============================
          print 'Process usr:',u
          ths.append(thread_cntl())
          thread.start_new_thread(get_feeds,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
       time.sleep(10)

       
       
def index_subs2():
 c=0
 if True :   
  indstr=1
  usrs=[]
  for u in get_dist_u_next2():
   usrs.append(u)
   indstr+=1
  #================================ 
  ths=[]
  for [u,uip] in usrs:
    print 'Process usr:',u
    try:    
     #get_feeds(u)
     #=============================
     ths.append(thread_cntl())
     thread.start_new_thread(get_feeds2,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
       print 'wait for pages...',len(ths)-ind_col
       fnds_t=False
       ind_col=0
       for ths1 in ths:    
        if not ths1.finished:
         fnds_t=True
        if ths1.finished: 
          [u,uip]=get_dist_u_next()
          ind_col+=1
          ths.remove(ths1)
          #============================
          print 'Process usr:',u
          ths.append(thread_cntl())
          thread.start_new_thread(get_feeds2,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
       time.sleep(10)
       
 

        
index_subs()
index_subs2()
 

 