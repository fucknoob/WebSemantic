#encoding: latin-1
import mdTb
import umisc
import logging
from StringIO import StringIO
import datetime
import time, datetime
import mdNeural
import mdTb
import sys


conn=None
conn3=None
  
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('DYNAMIC-CODE-ENGINE->mdNeural->GET_OBJECT(2)')


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

tb_object1=None
tb_object_dt1=None
tb_relaction1=None

tb_object31=None
tb_object_dt31=None
tb_relaction31=None

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
 #========
 tb_object1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT') 
 tb_object_dt1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT') 
 tb_relaction1 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS') 
 #
 tb_object31 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
 tb_object_dt31 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
 tb_relaction31 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 


def lp(s,len,ch):
 i=1
 while i <= len:
  s=ch+s
  i+=1
 return s 
 

def dump_layer(lr):
 def dump_nr(nr,lev=1):
  ls1=int(lev*4)
  s1=lp('NR:==========',ls1-1,'.')
  print s1,ls1
  s33=lp('SNDT:',ls1,'.')
  print s33,'nr-DT:',nr.dt,ls1
  s2='SINAPSES('+str(lev)+'):==========='
  s2=lp(s2,ls1,'.')
  print s2,ls1
  for s in nr.sinapses:
   print lp('[',ls1,'.'),s.nr.dt
   dump_nr(s.nr,lev+1)
  s3='end-nr======='
  s3=lp(s3,ls1-1,'.')
  print s3,ls1
 #=== 
 print 'TOPICOS:================='
 for l in lr.topicos:
  dump_nr(l)
 print 'END-TOPICOS=============='


def get_object_by_data2(obj,usr,uid=0):
  return mdTb.get_object_by_data2z(obj,uid) 

 
def get_object_by_data2P(obj,usr,uid=0):
 # 
 print 'Read object(g2):',obj,' uid:',uid 
 #
 Zeus_Mode=False
 obj_ret=mdTb.get_object_by_data2z(obj,uid,False)            
 Zeus_Mode=ant_z            
 #
 if obj_ret != None:
   obj_ret.get_links('')
 #print lay.topicos,'....................'
 #-----------
 return obj_ret 
 
def get_object_by_data29(obj,usr,max_purposes):
 lay=mdTb.get_object_by_data2z(obj,obj,True)
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
 return mdTb.get_object_by_data2z(obj,obj,True)  
  
  
def get_object_by_data22(obj,usr,plus):
 #-----------
 lay=mdTb.get_object_by_data2z(obj,obj,True)
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
 lay=mdTb.get_object_by_data2z(obj,obj,True)
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
 
 
def clear_obj(usr,name,links,uuid ):
 mdTb.delete_objz(name,uuid) 
 
 
def check_code_object(alias,usr):
 try:
  obj_ret=mdTb.tb_object1.get(alias) 
 except:
   return False  
 return True  
 
 
def get_ontology(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None    
 return mdTb.get_ontology_conditionz(aliases,purposes,'destination') 
 
 
def get_ontology_s2s(aliasc,opcode,usr ): #  considera os purposes nos filtros quando alias == None 
  cl4 = index.create_index_expression(column_name='obj_dest', value=str(aliasc))
  cl5 = index.create_index_expression(column_name='opcode', value=str(opcode))
  clausec = index.create_index_clause([cl4,cl5],count=1000000)
  if mdTb.Zeus_Mode:
   resultSet=tb_relaction1.get_indexed_slices(clausec)
  else: 
   resultSet=tb_relaction13.get_indexed_slices(clausec)
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
   obj_principal=mdTb.get_object_by_dataz(ido,ido) 
   rts.append(obj_principal) 
  return rts   
 
 
def get_ontology_s(aliases,purposes,destinats,usr ): #  considera os purposes nos filtros quando alias == None 
 return mdTb.get_ontology_conditionz(aliases,purposes,destinats) 
    
 


def parse_each_topico(tp):
 rt=tp.split('>')
 if len(rt) == 0:
   return [tp]
 else:
   return rt 

def parse_each_topico2(tp,sign):
 for ks in sign:
  rt=tp.split('>')
  if len(rt) == 0:
    return [tp]
  else:
    return rt 
 return [tp]  

def get_obj_pnd(usr,i):
 rt=[]
 if mdTb.Zeus_Mode:
  resultSet=[[i,tb_object.get(i) ]]
 else: 
  resultSet=[[i,tb_object31.get(i) ]]
 for ky,r in resultSet:
   rt.append([r[u'objeto'],ky])
 return rt



def valida_topico(purpose,usr,obj,first=True,topico='',index=0,topico_o=0):
 return mdTb.valida_topico31(purpose,usr,obj,first,topico,index,topico_o)


def get_ontology_ponderate(aliases,min_purposes,max_purposes,usr,dfin,sinapses_consid ): # min_purposes=mandatory, max_purposes=max ideal 
     rts=[]
     firp=True
     resultSet2=[]
     canditates=[]
     alias = aliases
     if alias == None:
      alias='%'
     #====================================================================================================================================== 
     #====================================================================================================================================== 
     def get_filter_in_objs(obj,sinapses_consid1,dfin1,canditates,firp):
      resultSet22=[]
      for mn in min_purposes:
       if umisc.trim(mn) == '':continue
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
        r=[[c,tb_object31.get(c)]]
        resultSet22.append(r) 
      return resultSet22  
     #====================================================================================================================================== 
     #====================================================================================================================================== 
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
         mn=parse_each_topico2(mn,dfin)
         #print 'start.min.p:',mn
         c2=mdTb.valida_topico31_2(mn,usr,alias,True,'',0,0,sinapses_consid)
         print 'min.p:',mn ,c2
         if len(c2) > 0: 
          kfnd=True
          for c1 in c2:        
           if c1 in canditates or firp:
            canditates.append(c1)
        #===============================================  
        if not kfnd: return [] 
       else: 
        mn=parse_each_topico2(mn,dfin)
        #print 'start.min.p:',mn
        c2=mdTb.valida_topico31_2(mn,usr,alias,True,'',0,0,sinapses_consid)
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
        try:
         r=[[[c,tb_object31.get(c)]]]
        except: 
         try:
           r=[[[c,tb_object1.get(c)]]]
         except:
             #r=[[c,tb_object.get(c)]] 
             pass # cache temporario tb_object, nao deve haver ponderacoes nesse cache
          
        resultSet2.append(r) 
     else:     
      #print 'Collect->get(2):',alias,usr 
      # 
      ########################################################################      
      #if mdTb.Zeus_Mode:
      #  r=[[alias,tb_object1.get(alias)]]
      #else:  
      #  r=[[alias,tb_object31.get(alias)]]
      r=get_filter_in_objs(alias,sinapses_consid,dfin,canditates,firp)  
      resultSet2.append(r)
      
      
     #============================================= 
     for resultSet23 in resultSet2:
      for resultSet in resultSet23:
       for key,results in resultSet:
         i=results[u'objeto'] 
         uid=key
         #====
         avaliable_objs=[]
         #===--------------------------------------
         #print 'get_object_by_data29()->(',i,',',usr,',',max_purposes,')'
         ant_z=mdTb.Zeus_Mode
         mdTb.Zeus_Mode=False
         [obj_principal,ratting]=get_object_by_data29(i,usr,max_purposes)
         obj_principal.get_links('')
         mdTb.Zeus_Mode=ant_z
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
      resultSet=mdTb.get_ontology_condition_idz(alias,purps,['destination'])
     else:     
      #print 'Collect->get(2):',alias,usr 
      # 
      if mdTb.Zeus_Mode:      
        resultSet1=[[alias,tb_object1.get(alias)]]
      else:  
        resultSet1=[[alias,tb_object31.get(alias)]]
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
      resultSet=mdTb.get_ontology_condition_idz(alias,purps,['destination'])
     else:     
      if mdTb.Zeus_Mode:
       resultSet1=[[alias,tb_object1.get(alias)]]
      else: 
       resultSet1=[[alias,tb_object31.get(alias)]]
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
  
  
 
def post_object_by_data_es(layer,usr): 
  posted_objs=[]
  cenario=0
  senti=0
  uuid=''
  foco=None
  l_p_ant=None
  termo='SYSTEM'
  for ts in layer.topicos:  
   if ts.uuid > 0:
    uuid=ts.uuid
    break  
  mdTb.post_object_by_dataz(layer,cenario,usr,termo,foco,posted_objs,senti,l_p_ant,True)
    
    
    
def get_ontology_s_p(aliases,purposes,destinats,usr ): #  considera os purposes nos filtros quando alias == None 
 if True:
     ant_z=mdTb.Zeus_Mode
     mdTb.Zeus_Mode=True
     rts=mdTb.get_ontology_conditionz(alias,purposes,destinats)
     mdTb.Zeus_Mode=ant_z
     return rts     
     
