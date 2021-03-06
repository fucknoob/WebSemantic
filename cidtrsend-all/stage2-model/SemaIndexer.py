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
from os import environ


import umisc


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping



#===================
def get_typ(obj,usr2,conn):
  cursor = conn.cursor ()
  cursor.execute ("select TYP from DATA_BEHAVIOUR_PY where OBJETO='"+obj+"' and USERNAME='"+usr2+"' order by i") 
  resultSet = cursor.fetchall()
  typ=0
  for results in resultSet:
    typ=results[0]
  return  typ
#=============================================== 

def prepare_search_customlayouts(purposes,dts,usr,conn):
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
 #====================================================================================================
 #chamar os codigos 
 codes_Result=[]
 for dt in purposes:
  cursor = conn.cursor ()
  cursor.execute ("select CODE from DATA_BEHAVIOUR_CODE_PY where OBJETO='"+dt+"' and USERNAME='"+usr+"' order by i") 
  resultSet = cursor.fetchall()
  for results in resultSet:
    typ=get_typ(dt,usr,conn)
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
 conn.close()
 return codes_Result 

def start_job_sec(start,path_j,th):
  cmd='python '+path_j+' '+str(start) + '  &  ' 
  #os.execv('/usr/bin/python',(path_j,str(start)) )
  os.system(cmd)
  th.finished=True


def mount_node(term,id,purpose):
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
 l=Identify.prepare_layout(conn,id,purpose)
 allp=[]
 onto=Identify.prepare_data_by_ask(l, term,id,purpose,allp )
 conn.close()
 return [onto,allp]

 
 
entry_doc =[]
 
#entry_doc = ['vectra � um bom carro com design inteligente, em composto por fibra de carbono restrito em carro de passeio ',' expectativas de carro com venda fortes','casa bom estado venda'] 
#entry('viagens melhores op��es',['viagem para o nordeste � muito mais tranquilo, composto por translados mas restrito para criancas '])
 
 
def post_object_by_data2(layer,usr,conn,termo,foco):
 def get_top_level(conn,obj,foc,usr):
   rts=[]
   cursor = conn.cursor ()
   cursor.execute ("SELECT LEV FROM  SEMANTIC_OBJECT_DT2 where OBJECT = %s and TOPICO= %s and USERNAME = %s  order by LEV ",(obj,foco,usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      i=results[0] 
      rts.append(i)
   return rts
 #=======================  
 nameo=layer.name
 sql1="insert into SEMANTIC_OBJECT2(username,objeto,TERMO) values(%s,%s,%s)"
 cursor = conn.cursor ()
 cursor.execute (sql,(usr,nameo,termo))
 for tp in topicos:
  #==========    ===============================================
  def post_nr(conn,usr,tp,level=1):
   tp_Dt=''
   for d in tp.dt:
    tp_Dt+=d
   tp_name=tp_Dt
   for sn in tp.sinapses:
    sn_dt=''
    for s1 in sn.nr.dr:
     sn_dt+=s1
    sql1="insert into SEMANTIC_OBJECT_DT2(username,object,dt,topico,LEV) values(%s,%s,%s,%s,%s)"
    cursor = conn.cursor ()
    try:
     cursor.execute (sql1,(usr,nameo,tp_Dt,sn_dt,level))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
    #==========
    post_nr(conn,usr,sn.nr,level+1)
  #==========    ===============================================
  def post_nr2(conn,usr,topdt,new_dt,sin_dt,level):
    sql1="insert into SEMANTIC_OBJECT_DT2(username,object,dt,topico,LEV) values(%s,%s,%s,%s,%s)"
    try:
     cursor.execute (sql1,(usr,topdt,new_dt,sin_dt,level))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
  
  #==========    ===============================================
  if len(foco) == 0:
    post_nr(conn,usr,tp)
  else:
    for l in foco:
      #achar o topico e o level
      dts=''
      for ldt in l.dt:
       dts+=ldt
      level=get_top_level(conn,nameo,l,usr)
      if len(level)>0:
       for level_s in level:
        post_nr2(conn,usr,dts,tp.dt,l.opcode,level_s)
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  SEMANTIC_RELACTIONS2(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D) values(%s,%s,%s,%s,%s,%s)' 
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
 
 
def post_datah_state(state_type,obj,composicao,rels,usr,conn):
 cursor = conn.cursor ()
 for sti in state_type:
  for compo in composicao:
   sql='insert into SEMANTIC_INFOSTATE( USERNAME,OBJECT,TOPICO,INDI_STATE ) VALUES(%s,%s,%s,%s)'
   cursor.execute (sql,(usr,obj,compo,sti))
  #== 
  for rels in composicao:
   sql='insert into SEMANTIC_INFOSTATE( USERNAME,OBJECT,TOPICO,INDI_STATE ) VALUES(%s,%s,%s,%s)'
   cursor.execute (sql,(usr,obj,compo,sti))
 
 
def post_object_by_data(layer,usr,conn,termo,foco):
 def get_top_level(conn,obj,foc,usr):
   rts=[]
   cursor = conn.cursor ()
   cursor.execute ("SELECT LEV FROM  SEMANTIC_OBJECT_DT where OBJECT = %s and TOPICO= %s and USERNAME = %s  order by LEV ",(obj,foco,usr))
   resultSet = cursor.fetchall()
   for results in resultSet:
      i=results[0] 
      rts.append(i)
   return rts
 #=======================  
 nameo=layer.name
 sql1="insert into SEMANTIC_OBJECT(username,objeto,TERMO) values(%s,%s,%s)"
 cursor = conn.cursor ()
 cursor.execute (sql,(usr,nameo,termo))
 for tp in topicos:
  #==========    ===============================================
  def post_nr(conn,usr,tp,level=1):
   tp_Dt=''
   for d in tp.dt:
    tp_Dt+=d
   tp_name=tp_Dt
   for sn in tp.sinapses:
    sn_dt=''
    for s1 in sn.nr.dr:
     sn_dt+=s1
    sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico,LEV) values(%s,%s,%s,%s,%s)"
    cursor = conn.cursor ()
    try:
     cursor.execute (sql1,(usr,nameo,tp_Dt,sn_dt,level))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
    #==========
    post_nr(conn,usr,sn.nr,level+1)
  #==========    ===============================================
  def post_nr2(conn,usr,topdt,new_dt,sin_dt,level):
    sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico,LEV) values(%s,%s,%s,%s,%s)"
    try:
     cursor.execute (sql1,(usr,topdt,new_dt,sin_dt,level))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
  
  #==========    ===============================================
  if len(foco) == 0:
    post_nr(conn,usr,tp)
  else:
    for l in foco:
      #achar o topico e o level
      dts=''
      for ldt in l.dt:
       dts+=ldt
      level=get_top_level(conn,nameo,l,usr)
      if len(level)>0:
       for level_s in level:
        post_nr2(conn,usr,dts,tp.dt,l.opcode,level_s)
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  SEMANTIC_RELACTIONS(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D) values(%s,%s,%s,%s,%s,%s)' 
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

def get_objs_purp(obj,purspe,usr,conn): 
 #-----------
 rts=[]
 cursor = conn.cursor ()
 sql='select DT, TOPICO from SEMANTIC_OBJECT_DT where  USERNAME = %s '
 cursor.execute (sql,(obj,usr))
 resultSet = cursor.fetchall()
 for results in resultSet:
      TOP=results[1]
      DT=results[0]
      OB=results[2]
      if TOP.upper() == 'SPECIAL-PURPOSE':
       if DT.upper() == purspe:
        rts.append(OB)
 return rts
 
def get_objectdt_by(objs,usr,conn): 
 #-----------
 rts=[]
 for obj in objs:
  cursor = conn.cursor ()
  sql='select distinct TOPICO from SEMANTIC_OBJECT_DT where OBJECT=%s and USERNAME = %s '
  cursor.execute (sql,(obj,usr))
  resultSet = cursor.fetchall()
  for results in resultSet:
      TOP=results[0]
      if TOP.upper() != 'SPECIAL-PURPOSE':
       rts.append(TOP)
       break
 return rts

 
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
  
def get_pages_len(usr):  
 pages=[]
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet') 
 sql='select count(*) from WEB_CACHE where USR = %s and PROCESSED <> \'S\' '
 cursor = conn.cursor ()
 cursor.execute (sql,(usr))
 resultSet = cursor.fetchall()
 obj_nm=None
 ind=0
 for results in resultSet:
   ind=results[0]
 conn.close()
 return ind
  
def get_pages(usr,start_c):
 pages=[]
 conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet') 
 sql='select URL,PG from WEB_CACHE where USR = %s and PROCESSED <> \'S\' LIMIT '+str(start_c)+' , 50'
 cursor = conn.cursor ()
 cursor.execute (sql,(usr))
 resultSet = cursor.fetchall()
 obj_nm=None
 idx=1
 for results in resultSet:
   pg_add=results[0]
   pg_txt=results[1]
   #print 'Page:',idx
   idx+=1
   pages.append(Task_C(pg_add,pg_txt)) 
 conn.close()
 return pages 
  
# //1

def get_class(purp,usr,conn):
 sql = "SELECT Label from knowledge_manager where USERNAME = '"+usr+"' and typ=4 and DT= s% order by i "
 cursor = conn.cursor ()
 cursor.execute (sql,(purp))
 resultSet = cursor.fetchall()
 for results in resultSet:
   return results[0]
 return ''
 
def process_termo(termo,usr,purp,start_c,path_j):
  pages=[]
  ths2=[]
  if start_c == 0:
   start_c=1
   all_pgs=get_pages_len(usr)
   ib=0
   lb=all_pgs
   print 'Process pages:',all_pgs
   while ib < all_pgs:
    if ib < 100:
     print 'Start collection at:',start_c
     pages=get_pages(usr,start_c)
     start_c+=100
    else:
     #start_job_sec(ib+1,path_j)
     ths2.append(thread_cntl())
     thread.start_new_thread(start_job_sec,(ib+1,path_j,ths2[len(ths2)-1]) )
     
    ib+=100
  else:
    print 'Start collection on:',start_c
    
  #========================================================================================================================================
  #========================================================================================================================================
  ind_col=0
  while True and len(ths2) > 0:
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
  #========================================================================================================================================
    
  #=====================================
  [onto_basis,allp]=mount_node(termo,usr,purp)
  #========================================
  cind2=0
  threads_fd=[]
  result_onto_tree_er=[] # caracteristicas,descricoes,etc...
  result_onto_tree_bpm=[] # fluxo de acoes, sequencia de actions
  result_linked=[]
  
  #print 'Init Process tree for pages:',len(pages)
  cnt_process=0
  all_p=[]
  addresses=[]
  for pagina in pages:
   cind2+=1
   if pagina.dt1 == None: continue
   endereco=pagina.dt1
   lines_doc=pagina.dt2
   def process_page(all_ps,id,purpose,pgs,finish,th):
    ln_o=''
    conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
    for lines_doc2_ in all_ps:      
    #try:
      endereco_url=lines_doc2_[0]
      lines_doc2=lines_doc2_[1]
      l2=Identify.prepare_layout(conn,id,purpose)
      if True :
       for s in lines_doc2:
        ln_o=s
        addresses.append(endereco_url)
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
    #print 'Thread ',pgs,' was finished.','Len:',len(ln_o),' process:',start_c/10
   if cnt_process >= 10:
    #print 'Start thread job :',cind2,' process:',
    threads_fd.append(thread_cntl())
    #process_page(all_p,usr,purp,cind2,threads_fd[len(threads_fd)-1],cind2)
    thread.start_new_thread(process_page,  (all_p,usr,purp,cind2,threads_fd[len(threads_fd)-1],cind2) )
    all_p=[]
    cnt_process=0
    continue
   else:
    all_p.append([endereco,lines_doc])
   cnt_process+=1
  #--
  ind_fs=0
  while True:
   if (len(threads_fd)-ind_fs) == 0: break
   #print 'Processing...',len(threads_fd)-ind_fs,',ind_fs:',ind_fs
   ind_fs=0
   time.sleep(10)
   conti=False
   for d in threads_fd:
    if not d.finished: conti=True
    if d.finished: ind_fs+=1
   if conti: continue
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
  
  # retorno:
  '''
   ->gravar na ontologia semantic_objects2, os qualificadores de definicao,composicao( achar objectos com destinacao(info-composicao), que contem as informacoes de propriedades )
   ->gravar na ontologia semantic_objects2, os qualificadores de estado( achar objectos com destinacao(info-state), que contem as informacoes de estado->links para cada momento das propriedades )
   
   ->gravar na ontologiao links_objetcts os qualificadores definidores de relacao , link ,conexao, etc.. ( achar objectos com destinacao(info-relaction), que contem as informacoes de relacoes )
   
   ->os qualificadores de filtro,foco informados na sentenca do clipping seram utilizados para o retorno no clipping
  '''
  
  
  

  layers_processed=[]
  
  for e in result_onto_tree_er:
    #================    
    topicos_composicao=[] # ->semantic_objects2
    topicos_relaction=[] # ->semantic_relactions2
    topicos_infostate=[] # ->semantic_infostate
    
    objs_prs=get_objs_purp(e.name,'COMPOSICAO',usr,conn)  
    tops_cmp_prs=get_objectdt_by(objs_prs,usr,conn)  
    
    objs_prs=get_objs_purp(e.name,'INFO-STATE',usr,conn)  
    tops_infos_prs=get_objectdt_by(objs_prs,usr,conn)  
    
    objs_prs=get_objs_purp(e.name,'RELACTION',usr,conn)  
    tops_rel_prs=get_objectdt_by(objs_prs,usr,conn)  
    
    objets_Real_post=[] # REAL-ONTOLOGY-POST=> qualificadores que indicam se deve ou nao fazer parte da ontologia primaria(ontologia principal de conhecimento )->instrucao privilegiada
    #================    
    layer_post=mdNeural.mdLayer()
    layers_processed.append(layer_post)
    foco_h=[] #-> usado para focar os elementos pertinentes � observacao para o historico
    foco_h2=[]
    #========================
    for t in  e.topicos:
     for d in t.dt:
        if d.upper() == 'FOCO':
          for s in t.sinases:
            foco_h2.append(s)
            for d2 in s.nr.dt: 
             foco_h.append(d2)
    #========================
    for t in  e.topicos:
     for d in t.dt:
        if d.upper() == 'REAL-ONTOLOGY-POST':
          for s in t.sinases:
            for d2 in s.nr.dt:      #[objecto] 
             objets_Real_post.append([d2])
     #==================================    
     fnd=False
     for d in t.dt:
      if not fnd:
        if d.upper() == 'IDENTIFICADOR':
          for s in t.sinases:
           if not fnd:
            for d2 in s.nr.dt:
             obj_nm=d2
             layer_post.name=obj_nm
             break
     #==================================    
     fnd=False
     for d in t.dt:
      if not fnd:
       for d2 in tops_cmp_prs:
        if d.upper() == d2.upper():
         fnd=True
         break
     if fnd:
        topicos_composicao.append(t)     
     #==================================    
     fnd=False
     for d in t.dt:
      if not fnd:
       for d2 in tops_rel_prs:
        if d.upper() == d2.upper():
         fnd=True
         break
     if fnd:
        topicos_relaction.append(t)     
     #==================================    
     fnd=False
     for d in t.dt:
      if not fnd:
       for d2 in tops_infos_prs:
        if d.upper() == d2.upper():
         fnd=True
         break
     if fnd:
        topicos_infostate.append(t)     
    #=    
    for t_com in topicos_composicao:
     for s in t_com.sinapses:
      layer_post.set_topico_nr(t_com.nr)
    #=====================  
    #
    links=[]
    for lnk_s in topicos_relaction:
     dt=[]
     for s in t_com.sinapses:
      for d in nr.dt:
       o= get_object_by_data(dt,usr,conn) 
       if o != None:
        layer_post.set_link(o,s.opcode) # opcode=> link, motivo da conexao
    if len(objets_Real_post)==0:
     post_object_by_data2(layer_post,usr,conn,termo,foco_h2)
    else:# se estiver na lista objets_Real_post, postar como ontologia principal
     post_object_by_data(layer_post,usr,conn,termo,foco_h2)
  
    # historico
    
    
    
    for t_hist in topicos_infostate: # historico, identificador do referencial
     state_type=t_hist.dt
     composicao=[]
     rels=[]
     #=========
     if len(foco_h)==0:
       for t_com in topicos_composicao:
         composicao.append(t_com)
     else:
      for t_com in topicos_composicao:
       fnd=False
       for f in foco_h: #composicao, elementos considerados
        if not fnd:
         for s in t_com.sinapses:
          if f.upper() in s.dt :
            composicao.append(t_com)
            fnd=True
            break
        else: break    
     #========= lnks
     if len(foco_h)==0:
       for t_com in topicos_relaction:
         rels.append(t_com)
     else:
      for t_com in topicos_relaction:
       fnd=False
       for f in foco_h: #rels, links considerados
        if not fnd:
         for s in t_com.sinapses:
          if f.upper() in s.dt :
            rels.append(t_com)
            fnd=True
            break
        else: break    
     
     post_datah_state(state_type,layer_post.name,composicao,rels,usr,conn)
   
  #==================================
  #   filtro,foco para  indicar o que extrair dos objetos acima postados
  #==================================
  s_foco=[]
  s_restricao=[]
  s_filtro=[]
  s_m=[] # msg ou clipping
  for lay in onto_basis.nodesER:
    nodes2=lay.get_links('FACT')  
    for lay in nodes2:
      lay=lay.lr
      for top in lay.topicos:
       for dts in top.dt:
        if dts.upper() == "FILTRO":
         for s in top.sinapses:
             s_filtro.append(s.nr)
        if dts.upper() == "FOCO":
         for s in top.sinapses:
             s_foco.append(s.nr)
        if dts.upper() == "RESTRICAO":
         for s in top.sinapses:
             s_restricao.append(s.nr)
        if dts.upper() == "PURPOSE-DST":
         for s in top.sinapses:
           for ds1 in s.nr.dt:
             s_m.append(ds1)
  #==================================
  '''
    1 -setar foco nos objectos
    2 -caracteristicas + links
    3 -layout-out com interesses
    4 -layout-code para extrair informacao
    5 -inserir no clipping return 
  '''
  for lr in layers_processed:
   lr_name=lr.name
   #foco 
   consid=[]
   #============================================
   for f in s_foco:
    for nr2 in lr.topicos:
     if lr.compare_dt_depend(conn,usr,purp,f,nr2,[]):
      consid.append(nr2)
   #============================================
   for f in s_filtro:
    for nr2 in lr.topicos:
     if lr.compare_dt_depend(conn,usr,purp,f,nr2,[]):
      consid.append(nr2)
   #============================================
   for f in s_restricao:
    for nr2 in lr.topicos:
     if lr.compare_dt_depend(conn,usr,purp,f,nr2,[]):
      consid.append(nr2)
   #============================================
   for c in consid:
     lr.put_publish(c)   
   #============================================
  #========================================================================================================================================
  #========================================================================================================================================
  data_return=[]
  # char  layoutcode
  ind_c=0
  for data_c in result_onto_tree_er:
   #==========
   cmps_nr=layers_processed[ind_c].get_all()
   ind_c+=1
   #==========
   runc=result_onto_tree_bpm[ind] # rct original, ractionline q processou as informacoes
   addr_url=addresses[ind]
   layout_codes=runc.get_links('LAYOUT-CODE')
   nms=[]
   for d in result_onto_tree_bpm:
    nms.append(d.lr.name)
   rts2=prepare_search_customlayouts(nms,cmps_nr,usr,conn) #purposes,dts,usr
   data_return.append(rts2)
   #========================================================================================================================================
   #  
   #==================================== 
   all_txt=''
   for dt in data_return: # post no clipping
    all_txt+=(' '+dt)
  
   all_txt=umisc.trim(all_txt)
   if all_txt != "":
    #==       classificacao/categoria
    #class=get_class(purpose) - > retorna o label do purpose
    class_c = get_class(purp,usr,conn)
    #==       post no clipping 
    if len(s_m) <=0 :
     cursor.execute (" insert into clipping_return(username,retorno,categoria,href) values ( %s , %s , %s , %s )", (usr, all_txt,class_c,''))   
    else:
     has_clipp=False
     has_msg=False
     for d in s_m: # verificar onde inserir
      if d.upper()=="CLIPPING":
       if not has_clipp:
         has_clipp=True       
         cursor.execute (" insert into clipping_return(username,retorno,categoria,href) values ( %s , %s , %s , %s )", (usr, all_txt,class_c,''))   
      elif d.upper()=="FEED":
       if not has_msg:
         has_msg=True       
         cursor.execute (" insert into  INBOX_MSG (username,MSG,SOURCE,REFERENCIAS) values ( %s , %s , %s , %s )", (usr, all_txt,class_c,addr_url))   
      
  #=========================================================================================================================================== 
  conn.close()  

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
 cursor.execute ("SELECT USERNAME,TERMO,TRIGGER_AS FROM clipping_info LIMIT 0 , 10 ") # 10 rows por vez
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
    for pur_p in purps:
     process_termo(termo,username,pur_p,start_c,sys.argv[0])

start_c=0
if len(sys.argv) > 1:     
 start_c=int(sys.argv[1])

      
process_sentences(start_c)

 
 