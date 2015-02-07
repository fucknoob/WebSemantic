
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
     
  
def post_termo(it,termo,purpose,user,prep):
 a_lock.acquire()
 print 'post text:',len(it)
 try:
     #ac.append( [ from_id,object_id,msg_story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     prep=conn.prepare(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp,tps) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,'F') ")
     for its in it:
         [ from_msg,msg_id,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message ]=its 
         
         if msg_message== None: msg_message=''
         if msg_caption== None: msg_caption=''
         if msg_description== None: msg_description=''
         if msg_name== None: msg_name=''
         if msg_story== None: msg_story=''
         if msg_picture== None: msg_picture=''
         if msg_link== None: msg_link=''
         if msg_icon== None: msg_icon=''
         if msg_type== None: msg_type=''
         if len(from_msg) == 0: from_msg.append(['0',msg_name])
         
         
         try:  
          msg_caption=msg_caption.encode('latin-1','ignore')   
         except : pass

         try:  
          m1=msg_name.encode('latin-1','ignore')
         except Exception,err : print 'Erro msg_caption(1):',err,msg_caption,msg_name

         try:  
          msg_caption=msg_caption+' '+m1
         except Exception,err : print 'Erro msg_caption(2):',err,msg_caption,msg_name
         

         try:  
          msg_link=msg_link.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_message=msg_message.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_description=msg_description.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_icon=msg_icon.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_picture=msg_picture.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_story=msg_story.encode('latin-1','ignore')   
         except : pass
         try:  
          msg_type=msg_type.encode('latin-1','ignore')   
         except : pass
         try:  
          from_msg[1]=from_msg[1].encode('latin-1','ignore')
         except : pass
         try:  
          msg_id=msg_id.encode('latin-1','ignore')
         except : pass
         
          
         
         msg_link=msg_link.replace('\n','')
         msg_icon=msg_icon.replace('\n','')
         msg_picture=msg_picture.replace('\n','')
         msg_story=msg_story.replace('\n','')
         msg_caption=msg_caption.replace('\n','')
         msg_message=msg_message.replace('\n','')
         msg_description=msg_description.replace('\n','')
          
         msg_link=msg_link.replace('\\n','')
         msg_message=msg_message.replace('\\n','')
         msg_description=msg_description.replace('\\n','')
         msg_icon=msg_icon.replace('\\n','')
         msg_picture=msg_picture.replace('\\n','')
         msg_story=msg_story.replace('\\n','')
         msg_caption=msg_caption.replace('\\n','')
         
         all_msg=msg_message +' '+msg_description 
         
         if msg_type == u'status':
          all_msg=msg_story 
          msg_link='{owner}'      
         
         #from_msg[0]=float(from_msg[0])
         #if umisc.trim(msg_id) == '' : msg_id='-'
         
         #conn.sqlX("insert into web_cache_sign(ID,ID_USR) values(?,?)",([msg_id,0]))
         
         if umisc.trim(all_msg) <> '' or umisc.trim(msg_caption) <> '': 
          if umisc.trim(msg_link) == '' : msg_link='-'
          if umisc.trim(all_msg) == '': all_msg='-'
          if umisc.trim(termo) == '' : termo='-'
          if umisc.trim(user) == '' : user='-'
          if umisc.trim(purpose) == '' :purpose ='-'
          if umisc.trim(msg_icon) == '' :msg_icon ='-'
          if umisc.trim(msg_picture) == '' : msg_picture='-'
          if umisc.trim(from_msg[0]) == '' : from_msg[0]='0'
          if umisc.trim(from_msg[1]) == '' :from_msg[1] ='-'
          if umisc.trim(msg_story) == '' :msg_story ='-'
          if umisc.trim(msg_type) == '' : msg_type='-'
          from_msg=float(from_msg)
          if umisc.trim(msg_id) == '' : msg_id='-'

          #insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
          
          mt=[msg_link ,all_msg,termo,user,purpose,'N',msg_icon ,msg_picture ,from_msg,'',msg_story ,msg_caption ,msg_id,msg_type]
          #mt=[msg_link ,all_msg]
          try:   
           #prep=conn.prepare(" insert into web_cache(url,pg) values(?,?) ")
           
           prep.execute(mt)
           
           #conn.sqlX(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?) ",mt)
           
          except Exception,err:
           print 'Error post facebook item:',err,mt 
           log.exception("")          
         else:
          #print 'Not enougth msg:[',all_msg,']'
          pass 
 except:
  log.exception("")
 conn.commit ()  
 a_lock.release()
 
 
 
def get_feeds(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    #print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '565607786802000|-zWYLRUaAsvZuJBtZ8NwddhYup0','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.1):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True
    
 
def get_feeds2(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
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
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.2):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True

      
      
def get_feeds3(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
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
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.3):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True
      
      
def get_feeds4(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '551320231564366|0st6A6ZIHSTnytvrwPozGoFf260','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.4):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True   
      
      
#
def get_feeds5(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '511192748901567|PO75Ulo6CECzYc9qG-HjSsK6J-U','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.5):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True       
      
 
#
def get_feeds6(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '130873000405995|5N0XoPtYqnfP0LBj8g-oeIO90MI','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.6):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True         
      
def get_feeds7(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '210200879116690|l8ZTuij9batvtjScFqr9s_WQIxE','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.7):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True        
      
      
def get_feeds8(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '130476403781113|JnKbEIwbD6c7YL0lXMAaRZSbmdk','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.8):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True       
      
      
def get_feeds9(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '133520460140565|sQ86q65pby1ek6CCngarywU51nA','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.9):',err2
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True       
      
      
def get_feeds10(id,cs,c_url,th,to_ins,pg_id,user):
 ac=[]
 idk=id
 try:
    args = {}
    
    print 'get page:',(cs)
    
    args['access_token'],args['limit'] =  '386459591441254|A5t_SUmvz8icX_KZZ4VmxAulrBU','500'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    if c_url != '':
     url=c_url
    
    file = urllib2.urlopen(url)

    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    msg_i=1
    object_id=''
    link=''
    icon=''
    type=''
    message=''
    created_time=''
    story=''
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
      
     try:
      story=ch[u'story']
     except: 
      story=''
       
     
     from_msg=''
     msg_story=''
     msg_caption=''
     msg_likes='0'
     msg_name=''
     msg_picture=''
     msg_description=''
     from_id=''
     if _from != None:
      msg_name=_from[u'name']
      from_id=_from[u'id']
      
     ac.append( [ from_id,object_id,story,msg_caption,msg_description,msg_picture,link,msg_name,icon,type,msg_likes,message ] )
     
     message=''
     
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=''
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         message='{like}'
         #print u_name,u_id
         ac.append( [ u_id,object_id,'','','','',link,u_name,icon,type,'0',message ] )
         #=================
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
       
    post_cmd(to_ins,pg_id,user)
    post_termo(ac,'user','user','igor.moraes','user' )
    if cs ==0 and th != None:
      th.finished=True
 except Exception,err2:
  print 'Error(2.10):',err2  
  log.exception("")
  reopen(idk)
  if cs == 0 and th != None: 
      th.finished=True       
      
def reopen(ids):      
  a_lock.acquire()
  print 're-open:',ids
  try:
        conn.sql("update fcb_users set indexed='N' where ID=\'"+str(ids) +'\'' )
        conn.commit()   
  except: 
   print 'Eror reopen:'
   log.exception("")
  a_lock.release()
      
def get_dist_u_next():
  a_lock.acquire()
  isd=[]
  try:
     cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno < 2 ") 
     for results in cursor:
        ids=results[0]
        i=results[1]    
        isd=[ids,i]
        conn.sql("update fcb_users set indexed='S' where i= "+str(i))
        conn.commit()   
        print 'Close usr(1):',ids
        break
  except: pass
  a_lock.release()
  return isd

def get_dist_u_next2():
  a_lock.acquire()
  isd=[]
  closes=[]
  try:
     cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno <= 10 ") 
     isd=[]
     for results in cursor:
        ids=results[0]
        i=results[1]    
        isd.append([ids,i])
        closes.append([i,ids])
        #==============
     for [cl,u_nm] in closes:   
        conn.sql("update fcb_users set indexed='S' where i= "+str(cl))
        print 'Close usr(2):',u_nm
     conn.commit()   
     #==
  except Exception, err2: 
   print 'Error collect:',err2
  a_lock.release()
  return isd

 
def post_cmd(arr,usr,u_nm):   
  a_lock.acquire()
  try:
   print 'insert rows.id:',len(arr)
   for its in arr:
     [a,u_id,u_name]=its
     insere_usr('',u_id,u_name)
  except: pass
  a_lock.release()
 
 
def index_subs(j1,j2):
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
     try:
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
     except: pass
     time.sleep(10)

       
       
def index_subs2(j1,j2):
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
     try:
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
     except:pass     
     time.sleep(10)
       
 
def index_subs3(j1,j2):
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
     thread.start_new_thread(get_feeds3,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds3,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)
       
        
def index_subs4(j1,j2):
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
     thread.start_new_thread(get_feeds4,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds4,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)        
        
        
def index_subs5(j1,j2):
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
     thread.start_new_thread(get_feeds5,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds5,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)            


def index_subs6(j1,j2):
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
     thread.start_new_thread(get_feeds6,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds6,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)      
        
        
def index_subs7(j1,j2):
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
     thread.start_new_thread(get_feeds7,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds7,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10) 
     
     
def index_subs8(j1,j2):
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
     thread.start_new_thread(get_feeds8,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds8,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)      
     
     
def index_subs9(j1,j2):
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
     thread.start_new_thread(get_feeds9,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds9,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)      
     
     
def index_subs10(j1,j2):
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
     thread.start_new_thread(get_feeds10,(u,0,'',ths[len(ths)-1],[],uip,u ) )
     #==  
    except:pass 
  ind_col=0
  while True:
     print 'wait for pages...',len(ths)-ind_col
     try:
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
          thread.start_new_thread(get_feeds10,(u,0,'',ths[len(ths)-1],[],uip,u ) )
          #============================
     except: pass
     time.sleep(10)      
     
thread.start_new_thread(index_subs,(1,1) )
thread.start_new_thread(index_subs2,(1,1) )
thread.start_new_thread(index_subs3,(1,1) )
thread.start_new_thread(index_subs4,(1,1) )
thread.start_new_thread(index_subs5,(1,1) )
thread.start_new_thread(index_subs6,(1,1) )
thread.start_new_thread(index_subs7,(1,1) )
thread.start_new_thread(index_subs8,(1,1) )
thread.start_new_thread(index_subs9,(1,1) )
thread.start_new_thread(index_subs10,(1,1) )

while True:
 time.sleep(100)
 
 