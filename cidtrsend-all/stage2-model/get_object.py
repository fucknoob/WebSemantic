#encoding: latin-1
import umisc
import logging
from StringIO import StringIO
import datetime
import time, datetime
import mdNeural

conn=None
conn3=None

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('DYNAMIC-CODE-ENGINE->mdNeural->GET_OBJECT')


self_usr=''

ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

tb_object=None
tb_object_dt=None
tb_relaction=None

tb_object31=None
tb_object_dt31=None
tb_relaction31=None

tb_object1=None
tb_object_dt1=None
tb_relaction1=None

import mdTb


def start_db(pool2):
 global tb_object
 global tb_object_dt
 global tb_relaction
 global tb_object31
 global tb_object_dt31
 global tb_relaction31
 #========
 tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3') 
 tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3') 
 tb_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3') 
 #
 tb_object31 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
 tb_object_dt31 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
 tb_relaction31 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 
 #
 tb_object1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT') 
 tb_object_dt1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT') 
 tb_relaction1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS') 
 # 
 mdTb.start_db(pool2)

def get_object_by_data2(obj,usr):   
 return mdTb.get_object_by_data2(obj,obj,True)
 
def get_object_by_data29(obj,usr,max_purposes):
 lay=mdTb.get_object_by_data2(obj,obj,True)
 rattings=0
 for ds1 in lay.topicos:
  for d in ds1.dt:
     for d in max_purposes:
           if TOP.lower() == d.lower():
             rattings+=1
             break
 #===============================================          
 return [lay,rattings]  
 
def get_object_by_data23(obj,usr):
 return mdTb.get_object_by_data2(obj,obj,True) 

def get_object_by_data22(obj,usr,plus):
 #-----------
 lay=mdTb.get_object_by_data2(obj,obj,True)
 plus_fnd=0
 for tps in lay.topicos:
   TOP=tps.dt[0]
   for s1 in tps.sinapses:
     DT=s1.nr.dt[0]
     if True:
          plusf=False
          for sd in plus:
           if TOP == 'way' and DT == sd:
            plusf=True
          if plusf:
            plus_fnd+=1
     
 #-----------
 return [lay,plus_fnd]  

 
def get_object_by_data223(obj,usr,plus):
 #-----------
 lay=mdTb.get_object_by_data2(obj,obj,True)
 plus_fnd=0
 for tps in lay.topicos:
   TOP=tps.dt[0]
   for s1 in tps.sinapses:
     DT=s1.nr.dt[0]
     if True:
          plusf=False
          for sd in plus:
           if TOP == 'need' and DT == sd:
            plusf=True
          if plusf:
            plus_fnd+=1     
 #-----------
 return [lay,plus_fnd]  
 
 
def clear_obj(usr,name ):
  mdTb.delete_obj(name,name)
 
 
def post_object_by_data_es(layer,usr): 
 cenario=0
 senti=0
 #def post_object_by_data3p( , , ,,, ,): 
 print 'Post LR:',nameo,',len:',len(nameo),', usr:',usr 
 nameo=layer.name
 nameo=umisc.trim(nameo)
 clear_obj(usr,nameo)
 #=======================  
 nameo=layer.name
 print 'Post layer:',nameo
 
 fnd_tops=False
 
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
 #========== 
 #if not no_post_o and len(layer.topicos)>0:
 print 'Insert-OBJ:'
 #==
 if not no_post_o :
  #sql1="insert into SEMANTIC_OBJECT3(username,objeto,cenar,senti) values(?,?,?,?)"
  try:   
   cols={"username":usr,"objeto":ky1,"cenar":str(cenario),"sento":str(senti)}
   tb_object.insert(ky1,cols)       
   #conn.sqlX (sql1,([usr,nameo,cenario,senti]))
  except Exception,err: print 'Erro ao post(OBJECT):',err
 else: print 'Skip:',nameo,senti
 #=============
 uid=ky1
 #= 
 print 'Post-NRS:'
 
 def post_alldt(arr):
   #=======================
   b = tb_object_dt.batch(queue_size=len(arr))   
   for k,cols in arr:
    b.insert(str(k),cols) 
   b.send()
 
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
         kyl1=uid+'|'+str(cnt)
         it={"UID":uid,"topico":tp_Dt,"LEV":"1","sin":'',"datach":'',"id_top":str(id_top),"username":usr,"cnt":str(cnt)}
         arr1.append( [ kyl1,it ] )
         cnt+=1
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
        kyl1=uid+'|'+str(cnt)
        it={"UID":uid,"topico":tp_Dt,"LEV":str(level),"sin":sn.opcode,"datach":sn_dt.lower(),"id_top":str(id_top),"username":usr,"cnt":str(cnt)}
        arr1.append( [ kyl1,it ] )
        cnt+=1
        #====================================================
        #==========
        post_nr(uid,cnt,arr1,usr,sn.nr,level+1,id_top,True)
   except Exception,e:
    #print 'Error post nr.' ,  e
    log.exception('[Error post nr...]')
 #==========    ===============================================
 
 print 'Post.Topicos{}:' 
 #==========    ===============================================
 indi=0
 arr_post=[]
 for tp in layer.topicos:
  #==========    ===============================================
  indi+=1
  print 'Post.nr.num:',indi
  #
  post_nr(ky1,indi,arr_post,usr,tp)
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
  #layer,cenario,usr,foco
  post_object_by_data_es(lnk.lr,usr) 
 #=============== 
 

def get_ontology(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None    
 return mdTb.get_ontology_condition(aliases,purposes,'destination')
 
 
 
def get_ontology_s(aliases,purposes,destinats,usr ): #  considera os purposes nos filtros quando alias == None 
 r= mdTb.get_ontology_condition(aliases,purposes,destinats) 
 if len(r) == 0:
   ant_z=mdTb.Zeus_Mode
   mdTb.Zeus_Mode=True
   r=mdTb.get_ontology_conditionz(aliases,purposes,destinats)
   mdTb.Zeus_Mode=ant_z
 return r  
 
 
 
 
def get_ontology_s2s(aliasc,opcode,usr ): #  considera os purposes nos filtros quando alias == None 
  cl4 = index.create_index_expression(column_name='obj_dest', value=str(aliasc))
  cl5 = index.create_index_expression(column_name='opcode', value=str(opcode))
  clausec = index.create_index_clause([cl4,cl5],count=1000000)
  resultSet=tb_relaction.get_indexed_slices(clausec)
  for ky,resultsC in resultSet: 
   ido=resultsC[u'obj_orig']
   ido2=resultsC[u'opcode']
   ido3=resultsC[u'foco']
   ido4=resultsC[u'foco_d']
   ido5=resultsC[u'cond']
   #===
   if ido2  == None:
    ido2=''
   if ido3  == None:
    ido3=''
   if ido4  == None:
    ido4=''
   if ido5  == None:
    ido5=''
   obj_principal=mdTb.get_object_by_data(ido,ido) 
   rts.append(obj_principal) 
  return rts  
 
 
def parse_each_topico(tp):
 rt=tp.split('>')
 if len(rt) == 0:
   return [tp]
 else:
   return rt 

def get_obj_pnd(usr,i):
 # 
 rt=[]
 resultSet=tb_object.get(i) 
 for ky,r in resultSet:
   rt.append([r[u'objeto'],ky])
 return rt
 
 
def get_ontology_ponderate(aliases,min_purposes,max_purposes,usr,dfin,sinapses_consid ): # min_purposes=mandatory, max_purposes=max ideal 
     rts=[]
     resultSet2=[]
     canditates=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None or umisc.trim(aliases) == '':
      for mn in min_purposes:
       tmpk=mn.split('|')
       if len(tmpk)>1:
        basec=mn.split('>')
        base=''
        lsk=len(basec)
        infk=0
        for b in basec:
          if base != '': base+='>'
          base+=b
          infk+=1
          if infk >= (lsk-1): break
        change=mn.split('>')[-1]
        tmpk=change.split('|')
        kfnd=False
        for mn2 in tmpk:
         mn=base+'>'+mn2
         print 'parse mn param:',mn
         mn=parse_each_topico2(mn,dfin1)
         #print 'start.min.p:',mn
         c2=mdTb.valida_topico31_2(mn,usr,obj,True,'',0,0,sinapses_consid1)
         print 'min.p:',mn ,c2
         if len(c2) > 0: 
          kfnd=True
          for c1 in c2:        
           if c1 in canditates or firp:
            canditates.append(c1)
        #===============================================  
        if not kfnd: return [] 
       else: 
        mn=parse_each_topico2(mn,dfin1)
        #print 'start.min.p:',mn
        c2=mdTb.valida_topico31_2(mn,usr,obj,True,'',0,0,sinapses_consid1)
        #print 'min.p:',mn ,c2
        if len(c2) == 0: return []
       for c1 in c2:        
          if c1 in canditates or firp:
           canditates.append(c1)
       firp=False
      canditates2=canditates
      canditates=[]
      for c in canditates2:
        if not c in canditates:
          canditates.append(c)
      for c in canditates: 
        # 
        r=tb_object.get(c)
        resultSet2.append(r) 
     else:     
      #print 'Collect->get(2):',alias,usr 
      # 
      r=[]
      try:
       r=[[alias,tb_object.get(alias)]]
      except:pass 
      resultSet2.append(r)
     for resultSet in resultSet2:
      for key,results in resultSet:
        i=results[u'objeto'] 
        uid=key
        #====
        avaliable_objs=[]
        #===--------------------------------------
        #print 'get_object_by_data29()->(',i,',',usr,',',max_purposes,')'
        [obj_principal,ratting]=get_object_by_data29(i,usr,max_purposes)
        obj_principal.get_links('')
        #if len(obj_principal.topicos) > 0 :
        rts.append([ratting,obj_principal])
        rts.sort()
        #===     
     return rts   
 
 
 
 
def get_ontology_ponderate2(aliases,min_purposes,max_purposes,usr ): # min_purposes=mandatory, max_purposes=max ideal 
 if True:
     rts=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None:
      purps=[]
      for d in min_purposes:
       purps.append(d)
      #print 'Collect->get(1):',ps,alias,usr
      # 
      resultSet=mdTb.get_ontology_condition_id(alias,purps,['destination'])
     else:     
      #print 'Collect->get(2):',alias,usr 
      # 
      resultSet1=tb_object.get(alias)
      resultSet=[]
      for ky,cols in resultSet1:
        resultSet.append([ky,ky])
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        #===--------------------------------------
        #===--------------------------------------
        #print 'get_object_by_data29()->(',i,',',usr,',',max_purposes,')'
        [obj_principal,ratting]=get_object_by_data29(i,usr,max_purposes)
        #if len(obj_principal.topicos) > 0 :
        rts.append([ratting,obj_principal])
        rts.sort()
 return rts   
 
 
def get_ontology2(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None 
 if True:
     rts=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None:
      purps=[]
      for d in purposes:
       purps.append(d)
      # 
      resultSet=mdTb.get_ontology_condition_id(alias,purps,['destination'])
     else:     
      resultSet1=tb_object.get(alias)
      resultSet=[]
      for ky,cols in resultSet1:
        resultSet.append([ky,ky])
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        obj_principal=get_object_by_data23(i,usr)
        #if len(obj_principal.topicos) > 0 :
        rts.append(obj_principal)
        #===
 return rts  
  
  
 
 

    
    
    