import simplejson
import urllib
import os
import sys
import urllib2
import thread
import time
import conn

conn= conn.conn_mx


def search_public(query):
    
    import gl_r
    result=gl_r.run(query,200) 
    return result



def get_public(query):   
  rt=[]
  res=search_public(query)  
  for r in res:
    lnk=r[0]
    title=r[1]
    body=r[2]
    
    id_msg='0'
    id_usr='0'
    usr=lnk
    dt=''
    msg=body
    to_usr=''
    msg_picture=''
    source=lnk
    #==
    rt.append([id_msg,id_usr,usr,dt,msg,to_usr,msg_picture,source])
  
  return rt



def get_purposes(usr):  
 resultSet = conn.sql ("SELECT DT,layout_onto FROM knowledge_manager where username='"+usr+"' and typ=4  and dt<>'language' order by i") 
 p=[]
 for results in resultSet:
    purps=results[0]
    p.append(purps)
    
 return p   

 
 
 

def post_termo(it,termo,purpose,user):
 [msg_id,id_usr,usr,dt,msg,to_usr,msg_picture,source]=it
 
 if usr== None: usr=''
 if msg==None : msg=''
 if source == None : source=''
 if msg_picture == None : msg_picture=''
 
 
 
 try:  
  msg=msg.encode('latin-1','ignore')   
 except : pass

 try:  
  source=source.encode('latin-1','ignore')   
 except : pass

 try:  
  msg_picture=msg_picture.encode('latin-1','ignore')   
 except : pass

 try:  
  id_usr=id_usr.encode('latin-1','ignore')   
 except : pass
 
 try:  
  msg_id=msg_id.encode('latin-1','ignore')   
 except : pass
 
 try:  
  usr=usr.encode('latin-1','ignore')   
 except : pass
 
 source=source.replace('\\n','')
 msg=msg.replace('\\n','')
 msg_picture=msg_picture.replace('\\n','')
 msg_picture=msg_picture.replace('\\n','')
 msg_id=msg_id.replace('\\n','')

 source=source.replace('\n','')
 msg=msg.replace('\n','')
 msg_picture=msg_picture.replace('\n','')
 msg_picture=msg_picture.replace('\n','')
 msg_id=msg_id.replace('\n','')
 
 id_usr=float(id_usr)

 
 mt=[source ,msg ,termo,user,purpose,'N',msg_picture ,msg_picture , id_usr ,usr,'' ,'' ,msg_id,'1111'] 
 try:
  conn.sqlX(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp,tps) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,'W') ",mt) 
 except Exception,e:
  print 'Error post web(1):',e,mt
 conn.commit() 
 
 
def processa_termo( query,usr,purpose ): 
  print 'Process post web...'
  public_rs=get_public(query)
  
  for sitem in public_rs:
    post_termo(sitem,query,purpose,usr)


def clean(USERNAME,termo,purpose):
 mt=[USERNAME,termo]
 conn.sqlX(" delete from web_cache where usr=? and  termo=? and tps='W'  ", mt)
 conn.commit () 
  
  
class thread_cntl:
 def __init__(self):
  self.finished=False    
 
def run_th(user,termo,purp,th,pth):
    cmd='python '+pth+'collect_it3.py '+ '"' + user +'\" \"'+ termo + ' \" \"' + purp + '"  '
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
    
    
def process_sentences(USERN,pth): 
 print 'User:',USERN,':',len(USERN)
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
 print 'Term.Len:',len(r1)
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
       
  
  
def hava_not_indexed(USER,TERMO):
 sqlcc='select * from web_cache where USR=? and termo= ? and indexed = \'N\' and  tps=\'W\' and rowno < 2 ' 
 resultSet= conn.sqlX  (sqlcc,[USER,TERMO])
 r1=[]
 fs=False
 for results in resultSet:
  fs=True
 
 return fs    
  
if len(sys.argv) > 1 :
 usr=parse(sys.argv[1])
 
 
 if len(sys.argv) > 2:
  username=usr
  termo=parse(sys.argv[2])
  pur_p=parse(sys.argv[3])
  if hava_not_indexed(usr,termo):
   print 'Index process not completed. Not start new process.'
  else:
   #===
   print 'Clean:',usr,termo,pur_p
   clean(username,termo,pur_p)
   #===
   try:
    processa_termo(termo,username,pur_p )
   except :
    pass  
  
 else:
  process_sentences(usr,remp(sys.argv[0]))   
 

conn.release()  
  
print 'Process [OK]'

