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

'''
import conn

conn= conn.conn_mx
'''

sys.path.append('./pymongo')
sys.path.append('./pycassa')

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily



pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

import mdTb
mdTb.start_db(pool2)

tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 
tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3') 
tb_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3') 

import conn_mongo

w_cache3 = conn_mongo.get_tb()


entry_doc =[]

fs_teste=True
tw_server=False # se indexa por outra servidor, abrir conn2


'''
fs_teste=False
tw_server=True # se indexa por outra servidor, abrir conn2
'''



re_post=True


just_one_index=True

RemoteL=False

if RemoteL:

        import sys
        sys.path.append('/Neural/Pyro')
        import Pyro.core

        Pyro.core.initClient()
        objectName = 'layoutBean'
        hostname = '91.205.172.85'
        port = '26'
        print 'Creating proxy for object',objectName,' on ',hostname+':'+port
        if port:
            URI='PYROLOC://'+hostname+':'+port+'/'+objectName
        else:	
            URI='PYROLOC://'+hostname+'/'+objectName
        print 'The URI is',URI
        proxy=Pyro.core.getProxyForURI(URI)



class Task_C:
 def __init__(self,Dt1=None,Dt2=None):
   self.dt1=Dt1
   self.dt2=Dt2

 
#create  table know_pages( i integer not null default serial, pg long, username varchar(20) , primary key (i)  ) 
def get_db_pages(usr2,pg_ex,connc):
  
  def fecha_pagina(uid):
    print 'Close MSG:',uid
    s=w_cache3.find({'doc_id':uid})
    s[u'PROCESSED']='S'
    w_cache3.update({'_id':s['_id']},s)
 
  
  def remote_f():
        print 'Getting remote-pages...'
        return  proxy.get_pages('',usr2)
  
  if RemoteL:
    return remote_f()
  
  print 'PG_EX',pg_ex,len(pg_ex)  
  
  pgs_exs= pg_ex.split(',')
 
  #resultSet = connc.sql ("select pg,i,title from web_cache3 where USR='"+usr2+"' and i in( "+pg_ex+" ) order by i") 
   
  resultSet=[]   
  for p1 in pgs_exs:
        rg=None
        for d in w_cache3.find({'doc_id':p1}):
         rg=d
        if rg != None: 
         try:
          rtc=str(rg[u'pg'])
          rtc2=str(rg[u'title'])        
          resultSet.append( [ rtc1.encode('latin-1'),p1,rtc2.encode('latin-1') ] )
         except:
          print 'Error.get.pg:',rg
          log.exception("")
          try:
           resultSet.append( [ rg[u'PG'].encode('latin-1'),p1,rg[u'TITLE'].encode('latin-1') ] )
          except:
           print 'Error.get.pg(2):',rg
           log.exception("")
  
          
  typ=[]
  print 'Collect pg:',pg_ex
  #===============================================  
  #typ.append(['O perfil da empresa no Twitter foi criado em 20 de Fevereiro de 2008.',35835 ])
  #return typ
  #================================================
  for [ts,ids,ids2] in resultSet:
    if ids2 == None: ids2= ''
    if umisc.trim(ids2) != '':
            ts=(ids2+': '+ts)
    #if umisc.trim(ts) != '' and umisc.trim(ts) != '\n' and umisc.trim(ts) != '\r':
    typ.append([ts,ids])    
    if re_post and not fs_teste:
     fecha_pagina(ids)
    print 'Read page',ids #,ts
  print 'Reuse pgs:',len(typ)
  return  typ 
 
def post_db_page(usr2,pg): 
  sql1="insert into know_pages(pg,username) values(?,?)"
  try:
   conn.sqlX (sql1,([pg,usr2]))
  except Exception,err: print 'Erro ao post(know-pages):',err

 
def load_pages_know(usr,pgex) :
 connd=None
 #if tw_server:
 #   import conn3
 #   connd=conn3.conn_mx
 rts=get_db_pages(usr,pgex,connd) 
 if len(rts) > 0:
  print 'Db-Pages:',len(rts)
  cnt=0
  for r2 in rts:
     [r,ids]=r2
     cnt+=1
     entry_doc.append([ Task_C(ids,r),cnt   ]  )  
 
     
           
           
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





mtx=mutex.mutex ()
mtx2=mutex.mutex ()





   
def  Identify_pre_process_data (l2,ln_o,onto_basis,purpose,id,t_h,ret_ps):   
 Identify.pre_process_data(l2,ln_o,onto_basis,purpose,id,t_h,ret_ps)   
   

#===================

def get_typ(obj,usr2):
  # 
  typ=0
  #=======================
  resultSet=mdTb.tb_py.get(obj)
  typ=int(resultSet[u'TYP'])
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
 

class icnt:
   def __init__(self,vl):
      self.valor=vl
   def inc(self):
      self.valor+=1
   def value(self):
      return self.valor     


# efetua o post de um layer {1}

def post_object_by_data3p(layer,cenario,usr,termo,foco,posted_objs,senti,l_p_ant): 
 if layer.name == '' : layer.name ='undef'
 def get_top_level(obj,foc,usr,termo_s):
   rts=[]
   cl1 = index.create_index_expression(column_name='OBJECT', value=obj)
   cl2 = index.create_index_expression(column_name='TOPICO', value=foc)
   cl3 = index.create_index_expression(column_name='USERNAME', value=usr)
   cl4 = index.create_index_expression(column_name='UID', value=termo_s)
   clausec = index.create_index_clause([cl1,cl2,cl3,cl4],count=1000000)
   rest=tb_object_dt.get_indexed_slices(clausec)
   # 
   #for results in resultSet:
   for kl,cols in rest:   
      i=cols[u'lev'] 
      id_top=cols[u'id_top'] 
      rts.append([i,id_top])
   return rts
 #=======================  
 nameo=layer.name
 print 'Post layer:',nameo
 if umisc.trim(nameo) == '' or umisc.trim(nameo) == '\n' :
  if l_p_ant != None:
    nameo=l_p_ant.name
  if umisc.trim(nameo) == '' or umisc.trim(nameo) == '\n' :  
   return
 
 fnd_tops=False
 
 l_p_ant=layer
 geral_uuid=cenario
 print 'POST:LR:',nameo
 print '++------------------------------------------'
 for s in layer.topicos:
  print 'DT:',s.dt
  fnd_tops=True
  for d in s.sinapses:
   print d.nr.dt
 print '++------------------------------------------'
 
 if not fnd_tops: return
 ky1=nameo+' '+str(cenario) 
 nameo=ky1 
 print 'Post-obj:[',nameo,']'
 no_post_o=False
 for [s,st] in posted_objs:
  if s == nameo and st==senti :
     no_post_o=True
 posted_objs.append([nameo,senti])
 #========== 
 #if not no_post_o and len(layer.topicos)>0:
 def post_alldt(arr):
   #=======================
   b = tb_object_dt.batch(queue_size=len(arr))   
   for k,cols in arr:
    b.insert(str(k),cols) 
   b.send()
 #
 def post_nr(uid,cnt,arr1,usr,tp,level=1,id_top=1,just_sin=False):   
   try:
       if not just_sin:
        tp_Dt=''
        try:
         for d in tp.dt:
           if type(d) == type([] ):
            tp_Dt+=d[0]
           else: 
            tp_Dt+=d
        except Exception,e:
          print 'Err:-nr.post(2):',tp.dt,'->',e
        tp_name=tp_Dt
        if len(tp.sinapses)==0:
         ##UID,topico,LEV,sin,dt,id_top,username 
         kyl1=uid+'|'+str(cnt.value())
         it={"UID":uid,"topico":tp_Dt,"LEV":"1","sin":'',"datach":'',"id_top":str(id_top),"username":usr,"cnt":str(cnt.value())}
         arr1.append( [ kyl1,it ] )
         cnt.inc()
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
        #sql1="insert into SEMANTIC_OBJECT_DT3(UID,dt,topico,LEV,sin,id_top,username) values(?,?,?,?,?,?,?)"
        if umisc.trim(sn.opcode) == '': sn.opcode='Relaction-oper-opcode'
        #====================================================
        #====================================================
        kyl1=uid+'|'+str(cnt.value())
        it={"UID":uid,"topico":tp_Dt,"LEV":str(level),"sin":sn.opcode,"datach":sn_dt,"id_top":str(id_top),"username":usr,"cnt":str(cnt.value())}
        arr1.append( [ kyl1,it ] )
        cnt.inc()
        #====================================================
        #==========
        post_nr(uid,cnt,arr1,usr,sn.nr,level+1,id_top,True)
   except Exception,e:
    #print 'Error post nr.' ,  e
    log.exception('[Error post nr...]')
 #==========    ===============================================
 print 'Post.Topicos{}:' 
 #==========    ===============================================
 indi=icnt(1) 
 arr_post=[]
 for tp in layer.topicos:
  #==========    ===============================================
  print 'Post.nr.num:',indi.value()
  #
  post_nr(ky1,indi,arr_post,usr,tp) 
 #=============
 print 'Insert-OBJ:'
 #==
 if not no_post_o :
  #sql1="insert into SEMANTIC_OBJECT3(username,objeto,cenar,senti) values(?,?,?,?)"
  try:   
   cols={"username":usr,"objeto":ky1,"cenar":str(cenario),"sento":str(senti),"conts_n":str(len(arr_post))}
   tb_object.insert(ky1,cols)       
   #conn.sqlX (sql1,([usr,nameo,cenario,senti]))
  except Exception,err: print 'Erro ao post(OBJECT):',err
 else: print 'Skip:',nameo,senti
 #=============
 uid=ky1
 #= 
 print 'Post-NRS:'
 #===============================================
 post_alldt(arr_post)
 print 'Post.LINKS{}:'
 for lnk in layer.links:
  #sqlc='insert into  SEMANTIC_RELACTIONS3(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D,UID) values(?,?,?,?,?,?,?)'   
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
   rky=ky1+' '+lnk.lr.name+' '+str(cenario)
   colsr={"OBJ_ORIG":ky1,"OBJ_DEST":lnk.lr.name+' '+str(cenario),"OPCODE":lnk.opcode,"USERNAME":usr,"FOCO":foco_o,"FOCO_D":foco_d,"UID":uid};
   #conn.sqlX (sqlc,([ky1,lnk.lr.name+' '+str(cenario),lnk.opcode,usr,foco_o,foco_d,uid]))
   tb_relaction.insert(rky,colsr);       
  except Exception,err: print 'Erro post links:',err
  #===============
  #layer,cenario,usr,termo,foco
  post_object_by_data3p(lnk.lr,cenario,usr,termo,foco,posted_objs,senti,l_p_ant) 
 #=============== 
 #conn.commit()
 
def post_datah_state(state_type,obj,composicao,rels,usr):
 for sti in state_type:
  for compo in composicao:
   sql='insert into SEMANTIC_INFOSTATE( USERNAME,OBJECT,TOPICO,INDI_STATE ) VALUES(?,?,?,?)'
   conn.sqlX (sql,([usr,obj,compo,sti]))
  #== 
  for rels in composicao:
   sql='insert into SEMANTIC_INFOSTATE( USERNAME,OBJECT,TOPICO,INDI_STATE ) VALUES(?,?,?,?)'
   conn.sqlX (sql,([usr,obj,compo,sti]))
 
 
 
  
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

 
def run_layout_parser(lay_names,dts,usr,extdt):
 #====================================================================================================
 #chamar os codigos 
 codes_Result=[]
 for dt in lay_names:
  print 'Layout-Code',dt
  #=========================
  try:  
   resultSet=mdTb.tb_py_code.get(dt)
  except: 
   resultSet=[] 
  # 
  if True:
    results = resultSet
    typ=get_typ(dt,usr)
    o=clean_s(results[u'CODE'])
    code=(o)

    print 'Code type:',typ
    if typ == 1: #executavel
     code+=' \n\nretorno_srt=run(sr_int_cmd_param,ex_Data)'
    else: # executa somente o codigo
     pass
    #================================== 
    try:
     sr_int_cmd_param=dts
     ex_Data=extdt
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
post_parsers=[]
 

def get_parsers(usr,purpos):
 prs=[] 
 # 
 tb_kn = pycassa.ColumnFamily(pool2, 'knowledge_manager')
 resultSet = tb_kn.get_range()
 for ky,results in resultSet:
  if results[u'USERNAME'] == usr and results[u'typ'] == '2' and results[u'DEST'] == 'postLayout' and results[u'layout_onto'] == purpos:
         prs.append( results[u'DT'] )
 return prs

#=================================================  



def post_object_by_data3(layer,cenario,usr,termo,foco,purpos,senti,l_p_ant,extdt):
 print 'LayoutOnto->Purpose:',purpos
 objects=[]
 global post_parsers
 if len(post_parsers) == 0:
     post_parsers=get_parsers(usr,purpos)     
 gc.collect ()
 # call run_layout_parser
 print 'Prepare post lay:' ,layer.name
 objects=run_layout_parser(post_parsers,layer,usr,extdt)
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
 
 

class thread_cntl:
 def __init__(self):
  self.finished=False

 
  
def get_pages(usr,start_c):
 pages=[]
 if len(entry_doc) > 0 :  
  return entry_doc
 
 
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
   extdt=[]
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
        post_object_by_data3(lay,uid_DS,usr,termo,[],purpose,indc2,l_p_ant,extdt)  
      except Exception,errc:
        sw= 'Error on post object:'
        log.exception(sw)         
      

      

#                 termo,username,pur_p,start_c,sys_argv,layouts_f ,layouts_f2                   
def process_termo(termo,usr,purp,start_c,path_j,layouts_fz,just_runned):
  pages=[]
  ths2=[]
  #========================================================================================================================================
  job_index=1
  pages=get_pages(usr,start_c)
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
  pg_index=start_c
  d1=1
  
  try:
      total_pages=len(pages)
      print 'Len to pgs:',total_pages,',Termo:',termo
       
      idx1=-1
      idx2=0
      for [pagina,uid_S] in pages:
       idx1+=1
       #if pg_index < idx1: continue
       idx2+=1
       #if idx2 > 10 : continue       
       #==
       if pagina.dt1 == None:
        print 'Page:',pg_index,' is null'
        pg_index+=1 
        continue
       all_p=[]
       endereco=pagina.dt1
       lines_doc=pagina.dt2
       uid_S=endereco
       #if not just_runned:
       # clear_termo(usr,uid_S )
       all_p.append([endereco,lines_doc])
       cnt_process+=1
       d1+=1
       cind2+=1
       if True:
        print 'Process page num(S):',pg_index,' len.doc:',len(lines_doc) ,'id:',uid_S
        process_page(all_p,usr,purp,cind2,None,cind2,pg_index,all_size_pg,job_index,addresses,result_onto_tree_er,layouts_fz,usr,termo,uid_S)
        #================
        print 'End page:',pg_index,' of total:',len(pages)
        #================
        
        
        
       pg_index+=1
      just_runned=True 
  except Exception,e:
       log.exception('Error Processing pages:') 
   
 
def get_layouts(usr,purpose): 
 import mdER3

 p =mdER3.get_LayoutsFZ(usr,purpose)
 return p   


def get_layouts2(usr,purpose): 
 import mdER3


 p=mdER3.get_LayoutsFZ2(usr,purpose)
 return p  
 

class th_i:
 def __init__(self):
  self.end=False 
 
 
def process_sentences(start_c,usr,purps):   
 r1=[]
 just_r=False
 if True:
    username=usr
    termo='SYSTEM'
    trigger_as=''
    r1.append([username,termo,trigger_as])
 to_run_c=[]
 print 'Process load layout...'
 for r in r1:
    [username,termo,trigger_as]=r 
    #===
    print 'Process termo:',termo
    
    
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
    print 'Start process page:---'    
    process_termo(termo,username,pur_p,start_c,'',all_layouts,just_r )
    #=========================
    if len(entry_doc) > 0 : return
  
  
start_c=0

import time
startTT = time.clock ()



def remp(s):
 r=''
 i=len(s)-1
 pos=0
 while i >= 0 :
  if s[i] == '\\' or s[i] == '/': 
   pos=i
   break
  r=s[i]+r
  i-=1
 return s[:pos+1]
     
def parse(s):
 r=''
 for d in s:
  kc=ord(d)
  if ( kc >= ord('a') and kc <= ord('z') ) or (kc >= ord('A') and kc <= ord('Z') )   or (kc >= ord('0') and kc <= ord('9') ) or d in ['.',',','!','?','\'','~','-']:
    r+=d
 return r  
  
 
def run_th(user,start_c,pth,th):   
    try:
     cmd='python '+pth+'SemaIndexerStage1.py '+ '"' + user +'\" '+ str(start_c)
     #print 'Exec.cmd:',cmd
     os.system(cmd)
    except: pass 
    print 'Process',start_c,' finished'
    th.finished=True  
    
    
debug_all=False    

argcnt1= len(sys.argv)

try:
 purps=[]
 usr=0
 pg_ex=''
 usr=parse(sys.argv[1])
 
 cpurps=parse(sys.argv[2])
 
 if len(sys.argv) > 3:
     pg_ex=(sys.argv[3])  
     if pg_ex == '-': pg_ex=''
 
 if argcnt1 > 4:
     debug_all=True
     mdLayout.dump_all_state=True
     mdLayout.dump_all_state2=True
     mdLayout.dump_all_state3=True
     mdLayout.dump_all_state4=True
     mdLayout.dump_all_state5=True
 else:    
     debug_all=True
     mdLayout.dump_all_state=False
     mdLayout.dump_all_state2=False
     mdLayout.dump_all_state3=False
     mdLayout.dump_all_state4=False
     mdLayout.dump_all_state5=False
 tmpcd=''
 ind=0
 
 for ds in cpurps:
  ind+=1
  if ds == ',' or len(cpurps) == ind:
   if len(cpurps) == ind:
     tmpcd+=ds
   purps.append(tmpcd)
   tmpcd=''
  else:
   tmpcd+=ds  
 
 print purps
 
 
 indckl=1
 while indckl <= 50:  
   try:         
         print 'Process sentences:',usr,pg_ex,debug_all
         load_pages_know(usr,pg_ex)
         print 'Doc len.',len(entry_doc)
         
         if len(entry_doc) > 0 :         
          process_sentences(0,usr,purps)
          #conn.commit () 
         indckl+=1  
         if just_one_index: break
   except Exception,err2:
         print 'Error process sentences(2):',err2
         log.exception('Error process sentences(2):')
          
except Exception,err:
         print 'Error process sentences:',err
         log.exception('Error process sentences:')
        #==== 
 
print 'End process.Time elapsed: ',time.clock () - startTT
 
 
