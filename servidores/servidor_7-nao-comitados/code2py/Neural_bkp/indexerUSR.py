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
import mutex

import gc

import logging
from StringIO import StringIO
import datetime

logging.basicConfig(level=logging.DEBUG)
logs = logging.getLogger('indexerUSR')


ch  = logging.StreamHandler()
lbuffer = StringIO()
logHandler = logging.StreamHandler(lbuffer)

logs.addHandler(logHandler) 
logs.addHandler(ch) 



conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
connTrace= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
conn4=MySQLdb.connect(host='dbmy0050.whservidor.com', user='mindnet_4' , passwd='acc159753', db='mindnet_4') 
conn3= MySQLdb.connect(host='dbmy0035.whservidor.com', user='mindnet_3' , passwd='acc159753', db='mindnet_3') 
conn5= MySQLdb.connect(host='dbmy0039.whservidor.com', user='mindnet_5' , passwd='acc159753', db='mindnet_5') 

def config_conns(conn_):
 cursor=conn_.cursor()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 
config_conns(connTrace) 
config_conns(conn4) 
config_conns(conn3) 
config_conns(conn5) 
 

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
   
 
mtx=mutex.mutex()
 
def traceQ(progress,usr):   
   if mtx.testandset():
    cursorTrace.execute ("insert into status_index(USERNAME,MSG,progress) values ( %s , '', %s ) ",(usr,progress))
    print 'TraceQ:===================='
    print progress
    print '==========================='
    mtx.unlock()
    return True
   return False 


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
 
def prepare_search_customlayouts(purposes,dts,dtsp,usr):
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
    print 'prepare Exec :',dt
    try:
     exec(code, locals(), locals())
    except Exception,e:
     print 'Exec Error:',e    
    if typ == 1: #executavel
     # adicionar ao codes_Result o retorno_srt(lines->[endereco,dados] ) 
     print 'Exec :',dt,' result:',retorno_srt
     if retorno_srt != None:
      codes_Result.append( retorno_srt )
 #===================
 return codes_Result 
 
def prepare_search(dts,dtsp):
 
 if len( entry_doc ) > 0 : #debug direto
  return [[['debug-title','debug-url']]]
 
 rets=[]
 try :
  qry=' '
  for d in dts:
   qry+=d+' '
  for d1 in dtsp:
      query=urllib.quote((d1+' '+qry))
      print 'Request web:',query
      #url_q='http://www.mind-net.com/mind-net/request_mind_ex2.php?query='+query 
      url_q='http://www.mind-net.com/mind-net/gl.php?query='+query   
      opener = urllib2.build_opener()
      data_Res = opener.open(url_q, '' ).read()
      lines=[]
      cl=[]
      tmp='';
      kind=1
      for ds in data_Res:
       if ds == '|':
         cl.append(tmp)
         lines.append(cl)
         tmp=''
         cl=[]
       elif ds == '^':
        cl.append(tmp)
        tmp=''     
       else:
        tmp+=ds
      rets.append(lines) 
  #
 except Exception,e:
  logs.exception( 'Error process sentences->prepare_search:' )
  
 #== 
 print 'Lens:',len(rets)
 return rets
 
def prepare_search_video(dts,dtsp):
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  for d1 in dtsp:
      query=urllib.quote(d1+' '+qry)
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

def prepare_search_news(dts,dtsp):
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  for d1 in dtsp:  
      query=urllib.quote(d1+' '+qry)
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


def prepare_search_info(dts,dtsp): # wikipedia
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  for d1 in dtsp: 
      query=urllib.quote(d1+' '+qry)
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

 
def prepare_search_reputacao(dts,dtsp):
 '''
   search all data
 ''' 
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  for d1 in dtsp: 
      query=urllib.quote(d1+' '+qry)
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

def prepare_search_people(dts,dtsp):
 '''
   search all data
 ''' 
 rets=[]
 if True :
  qry=''
  for d in dts:
   qry+=d+' '
  for d1 in dtsp:
      query=urllib.quote(d1+' '+qry)
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
  

cursorP = conn.cursor ()  
  
def post_pagina(endereco,conteudo_i,termo,usr,purp,cind2,errorp,ind_pag):
 try:
   conteudo=''
   for l in conteudo_i:
    conteudo+=(l+'\n')
   sql1="insert into WEB_CACHE (URL,PG,TERMO,PURPOSE,USR) values(%s,%s,%s,%s,%s)"
   if conteudo != "":
    print 'Post page:',cind2,'..'
    try:     
     cursorP.execute (sql1,(MySQLdb.escape_string(endereco),MySQLdb.escape_string(conteudo),MySQLdb.escape_string(termo),purp,usr))
    except Exception,e1 :  
     print '->', e1 ,'->'
     e1r=e1.__str__() 
     if e1r.find('Out of memory') > -1 : 
       conteudo=''
       time.sleep(1)
       errorp.append(ind_pag)
       return
 except : pass
 
 
def get_layouts(usr,purpose): 
 import mdER3
 mdER3.conn=conn 
 mdER3.conn4=conn4
 mdER3.conn3=conn3

 p=mdER3.get_LayoutsFZ(usr,purpose)
 return p   

def get_purpsz(usr,purpose): 
 import mdER3
 mdER3.conn=conn 
 mdER3.conn4=conn4
 mdER3.conn3=conn3

 p=mdER3.get_purpsz(usr,purpose)
 return p   


def get_layouts2(usr,purpose): 
 import mdER3
 mdER3.conn=conn 
 mdER3.conn4=conn4
 mdER3.conn3=conn3

 p=mdER3.get_LayoutsFZ2(usr,purpose)
 return p  

 
def process_termo(termo,usr,purp,start_c,path_j):
 # montar ontlogia
 layouts_f=get_layouts(usr,purp)
 layouts_f2=get_layouts2(usr,purp)
 t_threads=[]
 
 t_threads.append(thread_cntl())  
 ret_ps=[]
 ret_ps.append([])
 
 lines_doc2=termo
 id=usr
 
 onto_basis2=[]
 for onto_basisk in layouts_f:
     l2=Identify.prepare_layout(id,onto_basisk)
     onto_basis2.append(l2)
     
 onto_basis22=[]
 for onto_basisk in layouts_f2:
     l2=Identify.prepare_layout(id,onto_basisk)
     onto_basis22.append(l2)
 
 
 ret_ps[len(ret_ps)-1]=Identify.pre_process_data2(onto_basis2,onto_basis22,lines_doc2,purp,id,t_threads[len(t_threads)-1],[])

 objs_search2=[]
 complements=[]
 #=
 objs_search=[] 
 purposes=get_purpsz(usr,purp)
 print 'purposes:[',purposes,']'
 
 for lays in ret_ps:
   for lay in lays:
    for top in lay.topicos:
     for dts in top.dt:
      if dts.upper() == "IDENTIFICADOR" or dts.lower() in ['action' ] :
       for s in top.sinapses:
        for dts2 in s.nr.dt:
          if dts2 not in ['.',':','\'','"','?','?']:
           objs_search.append(dts2)
           print 'Identify:',dts2
      if dts.upper() == "REALID" or dts.upper() == "REALID2":
       for s in top.sinapses:
        for dts2 in s.nr.dt:
          if dts2 not in ['.',':','\'','"','?','?']:
           objs_search2.append(dts2)
           print 'RealID:',dts2
 
 #==================================
 print 'Objs:Search:',objs_search
 if len(objs_search2) > 0 or len(objs_search) > 0 :
  opener = urllib2.build_opener()
  def pg_open(addresss,th,pages,pgind,ind_emit,start_c,total_p):
   try:
    ind=0
    inds=0
    acumul=0
    print 'Process init open page:',len(addresss)
    total_p=total_p/len(addresss)
    for address in addresss:
      try:
        ind+=1
        inds+=1
        lines_doc=[]
        if address != 'debug-url':
         if inds > 2:
          print 'traceq i:',total_p
          if traceQ(acumul,usr) :
           acumul=0
          inds=0
         else:
           acumul+=total_p
         #======================  
         address=urllib.quote(address)
         address=address.replace('%3A',':')
         url='http://www.mind-net.com/get_Text.php?q='+address
         print 'Open page:',url         
         content = opener.open(url, '' ).read()
         tmpd=content.replace('\n',' ')
         lines_doc.append(tmpd)
         #tmpd=''
         #for d in content:
         # if d == '\n':
         #  lines_doc.append(tmpd)
         #  tmpd=''
         # else:
         #  tmpd+=d    
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
      except Exception,e:
       print 'Error PG_OPEN_I',e,'..'
             
    th.finished=True
   except Exception,e:
    print 'Error PG_OPEN',e,'..'
    #logs.exception( 'Error process sentences->pg_open:' )
    #logs.exception('[Layout(p) Exec Error]Stack execution---------------------------------')
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
  ''' /1/ '''
  if 'web' in purposes:
   results_search=prepare_search(objs_search,objs_search2)
  elif 'reputacao' in purposes:
   results_reputac=prepare_search_reputacao(objs_search,objs_search2)
  elif 'people' in purposes:
   results_peop=prepare_search_people(objs_search,objs_search2)
  elif 'news' in purposes:
   results_news=prepare_search_news(objs_search,objs_search2)
  elif 'video' in purposes:
   results_videos=prepare_search_video(objs_search,objs_search2)
  elif 'wiki' in purposes:
    results_wiki=prepare_search_info(objs_search,objs_search2)
  else:
   custom_layouts=prepare_search_customlayouts(purposes,objs_search,objs_search2,usr)
  
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
  start_c2=0;
  idx_pc=0
  #traceQC(usr)
  lensk=0
  for res in results_search:
   for addrs in res:
     lensk+=1
  
  if lensk > 0 :
   lensk=1.0/lensk
  else:
   lensk=0  
  lensk2=0
  lens_th=0
  errorp=[]
  for res in results_search:
   start_c2+=1
   indaddrs=0
   for addrs in res:
    try:
     lens_th+=1
     pg_add=addrs[1]
     ind_emit+=1
     lensk2+=lensk
     if len(tmp_pages) >=10 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      #===
      #print 'Process open:'
      try:
       #pg_open(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c2,lensk2)
       thread.start_new_thread(pg_open,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c2,lensk2) )
      except:
       pass      
      lensk2=0
      
      if lens_th > 100:
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
          ths=[]
          gc.collect()
          lens_th=0
          #=======================================
          
          indice_pag=0
          
          gc.collect()
          
          for pagina in pages:
           cind2+=1
           if pagina.dt1 == None: continue
           endereco=pagina.dt1
           lines_doc=pagina.dt2   
           time.sleep(0.1)

           post_pagina(endereco,lines_doc,termo,usr,purp,cind2,errorp,indice_pag)

           #progress=(cind2/len(pages))
           #traceQ(progress,usr,cind2,1,endereco,'Post page:' ) 
           indice_pag+=1
          
          pages=[]
          gc.collect()           
          

  
     else:
      tmp_pages.append(pg_add) 
    except:
     pass
   cind+=1
   indres+=1
  if len(tmp_pages) > 0 :
      ths.append(thread_cntl())
      ic=ind_emit
      tmp_pages2=tmp_pages
      tmp_pages=[]
      try:
       #pg_open(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c2,lensk2)
       thread.start_new_thread(pg_open,(tmp_pages2,ths[len(ths)-1],pages,kind,ic,start_c2,lensk2) )
      except:
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
    time.sleep(10)
    continue
   else:
    break
    
  print 'Open docs : OK'
  ths=[]
  onto_basis=None
  allp=None
  allp2=None
  tmp_pages=[]
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
  indice_pag=0
  
  gc.collect()
  
  for pagina in pages:
   cind2+=1
   if pagina.dt1 == None: continue
   endereco=pagina.dt1
   lines_doc=pagina.dt2   
   time.sleep(0.1)
   post_pagina(endereco,lines_doc,termo,usr,purp,cind2,errorp,indice_pag)
   #progress=(cind2/len(pages))
   #traceQ(progress,usr,cind2,1,endereco,'Post page:' ) 
   indice_pag+=1
  
  pages2=pages
  pages=[]
  for e2c in errorp:
   pages.append(pages2[e2c] )
  pages2=[]   
   
  gc.collect() 
   
  print 'ErrorP len:',len(errorp)
  while len(errorp)> 0: 
      errorp2=errorp
      errorp=[]
      indcp=0
      for e in errorp2:
       print 'Process errors:',e
       pagina=pages[indcp]
       indcp+=1
       endereco=pagina.dt1
       lines_doc=pagina.dt2   
       time.sleep(1)
       post_pagina(endereco,lines_doc,termo,usr,purp,e,errorp,e)
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
 
def get_ids2 (usr,term):
 cursor = conn.cursor ()
 cursor.execute ("SELECT I FROM WEB_CACHE where USR='"+usr+"' and  termo=%s ",(term))  
 resultSet = cursor.fetchall()
 for results in resultSet:
    tm=results[0]
    print 'UID:',tm    
    return tm
 return None


def clear_termo(username,termo):
 
 sql1=" delete from SEMANTIC_OBJECT_DT3 where UID in ( select I from SEMANTIC_OBJECT3 where username = %s and cenar= %s  )  "
 cursor = conn5.cursor ()
 try:
  cursor.execute (sql1,(username,termo))
 except Exception,err: print 'Erro ao del(OBJECT):',err

 sql1=" delete from SEMANTIC_RELACTIONS3 where UID in ( select I from SEMANTIC_OBJECT3 where username = %s and cenar = %s  ) "
 cursor = conn5.cursor ()
 try:
  cursor.execute (sql1,(username,termo))
 except Exception,err: print 'Erro ao del(OBJECT):',err

 sql1=" delete from SEMANTIC_OBJECT3 where username = %s and cenar  = %s  "
 cursor = conn5.cursor ()
 try:
  cursor.execute (sql1,(username,termo))
 except Exception,err: print 'Erro ao del(OBJECT):',err
 
 
def process_sentences(USERNAME): 
 cursor = conn.cursor ()
 cursor.execute ("SELECT USERNAME,TERMO FROM clipping_info  where USERNAME=%s LIMIT 0 , 50 ",(USERNAME)) # 50 rows por vez
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
     clear_termo(username,get_ids2(username,termo) )
     limpa_resultados_anteriores(termo,username,pur_p)
     process_termo(termo,username,pur_p,0,sys.argv[0])
    #=== fecha os ja executados
    #fecha_busca(termo,username)
    

start_c=0

usr=sys.argv[1]

print 'Process usr:',usr
#try:      
process_sentences(usr)
#except: pass

finish_Trace(usr)
 
 