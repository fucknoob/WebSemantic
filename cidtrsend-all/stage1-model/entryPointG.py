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

def mount_node(term,id,purpose):
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 l=Identify.prepare_layout(conn,id,purpose)
 allp=[]
 onto=Identify.prepare_data_by_ask(l, term,id,purpose,allp )
 conn.close()
 return [onto,allp]

 
 
entry_doc =[]
 
#entry_doc = ['vectra é um bom carro com design inteligente, em composto por fibra de carbono restrito em carro de passeio ',' expectativas de carro com venda fortes','casa bom estado venda'] 
#entry('viagens melhores opções',['viagem para o nordeste é muito mais tranquilo, composto por translados mas restrito para criancas '])
 
 
 
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

 
 
def post_object_by_data(layer,usr,conn):
 nameo=layer.name
 sql1="insert into SEMANTIC_OBJECT(username,objeto) values(%s,%s)"
 cursor = conn.cursor ()
 cursor.execute (sql,(usr,nameo))
 for tp in topicos:
  tp_Dt=''
  for d in tp.dt:
   tp_Dt+=d
  tp_name=tp_Dt
  for sn in tp.sinapses:
   sn_dt=''
   for s1 in sn.nr.dr:
    sn_dt+=s1
   sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico) values(%s,%s,%s,%s)"
   cursor = conn.cursor ()
   cursor.execute (sql,(usr,nameo,tp_Dt,sn_dt))
 #===============================================
 for lnk in layer.links:
  sqlc='insert into (OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D) values(%s,%s,%s,%s,%s)' 
  cursor = conn.cursor ()
  #====================   
  def get_nr_dts1(nrs):
   d=''
   for nr in nrs:
    for n in nr.dt:
     d+=n
    d+=','
   return d
  #====================   
  foco_o=get_nr_dts1(lnk.foco_o)
  foco_d=get_nr_dts1(lnk.foco_d)
  cursor.execute (sqlc,(nameo,lnk.lr.name,lnk.opcode,usr,foco_o,foco_d))
  #===============
  post_object_data(lnk.lr,usr,conn)

def post_objects_by_data(layers,usr,conn):
 for layer in layers:
  post_object_by_data(layer,usr,conn)
  
 
def get_object_by_data(obj,usr,conn): 
 cursor = conn.cursor ()
 sql='select objeto from SEMANTIC_OBJECT where i=%s and USERNAME = %s '
 cursor.execute (sql,(obj,usr))
 resultSet = cursor.fetchall()
 obj_nm=None
 for results in resultSet:
      obj_nm=results[0] 
 #-----------
 lay=mdNeural.mdLayer()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 cursor = conn.cursor ()
 sql='select DT,TOPICO from SEMANTIC_OBJECT_DT where OBJECT=%s and USERNAME = %s '
 cursor.execute (sql,(obj,usr))
 resultSet = cursor.fetchall()
 obj_nm=None
 for results in resultSet:
      DT=results[0] 
      TOP=results[1]
      nr= lay.set_nr(DT)
      tps=lay.get_topico(TOP)
      if tps == None:
       tps=lay.set_topico(TOP)
      tps.connect_to(lay,nr,'Composicao') 
  
 return lay   
 
def get_ontology(aliases,purposes,usr): 
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 tree_h=[]
 for alias in aliases:
     cursor = conn.cursor ()
     cursor.execute ("SELECT OBJETO FROM  SEMANTIC_OBJECT where OBJETO = %s  and USERNAME = %s  ",(alias,usr))
     resultSet = cursor.fetchall()
     for results in resultSet:
        i=results[0] 
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          cursor2 = conn.cursor ()          
          cursor2.execute ("SELECT OBJ_DEST,FOCO,FOCO_D FROM  SEMANTIC_RELACTIONS where OBJ_ORIG = %s and OPCODE = %s and USERNAME = %s ",(i,pr,usr))   
          resultSet = cursor2.fetchall()
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           fcd=resultsC[2]
           if fco == None : fco=''
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        def collect_objs_dest(sins,i,usr):
         objs_r=[]
         for pr in sins:
          cursor2 = conn.cursor ()          
          cursor2.execute ("SELECT OBJ_ORIG,FOCO,FOCO_D FROM  SEMANTIC_RELACTIONS where OBJ_DEST = %s and OPCODE = %s and USERNAME = %s ",(i,pr,usr))   
          resultSet = cursor2.fetchall()
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        obj_principal=get_object_by_data(i,usr,conn)
        tree_h.append(obj_principal)
        #===
        c1=collect_objs_orig(purposes,i,usr)
        #==----------------------------------------
        def parse_or(st):
         s=[]
         ind=0
         for i in st:          
          if i == ',' or len(i) == ind:
           if len(i) == 0 : tmp+=i
           s.append(tmp)
           tmp=''           
          else:  tmp+=i 
          ind+=1
        #==----------------------------------------
        for c in c1:
         obj_id=c[0]
         opc=c[1]
         fco=c[2]
         fcd=c[3]
         obj_k=get_object_by_data(obj_id,usr,conn)
         foco_o=[]
         foco_d=[]
         r1=parse_or(fco)
         for rc1 in r1:
           n=obj_principal.get_topico(rc1)
           foco_o.append(n)
         r2=parse_or(fcd)
         for rc1 in r1:
           n=obj_k.get_topico(rc1)
           foco_d.append(n)
         obj_principal.set_link_ds(obj_k,opc,foco_o,foco_d)
        #==
        c12=collect_objs_dest(purposes,i,usr)
        #==----------------------------------------
        for c in c12:
         obj_id=c[0]
         opc=c[1]
         fco=c[2]
         fcd=c[3]
         obj_k=get_object_by_data(obj_id,usr,conn)
         #===
         foco_o=[]
         foco_d=[]
         r1=parse_or(fco)
         for rc1 in r1:
           n=obj_k.get_topico(rc1)
           foco_o.append(n)
         r2=parse_or(fcd)
         for rc1 in r1:
           n=obj_principal.get_topico(rc1)
           foco_d.append(n)
         #===
         obj_k.set_link(obj_principal,opc)
         
 return tree_h       

class thread_cntl:
 def __init__(self):
  self.finished=False

class Task_C:
 def __init__(self,Dt1=None,Dt2=None):
   self.dt1=Dt1
   self.dt2=Dt2
  
def process_termo(termo,usr,purp,start_c,path_j):
 # montar ontlogia
 objs_search=[]
 purposes=[]
 [onto_basis,allp]=mount_node(termo,usr,purp)
 #=
 for sd in allp:
  for s2 in sd[1]:
   purposes.append(s2)
   
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
           objs_search.append(dts2)
 #==================================
 
 if len(objs_search) > 0 :
  def pg_open(address,th,page,pgind,ind_emit,start_c):
   if ind_emit > 0 : pgind=ind_emit
   if start_c > 0 : 
    #print 'Get content for page:',pgind,'\n'
    print 'Get content for page:',pgind
   else:
    print 'Get content for page:',pgind
   
   try:
    lines_doc=[]
    if address != 'debug-url':
     opener = urllib2.build_opener()
     address=urllib.quote(address)
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
    else:
     for line_deb in entry_doc:
      lines_doc.append(line_deb)
    page.dt1=pg_add
    page.dt2=lines_doc
    th.finished=True
   except Exception,er :
    print er,'................'
    th.finished=True
   print 'Get content for page:',pgind,' was finished.Len:',len(lines_doc)
  #=====================================================  
  #buscar ontologia no banco de dados
  # achar proposito(aprendizado,classificacao,coleta de informacao )
  tree_ondo=get_ontology(objs_search,purposes,usr)
  # executar buscas sobre o 'termo' e mais as dependencias,etc...  encontrados na ontologia
  results_search=[]
  results_reputac=[]
  results_peop=[]
  results_news=[]
  results_videos=[]
  #=====================================================
  if 'web' in purposes:
   results_search=prepare_search(objs_search)
  if 'reputacao' in purposes:
   results_reputac=prepare_search_reputacao(objs_search)
  if 'people' in purposes:
   results_peop=prepare_search_people(objs_search)
  if 'news' in purposes:
   results_news=prepare_search_news(objs_search)
  if 'video' in purposes:
   results_videos=prepare_search_video(objs_search)
  
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
  c_break=False
  if start_c == 0:
   #fazer o start de cada um dos jobs secundarios
   fx=0
   ix=10
   def start_job_sec(start,path_j,th):
    cmd='python '+path_j+' '+str(start)
    os.system(cmd)
    th.finished=True
   all_coll=0
   for res in results_search:
    for addrs in res:
      all_coll+=1
      
   while ix < all_coll:    
    ix+=10    
    fx+=1
   ix=1
   print 'Total jobs:',fx,' total collect:',all_coll
   while ix < fx:
     ths2.append(thread_cntl())
     thread.start_new_thread(start_job_sec,(ix*10,path_j,ths2[len(ths2)-1]) )
     ix+=1
   
  #========================
  ind_emit2=0
  for res in results_search:
   indaddrs=0
   for addrs in res:
    pass_c1=True
    if start_c > 0 :
      pass_c1=False
      if ind_emit >= start_c:
        pass_c1=True
    if pass_c1:
     pg_add=addrs[1]
     ths.append(thread_cntl())
     pages.append(Task_C())
     thread.start_new_thread(pg_open,(pg_add,ths[len(ths)-1],pages[len(pages)-1],kind,ind_emit,start_c) )
     ind_emit2+=1
    indaddrs+=1
    kind+=1
    if ind_emit2 >= 10:
      c_break=True
      break   
    ind_emit+=1
   cind+=1
   if c_break : break
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
  for res in results_videos:
   for addrs in res:
    pg_add=addrs[1]
    pages.append(Task_C(pg_add,addrs[2])) 
    #==============
   cind+=1
  #=====================================
  print 'Collect OK!!'
  cind2=0
  threads_fd=[]
  print 'Init Process pages:',len(pages)
  for pagina in pages:
   cind2+=1
   if pagina.dt1 == None: continue
   endereco=pagina.dt1
   lines_doc=pagina.dt2
   def process_page(lines_doc2,id,purpose,pgs,finish,th):
    ln_o=''
    conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
    if True:
    #try:
      l2=Identify.prepare_layout(conn,id,purpose)
      if True :
       for s in lines_doc2:
        ln_o=s
        if umisc.trim(ln_o) == '':
         finish.finished=True
         return 
        ir=Identify.process_data(conn,l2,ln_o,onto_basis,purpose,id,th) 
        if ir[0] != None :
         # procura identificador ---
         fnd_ident=False
         for es in ir[0].topicos:
          if ir[0].es_compare_dt(es,'identificador'):
           fnd_ident=True
         if not fnd_ident:
          ind=len(result_onto_tree_er)-1
          fond_cs=False
          while ind >=0 and not fond_cs:
           for es2 in result_onto_tree_er[ind].topicos:
            if ir[0].es_compare_dt(es2,'identificador'):
              ir[0].set_topico_nr(es2)
              fond_cs=True
              break
           ind-=1  
         
         # verificar se nao tem somente identificadores(elemento fact invalido)     
         oth=False         
         for es in ir[0].topicos:
          if ir[0].es_compare_dt(es,'identificador'):
           pass
          else:
           oth=True
         if not oth:
          continue 
         result_onto_tree_er.append(ir[0])
         # procurar group 
         ind=len(result_onto_tree_er)-1
         while ind >=0 :
           if ir[0] != result_onto_tree_er[ind]:
             for es2 in result_onto_tree_er[ind].topicos:
              if ir[0].es_compare_dt(es2,'identificador'):
               for top in ir[0].topicos:
                if ir[0].compare_dt_depend(conn,usr,purpose,es2,top,['']):
                  # encontrou referencias do mesmo identificador, incluir nos objetos linkados
                  rt=None
                  fnd_new=False
                  for k1 in result_linked:
                   for k2 in k1:
                    if k1 == ir[0]:
                     fnd_new=True
                     rt=k1
                  #= 
                  if not fnd_new:
                   result_linked.append([ir[0]])
                   rt= result_linked[len(result_linked)-1 ]
                  
                  #=======================================
                  fnd_new=False
                  for k2 in rt:
                    if k2 == result_onto_tree_er[ind]:
                     fnd_new=True
                  if not fnd_new:
                   rt.append(result_onto_tree_er[ind])                
           ind-=1  
         
         #==========================
        if ir[1] != None:
         result_onto_tree_bpm.append(ir[1])   
    #except Exception ,err:
    #  print 'Except:',err
    #  finish.finished=True    
    finish.finished=True
    conn.close()
    print 'Thread ',pgs,' was finished.','Len:',len(ln_o),' process:',start_c/10
   threads_fd.append(thread_cntl())
   print 'Start thread job :',cind2,' process:',
   thread.start_new_thread(process_page,  (lines_doc,usr,purp,cind2,threads_fd[len(threads_fd)-1],cind2) )
  
  #--
  ind_fs=0
  while True:
   if (len(threads_fd)-ind_fs) == 0: break
   print 'Processing...',len(threads_fd)-ind_fs,',ind_fs:',ind_fs
   ind_fs=0
   time.sleep(10)
   conti=False
   for d in threads_fd:
    if not d.finished: conti=True
    if d.finished: ind_fs+=1
   if conti: continue
  #===============================================
  #===============================================
  ind_col=0
  while True:
    print 'wait for secondary process...',len(ths2)-ind_col
    fnds_t=False
    ind_col=0
    for ths1 in ths2:    
     if not ths1.finished:fnds_t=True
     if ths1.finished: ind_col+=1
    if fnds_t:
     time.sleep(10)
     continue
    else:
     break
   
  #========================================================================================================================================
  # processar informacoes ( encontrar os ractionlines linkdas por 'CALL' )
  rts=[]
  ind=0
  def get_result_links(lr):
   for s in result_linked:
    for s2 in s:
     if s2 == lr:
       return s
   return []    
  conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
  for data_c in result_onto_tree_er:
   runc=result_onto_tree_bpm[ind] # rct original, ractionline q processou as informacoes
   #sd_link=result_linked[ind]
   sd_link=get_result_links(data_c)
   runc.process_Call_RCT(conn,data_c,usr,sd_link)
   rts.append(data_c)
   ind+=1
  conn.close()
  #========================================================================================================================================
  print 'ER:',len(result_onto_tree_er)
  for e in result_onto_tree_er:
    print '----------------------------------------'
    for t in  e.topicos:
     print t.dt
     print '**************************'
     for s in t.sinapses:
      print s.nr.dt
     print '**************************'
    print '----------------------------------------'
   #break 
  #==================================== 
  
  # extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime ,nao clipping
  #   class=get_class(rts) # classificacao/categoria
  #   purpose=get_purpose(rts) # preview de informacao, resumo
  # gravar rts como objetos no sgdb -> para aquisicao de conhecimento, usa-se esse recurso 
  #   conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet') 
  #   post_objects_by_data(rts,usr,conn)
  # retornar result da ontologia( results do tree ) ==> rts
  return []
  return rts

def get_purposes(conn): # retorna os purposes(triggers) de pesquisas, cada um com suas fontes e propositos
 cursor = conn.cursor ()
 cursor.execute ("SELECT DT FROM knowledge_manager where typ=4 order by i") 
 resultSet = cursor.fetchall()
 p=[]
 for results in resultSet:
    purps=results[0]
    p.append(purps)
    
 return p   
 
def process_sentences(start_c): 
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 cursor = conn.cursor ()
 cursor.execute ("SELECT USERNAME,TERMO,TRIGGER_AS FROM clipping_info LIMIT 0 , 50 ") # 50 rows por vez
 resultSet = cursor.fetchall()
 r1=[]
 for results in resultSet:
    username=results[0]
    termo=results[1] 
    trigger_as=results[2] 
    r1.append([username,termo,trigger_as])
 purps=get_purposes(conn) # purposes-> layouts definidos dentro dos facts dos ractionlines escalados
 conn.close()
 for r in r1:
    [username,termo,trigger_as]=r 
    #===
    purposes=[] # 
    focos=[]
    #===
    for pur_p in purps:
     result=process_termo(termo,username,pur_p,start_c,sys.argv[0])
     ##########################
     return
     ##########################
     for r in result:
      cursor.execute (" insert into clipping_return(username,retorno,categoria,href) values ( %s , %s , %s , %s )", (username, r[0],r[1],r[2]))   

start_c=int(sys.argv[0])

      
process_sentences(start_c)

 
 