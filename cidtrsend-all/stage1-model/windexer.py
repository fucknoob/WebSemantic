#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''

import MySQLdb
 

import base64
import calendar
import os
import rfc822
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse
import thread
import umisc
 
import subprocess
import string

 
conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 

def config_conns(conn_):
 cursor=conn_.cursor()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 
 
 
 
entry_doc =[]
 
#entry_doc = ['vectra é um bom carro com design inteligente, em composto por fibra de carbono restrito em carro de passeio ',' expectativas de carro com venda fortes','casa bom estado venda'] 
#entry('viagens melhores opções',['viagem para o nordeste é muito mais tranquilo, composto por translados mas restrito para criancas '])
 
#===================
def get_typ(obj,usr2):
  cursor = conn.cursor ()
  cursor.execute ("select TYP from DATA_BEHAVIOUR_PY where OBJETO='"+obj+"' and USERNAME='"+usr2+"' order by i") 
  resultSet = cursor.fetchall()
  typ=0
  for results in resultSet:
    typ=results[0]
  return  typ
#=============================================== 
 
def prepare_search_customlayouts(purposes,dts,usr):
 def clean_s(strc):

   strc=strc.replace('<subsign>','-')
   strc=strc.replace('<addsign>','+')
   strc=strc.replace('<divsign>','/')
   strc=strc.replace('<mulsign>','*')

   strc=strc.replace('<cite>','')
   strc=strc.replace('<em>','')
   strc=strc.replace('</em>','')
   strc=strc.replace('</cite>','')
   strc=strc.replace('<strong>','')
   strc=strc.replace('<string>','')
   strc=strc.replace('</string>','')
   strc=strc.replace('</strong>','')
   strc=strc.replace('<span style=\"text-decoration: underline;\">','')
   strc=strc.replace('<span','')
   strc=strc.replace('id=\"\">','')
   strc=strc.replace('</span>','')
   strc=strc.replace('<br>','\n')
   strc=strc.replace('<s>','')
   strc=strc.replace('</s>','')
   
   return strc
 
 #chamar os codigos 
 codes_Result=[]
 for dt in purposes:
  cursor = conn.cursor ()
  cursor.execute ("select CODE from DATA_BEHAVIOUR_CODE_PY where OBJETO='"+dt+"' and USERNAME='"+usr+"' order by i") 
  resultSet = cursor.fetchall()
  for results in resultSet:
    typ=get_typ(dt,usr)
    o=clean_s(results[0])
    code=(o)
    sr_int_cmd_param=dts
    if typ == 1: #executavel
     code+=' \n\nretorno_srt=run(sr_int_cmd_param)'
    else: # executa somente o codigo
     pass
    #================================== 
    try:
     exec(code, locals(), locals())
    except Exception,e:
     print 'Exec Error:',e    
    if typ == 1: #executavel
     # adicionar ao codes_Result o retorno_srt(lines->[endereco,dados] ) 
     if retorno_srt != None:
      codes_Result.append( retorno_srt )
 #===================
 return codes_Result 
 
def prepare_search(dts):
 
 if len( entry_doc ) > 0 : #debug direto
  return [[['debug-title','debug-url']]]
 
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=web'
  opener = urllib2.build_opener()
  data_Res = opener.open(url_q, '' ).read()
  lines=[]
  cl=[]
  tmp='';
  kind=1
  for ds in data_Res:
   if ds == '|':
    if len(tmp) > 0 :
     cl.append(tmp)
     tmp=''
    lines.append(cl)
    cl=[]
   elif ds == '^':
    cl.append(tmp)
    tmp=''     
   else:
    tmp+=ds
  rets.append(lines) 
  #
 return rets
 
def prepare_search_video(dts):
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=video'
  opener = urllib2.build_opener()
  data_Res = opener.open(url_q, '' ).read()
  lines=[]
  cl=[]
  tmp='';
  for ds in data_Res:
   if ds == '|':
    if len(tmp) > 0 :
     cl.append(tmp)
     tmp=''
    lines.append(cl)
    cl=[]
   elif ds == '^':
    cl.append(tmp)
    tmp=''     
   else:
    tmp+=ds
  rets.append(lines) 
  #
 return rets

def prepare_search_news(dts):
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=news'
  opener = urllib2.build_opener()
  data_Res = opener.open(url_q, '' ).read()
  lines=[]
  cl=[]
  tmp='';
  for ds in data_Res:
   if ds == '|':
    if len(tmp) > 0 :
     cl.append(tmp)
     tmp=''
    lines.append(cl)
    cl=[]
   elif ds == '^':
    cl.append(tmp)
    tmp=''     
   else:
    tmp+=ds
  rets.append(lines) 
  #
 return rets
 
def prepare_search_reputacao(dts):
 '''
   search all data
 ''' 
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=blog'
  opener = urllib2.build_opener()
  data_Res = opener.open(url_q, '' ).read()
  lines=[]
  cl=[]
  tmp='';
  for ds in data_Res:
   if ds == '|':
    if len(tmp) > 0 :
     cl.append(tmp)
     tmp=''
    lines.append(cl)
    cl=[]
   elif ds == '^':
    cl.append(tmp)
    tmp=''     
   else:
    tmp+=ds
  rets.append(lines) 
  #
 return rets

def prepare_search_people(dts):
 '''
   search all data
 ''' 
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=social'
  opener = urllib2.build_opener()
  data_Res = opener.open(url_q, '' ).read()
  lines=[]
  cl=[]
  tmp='';
  for ds in data_Res:
   if ds == '|':
    if len(tmp) > 0 :
     cl.append(tmp)
     tmp=''
    lines.append(cl)
    cl=[]
   elif ds == '^':
    cl.append(tmp)
    tmp=''     
   else:
    tmp+=ds
  rets.append(lines) 
  #
 return rets

 

class thread_cntl:
 def __init__(self):
  self.finished=False

class Task_C:
 def __init__(self,Dt1=None,Dt2=None,Dt3=None):
   self.dt1=Dt1
   self.dt2=Dt2
   self.dt3=Dt3
  

cursorpostp = conn.cursor ()
cursorpostl = conn.cursor ()
  
  
def post_pagina(endereco,conteudo_i,termo,usr,purp):
 try:
   conteudo=''
   for l in conteudo_i:
    conteudo+=(l+'\n')
   if umisc.trim(conteudo) != '':
    sql1="insert into WEB_CACHE (URL,PG,TERMO,PURPOSE,USR,SEMA_RESUME) values(%s,%s,%s,%s,%s,'')"
    cursorpostp.execute (sql1,(MySQLdb.escape_string(endereco),MySQLdb.escape_string(conteudo),MySQLdb.escape_string(termo),purp,usr))
 except :
   pass
   


def post_links(endereco,termo,usr,purp):
 try:
   sql1="insert into WEB_CACHE_LINKS (URL,TERMO,PURPOSE,USR,PROCESSED) values(%s,%s,%s,%s,'N')"
   if umisc.trim(endereco) != '':
    cursorpostl.execute (sql1,(MySQLdb.escape_string(endereco),MySQLdb.escape_string(termo),purp,usr))
 except:
  pass



def call_links(address,usr,termo,purpose):
  cmd="php /home/mindnet/public_html/get_links.php q="+address+" usr="+usr+" termo="+termo+" purpose="+purpose
  print 'Prepare cmd:',cmd
  os.system(cmd)  
  #proc = subprocess.Popen("php /home/mindnet/public_html/get_links.php q="+address, shell=True,stdout=subprocess.PIPE)
  #script_response = proc.stdout.read()
  #script_response=string.replace(script_response, 'Content-type: text/html\r\n\r\n', '') 
  #return script_response


def pg_open2(addresss,th,pages,pgind,ind_emit,start_c,usr,purp):
 print 'Start read page:',addresss
 try:
  for address in addresss:
      if address != 'debug-url':
       address=urllib.quote(address)
       pg_add=address
       call_links(address,usr,address,purp)
       pages.append(Task_C(pg_add,'',''))
       print 'Get content for page:',pgind,' was finished.'
       pgind+=1
      else:
       pages.append(Task_C(pg_add,'',''))
       print 'Get content for page:',pgind,' was finished.'
       pgind+=1
 except Exception,er :
  print er,'................'
 th.finished=True

  
def process_termo2(termos,usr,purp,start_c,path_j,layout):
 purposes=[]
 purposes.append(purp)
   
 #==================================
 objs_search=(termos)
 #==================================
 
 if True :
  #=====================================================  
  cind=0
  pages=[]
  kind=0
  print 'Init Collect...'
  #=====================================
  indres=0
  ths=[]
  ths2=[]
  #========================
  ind_emit=0
  thrsd=0
  tmp_pages=[]
  for res in objs_search:
     if thrsd > 45 : break
     pg_add=res
     ind_emit+=1
     if len(tmp_pages) >=50 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      thrsd+=1
      try:
        thread.start_new_thread(pg_open2,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c,usr,purp) )
      except:
        ths[len(ths)-1].finished=True
        pass      
      print 'Thread :',thrsd
     else:
      tmp_pages.append(pg_add)      
  if len(tmp_pages) > 0 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      thrsd+=1
      print 'Thread :',thrsd
      try:
       thread.start_new_thread(pg_open2,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c,usr,purp) )
      except:
       ths[len(ths)-1].finished=True
       pass
  
  ind_col=0
  #============================= 
  while True:
   print 'wait for pages...',len(ths)-ind_col
   fnds_t=False
   ind_col=0
   for ths1 in ths:    
    if not ths1.finished:fnds_t=True
    if ths1.finished: ind_col+=1
   if fnds_t:
    time.sleep(1)
    continue
   else:
    break
  
  
def process_termo(termo,usr,purp,start_c,path_j,layout):
 objs_search=[]
 purposes=[]
 purposes.append(purp)
   
 #==================================
 objs_search.append(termo)
 #==================================
 
 if len(objs_search) > 0 :
  def pg_open(addresss,th,pages,pgind,ind_emit,start_c):
   print 'Start read page:',addresss
   try:
    for address in addresss:
        lines_doc=[]
        links_k2=[]
        if address != 'debug-url':
         #======================
         opener = urllib2.build_opener()
         address=urllib.quote(address)
         url='http://www.mind-net.com/get_Text.php?q='+address
         content = opener.open(url, '' ).read()
         tmpd=''
         for d in content:
          if d == '\n':
           tmpd=umisc.trim(tmpd)
           lines_doc.append(tmpd)
           tmpd=''
          else:
           tmpd+=d    
         #======================
         opener = urllib2.build_opener()         
         url='http://www.mind-net.com/get_links2.php?q='+address
         content = opener.open(url, '' ).read()
         tmpd=''
         for d in content:
          if d == '\n':
           tmpd=umisc.trim(tmpd)
           links_k2.append(tmpd)
           tmpd=''
          else:
           tmpd+=d    
         #============
         pages.append(Task_C(pg_add,lines_doc,links_k2))
         print 'Get content for page:',pgind,' was finished.Len:',len(lines_doc),' links count:',len(links_k2)
         pgind+=1
        else:
         for line_deb in entry_doc:
          lines_doc.append(line_deb)
         pages.append(Task_C(pg_add,lines_doc,links_k2))
         print 'Get content for page:',pgind,' was finished.Len:',len(lines_doc)
         pgind+=1
         
    th.finished=True
   except Exception,er :
    print er,'................'
    th.finished=True
  #=====================================================  
  results_search=[]
  results_reputac=[]
  results_peop=[]
  results_news=[]
  results_videos=[]
  custom_layouts=[]
  #=====================================================
  if 'web' in purposes:
   results_search=prepare_search(objs_search)
  elif 'reputacao' in purposes:
   results_reputac=prepare_search_reputacao(objs_search)
  elif 'people' in purposes:
   results_peop=prepare_search_people(objs_search)
  elif 'news' in purposes:
   results_news=prepare_search_news(objs_search)
  elif 'video' in purposes:
   results_videos=prepare_search_video(objs_search)
  elif 'url' in purposes:
   results_search = [[['',objs_search[0]]]] #busca direta por url
  else:
   custom_layouts=prepare_search_customlayouts(purposes,objs_search,usr)
  
  #---
  
  result_onto_tree_er=[] # caracteristicas,descricoes,etc...
  result_onto_tree_bpm=[] # fluxo de acoes, sequencia de actions
  result_linked=[]
  # montar ontologia dos resultados
  cind=0
  pages=[]
  kind=0
  print 'Init Collect...'
  #=====================================
  indres=0
  ths=[]
  ths2=[]
  #========================
  ind_emit=0
  tmp_pages=[]
  for res in results_search:
   indaddrs=0
   for addrs in res:
     pg_add=addrs[1]
     ind_emit+=1
     if len(tmp_pages) >=5 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      thread.start_new_thread(pg_open,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c) )
     else:
      tmp_pages.append(pg_add)      
   cind+=1
   indres+=1
  if len(tmp_pages) > 0 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      thread.start_new_thread(pg_open,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c) )
  
  ind_col=0
  #============================= 
  while True:
   print 'wait for pages...',len(ths)-ind_col
   fnds_t=False
   ind_col=0
   for ths1 in ths:    
    if not ths1.finished:fnds_t=True
    if ths1.finished: ind_col+=1
   if fnds_t:
    time.sleep(10)
    continue
   else:
    break
  #=====================================  
  cind=0
  for res in results_reputac:
   for addrs in res:
    pg_add=addrs[1]
    pages.append(Task_C(pg_add,addrs[2])) 
    #==============
   cind+=1
  #=====================================
  cind=0
  for res in results_peop:
   for addrs in res:
    pg_add=addrs[1]
    pages.append(Task_C(pg_add,addrs[2])) 
    #==============
   cind+=1
  #=====================================
  cind=0
  for res in results_news:
   for addrs in res:
    pg_add=addrs[1]
    pages.append(Task_C(pg_add,addrs[2])) 
    #==============
   cind+=1
  #=====================================
  cind=0
  for res in results_videos:
   for addrs in res:
    pg_add=addrs[1]
    pages.append(Task_C(pg_add,addrs[2])) 
    #==============
   cind+=1
  #=====================================  
  cind=0
  for res in custom_layouts:
   for addrs in res:
    pg_add=addrs[0]
    pages.append(Task_C(pg_add,addrs[1])) 
    #==============
   cind+=1
  #=====================================
  print 'Collect OK!!',len(results_reputac),',',len(results_peop),',',len(results_news),',',len(results_videos),',',len(custom_layouts)
  cind2=0
  threads_fd=[]
  
  
  print 'Init Process pages:',len(pages)
  for pagina in pages:
   cind2+=1
   if pagina.dt1 == None: continue
   endereco=pagina.dt1
   lines_doc=pagina.dt2
   links=pagina.dt3
   post_pagina(endereco,lines_doc,endereco,usr,purp)
   for ln in links:
    post_links(ln,endereco,usr,purp)
   
   progress=(cind2/len(pages))
  
  


def fecha_busca(termo,username): 
 #==
 sql1=" update knowledge_manager  set srched='S' where USERNAME = %s  and dt= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,( username,MySQLdb.escape_string(termo)))
 #==
 
def fecha_busca2(termo,username): 
 #==
 sql1=" delete from WEB_CACHE_LINKS  where USR = %s  and url= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,( username,MySQLdb.escape_string(termo)))
 #==

def limpa_resultados_anteriores(termo,username,purp): 
 #==
 sql1="delete from WEB_CACHE where TERMO= %s and USR=%s and PURPOSE= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,(MySQLdb.escape_string(termo),username,purp))
 #==

def abre_buscas():
 cursor = conn.cursor ()
 cursor.execute ("update knowledge_manager set srched='N' where typ=2   ")  
 #================
 cursor = conn.cursor ()
 cursor.execute ("delete from WEB_CACHE  ") 
 #================
 cursor = conn.cursor ()
 cursor.execute ("delete from WEB_CACHE_LINKS  ") 
 
def process_sentences(start_c): 
 cursor = conn.cursor ()
 cursor.execute ("SELECT USERNAME,DT,LAYOUT_ONTO,DEST FROM knowledge_manager  where typ=2 and srched='N' LIMIT 0 , 50 ") # 50 rows por vez
 resultSet = cursor.fetchall()
 for results in resultSet:
    username=results[0]
    termo=results[1] 
    layout=results[2] 
    dest=results[3] 
    #r1.append([username,termo,layout,dest])
    limpa_resultados_anteriores(termo,username,dest)
    process_termo(termo,username,dest,start_c,sys.argv[0],layout)
    #=== fecha os ja executados
    fecha_busca(termo,username)
    

def process_sentences2(start_c): 
 def get_dist_usr():
     rt=[]
     cursor = conn.cursor ()
     cursor.execute ("SELECT distinct USERNAME  FROM knowledge_manager  where typ=2    ") #  
     resultSet = cursor.fetchall()
     for results in resultSet:
        username=results[0]
        rt.append(username)
     return rt
 
 usrs=get_dist_usr() 
 if True:
  for us in usrs:
     url=[]
     cursor = conn.cursor ()
     cursor.execute ("SELECT USR,URL,TERMO FROM WEB_CACHE_LINKS  where USR=%s LIMIT 0 , 3000 ",MySQLdb.escape_string(us)) # 3000 rows por vez
     resultSet = cursor.fetchall()
     username=''
     for results in resultSet:
        username=results[0]
        url.append(results[1]) 
        layout=results[2] 
        dest='url' 
     if len(url) > 0 :
      process_termo2(url,username,dest,start_c,sys.argv[0],layout)
     #=== fecha os ja executados
    
    
start_c=0

reindex=False

index_all_of=False #usando para indicar se vai indexar ou nao o web_cache_url

if len(sys.argv) > 1:     
 reindex= int(sys.argv[1]) >0
      
if len(sys.argv) > 2:     
 index_all_of= int(sys.argv[2]) >0
 
if reindex:
 abre_buscas() 
 
process_sentences(start_c)

if index_all_of:
 process_sentences2(start_c)

 
 