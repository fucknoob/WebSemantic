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
    url='http://graph.facebook.com/search?q='+query+'&type=post&start=1&limit=100'
    result = simplejson.load(urllib.urlopen(url))
    if 'Error' in result:
        raise  result['Error']
    return result


    
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
    
  r=search_public(query)    
  returns=[]
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
      msg_message=messagech['message']
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
 
 
 if umisc.trim(all_msg) <> '': 
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
  if umisc.trim(msg_id) == '' : msg_id='-'
  if umisc.trim(msg_type) == '' : msg_type='-'
  from_msg[0]=float(from_msg[0])

  #insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
  
  mt=[msg_link ,all_msg,termo,user,purpose,'N',msg_icon ,msg_picture ,from_msg[0],from_msg[1],msg_story ,msg_caption ,msg_id,msg_type]
  #mt=[msg_link ,all_msg]
  try:   
   #prep=conn.prepare(" insert into web_cache(url,pg) values(?,?) ")
   
   prep.execute(mt)
   
   #conn.sqlX(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?) ",mt)
   
  except Exception,err:
   print 'Error post facebook item:',err,mt 
  conn.commit () 
 
def processa_termo( query,usr,purpose,prep ): 
  print 'Process public post facebook...'
  public_rs=get_public(query)
  
  #print 'Process pages facebook...'
  #pages_rs=get_pages(query)
  
  print 'Process events facebook...'
  events_rs=get_events(query)
  intl=len(events_rs)
  
    
  
  for sitem in public_rs:
   try:
    post_termo(sitem,query,purpose,usr,prep )
   except: 
    print 'Error in post public-post:',sitem 
    
    
  #for sitem in pages_rs:
  #  post_termo2(sitem,query,purpose,usr )
  
  #print events_rs
  idxl=0
  while idxl < intl:
   try:
    sitem = events_rs[idxl]
    post_termo(sitem,query,purpose,usr,prep )
   except:
     print 'Error in post ev:',sitem   
   idxl+=1
    
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


def hava_not_indexed(USER,TERMO):
 sqlcc='select * from web_cache where USR=? and termo= ? and indexed = \'N\' and  tps=\'F\' and rowno < 2 ' 
 resultSet= conn.sqlX  (sqlcc,[USER,TERMO])
 r1=[]
 fs=False
 for results in resultSet:
  fs=True
 
 return fs

 
def process_sentences(USERN,pth): 
 USERN2='\''+USERN+'\'' 
 sqlcc=' select USERNAME,TERMO from clipping_info  where USERNAME= '+USERN2 
 resultSet= conn.sql  (sqlcc)
 r1=[]
 for results in resultSet:
    username=results[0]
    termo=results[1] 
    r1.append([username,termo])
 #==========================    
 finds=0
 ths=[]
 for r in r1:
    [username,termo]=r 
    if True:    
     pur_p=termo
     if finds >= 5:
      ids=len(ths)
      ids1=0
      #========================================
      while ids1 < ids:
       if not ths[ids1].finished:
        ids1=0
        time.sleep(5)
        print 'Wait for....'
        continue
       ids1+=1
      ths=[]
     else:
      th=thread_cntl() 
      ths.append(th)
      thread.start_new_thread(run_th,(username,termo,pur_p,th,pth))
     finds+=1
 if True:
      ids=len(ths)
      ids1=0
      #========================================
      while ids1 < ids:
       if not ths[ids1].finished:
        ids1=0
        time.sleep(5)
        print 'Wait for....'
        continue
       ids1+=1
      ths=[]

     

  
if len(sys.argv) > 1 :
 usr=parse(sys.argv[1])
 
 if len(sys.argv) > 2:
  termo=parse(sys.argv[2])
  pur_p=parse(sys.argv[3])
  
  if hava_not_indexed(usr,termo):
   print 'Index process not completed. Not start new process.'
  else: 
   #===
   print 'Clean:',usr,termo,pur_p
   clean(usr,termo,pur_p)
   #===
   prep=None
  
   prep=conn.prepare(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp,tps) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,'F') ")
   try:
    processa_termo(termo,usr,pur_p ,prep)
   except :
    pass    
 else:
  process_sentences(usr,remp(sys.argv[0]))   
  

#just get friends of login user
#r=get_usrs('1773861276')

conn.release()



print 'Process [OK]'