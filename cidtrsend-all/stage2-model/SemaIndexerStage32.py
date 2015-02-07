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



pool2 = None

import mdTb

import get_object

import get_object2

 



import mdLayout
import mdER
import mdNeural
import Identify 


import logging
import mdOntology


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('SemanticIndexer-Stage2')


# obs : extrair informacoes -> preview de informacoes->pagina para exibir o resultado (href), titulo ou foco principal como result, classificacao como categoria --> para busca web realtime(busca na ontologia semanti_objects2 ,nao clipping

 
   
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
      for topico in ir.topicos:
       if len(topico.dt) > 0 :
        topicodt=topico.dt
        if 'identificador' in topicodt or 'realid' in topicodt or 'realid2' in topicodt  or 'object' in topicodt: 
         tmpcs=''          
         for p in topico.sinapses:
          for dts1 in p.nr.dt:          
           tmpcs+=' '+dts1
         str_ret.append(umisc.trim(tmpcs) )
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
  
def process_sentences(usr,rcts_impo,no_cache): 
 no_cache=True
 purps=get_aliases_p( rcts_impo )
 print 'Purps:',purps
 print 'NO_cache:',no_cache
 if no_cache:
  for pur_p in purps:
     print 'Collect ractionlines for(1):',pur_p,'-----'
     ractionlines=mdOntology.mdAbstractBaseOntology ()
     ractionlines.nodesER=rcts_impo
     print 'Found:',len(ractionlines.nodesER),'-> Ready to start inference-engine:'
     #===============
     process_termo(rcts_impo,usr,pur_p,ractionlines)
                       
     
def process_sentences2(usr,rcts_impo,layers_param):   
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
 def call_process(self,usr,rcts_impo,no_cache=True):
  process_sentences(usr,rcts_impo,no_cache)
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
  
  
import socket 
            

ID='1'

mdLayout.dump_all_state=False
mdLayout.dump_all_state2=False
mdLayout.dump_all_state3=False
mdLayout.dump_all_state4=False
mdLayout.dump_all_state5=False


import time
sock=None


def ping_socket(a1,a2):# ping to the server
  while True:
    try:
     print 'start ping....'
     host1 = '79.143.185.3'
     port1 = 91 
     sock1 = socket.socket()          
     sock1.connect((host1, port1))
     sock1.send('pingZ4')
     r=sock1.recv(10)
     time.sleep(10)
     sock1.close()
     print 'end ping...'
    except : 
     log.exception("-----ping-----")
     pass     
    time.sleep(20)
   
  
thread.start_new_thread(ping_socket,(0,0) ) 

def _init_cols():
 global sock
 global pool2
 print 'Start.process.queue....'
 sock = socket.socket()          
 host = '79.143.185.3'
 port = 61 
 pur_p=''
 #
 sentence=''
 #
 usr='igor.moraes'
 def start_socket():
  global sock
  global pool2
  while True:
   try:
    pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000000000)
    mdTb.start_db(pool2)
    get_object.start_db(pool2)
    get_object2.start_db(pool2)
    Identify.start_db(pool2)   
   except Exception,e:
    print 'Not connected(cassandra)....',e
    time.sleep(5)
    continue    
   break 
  while True:
   try:
    sock = socket.socket()          
    sock.connect((host, port))
   except Exception,e:
    print 'Not connected....',e
    time.sleep(5)
    continue    
   sock.settimeout(None)
   sock.send(ID)
   pur_p2=sock.recv(1024)
   print 'receive-purpose:',pur_p2
   return pur_p2
 #
 pur_p=start_socket()
 ractionlinesG=mdOntology.mdBaseOntology(usr,pur_p)
 mdNeural.self_usr=usr
 mdNeural.type_coll='1'
 SemaIniParser.start_module(usr,pur_p)
 #==========================================================
 #==========================================================
 #==========================================================
 #==========================================================
 conts=0
 while True:
  # receive sentences an process them
  print 'Wait for sentences....'
  try:
   sentence=sock.recv(1024)
   print 'Start process new sentence..',sentence
   #===========
   if sentence == '$$refresh$$': # atualizar o cache de codigos executaveis
       import atualiza_exec_code as exec1
       exec1.atualiza_code()
       sock.send('$$OK$$')
   #=======================================
   if sentence == '$$test$$': 
    sock.send('$$test$$')  
    continue
  except: 
   print 'Start process new sentence..'
   start_socket()   
   time.sleep(2)   
   continue
  if type(sentence) != type('') and type(sentence) != type(""): sentence=str(sentence) 
  if umisc.trim(sentence) == '' :
    if conts > 5:
     start_socket()     
    time.sleep(1) 
    conts+=1
    continue
  conts=0
  layer_proc=SemaIniParser.entry(sentence,usr,pur_p)
  layer_processes.lrs=layer_proc[0] 
  layers=layer_processes.lrs
  #
  mdNeural.kstermo=[sentence,False]
  #
  process_termost(layers,usr,pur_p,ractionlinesG)
  #
  #return 
  kds=mdNeural.GlobalStack.tmp
  rt=''
  for k in kds:
    rt+=' '+k
  rt=umisc.trim(rt)  
  sock.send(rt)
  # end
  
_init_cols()

 
 


 
 
 