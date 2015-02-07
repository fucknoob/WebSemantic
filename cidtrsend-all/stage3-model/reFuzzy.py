#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''
''' indexar objetos para classificacao,relacionamento -->  conhecimento seguro, para formar base de conhecimento   '''


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
import gc
import time

from weakref import proxy

import umisc

import mdLayout
import mdER
import mdNeural
import mutex

import logging
from StringIO import StringIO
import datetime


import conn

conn= conn.conn_mx


entry_doc =[]

class Task_C:
 def __init__(self,Dt1=None,Dt2=None):
   self.dt1=Dt1
   self.dt2=Dt2

 
#create  table know_pages( i integer not null default serial, pg long, username varchar(20) , primary key (i)  ) 
def get_db_pages(usr2):
  resultSet = conn.sql ("select pg from know_pages where USERNAME='"+usr2+"' order by i") 
  typ=[]
  for results in resultSet:
    ts=results[0].read()
    if umisc.trim(ts) != '' and umisc.trim(ts) != '\n' and umisc.trim(ts) != '\r':
     typ.append(ts)
  print 'Reuse pgs:',len(typ)
  return  typ 
 
def post_db_page(usr2,pg): 
  sql1="insert into know_pages(pg,username) values(?,?)"
  try:
   conn.sqlX (sql1,([pg,usr2]))
  except Exception,err: print 'Erro ao post(know-pages):',err

 
def load_pages_know(usr) :
 rts=get_db_pages(usr)
 if len(rts) > 0:
  cnt=0
  for r in rts:
     cnt+=1
     entry_doc.append([ Task_C('debug',r),cnt   ]  )  
 elif len(rts) == 0:
  file = open("c:\\wamp\\www\Neural\\tst_training.txt")
  cnt=0
  lsn=''
  while 1:
    line = file.readline()
    if not line:
        #if umisc.trim(lsn) != '':
        # cnt+=1        
        # entry_doc.append([ Task_C('debug',lsn),cnt   ]  )
        break
    #===============================    
    s=umisc.trim(line)
    if  s == '' or s =='\n':
     cnt+=1
     lsn=lsn.replace('\r',' ')
     lsn=lsn.replace('\n',' ')     
     entry_doc.append([ Task_C('debug',lsn),cnt   ]  )
     post_db_page(usr,lsn)
     lsn=''
    else:
     lsn+=(' '+line)
     
           
           
#entry_doc= [Task_C('debug','Groupon é um site de compra coletiva. É o primeiro no mundo.')]
#entry_doc= [Task_C('debug','O Groupon é o primeiro no mundo.')]

#entry_doc=[[ Task_C('debug','A fome é a causa de tanta violência no mundo que os líderes deixam acontecer bem proximo do povo , sendo maior que as guerras.') ,1 ]]

 
#entry_doc = ['vectra é um bom carro com design inteligente, em composto por fibra de carbono restrito em carro de passeio ',' expectativas de carro com venda fortes','casa bom estado venda'] 
#entry('viagens melhores opções',['viagem para o nordeste é muito mais tranquilo, composto por translados mas restrito para criancas '])
 

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('DYNAMIC-CODE-ENGINE')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping



connTrace=conn
conn4=conn
conn5=conn
conn3=conn


mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn3
mdNeural.conn4=conn4


mtx=mutex.mutex ()
mtx2=mutex.mutex ()




   
def  Identify_pre_process_data (l2,ln_o,onto_basis,purpose,id,t_h,ret_ps):   
 Identify.pre_process_data(l2,ln_o,onto_basis,purpose,id,t_h,ret_ps)   
   

#===================
def get_typ(obj,usr2):
  resultSet = conn.sql ("select TYP from DATA_BEHAVIOUR_PY where OBJETO='"+obj+"' and USERNAME='"+usr2+"' order by i") 
  typ=0
  for results in resultSet:
    typ=results[0]
  return  typ
#=============================================== 

def mount_node(term,id,purposes):
 rets=[]
 for purpose in purposes:
     l=Identify.prepare_layout(id,purpose)
     allp=[]
     onto=Identify.prepare_data_by_ask(l, term,id,purpose,allp )
     rets.append( [onto,allp] )
 return rets

 
#SEMANTIC_OBJECT_DT2->3, SEMANTIC_OBJECT2->3,SEMANTIC_RELACTIONS2->3
 
 

# efetua o post de um layer
def post_object_by_data3p(layer,cenario,usr,termo,foco,posted_objs,senti,l_p_ant): 
 if layer.name == '' : return
 def get_top_level(obj,foc,usr,termo_s):
   rts=[]
   resultSet = conn.sqlX ("SELECT lev,id_top FROM  SEMANTIC_OBJECT_DT3 where OBJECT = ? and TOPICO= ? and USERNAME = ? and UID= ?  order by LEV ",([obj,foc,usr,termo_s]))
   for results in resultSet:
      i=results[0] 
      id_top=results[1]
      rts.append([i,id_top])
   return rts
 #=======================  
 nameo=layer.name
 if umisc.trim(nameo) == '' or umisc.trim(nameo) == '\n' :
  if l_p_ant != None:
    nameo=l_p_ant.name
  if umisc.trim(nameo) == '' or umisc.trim(nameo) == '\n' :  
   return
 
 fnd_tops=False
 
 l_p_ant=layer
 
 print 'POST:LR:',nameo
 print '++------------------------------------------'
 for s in layer.topicos:
  print 'DT:',s.dt
  fnd_tops=True
  for d in s.sinapses:
   print d.nr.dt
 print '++------------------------------------------'
 
 if not fnd_tops: return
 
 print 'Post-obj:[',nameo,']'
 no_post_o=False
 for [s,st] in posted_objs:
  if s == nameo and st==senti :
     no_post_o=True
 posted_objs.append([nameo,senti])
 #========== 
 #if not no_post_o and len(layer.topicos)>0:
 if not no_post_o :
  sql1="insert into SEMANTIC_OBJECT3(username,objeto,cenar,senti) values(?,?,?,?)"
  try:
   conn.sqlX (sql1,([usr,nameo,cenario,senti]))
  except Exception,err: print 'Erro ao post(OBJECT):',err
 else: print 'Skip:',nameo,senti
 
 
 uid=0
 if len(layer.topicos) >0:
  resultSet2 =conn.sqlX ("select max(I) from SEMANTIC_OBJECT3 where username =? and objeto = ? and cenar = ? ",([usr,nameo,cenario]))
  for results2 in resultSet2:
      uid=results2[0] 
      break
 
 #if len(layer.topicos) >0:
 # print 'Obj:',layer.name,' Num tópicos:', len(layer.topicos)
 #= 
 
 def post_nr(usr,tp,level=1,id_top=1,just_sin=False):   
   try:
       if not just_sin:
        tp_Dt=''
        try:
         for d in tp.dt:
           if type(d) == type([] ):
            tp_Dt+=d[0]
           else: 
            tp_Dt+=d
        except :
          print 'Err:-nr.post(2):',tp.dt
        tp_name=tp_Dt
        if len(tp.sinapses)==0:
         sql1="insert into SEMANTIC_OBJECT_DT3(UID,topico,LEV,sin,dt,id_top,username) values(?,?,1,\'\',\'\',?,?)"
         try:
          conn.sqlX (sql1,([uid,tp_Dt,id_top,usr]))
         except Exception,escp:
          print 'Erro ao post(OBJ_DT):',escp,' DT:',nameo,tp_Dt
       else:
        tp_Dt=''
        try:
         for d in tp.dt:
           if type(d) == type([] ):
            tp_Dt+=d[0]
           else: 
            tp_Dt+=d
        except :
          print 'Err:-nr.post(2):',tp.dt
       #=================   
       for sn in tp.sinapses:
        sn_dt=''
        try:
         for s1 in sn.nr.dt:
          if type(s1) == type([] ):
           sn_dt+=s1[0]
          else: 
           sn_dt+=s1
        except :
         print 'Err:-nr.post:',sn.nr.dt
        sql1="insert into SEMANTIC_OBJECT_DT3(UID,dt,topico,LEV,sin,id_top,username) values(?,?,?,?,?,?,?)"
        if umisc.trim(sn.opcode) == '': sn.opcode='Relaction-oper-opcode'
        try:
         conn.sqlX (sql1,([uid,sn_dt,tp_Dt,level,sn.opcode,id_top,usr]))
        except Exception,es:
         print 'Erro ao post(OBJ_DT):',nameo,tp_Dt,sn_dt,sn.opcode,'{',es,'}'
         
        try: 
         sqlcc='select id_top from SEMANTIC_OBJECT_DT3 where uid=? and topico=? and lev=? and sin=? and id_top=?' 
         rest=conn.sqlX (sqlcc,([uid,tp_Dt,level,sn.opcode,id_top]))
         id_top=1
         for ns in rest:
           id_top=ns[0]
           break          
        except Exception,e:
          print 'Error post nr.',e,'->',[uid,tp_Dt,level,sn.opcode,id_top]         
        #==========
        post_nr(usr,sn.nr,level+1,id_top,True)
   except Exception,e:
    #print 'Error post nr.' ,  e
    log.exception('[Error post nr...]')
 #==========    ===============================================
 
 def post_nr2(usr,topdt,new_dt,sin_dt,level,id_top,sinapse):
    sql1="insert into SEMANTIC_OBJECT_DT3(UID,dt,topico,LEV,sin,id_top,username) values(?,?,?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([uid,topdt,new_dt,sin_dt,level,sinapse,id_top,usr]))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
  
 #==========    ===============================================
 indi=0
 for tp in layer.topicos:
  #==========    ===============================================
  indi+=1

  if len(foco) == 0:
    post_nr(usr,tp)
  else:
    print 'Get foco:',len(foco)
    for l in foco:
      #achar o topico e o level
      dts=''
      for ldt in l.dt:
       dts+=ldt
      level=get_top_level(nameo,l,usr,uid)
      if len(level)>0:
       for level_s in level:
        post_nr2(usr,dts,tp.dt,l.opcode,level_s[0],level_s[1],'FOCO')
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  SEMANTIC_RELACTIONS3(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D,UID) values(?,?,?,?,?,?,?)'   
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
  try:
   conn.sqlX (sqlc,([nameo,lnk.lr.name,lnk.opcode,usr,foco_o,foco_d,uid]))
  except Exception,err: print 'Erro post links:',err
  #===============
  #layer,cenario,usr,termo,foco
  post_object_by_data3p(lnk.lr,cenario,usr,termo,foco,posted_objs,senti,l_p_ant) 
 
 
def post_datah_state(state_type,obj,composicao,rels,usr):
 for sti in state_type:
  for compo in composicao:
   sql='insert into SEMANTIC_INFOSTATE( USERNAME,OBJECT,TOPICO,INDI_STATE ) VALUES(?,?,?,?)'
   conn.sqlX (sql,([usr,obj,compo,sti]))
  #== 
  for rels in composicao:
   sql='insert into SEMANTIC_INFOSTATE( USERNAME,OBJECT,TOPICO,INDI_STATE ) VALUES(?,?,?,?)'
   conn.sqlX (sql,([usr,obj,compo,sti]))
 
 
def post_object_by_data(layer,usr,termo,foco):
 def get_top_level(obj,foc,usr):
   rts=[]
   resultSet = conn4.sqlX ("SELECT LEV,id_top FROM  SEMANTIC_OBJECT_DT where OBJECT = ? and TOPICO= ? and USERNAME = ?  order by LEV ",([obj,foco,usr]))
   for results in resultSet:
      i=results[0] 
      id_top=results[1]
      rts.append([i,id_top])
   return rts
 #=======================  
 nameo=layer.name
 sql1="insert into SEMANTIC_OBJECT(username,objeto,TERMO) values(?,?,?)"
 conn.sqlX (sql,([usr,nameo,termo]))
 for tp in topicos:
  #==========    ===============================================
  def post_nr(usr,tp,level=1,id_top=1):
   tp_Dt=''
   for d in tp.dt:
    tp_Dt+=d
   tp_name=tp_Dt
   for sn in tp.sinapses:
    sn_dt=''
    for s1 in sn.nr.dr:
     sn_dt+=s1
    sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico,LEV,id_top) values(?,?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,nameo,tp_Dt,sn_dt,level,id_top]))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
    #==========
    if True:
        sqlcc='select id_top from SEMANTIC_OBJECT_DT where uid=? and topico=? and lev=? and sin=? and id_top=?' 
        res=conn.sqlX (sqlcc,([usr,nameo,tp_Dt,sn_dt,level,id_top]))
        id_top=1
        for ns in res:
          id_top=ns[0]
          break              
    post_nr(usr,sn.nr,level+1,id_top)
  #==========    ===============================================
  def post_nr2(usr,topdt,new_dt,sin_dt,level,id_top):
    sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico,LEV,id_top) values(?,?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,topdt,new_dt,sin_dt,level,id_top]))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
  
  #==========    ===============================================
  if len(foco) == 0:
    post_nr(usr,tp)
  else:
    for l in foco:
      #achar o topico e o level
      dts=''
      for ldt in l.dt:
       dts+=ldt
      level=get_top_level(nameo,l,usr)
      if len(level)>0:
       for level_s in level:
        post_nr2(usr,dts,tp.dt,l.opcode,level_s[0],level_s[1])
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  SEMANTIC_RELACTIONS(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D) values(?,?,?,?,?,?)' 
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
  conn.sqlX (sqlc,([nameo,lnk.lr.name,lnk.opcode,usr,foco_o,foco_d]))
  #===============
  post_object_data(lnk.lr,usr)

  
def clean_s(strc2):
   k=''
   if (type(strc2).__name__) == 'SapDB_LongReader':
     strc=strc2.read()
   else:  
     strc=''+strc2
   for ss in strc:
     if ss.lower () in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','y','w',
                       '0','1','2','3','4','5','6','7','8','9', 
                       '~','`','!','@','#','$','%','^','&','*','(',')','{','}','[',']','\'','"',':',';','/','?','<',',','>','.','\\','|','-','_','=','+',' ','\n']:     
      k+=(ss)
   return k

 
def run_layout_parser(lay_names,dts,usr):
 #====================================================================================================
 #chamar os codigos 
 codes_Result=[]
 for dt in lay_names:
  print 'Layout-Code',dt
  #=========================
  resultSet = conn.sql ("select CODE from DATA_BEHAVIOUR_CODE_PY where OBJETO='"+dt+"' and USERNAME='"+usr+"' order by i") 
  for results in resultSet:
    typ=get_typ(dt,usr)
    orig_code=results[0]
    o=clean_s(results[0])
    #o=results[0]
    code=o

    print 'Code type:',typ
    if typ == 1: #executavel
     code+=' \n\nretorno_srt=run(sr_int_cmd_param)'
    else: # executa somente o codigo
     pass
    #================================== 
    try:
     sr_int_cmd_param=dts
     exec(code, locals(), locals())
     pass
    except Exception,e:
     log.exception('[Layout(p) Exec Error]Stack execution---------------------------------')
     print '[code]','\n',code,'\n\n\n','}'     
     #log.info(code)     
     #====
    if typ == 1: #executavel
     # adicionar ao codes_Result o retorno_srt(lines->[endereco,dados] ) 
     if retorno_srt != None:
      codes_Result.append( retorno_srt )
 #===================
 return codes_Result    
  
# cenario=> endereco da pagina, documento ou fonte que contem fatos+elementos envolvidos-> pode descrever uma parte de um macrocenario(cenario composto por varios docs) ou microcenario(cenario composto por um unico doc) 
#  gravacao
#     layout -> identificador=objeto -> topicos
#               referencia -> links p outros objetos
#               composicao -> propriedades
#               state -> estado  
# --------------- tipos de referencias adicionais
#               classificacao -> enquadramento
#               dominio -> agrupamento
#               mean -> significado
#               indicador-> auxiliar de indicacao, usado p solucionar ambiguidades

#composicao,mean,dominio,classificacao,indicador,referencial,relacao

def post_object_by_data3(layer,cenario,usr,termo,foco,purpos,senti,l_p_ant):
 print 'LayoutOnto->Purpose:',purpos
 def get_parsers():
  prs=[] 
  sql = "SELECT DT from knowledge_manager where USERNAME = '"+usr+"' and typ=2 and DEST=\'postLayout\' and layout_onto = ? order by i "
  resultSet = conn.sqlX (sql,([purpos]))
  for results in resultSet:
   prs.append( results[0] )
  return prs
 #=================================================  
 objects=[]
 post_parsers=get_parsers ()
 gc.collect ()
 # call run_layout_parser
 #print 'Prepare post lay:' ,layer.name
 objects=run_layout_parser(post_parsers,layer,usr)
 gc.collect ()
 #print 'Post lay ok:' 
 #
 #print 'Post lays---:' 
 ind_objs=0
 ind_objs2=0
 posted_objs=[]
 for arro in objects:
  for o in arro:
   ind_objs+=1
   ind_objs2+=1
   if ind_objs2 >= 500 :
    #print 'Post lr:',ind_objs
    ind_objs2=0
   post_object_by_data3p(o,cenario,usr,termo,foco,posted_objs,senti,l_p_ant)
 #print 'Post ok----------------'  
  
  
  
   
def get_object_by_data(obj,usr):
 sql='select objeto from SEMANTIC_OBJECT where i=? and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 for results in resultSet:
      obj_nm=results[0] 
 #-----------
 lay=mdNeural.mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 sql='select DT,TOPICO from SEMANTIC_OBJECT_DT where OBJECT=? and USERNAME = ? '
 resultSet = conn4.sqlX (sql,([obj,usr]))
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

def get_objs_purp(obj,purspe,usr): 
 #-----------
 rts=[]
 sql='select DT, TOPICO from SEMANTIC_OBJECT_DT where  USERNAME = ? '
 resultSet = conn.sqlX (sql,([obj,usr]))
 for results in resultSet:
      TOP=results[1]
      DT=results[0]
      OB=results[2]
      if TOP.upper () == 'SPECIAL-PURPOSE':
       if DT.upper () == purspe:
        rts.append(OB)
 return rts
 

def get_objectdt_by(objs,usr): 
 rts=[]
 for obj in objs:
  sql='select distinct TOPICO from SEMANTIC_OBJECT_DT where OBJECT=? and USERNAME = ? '
  resultSet = conn.sqlX (sql,([obj,usr]))
  for results in resultSet:
      TOP=results[0]
      if TOP.upper () != 'SPECIAL-PURPOSE':
       rts.append(TOP)
       break
 return rts

#//2 
def get_ontology(aliases,purposes,usr): 
 tree_h=[]
 for alias in aliases:
     resultSet = conn3.sqlX ("SELECT OBJETO FROM  SEMANTIC_OBJECT where OBJETO = ?  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn.sqlX ("SELECT OBJ_DEST,FOCO,FOCO_D FROM  SEMANTIC_RELACTIONS where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn.sqlX ("SELECT OBJ_ORIG,FOCO,FOCO_D FROM  SEMANTIC_RELACTIONS where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        obj_principal=get_object_by_data(i,usr)
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
         obj_k=get_object_by_data(obj_id,usr)
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
         obj_k=get_object_by_data(obj_id,usr)
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

 
def get_pages_len(usr):
 if len(entry_doc) > 0 :
  return len(entry_doc)
 
 pages=[]
 sql='select count(*) from WEB_CACHE where USR = ? and PROCESSED <> \'S\'  '
 resultSet = conn.sqlX (sql,([usr]))
 obj_nm=None
 ind=0
 for results in resultSet:
   ind=results[0]
   if ind > 500 : ind=500   
   
 return ind
  
def get_pages(usr,start_c):
 pages=[]
 if len(entry_doc) > 0 :  
  return entry_doc
 
 #sql='select URL,PG,I,TITLE,PURPOSE from WEB_CACHE where USR = ? and PROCESSED <> \'S\' and termo= ?  and  pg is not null and length(pg) > 1  order by i '
 #resultSet = conn.sqlX (sql,([usr,termo]))
 #==
 resultSet = conn.sqlX(" call ret_pages (:usr,:starti )",[usr,start_c] )
 #==
 obj_nm=None
 idx=1
 print 'Start index:',start_c 
 for results in resultSet:
   pg_add=results[0].read()
   pg_txt=results[1].read()
   pg_txt=pg_txt.replace('\n',' ')
   pg_txt=pg_txt.replace('\r',' ')
   id_p=results[2]
   title=results[3].read()
   purp=results[4]
   #print 'Page:',idx
   pg_txt=( title+' ! '+ pg_txt )
   idx+=1
   pages.append([Task_C(pg_add,pg_txt),id_p]) 

   
 return pages 
  


def get_class(purp,usr):
 sql = "SELECT Label from knowledge_manager where USERNAME = '"+usr+"' and typ=4 and DT= s% order by i "
 resultSet = conn.sqlX (sql,([purp]))
 for results in resultSet:
   return results[0]
 return ''
 
#//2 
def process_page(all_ps,id,purpose,pgs,finish,th,pg_index_rs,all_size_pg,job_index,addresses,result_onto_tree_er,c_ontos,usr,termo,uid_S):
 #try:
 l_p_ant=None
 if True:
   ln_o=''
   endereco_url=all_ps[0]
   result_onto_tree_er=[]
   #===
   progress=int(pg_index_rs/all_size_pg)   
   #if True:
   for lines_doc2_ in all_ps :
    #lines_doc2_=all_ps;
    #try:
    print 'Start page:',pg_index_rs,' of total:',all_size_pg
    if True:
     endereco_url=lines_doc2_[0]
     lines_doc2=lines_doc2_[1]
     uid_DS=uid_S
     print 'UID:',uid_DS,'-----------------------'
     if True :
      #============= parse fuzzy ===========================================
      t_threads=[]
      ret_ps=[]
      indice_linha=0;
      inds2p=0
      if True:
      #for s in lines_doc2:
       indice_linha+=1
       addresses.append(endereco_url)
        
       
       print 'Preprocessdata in page:',pg_index_rs,' of total:',all_size_pg, ' line:',indice_linha,' of:', len(lines_doc2)
       if inds2p> 100:
        pro=(indice_linha*1.0)/len(lines_doc2)
        print 'TraceQI:', pro 
        inds2p=0
       inds2p+=1
       
       for [onto_basis2,onto_basis22,purpose] in c_ontos:
        ret_ps.append([])
        t_threads.append(thread_cntl())       
        print 'Start Identify->pre_process_data():',purpose
        ret_ps[len(ret_ps)-1]=Identify.pre_process_data2(onto_basis2,onto_basis22,lines_doc2,purpose,id,t_threads[len(t_threads)-1],[])
        print 'End Identify->pre_process_data():'
       #-> ret_ps = layers da pagina
      result_onto_tree_er.append([ret_ps,endereco_url,uid_DS])
      print 'DBG:',result_onto_tree_er  
   #================   
   indc=0
   returns=[]
   for sb in result_onto_tree_er:
    [ret_psk,endereco_url,uid_DS]=sb
    indc+=1
    #post page
    indc2=0    
    for [lays,purpose] in ret_psk:
     for lay in lays:
      indc2+=1 # cada layer é uma sentenca
      try:
        #print 'Post layer',lay.name,'--------------------------------------','->',uid_DS, ' Result onto:',indc,' of ',len(result_onto_tree_er),' Pg:',indc2, ' of ',len(ret_psk)*len(lays)
        #for tps  in lay.topicos:
        # print tps.dt
        # print 'SNS:-------------------'
        # for t in tps.sinapses:
        #  print t.nr.dt
        # print 'SNS(END):-------------------'
        #print '------------------------------' 
        returns.append(lay)  
      except Exception,errc:
        sw= 'Error on post object:'
        log.exception(sw)         
        
   return returns
   
#                 termo,username,pur_p,start_c,sys_argv,layouts_f ,layouts_f2                   
def process_termo(dt,usr,purp,start_c,path_j,layouts_fz):
  pages=[]
  ths2=[]
  #========================================================================================================================================
  job_index=1
  pages=dt
  if len(pages) > 0:
   print 'Process pages:(',len(pages),')'
   
  #=====================================
  cind2=0
  threads_fd=[]
  result_onto_tree_er=[] # caracteristicas,descricoes,etc...
  result_onto_tree_bpm=[] # fluxo de acoes, sequencia de actions
  result_linked=[]
  
  cnt_process=0
  addresses=[]
  all_size_pg=len(pages)
  pg_index=0
  d1=1
  rets=[]
  
  try:
      total_pages=len(pages)
      if total_pages ==0 : 
       return
       
       
      idx1=-1
      idx2=0
      for pagina in pages:
       uid_S=0
       idx1+=1
       if pg_index < idx1: continue
       idx2+=1
       if idx2 > 10 : continue       
       #==
       all_p=[]
       endereco='internal'
       lines_doc=pagina
       all_p.append([endereco,lines_doc])
       cnt_process+=1
       d1+=1
       cind2+=1
       if True:
        print 'Process page num:',pg_index,' len.doc:',len(lines_doc)
        rt=process_page(all_p,usr,purp,cind2,None,cind2,pg_index,all_size_pg,job_index,addresses,result_onto_tree_er,layouts_fz,usr,'internal',uid_S)
        for r in rt:
         rets.append(r)
        #================
        print 'End page:',pg_index,' of total:',len(pages)
        #================
        
        
        
       pg_index+=1
  except Exception,e:
       log.exception('Error Processing pages:') 
  
  return rets
 
def get_layouts(usr,purpose): 
 import mdER3
 mdER3.conn=conn 
 mdER3.conn4=conn4
 mdER3.conn3=conn3

 p =mdER3.get_LayoutsFZ(usr,purpose)
 return p   


def get_layouts2(usr,purpose): 
 import mdER3
 mdER3.conn=conn 
 mdER3.conn4=conn4
 mdER3.conn3=conn3

 p=mdER3.get_LayoutsFZ2(usr,purpose)
 return p  
 
def clear_termo(username ):
 
 sql1=" delete from SEMANTIC_OBJECT_DT3 where  username = ?    "
 try:
  conn.sqlX (sql1,([username]))
 except Exception,err: print 'Erro ao del(OBJECT-DT):',err,[username]

 sql1=" delete from SEMANTIC_RELACTIONS3  where username = ?   "
 try:
  conn5.sqlX (sql1,([username]))
 except Exception,err: print 'Erro ao del(OBJECT-REL):',err,[username]

 sql1=" delete from SEMANTIC_OBJECT3 where username = ?   "
 try:
  conn5.sqlX (sql1,([username]))
 except Exception,err: print 'Erro ao del(OBJECT):',err,[username]
 
 conn.commit()

class th_i:
 def __init__(self):
  self.end=False 
 
 
def process_sentences(dt,purpose,usr): 
 
 
 purps=purpose # purposes-> layouts definidos dentro dos facts dos ractionlines escalados
 to_run_c=[]
 print 'Process load layout...'
 if True:
    all_layouts=[]
    for pur_p in purps:
     print 'Start purpose-load-layout:',pur_p,'--------------------------------------------------------------'
     
     layouts_f =get_layouts(usr,pur_p)
     layouts_f2=get_layouts2(usr,pur_p)
     
     onto_basis2=[]
     for onto_basisk  in layouts_f:
         l2=Identify.prepare_layout(usr,onto_basisk)
         onto_basis2.append(l2)
         
     onto_basis22=[]
     for onto_basisk in layouts_f2:
         l2=Identify.prepare_layout(usr,onto_basisk)
         #print 'Prepare layout(2):',onto_basisk,'->',l2.fzs
         onto_basis22.append(l2)     
     
     all_layouts.append([onto_basis2,onto_basis22,pur_p])     
      
     print 'End   purpose:',pur_p, '--------------------------------------------------------------'
    #
    return process_termo(dt,usr,pur_p,0,'',all_layouts )
    #=========================
     
  
  
 

import time
startTT = time.clock ()

 
   
def entry(dt,purpose,usr):  
  ret=process_sentences(dt,purpose,usr)
  print 'reFuzzy:',ret
  return ret
 
 
#entry(['groupon classe'], ['simple-search-classify'],'igor.moraes')
 


