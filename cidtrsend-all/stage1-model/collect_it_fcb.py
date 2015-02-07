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


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 



def search_events(query):
    url='http://graph.facebook.com/search?q='+query+'&type=event&start=1&limit=100'
    result = simplejson.load(urllib.urlopen(url))
    if 'Error' in result:
        raise  esult['Error']
    return result
 
 
def search_pages(query):
    url='http://graph.facebook.com/search?q='+query+'&type=page&start=1&limit=100'
    result = simplejson.load(urllib.urlopen(url))
    if 'Error' in result:
        raise  esult['Error']
    return result

def search_public(query):
    try:
        ind=1
        i=1
        res=[]
        trys=0
        try:
         args = {}
         args["q"]=query
         query=urllib.urlencode(args)
        except Exception,e:
          print 'err:',type(query),':','->',e        
        print 'query:',query
        while i <= 50:
         url='http://graph.facebook.com/search?'+query+'&type=post&start='+str(ind)+'&limit=100&locale=pt_BR'
         print 'Get public results:start:',ind
         errc=False
         result=[]
         content_dt=[]
         try:
          content_dt=urllib.urlopen(url)
          result = simplejson.load(content_dt)
          if 'Error' in result:
               trys+=1
               if trys >  5:
                ind+=100
                i+=1
                errc=True
                print 'Try:',trys
                continue
            #raise  result['Error']         
         except Exception,e:
           log.exception('[Error in get-public.url.load(',e,')]') 
           print 'result:',result,content_dt
           trys+=1
           if trys >  5:
            ind+=100
            i+=1
            errc=True
            print 'Try:',trys
         if errc:continue        
         errc=False
         trys=0
         ind+=100
         i+=1
         res.append(result)
    except Exception,e: 
      log.exception('[Error in get-public]') 
    return res
    
    
def get_usrs(uid):
    fql='SELECT uid2 FROM friend WHERE uid1 = '+uid
    args = {}
    args["query"], args["format"] , args['access_token'] = fql, "json" ,'AAAAAAITEghMBABvjybLijPQ5t3VBPPDHj0YIPldbnDObcJhxmRyWvGWT5I3WHGtODQ1ookC38oYQnR1F4oBhLIpcj7dtjoVa4Da9qD03l4hIHQlv'

    url='http://api.facebook.com/method/fql.query?'+ urllib.urlencode(args)
    file = urllib2.urlopen("https://api.facebook.com/method/fql.query?" + urllib.urlencode(args))
    #rets=file.read ()
    #print rets
    #
    result = simplejson.load(file)
    return result
    
    
def get_events(query):
    
  r=search_events(query)    
  returns=[]
  msg_link=None
  r2=r['data']
  for ch in r2:
     msg_id=ch['id'] 
     from_msg=[ch['id'],ch['name']]
     
     msg_story=None

     #===
     msg_caption=None
     msg_description=None
     msg_story_flags=[]
     msg_picture=None
     
     msg_name=ch['name']
     try:
      msg_description=ch['location']
     except: pass 
     msg_icon=None
     msg_type='9998' # mark event
     msg_application=None
     msg_created_time=ch['start_time']
     msg_updated_time=ch['end_time']
     msg_message=None
     try:
      msg_message=''
     except:pass
     msg_likes=[]      
     
     returns.append( [ msg_id,from_msg,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message ] )
  return returns    
   
def get_pages(query):
    
  r=search_pages(query)    
  returns=[]
  r2=r['data']
  c2=len(r2)
  i=0
  for ch in r2:
     i+=1
     print 'Page :',i,' of',c2
     msg_id=ch['id'] 
     #========================
     url2='http://graph.facebook.com/'+msg_id
     result2 = simplejson.load(urllib.urlopen(url2))
     if 'Error' in result2:
        raise  esult['Error']
     
     #========================
     from_msg=[ch['id'],ch['name']]
     #=     
     msg_story=None
     #===
     msg_caption=None
     msg_description=None
     msg_story_flags=[]
     msg_picture=None
     try:
      msg_picture=result2['picture']
     except : pass 
     msg_link=result2['link']
     msg_name=result2['username']
     try:
      msg_caption=result2['category']
     except: pass
     try:
      msg_description=result2['description']
     except: pass 
     try:
      msg_description+= ' ' + result2['company_overview']
     except: pass 
     msg_icon=None
     msg_type='9999'  # definidor de perfil
     msg_application=None
     try:
      msg_application=result2['website']
     except:pass
     msg_created_time=None
     msg_updated_time=None
     msg_message=None
     try:
      msg_message=result2['message']
     except:pass
     msg_likes=[result2['likes'],result2['likes']]
     
     msg_phone=None
     try:
      msg_phone=result2['phone']
     except: pass
     msg_location=[]
     
     try:
       street=''
       city=''
       country=''
       zip=''
       latitude=''
       longitude=''
       location=result2['location']
       try:
        street=result2['street']
       except:pass
       try:
        city=result2['city']
       except:pass
       try:
        country=result2['country']
       except:pass
       try:
        zip=result2['zip']
       except:pass
       try:
        latitude=result2['latitude']
       except:pass
       try:
        longitude=result2['longitude']
       except:pass
       msg_location=[street,city,country,zip,latitude,longitude]
     except:pass
     
     returns.append( [ msg_id,from_msg,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message,msg_location,msg_phone ] )
  return returns   

def get_public(query):
  returns=[]
  for r in search_public(query) :  
      r2=r['data']
      for ch in r2:
         msg_id=ch['id'] 
         from_msg=[]
         _from = ch['from']
         if _from != None:
          from_msg=[_from['id'],_from['name']]
         
         msg_story=None
         try :
          msg_story=ch['story'] 
         except: pass
         #===
         msg_caption=None
         msg_description=None
         msg_story_flags=[]
         msg_picture=None
         try:
          story_flags=ch['story_tags']
          if story_flags != None:
            msg_story_flags=[ story_flags['name'],story_flags['offset'],story_flags['length']] 
         except : pass
         try:
          msg_picture=ch['picture']
         except : pass 
         msg_link=''
         try:
          msg_link=ch['link']
         except: pass
         msg_name=''
         try:
          msg_name=ch['name']
         except: pass 
         msg_caption=''
         try:
          msg_caption=ch['caption']
         except: pass
         msg_description=''
         try:
          msg_description=ch['description']
         except: pass 
         msg_icon=''
         try:
          msg_icon=ch['icon']
         except:pass      
         msg_type=ch['type']
         msg_application=''
         msg_created_time=''
         msg_updated_time=''
         try:
          msg_application=ch['application']
         except:pass 
         try:
          msg_created_time=ch['created_time']
         except:pass 
         try:
          msg_updated_time=ch['updated_time']
         except:pass 
         msg_message=None
         try:
          msg_message=ch['message']
         except:pass
         msg_likes=[]
         try:
          likes=ch['likes']
          likes_Dt=likes['data']
          for dt in likes_Dt:
           nm=dt['name']
           id=dt['id']
           msg_likes.append([id,nm])
         except : pass
         
         returns.append( [ msg_id,from_msg,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message ] )
  return returns



def get_purposes(usr):  
 cursor = conn.sql("SELECT DT,layout_onto FROM knowledge_manager where username='"+usr+"' and typ=4  and dt<>'language' order by i") 
 p=[]
 for results in cursor:
    purps=results[0]
    p.append(purps)
 
 return p   

 

def post_termo2(it,termo,purpose,user):
 [ msg_id,from_msg,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message,msg_location,msg_phone ]=it
 
 if msg_phone == None : msg_phone=''
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
 
 msg_caption=msg_caption+' '+msg_name.encode('latin-1','ignore')
 
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
  msg_caption=msg_caption.encode('latin-1','ignore')   
 except : pass
 try:  
  msg_type=msg_type.encode('latin-1','ignore')   
 except : pass
 
 street=''
 city=''
 country=''
 zip=''
 latitude=''
 longitude=''
 
 if len(msg_location) > 0 :
  [street,city,country,zip,latitude,longitude]=msg_location
 
 rpg=(msg_message +' '+msg_description)
 
 msg_link=msg_link.replace('\n','')
 rpg=rpg.replace('\n','')
 msg_icon=msg_icon.replace('\n','')
 msg_picture=msg_picture.replace('\n','')
 msg_story=msg_story.replace('\n','')
 msg_caption=msg_caption.replace('\n','')
  
 msg_link=msg_link.replace('\\n','')
 rpg=rpg.replace('\\n','')
 msg_icon=msg_icon.replace('\\n','')
 msg_picture=msg_picture.replace('\\n','')
 msg_story=msg_story.replace('\\n','')
 msg_caption=msg_caption.replace('\\n','')

 mt=[msg_link , rpg,termo,user,purpose,'N',msg_icon ,msg_picture ,from_msg[0] ,from_msg[1].encode('latin-1','ignore'),msg_story ,msg_caption ,msg_id,msg_type,msg_phone,street,city,country,zip,latitude,longitude]
 
 #prep=conn.prepare(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp,phone,street,city,country,zip,latitude,longitude) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ")
 #prep.execute(mt)
 
 conn.commit () 


 
def post_termo(it,termo,purpose,user,prep):
 [ msg_id,from_msg,msg_story,msg_caption,msg_description,msg_picture,msg_link,msg_name,msg_icon,msg_type,msg_likes,msg_message ]=it
 
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
 
 #from_msg[0]=float(from_msg[0])
 #if umisc.trim(msg_id) == '' : msg_id='-'
 
 conn.sqlX("insert into web_cache_sign(ID,ID_USR) values(?,?)",([msg_id,0]))
 
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
  from_msg[0]=float(from_msg[0])
  if umisc.trim(msg_id) == '' : msg_id='-'

  #insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
  
  mt=[msg_link ,all_msg,termo,user,purpose,'N',msg_icon ,msg_picture ,from_msg[0],from_msg[1],msg_story ,msg_caption ,msg_id,msg_type]
  #mt=[msg_link ,all_msg]
  try:   
   #prep=conn.prepare(" insert into web_cache(url,pg) values(?,?) ")
   
   prep.execute(mt)
   
   #conn.sqlX(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?) ",mt)
   
  except Exception,err:
   print 'Error post facebook item:',err,mt 
   log.exception("")
  conn.commit () 
 else:
  #print 'Not enougth msg:[',all_msg,']'
  pass
 
def processa_termo( query,usr,purpose,prep ): 
  print 'Process public post facebook...'
  public_rs=get_public(query)
  print 'Public post:',len(public_rs)
  #print 'CT:',public_rs
  
  #print 'Process pages facebook...'
  #pages_rs=get_pages(query)
  
  '''
  print 'Process events facebook...'
  events_rs=get_events(query)
  intl=len(events_rs)
  '''
    
  itnr=1
  for sitem in public_rs:
   try:
    #print 'Post item:',itnr
    post_termo(sitem,query,purpose,usr,prep )
   except: 
    print 'Error in post public-post:',sitem 
    log.exception("post-public:")
   itnr+=1 
    
    
  #for sitem in pages_rs:
  #  post_termo2(sitem,query,purpose,usr )
  
  #print events_rs
  ''' 
  idxl=0
  while idxl < intl:
   try:
    sitem = events_rs[idxl]
    post_termo(sitem,query,purpose,usr,prep )
   except:
     print 'Error in post ev:',sitem   
   idxl+=1
  '''
  
def clean(USERNAME,termo,purpose):
 mt=[USERNAME,termo]
 conn.sqlX(" delete from web_cache where usr=? and  termo=? and tps='F'  ", mt)
 conn.commit () 
    
class thread_cntl:
 def __init__(self):
  self.finished=False    
 
def run_th(user,termo,purp,th,pth):
    cmd='python '+pth+'collect_it.py '+ '"' + user +'\" \"'+ termo + ' \" \"' + purp + '"  '
    os.system(cmd)
    th.finished=True

  
   
def remp(s):
 r=''
 i=len(s)-1
 pos=0
 while i >= 0 :
  if s[i] == '\\' or s[i] == '/': 
   pos=i
   break
  r=s[i]+r
  i-=1
 return s[:pos+1]
     
def parse(s):
 r=''
 for d in s:
  kc=ord(d)
  if ( kc >= ord('a') and kc <= ord('z') ) or (kc >= ord('A') and kc <= ord('Z') )   or (kc >= ord('0') and kc <= ord('9') ) or d in ['.',',','!','?','\'','~','-']:
    r+=d
 return r

 
def clean_marcador():
 conn.sql("delete from web_cache_sign")
 conn.commit()
 # temporario dos usuarios, para coleta e depois limpesa geral
 conn.sql("delete from web_cache where termo <> 'SYSTEM' and purpose <> 'SYSTEM'")
 conn.commit()
 

def entry_Sents(termos,usr):     
 for term in termos:
   pur_p=term
   termo=term
 
   print 'Clean:',usr,termo,pur_p
   clean(usr,termo,pur_p)
   
 for term in termos:
   pur_p=term
   termo=term
 
   #===
   prep=None
  
   prep=conn.prepare(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp,tps) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,'F') ")
   try:
    processa_termo(termo,usr,pur_p ,prep)
   except Exception,ecr :
    print 'Error on process web_ache:',ecr
    pass    
 
 