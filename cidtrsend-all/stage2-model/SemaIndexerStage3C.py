#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''
''' ractionline p auto-ask(classify,relactionate,composition) ->auto-ask para classificar,relacionar,build objectos dentro dos purposes(ambientes) , as quais sao passadas por linha de comando, roda automaticamente '''
import mdTb
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

from weakref import proxy

import umisc

import mdLayout
import mdER
import mdNeural
import Identify 

import logging
import mdOntology


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('SemanticIndexer-Stage2')


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping


import conn

conn= conn.conn_mx

connTrace=conn
conn4=conn
conn5=conn
conn3=conn

'''
conn= MySQLdb.connect(host='dbmy0023.whservidor.com', user='mindnet' , passwd='acc159753', db='mindnet')
connTrace= MySQLdb.connect(host='dbmy0032.whservidor.com', user='mindnet_2' , passwd='acc159753', db='mindnet_2')
conn4=MySQLdb.connect(host='dbmy0050.whservidor.com', user='mindnet_4' , passwd='acc159753', db='mindnet_4') 
conn5= MySQLdb.connect(host='dbmy0035.whservidor.com', user='mindnet_3' , passwd='acc159753', db='mindnet_3') 
conn3= MySQLdb.connect(host='dbmy0039.whservidor.com', user='mindnet_5' , passwd='acc159753', db='mindnet_5') 


def config_conns(conn_):
 cursor=conn_.cursor ()
 cursor.execute('SET SESSION wait_timeout = 90000')

config_conns(conn) 
config_conns(connTrace) 
config_conns(conn4) 
config_conns(conn3) 
 
'''


mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn3
mdNeural.conn4=conn4

   
def  Identify_pre_process_data (l2,ln_o,onto_basis,purpose,id,t_h,ret_ps):   
 Identify.pre_process_data(l2,ln_o,onto_basis,purpose,id,t_h,ret_ps)   
   


def start_job_sec(start,usr,path_j,th):
  cmd='python '+path_j+' "'+usr+'" '+str(start)  
  #os.execv('/usr/bin/python',(path_j,str(start)) )
  print 'Prepare cmd:',cmd
  os.system(cmd)
  th.finished=True


def mount_node(term,id,purpose):
 l=Identify.prepare_layout(id,purpose)
 allp=[]
 onto=Identify.prepare_data_by_ask(l, term,id,purpose,allp )
 return [onto,allp]

 
 
entry_doc =[]
 
#entry_doc = ['vectra é um bom carro com design inteligente, em composto por fibra de carbono restrito em carro de passeio ',' expectativas de carro com venda fortes','casa bom estado venda'] 
#entry('viagens melhores opções',['viagem para o nordeste é muito mais tranquilo, composto por translados mas restrito para criancas '])

 
 
def post_object_by_data2(layer,usr,termo,foco):
 def get_top_level(obj,foc,usr):
   rts=[]
   resultSet =conn.sqlX ("SELECT LEV FROM  SEMANTIC_OBJECT_DT2 where OBJECT = ? and TOPICO= ? and USERNAME = ?  order by LEV ",([obj,foc,usr]))
   for results in resultSet:
      i=results[0] 
      rts.append(i)
   return rts
 #=======================  
 nameo=layer.name
 sql1="insert into SEMANTIC_OBJECT2(username,objeto,TERMO) values(?,?,?)"
 conn.sqlX (sql,([usr,nameo,termo]))
 for tp in topicos:
  #==========    ===============================================
  def post_nr(usr,tp,level=1):
   tp_Dt=''
   for d in tp.dt:
    tp_Dt+=d
   tp_name=tp_Dt
   for sn in tp.sinapses:
    sn_dt=''
    for s1 in sn.nr.dr:
     sn_dt+=s1
    sql1="insert into SEMANTIC_OBJECT_DT2(username,object,dt,topico,LEV) values(?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,nameo,tp_Dt,sn_dt,level]))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
     log.exception("================")
    #==========
    post_nr(usr,sn.nr,level+1)
  #==========    ===============================================
  def post_nr2(usr,topdt,new_dt,sin_dt,level):
    sql1="insert into SEMANTIC_OBJECT_DT2(username,object,dt,topico,LEV) values(?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,topdt,new_dt,sin_dt,level]))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
     log.exception("================")
  
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
        post_nr2(usr,dts,tp.dt,l.opcode,level_s)
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  SEMANTIC_RELACTIONS2(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D) values(?,?,?,?,?,?)' 
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
   resultSet =conn4.sqlX ("SELECT LEV FROM  SEMANTIC_OBJECT_DT where OBJECT = ? and TOPICO= ? and USERNAME = ?  order by LEV ",([obj,foc,usr]))
   for results in resultSet:
      i=results[0] 
      rts.append(i)
   return rts
 #=======================  
 nameo=layer.name
 sql1="insert into SEMANTIC_OBJECT(username,objeto,TERMO) values(?,?,?)"
 conn.sqlX (sql,([usr,nameo,termo]))
 for tp in topicos:
  #==========    ===============================================
  def post_nr(usr,tp,level=1):
   tp_Dt=''
   for d in tp.dt:
    tp_Dt+=d
   tp_name=tp_Dt
   for sn in tp.sinapses:
    sn_dt=''
    for s1 in sn.nr.dr:
     sn_dt+=s1
    sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico,LEV) values(?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,nameo,tp_Dt,sn_dt,level]))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
     log.exception("================")
    #==========
    post_nr(usr,sn.nr,level+1)
  #==========    ===============================================
  def post_nr2(usr,topdt,new_dt,sin_dt,level):
    sql1="insert into SEMANTIC_OBJECT_DT(username,object,dt,topico,LEV) values(?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,topdt,new_dt,sin_dt,level]))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
     log.exception("================")
  
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
        post_nr2(usr,dts,tp.dt,l.opcode,level_s)
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

def get_object_by_data(obj,usr):
 
 sql='select trim(objeto),i from SEMANTIC_OBJECT3 where objeto=? and USERNAME = ? '
 resultSet =conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdNeural.mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 tpc2=lay.set_topico('identificador')
 nrc2= lay.set_nr(lay.name)
 tpc2.connect_to(lay,nrc2,'Composicao') 
 #print lay.topicos,'....................'
 print 'Read object:',obj,' uid:',uid
 #-----------
 if True :
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO),i from SEMANTIC_OBJECT_DT3 where "UID" = ' + str(uid) + ' and lev <=1 ' )
     obj_nm=None
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          ic=results[2]
          if ic == None: ic=0
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          # ---
          tps=lay.set_topico(TOP)
          #===
          #print 'Set topico:',TOP,' for layer:',obj_nm,' uid:',uid
          # ---
          tps.connect_to(lay,nr,'Composicao') 
          if True:
             #==     
             resultSet = conn3.sql ( 'select id_top,trim(DT),trim(TOPICO) from SEMANTIC_OBJECT_DT3 where UID = ' + str(uid) + ' and lev >  1 and id_top='+str(ic) + 'and i <> '+str(ic),  )
             obj_nm=None
             for results in resultSet:
                  DT=results[0] 
                  TOP=results[1]
                  nrc= lay.set_nr(DT)
                  #==
                  nr.connect_to(lay,nrc,'Composicao') 
 return lay   

def get_object_by_data_s2(obj,usr):
 
 sql='select trim(objeto),i from '+mdTb.table_object+' where objeto=? and USERNAME = ? '
 resultSet =conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdNeural.mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 tpc2=lay.set_topico('identificador')
 nrc2= lay.set_nr(lay.name)
 tpc2.connect_to(lay,nrc2,'Composicao') 
 #print lay.topicos,'....................'
 print 'Read object:',obj,' uid:',uid
 #-----------
 if True :
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO),i from '+mdTb.table_dt+' where "UID" = ' + str(uid) + ' and lev <=1 ' )
     obj_nm=None
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          ic=results[2]
          if ic == None: ic=0
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          # ---
          tps=lay.set_topico(TOP)
          #===
          #print 'Set topico:',TOP,' for layer:',obj_nm,' uid:',uid
          # ---
          tps.connect_to(lay,nr,'Composicao') 
          if True:
             #==     
             resultSet = conn3.sql ( 'select id_top,trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where UID = ' + str(uid) + ' and lev >  1 and id_top='+str(ic) + 'and i <> '+str(ic),  )
             obj_nm=None
             for results in resultSet:
                  DT=results[0] 
                  TOP=results[1]
                  nrc= lay.set_nr(DT)
                  #==
                  nr.connect_to(lay,nrc,'Composicao') 
 return lay  
 
 
def get_objs_purp(obj,purspe,usr): 
 #-----------
 rts=[]
 sql='select DT, TOPICO from SEMANTIC_OBJECT_DT where  USERNAME = ? '
 resultSet =conn4.sqlX (sql,([obj,usr]))
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
  resultSet = conn4.sqlX (sql,([obj,usr]))
  for results in resultSet:
      TOP=results[0]
      if TOP.upper () != 'SPECIAL-PURPOSE':
       rts.append(TOP)
       break
 return rts

#//2 

def get_cenars( alias ,usr):
     rs=[]
     alias='%'+alias+'%'
     resultSet = conn3.sqlX ("SELECT distinct cenar FROM  SEMANTIC_OBJECT3 where upper(OBJETO) like upper(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        cenar=results[0]
        rs.append(cenar)
     #print 'Cenars for:',alias,'->',rs
     return rs     
     
def get_senti( cenar ,usr):
     rs=[]
     resultSet =conn3.sqlX ("SELECT distinct senti FROM  SEMANTIC_OBJECT3 where cenar  = ?  and USERNAME = ?  ",([cenar,usr]))
     for results in resultSet:
        cenar=results[0]
        rs.append(cenar)
     #print 'Sentis for :',cenar,'->',rs
     return rs     
     
def get_ontology(aliases,purposes,usr): 
 tree_h=[]
 for alias in aliases:
  #cenars=get_cenars(alias,usr)
  #for cenar in cenars:
  if True:
   tree_cen=[]
   #sentis=get_senti( cenar ,usr)
   #for senti in sentis:
   if True:
     ''' '''
     if alias == '$$all$$': alias=''
     alias='%'+alias+'%'
     ''' '''
     h_tree_v=[]
     #resultSet = conn3.sqlX ("SELECT trim(OBJETO),i,cenar FROM  SEMANTIC_OBJECT3 where cenar = ?  and USERNAME = ? and senti=?   ",([cenar,usr,senti]))
     resultSet = conn3.sqlX ("SELECT trim(OBJETO),i,cenar FROM  SEMANTIC_OBJECT3 where upper(OBJETO) like upper(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        cenar=results[2]
        #===
        #print 'Obj: ',i, '->collects'
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS3 where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS3 where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
        #if len(obj_principal.topicos) > 0 :
        h_tree_v.append(obj_principal)
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
     if len(h_tree_v) > 0 :
      tree_cen.append(h_tree_v)      
   if len(tree_cen) > 0 :
    tree_h.append(tree_cen) 
 return tree_h       

 
def get_ontology_s2(aliases,purposes,usr): 
 tree_h=[]
 for alias in aliases:
  #cenars=get_cenars(alias,usr)
  #for cenar in cenars:
  if True:
   tree_cen=[]
   #sentis=get_senti( cenar ,usr)
   #for senti in sentis:
   if True:
     ''' '''
     if alias == '$$all$$': alias=''
     alias='%'+alias+'%'
     ''' '''
     h_tree_v=[]
     resultSet = conn3.sqlX ("SELECT trim(OBJETO),i,cenar FROM  "+mdTb.table_object+" where upper(OBJETO) like upper(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        cenar=results[2]
        #===
        #print 'Obj: ',i, '->collects'
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS3_1_4 where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS3_1_4 where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        obj_principal=get_object_by_data_s2(i,usr)
        #if len(obj_principal.topicos) > 0 :
        h_tree_v.append(obj_principal)
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
         obj_k=get_object_by_data_s2(obj_id,usr)
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
         obj_k=get_object_by_data_s2(obj_id,usr)
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
     if len(h_tree_v) > 0 :
      tree_cen.append(h_tree_v)      
   if len(tree_cen) > 0 :
    tree_h.append(tree_cen) 
 return tree_h  
 
 
 
def get_ontology2(aliases,purposes,usr): # sentencas do mesmo documento, relacionadas
 tree_h=[]
 for alias in aliases:
  cenars=get_cenars(alias,usr)
  for cenar in cenars:
   tree_cen=[]
   sentis=get_senti( cenar ,usr)
   for senti in sentis:
     h_tree_v=[]
     resultSet =conn3.sqlX ("SELECT trim(OBJETO),i,cenar FROM  SEMANTIC_OBJECT3 where cenar = ?  and USERNAME = ? and senti=?   ",([cenar,usr,senti]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        cenar=results[2]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        '''
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          cursor2 = conn3.cursor  ()          
          cursor2.execute ("SELECT OBJ_DEST,FOCO,FOCO_D FROM  SEMANTIC_RELACTIONS3 where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",(i,pr,usr))   
          resultSet = cursor2.fetchall ()
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
          cursor2 = conn3.cursor  ()          
          cursor2.execute ("SELECT OBJ_ORIG,FOCO,FOCO_D FROM  SEMANTIC_RELACTIONS3 where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",(i,pr,usr))   
          resultSet = cursor2.fetchall ()
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        '''
        #===--------------------------------------
        obj_principal=get_object_by_data(i,usr)
        if len(obj_principal.topicos) > 0 :
         h_tree_v.append(obj_principal)
        #===
        #c1=collect_objs_orig(purposes,i,usr)
        #==----------------------------------------
        #def parse_or(st):
        # s=[]
        # ind=0
        # for i in st:          
        #  if i == ',' or len(i) == ind:
        #   if len(i) == 0 : tmp+=i
        #   s.append(tmp)
        #   tmp=''           
        #  else:  tmp+=i 
        #  ind+=1
        #==----------------------------------------
        #for c in c1:
        # obj_id=c[0]
        # opc=c[1]
        # fco=c[2]
        # fcd=c[3]
        # obj_k=get_object_by_data(obj_id,usr)
        # foco_o=[]
        # foco_d=[]
        # r1=parse_or(fco)
        # for rc1 in r1:
        #   n=obj_principal.get_topico(rc1)
        #   foco_o.append(n)
        # r2=parse_or(fcd)
        # for rc1 in r1:
        #   n=obj_k.get_topico(rc1)
        #   foco_d.append(n)
        # obj_principal.set_link_ds(obj_k,opc,foco_o,foco_d)
        #==
        #c12=collect_objs_dest(purposes,i,usr)
        #==----------------------------------------
        #for c in c12:
        # obj_id=c[0]
        # opc=c[1]
        # fco=c[2]
        # fcd=c[3]
        # obj_k=get_object_by_data(obj_id,usr)
        # #===
        # foco_o=[]
        # foco_d=[]
        # r1=parse_or(fco)
        # for rc1 in r1:
        #   n=obj_k.get_topico(rc1)
        #   foco_o.append(n)
        # r2=parse_or(fcd)
        # for rc1 in r1:
        #   n=obj_principal.get_topico(rc1)
        #   foco_d.append(n)
        # #===
        # obj_k.set_link(obj_principal,opc)
     if len(h_tree_v)>0:
      tree_cen.append(h_tree_v)    
   if len(tree_cen) > 0 :      
    tree_h.append(tree_cen) 
 return tree_h  
 
class thread_cntl:
 def __init__(self):
  self.finished=False

class Task_C:
 def __init__(self,Dt1=None,Dt2=None):
   self.dt1=Dt1
   self.dt2=Dt2

   
def get_pages_len(usr,termo,purpose):  
 pages=[]
 sql='select count(*) from WEB_CACHE where USR = ? and PROCESSED <> \'S\'  and purpose= ? and termo = ? '
 resultSet =conn.sqlX (sql,([usr,purpose,termo]))
 obj_nm=None
 ind=0
 for results in resultSet:
   ind=results[0]
   if ind > 500 : ind=500  
 return ind
  
def get_pages(usr,start_c,termo,purpose):
 pages=[]
 sql='select URL,PG from WEB_CACHE where USR = ? and PROCESSED <> \'S\' and termo= ? and purpose = ?  LIMIT '+str(start_c)+' , 15 '
 resultSet =conn.sqlX (sql,([usr,termo,purpose]))
 obj_nm=None
 idx=1
 for results in resultSet:
   pg_add=results[0]
   pg_txt=results[1]
   #print 'Page:',idx
   idx+=1
   pages.append(Task_C(pg_add,pg_txt)) 
 return pages 
  


def get_class(purp,usr):
 sql = "SELECT Label from knowledge_manager where USERNAME = '"+usr+"' and typ=4 and DT= s% order by i "
 resultSet = conn.sqlX (sql,([purp]))
 for results in resultSet:
   ar=results[0]
   return ar
 return ''
 
#//2 
def process_page(layersc,purpose,usr,result_onto_tree_er,onto_basis,relactionate):
 #try:
 id=usr
 if True:
    #===
    #try:
    if True:
       print 'LayersC:',layersc
       try:
        ir=Identify.resume_process_datac(layersc,onto_basis,purpose,id,relactionate) 
       except Exception,errc:
        print 'Error resume_process_datac:',errc
        log.exception("-------------------------")        
       print 'Process->resume_data()',ir
       if ir[0] != None :
        # procura identificador ---
        fnd_ident=False
        for es in ir[0].topicos:
         if ir[0].es_compare_dt(es,'identificador') or ir[0].es_compare_dt(es,'realid') or ir[0].es_compare_dt(es,'realid2'):
          fnd_ident=True
        if not fnd_ident:
         ind=len(result_onto_tree_er)-1
         fond_cs=False
         while ind >=0 and not fond_cs:
          for es2 in result_onto_tree_er[ind].topicos:
           if ir[0].es_compare_dt(es2,'identificador') or ir[0].es_compare_dt(es2,'realid') or ir[0].es_compare_dt(es2,'realid2'):
             ir[0].set_topico_nr(es2)
             fond_cs=True
             break
          ind-=1  
        
        # verificar se nao tem somente identificadores(elemento fact invalido)     
        oth=False         
        print 'RCT TPS:{',ir[0].topicos,'}'
        indtotph=0
        for es in ir[0].topicos:
         indtotph+=1
         print 'RCT TPS('+str(indtotph)+'):{',es.dt,'}'
         if ir[0].es_compare_dt(es,'identificador') or  ir[0].es_compare_dt(es,'realid')or  ir[0].es_compare_dt(es,'realid2') :
          pass
         else:
          oth=True
        print 'OTH:',oth

class  layer_processesC:
  def __init__(self):
    self.lrs=[]
    
   
import SemaIniParser
SemaIniParser.conn=conn
SemaIniParser.conn3=conn3
SemaIniParser.conn4=conn4

mdLayout.conn=conn
mdER.conn=conn
mdER.conn3=conn3
mdER.conn4=conn4

mdNeural.conn=conn
mdNeural.conn3=conn3
mdNeural.conn4=conn4

# global 
layer_processes=layer_processesC ()
   
  
''' 
 obs: filtros/restricoes ou informacoes compl, devem ser lidos dos layer_processes, que contem as informacoes da sentenca passada
'''   
def process_termo(layers,usr,pur_p,onto_basis,relactionate=False):
  #=====================================
  result_onto_tree_er=[] # caracteristicas,descricoes,etc...
  
  print 'Inter -stack executing : '
  for n in onto_basis.nodesER:
   print n.name
  print '======================================='
  print '======================================='
  print '======================================='
  
  
  process_page(layers,pur_p,usr,result_onto_tree_er,onto_basis,relactionate)
  
  #========================================================================================================================================
  print 'ER---Final-Exec:',len(result_onto_tree_er)
  for e in result_onto_tree_er:
    print '----------------------------------------'
    for t in  e.topicos:
     print t.dt
     print '**************************'
     for s in t.sinapses:
      print s.nr.dt
     print '**************************'
    print '----------------------------------------'
    
    
  print '======================================='
  print '======================================='
  print '======================================='
    
  '''
   ->gravar na ontologia semantic_objects2, os qualificadores de definicao,composicao( achar objectos com destinacao(info-composicao), que contem as informacoes de propriedades )
   ->gravar na ontologia semantic_objects2, os qualificadores de estado( achar objectos com destinacao(info-state), que contem as informacoes de estado->links para cada momento das propriedades )
   
   ->gravar na ontologiao links_objetcts os qualificadores definidores de relacao , link ,conexao, etc.. ( achar objectos com destinacao(info-relaction), que contem as informacoes de relacoes )
   
   ->os qualificadores de filtro,foco informados na sentenca do clipping seram utilizados para o retorno no clipping

    1 -setar foco nos objectos
    2 -caracteristicas + links
    3 -layout-out com interesses
    4 -layout-code para extrair informacao
    5 -inserir no clipping return 
  '''
 
      
def  ret_usr_inter(sessao):
   params=[ sessao]
   resultSet =conn.sqlX ("SELECT action_def,cenario from interaction_usr where useranme= ? ",(params))
   rt=[]
   for results in resultSet:
      j=results[1]       
      rt.append([j])      
   return rt
      
      
def get_purposes(usr): # retorna os purposes(triggers) de pesquisas, cada um com suas fontes e propositos
 resultSet =conn.sql ("SELECT DT FROM knowledge_manager where username='"+usr+"' and typ=4  and dt<>'language' order by i ") 
 p=[]
 for results in resultSet:
    purps=results[0]
    p.append(purps)
 return p   



def get_aliases_ob( ):    
  str_ret=[]
  for ir in layer_processes.lrs:
      print 'get_aliases_ob()->ir(1):',ir
      for topico in ir.topicos:
       if len(topico.dt) > 0 :
        topicodt=topico.dt
        if 'identificador' in topicodt or 'realid' in topicodt or 'realid2' in topicodt  or 'object' in topicodt: 
         for p in topico.sinapses:
          for dts1 in p.nr.dt:          
           str_ret.append(dts1)
  return str_ret

def get_aliases_p( rcts_impo ):    
  str_ret=[]
  for ir in rcts_impo :
      #print 'get_aliases_ob()->ir(2):',ir,ir.name
      for topico in ir.topicos:
       if len(topico.dt) > 0 :
        topicodt=topico.dt
        #print topicodt,'<<<'
        if 'purpose' in topicodt or 'destination' in topicodt  : 
         for p in topico.sinapses:
          for dts1 in p.nr.dt:          
           str_ret.append(dts1)
  return str_ret
  
def process_sentences(usr,rcts_impo): 
 #purps=ret_usr_inter(usr)  
 purps=get_aliases_p( rcts_impo )
 print 'Purps:',purps
 for pur_p in purps:
     aliases=get_aliases_ob ()
     layers=[]
     layers2=[]
     layers=get_ontology_s2(aliases,pur_p,usr)
     print 'GetLayers:(',aliases,',',pur_p,')->',(layers)
     '''
     layers2=get_ontology2(aliases,pur_p,usr)
     print 'GetLayers2:(',aliases,',',pur_p,')->',len(layers2)
     '''
     #===============
     #======== load ractionlines baseado no cenario escolhido => parametro de linha de comando purpose
     print 'Collect ractionlines for(1):',pur_p,'-----'
     ractionlines=mdOntology.mdAbstractBaseOntology ()
     ractionlines.nodesER=rcts_impo
     print 'Found:',len(ractionlines.nodesER),'-> Ready to start inference-engine:'
     #===============
     print 'OBJS:',aliases,' Result:',layers
     if len(layers)>0:
      print 'Start process of rct:-------------------------'
      # doc
      print 'Process layers:',len(layers)
      for doc in layers:
       #sente
       print 'Process doc:',len(doc)
       for sentece in doc:
         #lines
         print 'Process Sentence:',len(sentece)
         ids=0
         try:
          for s in sentece:
           ids+=1
           #print s.name,'---',ids
          print 'AK-sentence:[',sentece,']' 
          process_termo(sentece,usr,pur_p,ractionlines)
         except Exception,ess1:
          print 'Error process termo:',ess1
          log.exception( '===========================' )
     #===============
     '''
     print 'OBJS Rels:',aliases,' Result:',layers2
     if len(layers2)>0:
      print 'Start process of rct:-------------------------'
      # doc
      for doc in layers2:
       #sente
       for sentece in doc:
         #lines
         process_termo(sentece,usr,pur_p,ractionlines,True)  
     '''
     
def process_sentences2(usr,rcts_impo,layers_param): 
 #purps=ret_usr_inter(usr)  
 purps=get_aliases_p( rcts_impo )
 print 'Purps:',purps
 for pur_p in purps:
     aliases=get_aliases_ob ()
     layers=[]
     layers2=[]
     #======== load ractionlines baseado no cenario escolhido => parametro de linha de comando purpose
     print 'Collect ractionlines for(1):',pur_p,'-----'
     ractionlines=mdOntology.mdAbstractBaseOntology ()
     ractionlines.nodesER=rcts_impo
     print 'Found:',len(ractionlines.nodesER),'-> Ready to start inference-engine:'
     #===============
     print 'OBJS:',aliases,' Result:',layers
     if True :
         try:          
          process_termo(layers_param,usr,pur_p,ractionlines)
         except Exception,ess1:
          log.exception( '===========================' )
          print 'Error process termo:',ess1
 

class ProcessPgStack:
 def __init_(self):
  pass
 def call_process(self,usr,rcts_impo):
  process_sentences(usr,rcts_impo)
 def call_process2(self,usr,rcts_impo,layers_param=[]):
  process_sentences2(usr,rcts_impo,layers_param)
  
mdNeural.GlobalStack.proc_pg=ProcessPgStack ()  
  
def process_pagest(layersc,purpose,usr,result_onto_tree_er,onto_basis,relactionate):
 #try:
 id=usr
 if True:
    #===
    #try:
    if True:
       print 'LayersC-1:',layersc
       ir=Identify.resume_process_datac(layersc,onto_basis,purpose,id,relactionate) 
       print 'LayersC-2:',layersc
       print 'Process->resume_data()',ir
       if ir[0] != None :
        # procura identificador ---
        fnd_ident=False
        for es in ir[0].topicos:
         if ir[0].es_compare_dt(es,'identificador') or ir[0].es_compare_dt(es,'realid') or ir[0].es_compare_dt(es,'realid2'):
          fnd_ident=True
        if not fnd_ident:
         ind=len(result_onto_tree_er)-1
         fond_cs=False
         while ind >=0 and not fond_cs:
          for es2 in result_onto_tree_er[ind].topicos:
           if ir[0].es_compare_dt(es2,'identificador') or ir[0].es_compare_dt(es2,'realid') or ir[0].es_compare_dt(es2,'realid2'):
             ir[0].set_topico_nr(es2)
             fond_cs=True
             break
          ind-=1  
        
        # verificar se nao tem somente identificadores(elemento fact invalido)     
        oth=False         
        print 'RCT TPS:{',ir[0].topicos,'}'
        indtotph=0
        for es in ir[0].topicos:
         indtotph+=1
         print 'RCT TPS('+str(indtotph)+'):{',es.dt,'}'
         if ir[0].es_compare_dt(es,'identificador') or  ir[0].es_compare_dt(es,'realid')or  ir[0].es_compare_dt(es,'realid2') :
          pass
         else:
          oth=True
        print 'OTH:',oth  
  
  

         
         
def process_termost(layers,usr,pur_p,onto_basis,relactionate=False):
  #=====================================
  result_onto_tree_er=[] # caracteristicas,descricoes,etc...  
  process_pagest(layers,pur_p,usr,result_onto_tree_er,onto_basis,relactionate)  
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
  
def process_sentences_ST1(usr,layers,pur_p):
     print 'Collect ractionlines for(2):',pur_p,'-----'
     ractionlines=mdOntology.mdBaseOntology(usr,pur_p)
     print 'Found:',len(ractionlines.nodesER)
     process_termost(layers,usr,pur_p,ractionlines)
         
 
def  ret_usr(sessao):
   params=[ sessao]
   resultSet = conn.sqlX ("SELECT USERNAME from usuarios where SESSAO= ? ",(params))
   print resultSet
   for results in resultSet:
      i=results[0]       
      return i
 
 
def Gentry(logid,action_def,purp):
 sentence=''
 usr=''
 sessao=''
 tmp=''
 try:
     fnds=False
     purpose=''
     #=============
     #=============
     usr=logid
     start_c=0
     sentence=action_def
     purpose=purp
     if True:
      #print usr,purpose,sentence
      print 'SemaIniParser:',sentence,'|',usr,'|',purpose
      layer_proc=SemaIniParser.entry(sentence,usr,purpose)
      layer_processes.lrs=layer_proc[0]
      process_sentences_ST1(usr,layer_processes.lrs,purpose)
      
 except: 
  log.exception( 'Error process sentences:' )
 return usr 
 
 
def entry(args):
 usuario='' 
 ext=''
 
 try:
 
  start_c=0
  usr=0
  usr=args[0]
  sentence=args[1]
  purp=args[2]
  tp_n=args[3] # type of neural objects
  termo=args[4] # type of neural objects
  mdNeural.kstermo=[termo,False]
   
  #print 'Cmd line :',usr  
  mdNeural.self_usr=usr
  mdNeural.type_coll=tp_n
  usuario=Gentry(usr,sentence,purp)
  conn.commit ()
 except Exception,err:
  log.exception( 'Error process sentences:' )
  ext='Error process sentences:'+err.__str__()
   
  
 return '{[RUN_OK]}'+ext
 


 
 
 