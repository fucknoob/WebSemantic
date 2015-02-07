# coleta paginas dos servidores mysql e deposita no maxdb

import sys
import string
sys.path.append('/home/mdnetsearc/public_html/Neural/MySQLdb')
sys.path.append('/Neural/mxdb')
        
import MySQLdb 
import maxdb

user = 'MIND'
pwd = 'MIND'

dbname = 'mindnet'
host = '127.0.0.1'

conn_mx = maxdb.connect (user, pwd, dbname, host)
iconn1= MySQLdb.connect(host='200.98.197.245', user='esyns1' , passwd='acc159753', db='esyns1') 
iconn2= MySQLdb.connect(host='200.98.197.232', user='esyns1_1' , passwd='acc159753', db='esyns1_1') 
iconn3= MySQLdb.connect(host='200.98.197.249', user='esyns1_2' , passwd='acc159753', db='esyns1_2') 

def get_pgs_to_index(connect,us):
  rts=[]
  try:
   cursor = connect.cursor ()
   cursor2 = connect.cursor ()
   cursor3 = connect.cursor ()
   cursor4 = connect.cursor ()
   cursor.execute ('select url_id,sval from urlinfo where url_id not in( select just_processed from pg_processed  ) and sname = \'body\' order by url_id  LIMIT 1,50')  
   resultSet = cursor.fetchall()
   for results in resultSet:     
     id= results[0]
     pg= results[1]
     url_d=''     
     #
     sql2="SELECT url FROM  url WHERE rec_id = " + str(id)
     cursor3.execute (sql2) 
     resultSet2 = cursor3.fetchall()
     for results2 in resultSet2:
        url_d=results2[0] 
        break     
     #    
     caption_S=''     
     cursor4.execute ('select sval from urlinfo where url_id = '+str(id)+' and sname = \'title\'  ')
     resultSet3 = cursor4.fetchall()
     for results3 in resultSet3:
        caption_S=results3[0] 
        break     
     # fecha a pagina
     sql_f=" insert  into pg_processed (just_processed)  values("+str(id)+")"
     print 'Cmd-insert('+us+'):',sql_f
     cursor2.execute (sql_f) 
     rts.append([(id),pg,url_d,caption_S])
  except Exception,err:
   print 'Error get_pages:',err  
  return rts
 
def verify_has_chars(s):
 s=s.upper()
 dr=False
 lts=set(string.ascii_uppercase)
 for d in s:
  if d in lts:
    dr=True
    break
 return dr  
 
def post_in_mx(pgs): 
 prep=conn_mx.prepare(" insert into web_cache(url,pg,termo,usr,purpose,processed,url_icon,url_picture,id_usr,name_usr,story,title,doc_id,tp,tps) values(?,?,'SYSTEM','igor.moraes','SYSTEM','N','','',?,'SYSTEM','',?,'','','F') ")
 for [id,data,url,caption_s] in pgs:
  #mt=[url,data,'SYSTEM','igor.moraes','SYSTEM','N','','',id,'SYSTEM','',caption ,'',''] 
  mt=[url,data,id,caption_s] 
  if verify_has_chars(data):
   #print 'mt:',mt
   try:   
    prep.execute(mt)
   except Exception,err:
    print 'Error post web item:',err ,mt 
 conn_mx.commit () 

cdc=4
#cdc=1 -> serv1
#cdc=2 -> serv1_1
#cdc=3 -> serv 1_2
#cdc=4 -> todos
#
 
if len(sys.argv) > 1:     
 cdc= int(sys.argv[1]) 
 
  
ind1=0
#while ind1 <= 100:
while ind1 <= 100:
  pgs1=[]
  pgs2=[]
  pgs3=[]
  
  if cdc in [1,4]:
   pgs1=get_pgs_to_index(iconn1,'1')
   
  if cdc in [2,4]:
   pgs2=get_pgs_to_index(iconn2,'2')
   
  if cdc in [3,4]:
   pgs3=get_pgs_to_index(iconn3,'3')
   
  pgst=[]
  #======================================== 
  for pg_t in pgs1:
   pgst.append(pg_t)
  #======================================== 
  for pg_t in pgs2:
   pgst.append(pg_t)
  #======================================== 
  for pg_t in pgs3:
   pgst.append(pg_t)
  #======================================== 
  post_in_mx(pgst)
  ind1+=1  
  conn_mx = maxdb.connect (user, pwd, dbname, host)
  iconn1= MySQLdb.connect(host='200.98.197.245', user='esyns1' , passwd='acc159753', db='esyns1') 
  iconn2= MySQLdb.connect(host='200.98.197.232', user='esyns1_1' , passwd='acc159753', db='esyns1_1') 
  iconn3= MySQLdb.connect(host='200.98.197.249', user='esyns1_2' , passwd='acc159753', db='esyns1_2') 
  



  
  