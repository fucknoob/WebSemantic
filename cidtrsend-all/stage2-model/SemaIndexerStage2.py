#coding: latin-1

''' inicializa o ambiente para captura de informacoes do clipping  '''
''' ractionline p auto-ask(classify,relactionate,composition) ->auto-ask para classificar,relacionar,build objectos dentro dos purposes(ambientes) , as quais sao passadas por linha de comando, roda automaticamente '''

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


import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily



pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

import mdTb
mdTb.start_db(pool2)

import get_object
get_object.start_db(pool2)

import get_object2
get_object2.start_db(pool2)

import mdLayout
import mdER
import mdNeural
import Identify 

import logging
import mdOntology


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('SemanticIndexer-Stage2')


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping

'''
import conn

conn= conn.conn_mx

connTrace=conn
conn4=conn
conn5=conn
conn3=conn
'''

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
 
tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 
tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3') 
tb_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3') 

mdNeural.tb_object=tb_object
mdNeural.tb_object_dt=tb_object_dt
mdNeural.tb_relaction=tb_relaction





def get_object_by_data(obj,usr,uid):
 #======== 
 if uid != '':
  resultSet=tb_object.get(uid)     
  key1=uid
 else:
   resultSet=tb_object.get(obj)  
   key1=uid
 #
 #
 obj_nm=None
 uid=None
 cenar=0
 cnts_all_tps=0
 if True:
      results = resultSet
      obj_nm=results[u'objeto'] 
      uid=key1
      cenar=results[u'cenar'] 
      cnts_all_tps=results[u'conts_n'] 
 #-----------
 lay=mdNeural.mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 tpc2=lay.set_topico('identificador')
 tpc2.uuid=cenar
 nrc2= lay.set_nr(lay.name)
 nrc2.uuid=cenar
 tpc2.connect_to(lay,nrc2,'Composicao') 
 #print lay.topicos,'....................'
 print 'Read object(g1):',obj,' uid:',uid
 #-----------
 def cached_dt(objectkey,cnts_all_tp):
   '''
   cached=[]
   keyc=objectkey 
   i=1
   while i <= cnts_all_tp:
     try:
      c1=tb_object_dt.get(keyc+"|"+str(i))
      cached.append([keyc+"|"+str(i),c1])
     except: break 
     i+=1
        
   '''
   
   
   cached=[]
   keyc=objectkey 
   i=1
   keys=[]
   while i <= int(cnts_all_tp):
    keys.append( keyc+"|"+str(i) )
    i+=1
   i=0 
   if True: 
     try:
      c1=tb_object_dt.multiget(keys,column_count=10000)
      for kd in c1.items():
        cached.append([kd[0],kd[1]])
        i+=1
     except Exception,e: 
       print 'ERROR:',e       
       pass
       
   return cached  
 if True :
     class iter_cd:
       def dump(self):
         fil=open("c:\\python24\\kk.txt","w")          
         for ky,s in self.arr:
          s1=str(s)
          fil.write(s1+'\n')
         fil.close() 
       def __init__(self,arr1):
         self.arr=arr1
         self.start=-1
       def get_level(self,level2):
         rt=[]
         arr=self.arr
         for ky,cols in arr:
          for level in level2:
           if int(cols[u'LEV']) == level:
             rt.append([ky,cols])
         rt2=iter_cd(rt)
         return rt2
       def get_all(self):
         rt=[]
         while True:
           s=self.next()
           if s[0] == None: break
           rt.append(s)
         return rt  
       def next(self):
         if self.start == -1:
          self.start=0
         else:
          self.start+=1
         if self.start < len(self.arr): 
           return self.arr[self.start] 
         else:
           return [None,None]  
     rows=cached_dt(uid,cnts_all_tps) 
     iterat=iter_cd(rows)
     #iterat.dump()
     def read_dt_level( nr_top,level,uid1,ic1,lay1,results,resultSet,uuid):
             while results  :
                  DT=results[u"datach"] 
                  TOP=results[u'topico']
                  ic1=uuid
                  lev=results[u'LEV']
                  #print 'READ(g2).top-init:',TOP,DT,'->',lev , level
                  if int(lev) != level: 
                   return results
                   break
                  nrc= lay1.set_nr(DT)
                  nrc.uuid=uuid
                  #print 'READ(g2).top:',TOP,DT
                  #==
                  nr_top.connect_to(lay1,nrc,'Composicao') 
                  ky,results = resultSet.next()
                  read_dt_level(nrc,(level+1),uid1,ic1,lay1,results,resultSet,uuid)
             return results     
     #==================== 
     
     # 
     resultSet =iterat.get_level([0,1]).get_all()
     obj_nm=None     
     for ky,results in resultSet:
          DT=results[u"datach"] 
          TOP=results[u'topico']
          cnti=int(results[u'cnt'])
          ic=ky
          uuid=ky
          nr= lay.set_nr(DT)
          nr.uuid=cenar
          if ic == None: ic=0
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          # ---
          tps=lay.set_topico(TOP)
          tps.uuid=cenar
          #===
          #print 'Set topico:',TOP,' for layer:',obj_nm,' uid:',uid,'tps.uid:',tps.uuid
          # ---
          
          tps.connect_to(lay,nr,'Composicao') 
          if True:
             #==     
             # 
             levs=range(0,50)             
             resultSet1=iterat.get_level(levs)             
             #sess=conn3.prepare(sql1)
             #resultSet = sess.execute ()
             ky,results = resultSet1.next()
             while results  :
                  DT=results[u"datach"] 
                  TOP=results[u'topico']
                  ic2=ky
                  lev=results[u'LEV']
                  uuid=ky
                  if int(results[u'cnt']) <= cnti:
                    ky,results = resultSet1.next()
                    continue
                  #print 'Level 2(ind):',lev,TOP,DT
                  if int(lev) != 2:
                    break
                  #==
                  #print 'Level 2(dt) :',nrc.dt
                  nrc= lay.set_nr(DT)
                  nrc.uuid=cenar
                  nr.connect_to(lay,nrc,'Composicao') 
                  ky,results = resultSet1.next()
                  results = read_dt_level( nrc,3,uid,ic2,lay,results,resultSet1,cenar ) ##### 
                  #lay.dump_layer_file()
                  
 #print 'collected.layer.dump():============================================='
 #lay.dump_layer_file()
 return lay   

 
 
     
def get_ontology(aliases,purposes,usr): 
 tree_h=[]
 for alias in aliases:
  if True:
   tree_cen=[]
   if True:
     ''' '''
     if alias == '$$all$$': alias=''
     #alias='%'+alias+'%'
     #alias=alias+'%'
     ''' '''
     h_tree_v=[]
     #      
     resultSet=None
     try:
      resultSet=tb_object.get(alias)
     except: pass 
     ky=alias
     if resultSet:
        results = resultSet
        i=results[u'objeto'] 
        uid=ky
        cenar=results[u'cenar']
        #===
        print 'read-Obj-onto:[',alias,'] ',i, '->collects:',uid
        #====
        avaliable_objs=[]
        #===--------------------------------------
        obj_principal=get_object_by_data(i,usr,uid)
        #if len(obj_principal.topicos) > 0 :
        h_tree_v.append(obj_principal)
        #==----------------------------------------
        #break
     if len(h_tree_v) > 0 :
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

 
  
 
#//2 
def process_page(layersc,purpose,usr,result_onto_tree_er,onto_basis,relactionate):
 #try:
 id=usr
 if True:
    #===
    #try:
    if True:
       #print 'LayersC:',layersc
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
 
 

def get_aliases_ob( ):    
  str_ret=[]
  for ir in layer_processes.lrs:
      print 'get_aliases_ob()->ir(1):',ir
      #if ir != None: print 'lr:',ir.name
      for topico in ir.topicos:
       if len(topico.dt) > 0 :
        topicodt=topico.dt
        if 'identificador' in topicodt or 'realid' in topicodt or 'realid2' in topicodt  or 'object' in topicodt: 
         dtk=''
         for p in topico.sinapses:
          for dts1 in p.nr.dt:                
           dtk+=' '+umisc.trim(dts1)
         if umisc.trim(dtk) != '': 
           print 'Collect.element:',dtk
           str_ret.append(umisc.trim(dtk) )
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
 #   
 purps=get_aliases_p( rcts_impo )
 print 'Purps:',purps
 for pur_p in purps:
     aliases=get_aliases_ob ()
     layers=[]
     layers2=[]
     layers=get_ontology(aliases,pur_p,usr)
     nms=[]
     for dks in layers:
      for dk1 in dks:
       for dk in dk1:
        nms.append(dk.name)
     print 'GetLayers:(',aliases,',',pur_p,')->',(layers),'{',nms,'}'

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
     else: 
       process_termo([],usr,pur_p,ractionlines)      
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
 #  
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
      sentence=sentence.replace('*','%')
      print 'SemaIniParser:',sentence,'|',usr,'|',purpose
      layer_proc=SemaIniParser.entry(sentence,usr,purpose)
      layer_processes.lrs=layer_proc[0]
      process_sentences_ST1(usr,layer_processes.lrs,purpose)
      
 except: 
  log.exception( 'Error process sentences:' )
 return usr 
 
import time
startTT = time.clock ()

usuario='' 
try:
 
 mdLayout.dump_all_state=False
 mdLayout.dump_all_state2=False
 mdLayout.dump_all_state3=False
 mdLayout.dump_all_state4=False
 mdLayout.dump_all_state5=False
  
   
 start_c=0
 usr=0
 usr=sys.argv[1]
 #print usr
 sentence=sys.argv[2]
 #print sentence
 purp=sys.argv[3]
 #print purp
 tp_n=sys.argv[4] # type of neural objects
   
 #print 'Cmd line :',usr  
 mdNeural.self_usr=usr
 mdNeural.type_coll=tp_n
 
 if sentence.find('.') <=-1 and sentence.find('!') <=-1 and sentence.find('?') <=-1 and sentence.find(';') <=-1:
   sentence=sentence+'.'
    
     
 #print 'sentence:',sentence  
 usuario=Gentry(usr,sentence,purp)
 
 

except Exception,err:
 log.exception( 'Error process sentences:' )


 

print 'End process.Time elapsed: ',time.clock () - startTT


 
 
 