
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
conn= conn.conn_mx

import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')




#ch  = logging.StreamHandler ()
#lbuffer = StringIO ()
#logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

#log.addHandler(logHandler) 
#log.addHandler(ch) 

#import conn
#conn= conn.conn_mx


sql_insert_p='insert into fcb_users(user_name,id,u_name) values(?,?,?)'

def insere_usr(user_name,id,u_name): 
 #print 'insert:',[user_name,id,u_name] 
 try:
  conn.sqlX(sql_insert_p,([user_name,id,u_name]))
 except: pass 
     
  
def post_termo(it,termo,purpose,user,prep):
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
           
           conn.commit ()  
           #conn.sqlX(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?) ",mt)
           
          except Exception,err:
           print 'Error post facebook item:',err,mt 
           log.exception("")          
         else:
          pass 
 except:
  log.exception("")
 print 'post.term OK.' 
 
 
 
 
tokens=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]

tokens[17]='140340406129503|H-KmDtTR0gGy_vzPSHttzxgRS6k'
tokens[16]='338624246246319|-Dz-etLgJsEHiUihA4f9tAJBcQk'
tokens[15]='430951943650688|ZhUkw8DNJxhPnHVvGZ_GUiWVMDk'
tokens[14]='333625310075436|mFLhsN4JXIRHdhNrs2WBjl8UBc8'
tokens[13]='333862646714535|oGpuv_fwa74hQAOWEW8cJeTqZww'
tokens[12]='123277254516880|0UtUhYxFzfOhqaUQ6ryoG0NiGeA'
tokens[11]='326490144129558|FAGR3TiWLerriH_XUIHkQMJcpo8'

tokens[10]='426035490806918|vJftgwMhcHpY3wFVjjNcVZvwM7k' 
tokens[9]='386459591441254|A5t_SUmvz8icX_KZZ4VmxAulrBU'      
tokens[8]='133520460140565|sQ86q65pby1ek6CCngarywU51nA'      
tokens[7]='130476403781113|JnKbEIwbD6c7YL0lXMAaRZSbmdk'      
tokens[6]='210200879116690|l8ZTuij9batvtjScFqr9s_WQIxE'      
tokens[5]='130873000405995|5N0XoPtYqnfP0LBj8g-oeIO90MI'    
tokens[4]='511192748901567|PO75Ulo6CECzYc9qG-HjSsK6J-U'      
tokens[3]='551320231564366|0st6A6ZIHSTnytvrwPozGoFf260'      
tokens[2]='323755687729999|p-YAUWo1Sc-2hRYPqi9mHUu6_k0'      
tokens[1]='301848573269756|fDJa-7eeto12npt2JpdDO4X7P6E'      
tokens[0]='565607786802000|-zWYLRUaAsvZuJBtZ8NwddhYup0'      
 
 
def get_feeds(id,cs,c_url,to_ins,pg_id,user,processo=1):
 ac=[]
 idk=id
 errorcks=False
 try:
    args = {}
    
    print 'get page(process):',processo
    
    
    args['access_token'],args['limit'] =  tokens[processo-1],'500'

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
       
     if id != None:  
      object_id=id
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
       
    post_cmd(to_ins,pg_id,user,idk)
    post_termo(ac,'user','user','igor.moraes','user' )
 except Exception,err2:
  print 'Error(2.1):',err2
  log.exception("")
  reopen(idk)
  errorcks=True
 

 

    
def reopen(ids):      
  print 're-open:',ids
  try:
        conn.sql("insert into to_reopen(ids) values( "+str(ids) +")" )
        conn.commit()   
  except: 
   print 'Eror reopen:'
   log.exception("")
      
 
def post_cmd(arr,usr,u_nm,idk):   
  try:
   print 'insert rows.id(',idk,'):',len(arr)
   for its in arr:
     [a,u_id,u_name]=its
     insere_usr('',u_id,u_name)
     conn.commit()
  except: 
   log.exception("error insert rowds.id("+str(idk)+")")
  print 'insert',idk,' OK!!'
 
 

def parse(s):
 rt=[]
 tmp=''
 for s1 in s:
  if s1 == ',':
     rt.append(tmp)
     tmp=''
  else:
     tmp+=s1
 return rt      

a=sys.argv[1]
sents=parse(a) 
#print sents

get_feeds(sents[0],0,'',[],int(sents[1]),sents[2],int(sents[3]) )


 