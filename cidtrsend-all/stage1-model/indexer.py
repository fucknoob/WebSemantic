#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''

import MySQLdb
import Identify 
import mdNeural


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
import mdLayout
import mdER
import mdNeural


conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
connTrace= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
conn4=MySQLdb.connect(host='dbmy0050.whservidor.com', user='mindnet_4' , passwd='acc159753', db='mindnet_4') 
conn3= MySQLdb.connect(host='dbmy0035.whservidor.com', user='mindnet_3' , passwd='acc159753', db='mindnet_3') 

def config_conns(conn_):
 cursor=conn_.cursor()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 
config_conns(connTrace) 
config_conns(conn4) 
config_conns(conn3) 
 

cursorTrace = connTrace.cursor ()

mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn3
mdNeural.conn4=conn4

def clean_Trace(usr):
   cursorTrace.execute ("delete from status_index where USERNAME = %s  ",(usr))
   conn.commit()

def finish_Trace(usr):
   cursorTrace.execute ("insert into status_index(USERNAME,MSG) values ( %s , 'OK-FINAL' ) ",(usr))
   
   
def traceQ(progress,usr,pg_numer,job,address,msg ):   
   linha=str(progress)+'|'+ msg+ ',Pg:'+str(pg_numer)+',Process:'+str(job)+',Address:'+address
   cursorTrace.execute ("insert into status_index(USERNAME,MSG) values ( %s , %s )  ",(usr,linha))
   print 'TraceQ:===================='
   print linha
   print '==========================='



def mount_node(term,id,purpose): 
 l=Identify.prepare_layout(id,purpose)
 allp=[]
 onto=Identify.prepare_data_by_ask(l, term,id,purpose,allp )
 return [onto,allp]

 
 
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
  print 'Request web:',query
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
  print 'Prepara search video:',query
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
  print 'Prepare query news:',query
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


def prepare_search_info(dts): # wikipedia
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  query=urllib.quote(qry)
  print 'Prepare query wiki:',query
  url_q='http://www.mind-net.com/Neural/request_md3.py/entry?query='+query+'&t=wiki'
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
  print 'Request reputc:',query
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
  print 'prepare query people:',query
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
 def __init__(self,Dt1=None,Dt2=None):
   self.dt1=Dt1
   self.dt2=Dt2
  

def post_pagina(endereco,conteudo_i,termo,usr,purp):
   conteudo=''
   for l in conteudo_i:
    conteudo+=(l+'\n')
   sql1="insert into WEB_CACHE (URL,PG,TERMO,PURPOSE,USR,SEMA_RESUME) values(%s,%s,%s,%s,%s,'')"
   if umisc.trim(conteudo) != "":
    try:
     cursor = conn.cursor ()
     cursor.execute (sql1,(MySQLdb.escape_string(endereco),MySQLdb.escape_string(conteudo),MySQLdb.escape_string(termo),purp,usr))
    except Exception,e1 :  print  e1
def process_termo(termo,usr,purp,start_c,path_j):
 # montar ontlogia
 objs_search=[]
 purposes=[]
 complements=[]
 [onto_basis,[allp,allp2]]=mount_node(termo,usr,purp)
 #=
 for sd in allp:
  for s2 in sd[1]:   
   purposes.append(s2)
 
 objs_search2=[] 
 #==================================
 for lay in onto_basis.nodesER:
  nodes2=lay.get_links('FACT')  
  for lay in nodes2:
    lay=lay.lr
    for top in lay.topicos:
     for dts in top.dt:
      if dts.upper() == "IDENTIFICADOR":
       for s in top.sinapses:
        for dts2 in s.nr.dt:
          if dts2 not in ['.',':','\'','"','?','?']:
           objs_search2.append(dts2)
 #==================================
 if len(objs_search2) > 0 :
  for sd in allp2:
   for s2 in sd[1]:   
    objs_search.append(s2)
  for sd in objs_search2:
    objs_search.append(sd)
 #==================================
 
 if len(objs_search) > 0 :
  def pg_open(addresss,th,pages,pgind,ind_emit,start_c):
   try:
    for address in addresss:
        lines_doc=[]
        if address != 'debug-url':
         opener = urllib2.build_opener()
         address=urllib.quote(address)
         print 'Open page:',address
         url='http://www.mind-net.com/get_Text.php?q='+address
         content = opener.open(url, '' ).read()
         tmpd=''
         for d in content:
          if d == '\n':
           tmpd=umisc.trim(tmpd)
           if tmpd.find('http://') > -1:
            ''' '''
           else:
            lines_doc.append(tmpd)
           tmpd=''
          else:
           tmpd+=d    
         #============
         pages.append(Task_C(pg_add,lines_doc))
         print 'Get content for page:',pgind,' was finished.Len:',len(lines_doc)
         pgind+=1
        else:
         for line_deb in entry_doc:
          lines_doc.append(line_deb)
         pages.append(Task_C(pg_add,lines_doc))
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
  results_wiki=[]
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
  elif 'wiki' in purposes:
    results_wiki=prepare_search_info(objs_search)
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
  for res in results_wiki:
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
   post_pagina(endereco,lines_doc,termo,usr,purp)
   progress=(cind2/len(pages))
   traceQ(progress,usr,cind2,1,endereco,'Processed page:' ) 
  
  #===  
  clean_Trace(usr)
  finish_Trace(usr)
  

def get_purposes(usr): # retorna os purposes(triggers) de pesquisas, cada um com suas fontes e propositos
 cursor = conn.cursor ()
 cursor.execute ("SELECT DT,layout_onto FROM knowledge_manager where username='"+usr+"' and typ=4  and dt<>'language' order by i") 
 resultSet = cursor.fetchall()
 p=[]
 for results in resultSet:
    purps=results[0]
    p.append(purps)
    
 return p   

def fecha_busca(termo,username): 
 #==
 sql1=" update clipping_info  set TRIGGER_AS='S' where USERNAME = %s  and termo= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,( username,MySQLdb.escape_string(termo)))
 #==
 
def limpa_resultados_anteriores(termo,username,purp): 
 #==
 sql1="delete from WEB_CACHE where TERMO= %s and USR=%s and PURPOSE= %s "
 cursor = conn.cursor ()
 cursor.execute (sql1,(MySQLdb.escape_string(termo),username,purp))
 #==
 
def process_sentences(start_c): 
 cursor = conn.cursor ()
 cursor.execute ("SELECT USERNAME,TERMO FROM clipping_info  where TRIGGER_AS='' or TRIGGER_AS is null LIMIT 0 , 50 ") # 50 rows por vez
 resultSet = cursor.fetchall()
 r1=[]
 for results in resultSet:
    username=results[0]
    termo=results[1] 
    r1.append([username,termo])
 for r in r1:
    [username,termo]=r 
    #===
    purps=get_purposes(username) # purposes-> layouts definidos dentro dos facts dos ractionlines escalados
    #=== limpas as buscas anteriores
    for pur_p in purps:
     limpa_resultados_anteriores(termo,username,pur_p)
     process_termo(termo,username,pur_p,start_c,sys.argv[0])
     return
    #=== fecha os ja executados
    fecha_busca(termo,username)
    

start_c=0

      
process_sentences(start_c)

 
 