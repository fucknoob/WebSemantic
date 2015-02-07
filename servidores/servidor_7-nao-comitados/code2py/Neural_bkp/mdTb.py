#in zeus mode, SEMANTIC_OBJECT_DT3_1_4 e SEMANTIC_OBJECT3_1_4 sao substituidos por SEMANTIC_OBJECT e SEMANTIC_OBJECT_DT e 
#  convivem os rct junto com os obj de base, pois para processo de aprendizado de maquina, os rct podem ser apliados e complementados como
#  object data comum

Zeus_Mode=False

if Zeus_Mode:
 table_object='SEMANTIC_OBJECT'
 table_dt='SEMANTIC_OBJECT_DT'
 table_relaction='SEMANTIC_RELACTIONS'

else:
 table_object='SEMANTIC_OBJECT3_1_4'
 table_dt='SEMANTIC_OBJECT_DT3_1_4'
 table_relaction='SEMANTIC_RELACTIONS3_1_4'


tb_object=None
tb_object_dt=None
tb_relaction=None

tb_object1=None
tb_object_dt1=None
tb_relaction1=None

tb_object31=None
tb_object_dt31=None
tb_relaction31=None

tb_py=None
tb_py_code=None

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

import gt
import umisc
import mdNeural
 
def start_db(pool2):
  global tb_object
  global tb_object_dt
  global tb_relaction
  global tb_object1
  global tb_object_dt1
  global tb_relaction1
  global tb_object31
  global tb_object_dt31
  global tb_relaction31
  global tb_py
  global tb_py_code
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
  #
  tb_py=pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_PY') 
  tb_py_code=pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_CODE_PY') 
  
  
  
import gradiente  
  
class iter_cd:
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
          return [None,None]    
 
if not Zeus_Mode: 
 
 def get_object_by_data(obj,uid):
  if uid != '':
   resultSet=[[uid,tb_object.get(uid)]]  
    
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    resultSet=tb_object.get_indexed_slices(clausec)  
  #
  obj_nm=None
  #uid=None
  cenar=0
  cnts_all_tps=0
  for key1,results in resultSet:
       obj_nm=results[u'objeto'] 
       #uid=key1
       cenar=results[u'cenar'] 
       cnts_all_tps=results[u'conts_n'] 
       break
  #-----------
  lay=mdNeural.mdLayer ()
  lay.tb=2
  if obj_nm == None: obj_nm=obj
  lay.name=obj_nm
  tpc2=lay.set_topico('identificador')
  tpc2.uuid=cenar
  nrc2= lay.set_nr(lay.name)
  nrc2.uuid=cenar
  tpc2.connect_to(lay,nrc2,'Composicao') 
  #print lay.topicos,'....................'
  print 'Read object(g1):',obj,' uid:',uid,',cenar:',cenar
  #-----------def cached_dt(objectkey,cnts_all_tp):
  def cached_dt(objectkey,cnts_all_tp):  
    '''
    cached=[]
    key_ini=objectkey+'|1'
    key_end=objectkey+'|300000'
    rg=gt.get_range(objectkey,tb_object_dt)
    #rg=tb_object_dt.get_range(key_ini,key_end)
    for ky,cols in rg:
      cached.append([ky,cols])
    return cached  
    '''
    #   
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
    #    
    return cached 
   
  if True : 
      rows=cached_dt(uid,cnts_all_tps) 
      iterat=iter_cd(rows)
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
           try:
             DT=results[u'dat'] 
           except:  
             DT=results[u'datach'] 
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
                   nrc= lay.set_nr(DT)
                   ic2=ky
                   lev=results[u'LEV']
                   uuid=ky
                   nrc.uuid=cenar
                   #print 'Level 2(ind):',lev,TOP,DT
                   if int(results[u'cnt']) <= cnti:
                    ky,results = resultSet1.next()
                    continue
                   
                   if int(lev) != 2:
                     break
                   #==
                   #print 'Level 2(dt) :',nrc.dt
                   nr.connect_to(lay,nrc,'Composicao') 
                   ky,results = resultSet1.next()
                   results = read_dt_level( nrc,3,uid,ic2,lay,results,resultSet1,cenar ) #####                  
  return lay  
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_object_by_data2(obj,uid,parsed):
  if uid != '':
   resultSet=[[uid,tb_object.get(uid)]]  
    
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    resultSet=tb_object.get_indexed_slices(clausec)  
  #
  obj_nm=None
  #uid=None
  cenar=0
  cnts_all_tps=0
  for key1,results in resultSet:
       obj_nm=results[u'objeto'] 
       #uid=key1
       cenar=results[u'cenar'] 
       cnts_all_tps=results[u'conts_n'] 
       break
  #-----------
  lay=mdNeural.mdLayer ()
  lay.tb=2
  if obj_nm == None: obj_nm=obj
  lay.name=obj_nm
  tpc2=lay.set_topico('identificador')
  tpc2.uuid=cenar
  nrc2= lay.set_nr(lay.name)
  nrc2.uuid=cenar
  tpc2.connect_to(lay,nrc2,'Composicao') 
  #print lay.topicos,'....................'
  print 'Read object(g1):',obj,' uid:',uid,',cenar:',cenar
  #-----------
  def cached_dt(objectkey,cnts_all_tp):
    cached=gt.get_range(objectkey,tb_object_dt,1,cnts_all_tp)
    return cached  
  if True :
      rows=cached_dt(uid,cnts_all_tps) 
      iterat=iter_cd(rows)
      def read_dt_level( nr_top,levelc1,uid1,ic1,lay1,results,resultSet,uuid):
              while results  :
                   DT=results[u'dat'] 
                   TOP=results[u'topico' ]
                   ic1=uuid
                   lev=results[u'LEV']
                   #print 'READ(g2).top-init:',TOP,DT,'->',lev , levelc1
                   if int(lev) != levelc1: 
                    return results
                    break
                                      
                   if parsed:
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrc=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      nr_top.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrc=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       nr_top.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrc=nr
                    ky,results = resultSet.next()
                    if nrc != None:
                      read_dt_level(nrc,(levelc1+1),uid1,ic1,lay1,results,resultSet,uuid)
                   else: 
                    nrc= lay1.set_nr(DT)
                    nrc.uuid=uuid
                    #print 'READ(g2).top:',TOP,DT
                    #==
                    nr_top.connect_to(lay1,nrc,'Composicao') 
                    ky,results = resultSet.next()
                    read_dt_level(nrc,(levelc1+1),uid1,ic1,lay1,results,resultSet,uuid)
              return results     
      #==================== 
      #      
      #
      resultSet =iterat.get_level([0,1]).get_all()
      obj_nm=None     
      for ky,results in resultSet:
           DT=results[u'dat'] 
           TOP=results[u'topico']
           cnti=int(results[u'cnt'])
           ic=ky
           uuid=ky
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
           if parsed:            
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrTO=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      tps.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrTO=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       tps.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrTO=nr
            
           else: 
            nrTO= lay.set_nr(DT)
            nrTO.uuid=cenar
            tps.connect_to(lay,nrTO,'Composicao') 
           if True:
              #==     
              #
              levs=range(0,50)             
              resultSet1=iterat.get_level(levs)             
              #
              #
              ky,results = resultSet1.next()
              while results  :
                   DT=results[u'dat'] 
                   TOP=results[u'topico']
                   ic2=ky
                   lev=results[u'LEV']
                   uuid=ky
                   #print 'Level 2(ind):',lev,TOP,DT
                   if int(results[u'cnt']) <= cnti:
                    ky,results = resultSet1.next()
                    continue
                   
                   if int(lev) != 2:
                     break
                   #==
                   if parsed:
                    
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrc=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      nrTO.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrc=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       nrTO.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrc=nr
                    ky,results = resultSet1.next()
                    if nrc != None:
                      read_dt_level(nrc,(3),uid,ic2,lay,results,resultSet1,cenar)                    
                   else: 
                    nrc= lay.set_nr(DT)
                    nrc.uuid=cenar
                    #print 'Level 2(dt) :',nrc.dt
                    nrTO.connect_to(lay,nrc,'Composicao')                    
                    ky,results = resultSet1.next()
                    results = read_dt_level( nrc,3,uid,ic2,lay,results,resultSet1,cenar ) #####                  
  return lay   
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def delete_obj(obj,uid):
  if uid != '':
   resultSet=[[uid, tb_object.get(uid) ]] 
    
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    resultSet=tb_object.get_indexed_slices(clausec)  
  #
  obj_nm=None
  uid=None
  cenar=0
  for key1,results in resultSet:
     tb_object.remove(key1)
     #-----------
     key_ini=objectkey+'|1'
     key_end=objectkey+'|300000'
     #rg=tb_object_dt.get_range(key_ini,key_end)
     rg=gt.get_range(objectkey,tb_object_dt)
     for ky,cols in rg:
       tb_object_dt.remove(ky)
     #===============================  
     cl4 = index.create_index_expression(column_name='obj_orig', value=key1)
     clausec = index.create_index_clause([cl4],count=1000000)
     resultSet=tb_relaction.get_indexed_slices(clausec)
     for ky,resultsC in resultSet: 
      tb_relaction.remove(ky)   
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_ontology_condition(obj1,dt,topicos ): 
  if True:
     rts=[]
     collects=[]
     print 'Special get_ontology_condition:',obj1,dt,topicos 
     if obj1 == '$$all$$': 
       obj1=None
     if True:
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos]       
      ps=''
      f=False
      ps2=''
      clas=[]
      for d in dt:
       cl4 = index.create_index_expression(column_name='datah', value=d)
       clas.append(cl4)
      for ds in topicos:
       cl4 = index.create_index_expression(column_name='topico', value=ds)
       clas.append(cl4)
      #==============================================================      
      clausec = index.create_index_clause(clas,count=1000000)
      resultSet=tb_object_dt.get_indexed_slices(clausec)  
      #print 'get_ontology_s_p.sql:',sqlc2t
      for ky,cols in resultSet:
        obj=cols[u'UID']         
        if obj not in collects:         
         obj_principal=get_object_by_data(obj,obj)        
         obj_principal.get_links('')
         if obj1 != None:
          if obj_principal.name == obj1:
           rts.append(obj_principal)
           collects.append(obj)
         else:
          rts.append(obj_principal)
          collects.append(obj)
  return rts
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_ontology_condition_id(obj,dt,topicos ): 
  if True:
     rts=[]
     collects=[]
     print 'Special get_ontology_condition:',obj,dt,topicos 
     if obj == '$$all$$': 
       obj=None
     if True:
      ps=''
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos]       
      f=False
      ps2=''
      clas=[]
      for d in dt:
       cl4 = index.create_index_expression(column_name="datach", value=d)
       clas.append(cl4)
      for ds in topicos:
       cl4 = index.create_index_expression(column_name='topico', value=ds)
       clas.append(cl4)
      #==============================================================      
      clausec = index.create_index_clause(clas,count=1000000)
      resultSet=tb_object_dt.get_indexed_slices(clausec)  
      #print 'get_ontology_s_p.sql:',sqlc2t
      for ky,cols in resultSet:
        obj1=cols[u'UID']         
        if obj not in collects:         
         obj_principal=get_object_by_data(obj1,obj1)        
         if obj_principal != None:
          if obj1 != None:
           if obj_principal.name == obj:
            rts.append([obj1,obj1])
            collects.append(obj1)
          else:
           rts.append(obj_principal)
           collects.append(obj1)
  return rts 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_ontology_topic_condition(obj,dt,topicos,level=-1 ): 
  if True:
     rts=[]
     collects=[]
     print 'Special get_ontology_condition:',obj,dt,topicos 
     if obj == '$$all$$': 
       obj=None
     if True:
      ps=''
      f=False
      ps2=''
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos]       
      clas=[]
      if obj == None:
        key_ini=objectkey+'|1'
        key_end=objectkey+'|300000'
        rg=tb_object_dt.get_range(key_ini,key_end)
        for ky,cols in rg:
         tps1=False
         tps2=False
         for d in dt:
           if d==cols[u"datach"]:
             tps1=True
             break
         for ds in topicos:
           if ds==cols[u'topico']:
             tps2=True
             break
         if len(dt)==0:
           tps1=True 
         if len(topicos)==0:
           tps2=True
         if level > -1:
           lev2=int(cols[u'LEV'])
           if lev2==None: lev2=''
           if lev2=='': lev2='-1'
           lev1=int(umisc.trim(lev2))
           if level != lev1:
             tps2=False
         if tps1 and tps2:
          TOP=cols[u'topico']         
          DT=cols[u"datach"]    
          rts.append([ky,TOP,DT])
      else:
       for d in dt:
        cl4 = index.create_index_expression(column_name="datach", value=d)
        clas.append(cl4)
       for ds in topicos:
        cl4 = index.create_index_expression(column_name='topico', value=ds)
        clas.append(cl4)
       if level < -1:
        cl4 = index.create_index_expression(column_name='LEV', value=str(level))
        clas.append(cl4)
       #==============================================================      
       clausec = index.create_index_clause(clas,count=1000000)
       resultSet=tb_object_dt.get_indexed_slices(clausec)  
       #print 'get_ontology_s_p.sql:',sqlc2t
       for ky,cols in resultSet:
         TOP=cols[u'topico']         
         DT=cols[u"datach"]    
         rts.append([ky,TOP,DT])
  return rts
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_ontology_topic_condition31(obj,dt,topicos,level=-1 ): 
  if True:
     objectkey=obj
     rts=[]
     def not_ins(cmd):
       [ky1,TOP1,DT1,obj1]=cmd
       br=False
       for [ky,TOP,DT,obj] in rts:
         if TOP==TOP1 and obj==obj1:
           br=True
           break
       return br   
     collects=[]
     print 'Special get_ontology_condition:',obj,dt,topicos 
     if obj == '$$all$$': 
       obj=None
     if True:
      ps=''
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos]       
      f=False
      ps2=''
      clas=[]
      try:
       obj_referec=tb_object31.get(objectkey) 
      except:
       obj=None 
      if obj != None:
        obj_refere=tb_object31.get(objectkey)
        key_ini=objectkey+'|1'
        key_end=objectkey+'|300000'
        #rg=tb_object_dt31.get_range(key_ini,key_end)
        rg=gt.get_range(objectkey,tb_object_dt31,1,int(obj_refere[u'conts_n']) )
        for ky,cols in rg:
         tps1=False
         tps2=False
         for d in dt:
           #if d==cols[u"datach"]:
           if gradiente.simple_compare( d,cols[u"datach"] ) >0:
             tps1=True
             break
         for ds in topicos:
           #if gradiente.simple_compare(ds,cols[u'topico']) > 0: 
           if ds==cols[u'topico']:
             tps2=True
             break
         if len(dt)==0:
           tps1=True 
         if len(topicos)==0:
           tps2=True
         if level > -1:
           lev2=int(cols[u'LEV'])
           if lev2==None: lev2=''
           if lev2=='': lev2='-1'
           lev2=str(lev2)
           lev1=int(umisc.trim(lev2))
           if level != lev1:
             tps2=False
         if tps1 and tps2:
          TOP=cols[u'topico']         
          DT=cols[u"datach"]   
          if not not_ins([ky,TOP,DT,obj]):
           rts.append([ky,TOP,DT,obj])
      else:
       for d in dt:
        cl4 = index.create_index_expression(column_name="datach", value=d)
        clas.append(cl4)
       for ds in topicos:
        cl4 = index.create_index_expression(column_name='topico', value=ds)
        clas.append(cl4)
       if level < -1:
        cl4 = index.create_index_expression(column_name='LEV', value=str(level))
        clas.append(cl4)
       #==============================================================      
       clausec = index.create_index_clause(clas,count=1000000)
       resultSet=tb_object_dt31.get_indexed_slices(clausec)  
       #print 'get_ontology_s_p.sql:',sqlc2t
       for ky,cols in resultSet:
         TOP=cols[u'topico']         
         DT=cols[u"datach"]  
         obj=cols[u"UID"]  
         if not not_ins([ky,TOP,DT,obj]):
          rts.append([ky,TOP,DT,obj])
  return rts 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def valida_topico(purpose,usr,obj,first=True,topico='',index=0,topico_o=0):
   rt=[]
   if first: # primeiro topico  
      #print 'start valida.topico:',purpose,index
      ps=purpose[index].lower()    
      #================================================================================  
      if obj != "%":
       cl4 = index.create_index_expression(column_name='obj_orig', value=obj)
       clausec = index.create_index_clause([cl4],count=1000000)
       resultSet=tb_relaction.get_indexed_slices(clausec)
       for ky,resultsC in resultSet: 
        obj_dest=[u'obj_dest']  
        try:
          obj_r=tb_object.get(obj_dest)
          #===========
          objs1=get_ontology_topic_condition(obj_dest,[],[ps])
          #===========
        except:pass   
      else:
        objs1=get_ontology_topic_condition([],[],[ps])
            
      index+=1
      # resultSet -> passaram pela etapa      
      for [ky,tp,dt] in objs1:
        i=ky
        #print 'Start.level:',index
        rt2c=valida_topico(purpose,usr,obj,False,tp,index,i)
        if len(rt2c) > 0 :         
          rt.append(i)         
   else: # topico encadeado 
      #print 'start.second.level:',purpose,index 

      #==================== 
      if len(purpose)<=(index):
        return [topico_o]
      ps=purpose[index]
      #
      
      rts=get_ontology_topic_condition(topico_o,[],[topico],index)
      
      #print 'valida.topico.f:(',topico_o,(index),')',sqlcc2
      # resultSet -> passaram pela etapa      
      index+=1
      for [ky,TOP,DT] in resultSet:
        tp=TOP
        rt2=valida_topico(purpose,usr,obj,False,tp,index,ky)
        if len(rt2) == 0: return []
        for r in rt2:
          rt.append(r)
        
   return rt 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def valida_topico31(purpose,usr,obj,first=True,topico='',index=0,topico_o=0):
   rt=[]
   if first: # primeiro topico  
      #print 'start valida.topico:',purpose,index
      ps=purpose[index].lower()    
      #================================================================================  
      if obj != "%" and obj != None:
       cl4 = index.create_index_expression(column_name='obj_orig', value=obj)
       clausec = index.create_index_clause([cl4],count=1000000)
       resultSet=tb_relaction31.get_indexed_slices(clausec)
       for ky,resultsC in resultSet: 
        obj_dest=[u'obj_dest']  
        try:
          obj_r=tb_object31.get(obj_dest)
          #===========
          objs1=get_ontology_topic_condition31(obj_dest,[],[ps])
          #===========
        except:pass   
      else:
        ps2=[]
        if len(purpose)> index+1:
          ps2=[purpose[index+1].lower()]  
          index+=1
        objs1=get_ontology_topic_condition31(obj,ps2,[ps])
            
      index+=1
      # resultSet -> passaram pela etapa      
      for [ky,tp,dt,okb] in objs1:
        i=ky
        #print 'Start.level:',index
        rt2c=valida_topico31(purpose,usr,okb,False,tp,index,okb)
        if len(rt2c) > 0 :         
          rt.append(okb)         
   else: # topico encadeado 
      #print 'start.second.level:',purpose,index 

      #==================== 
      if len(purpose)<=(index):
        return [topico_o]
      ps=purpose[index]
      #
      rts=get_ontology_topic_condition31(topico_o,[ps],[topico],index)
      index+=1
      for [ky,TOP,DT,obj] in rts:
        tp=DT
        rt2=valida_topico31(purpose,usr,obj,False,tp,index,obj)
        if len(rt2) == 0: return []
        for r in rt2:
          rt.append(r)
        
   return rt   
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_object_by_data2z(obj,uid,parsed):
  if uid != '' and uid != None:
   if Zeus_Mode:
    resultSet=[[uid,tb_object1.get(uid)  ]]
   else: 
    resultSet=[[uid,tb_object31.get(uid) ]]
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    if Zeus_Mode:
     resultSet=tb_object1.get_indexed_slices(clausec)  
    else: 
     resultSet=tb_object31.get_indexed_slices(clausec)  
  #
  obj_nm=None
  #uid=None
  cenar=0
  cnts_all_tps=0
  for key1,results in resultSet:
       obj_nm=results[u'objeto'] 
       #uid=key1
       cenar=results[u'cenar'] 
       cnts_all_tps=results[u'conts_n'] 
       break
  #-----------
  lay=mdNeural.mdLayer ()
  if Zeus_Mode:
   lay.tb=1
  else:
   lay.tb=3
  if obj_nm == None: obj_nm=obj
  lay.name=obj_nm
  tpc2=lay.set_topico('identificador')
  tpc2.uuid=cenar
  nrc2= lay.set_nr(lay.name)
  nrc2.uuid=cenar
  tpc2.connect_to(lay,nrc2,'Composicao') 
  #print lay.topicos,'....................'
  print 'Read object(g1):',obj,' uid:',uid,',cenar:',cenar
  #-----------
  def cached_dt(objectkey,cnt):
    cached=[]
    if Zeus_Mode:
     rg=gt.get_range(objectkey,tb_object_dt1,1,cnt)
     #rg=tb_object_dt1.get_range(key_ini,key_end)
    else: 
     #rg=tb_object_dt31.get_range(key_ini,key_end)
     rg=gt.get_range(objectkey,tb_object_dt31,1,cnt)
    for ky,cols in rg:
      cached.append([ky,cols])
    return cached  
  if True :
      rows=cached_dt(uid,cnts_all_tps) 
      iterat=iter_cd(rows)
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
                                      
                   if parsed:
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrc=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      nr_top.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrc=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       nr_top.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrc=nr
                    ky,results = resultSet.next()
                    if nrc != None:
                      read_dt_level(nrc,(level+1),uid1,ic1,lay1,results,resultSet,uuid)
                   else: 
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
           ic=ky
           cnti=int(results[u'cnt'])
           uuid=ky
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
           if parsed:            
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrTO=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      tps.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrTO=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       tps.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrTO=nr
            
           else: 
            nrTO= lay.set_nr(DT)
            nrTO.uuid=cenar
            tps.connect_to(lay,nrTO,'Composicao') 
           if True:
              #==     
              #
              levs=range(0,50)             
              resultSet1=iterat.get_level(levs)             
              # 
              # 
              ky,results = resultSet1.next()
              while results  :
                   DT=results[u"datach"] 
                   TOP=results[u'topico']
                   ic2=ky
                   lev=results[u'LEV']
                   uuid=ky
                   #print 'Level 2(ind):',lev,TOP,DT
                   if int(results[u'cnt']) <= cnti:
                    ky,results = resultSet1.next()
                    continue
                   
                   if int(lev) != 2:
                     break
                   #==
                   if parsed:
                    
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrc=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      nrTO.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrc=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       nrTO.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrc=nr
                    ky,results = resultSet1.next()
                    if nrc != None:
                      read_dt_level(nrc,(3),uid,ic2,lay,results,resultSet1,cenar)                    
                   else: 
                    nrc= lay.set_nr(DT)
                    nrc.uuid=cenar
                    #print 'Level 2(dt) :',nrc.dt
                    nrTO.connect_to(lay,nrc,'Composicao')                    
                    ky,results = resultSet1.next()
                    results = read_dt_level( nrc,3,uid,ic2,lay,results,resultSet1,cenar ) #####                  
  return lay   
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################  
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def delete_objz(obj,uid):
  if uid != '':
   if Zeus_Mode:
    resultSet=[[uid,tb_object1.get(uid) ]]
   else: 
    resultSet=[[uid,tb_object31.get(uid)  ]]
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    if Zeus_Mode:
     resultSet=tb_object1.get_indexed_slices(clausec)  
    else: 
     resultSet=tb_object31.get_indexed_slices(clausec)  
  #
  obj_nm=None
  uid=None
  cenar=0
  for key1,results in resultSet:
     if Zeus_Mode:
      tb_object1.remove(key1)
     else:
      tb_object31.remove(key1)
     #-----------
     key_ini=objectkey+'|1'
     key_end=objectkey+'|300000'
     if Zeus_Mode:
      rg=gt.get_range(objectkey,tb_object_dt1)
      #rg=tb_object_dt1.get_range(key_ini,key_end)
     else: 
      rg=gt.get_range(objectkey,tb_object_dt31)
      #rg=tb_object_dt31.get_range(key_ini,key_end)
     for ky,cols in rg:
       if Zeus_Mode:
        tb_object_dt1.remove(ky)
       else: 
        tb_object_dt31.remove(ky)
     #===============================  
     cl4 = index.create_index_expression(column_name='obj_orig', value=key1)
     clausec = index.create_index_clause([cl4],count=1000000)
     if Zeus_Mode:
      resultSet=tb_relaction1.get_indexed_slices(clausec)
     else: 
      resultSet=tb_relaction31.get_indexed_slices(clausec)
     for ky,resultsC in resultSet: 
      if Zeus_Mode: 
       tb_relaction1.remove(ky)   
      else: 
       tb_relaction31.remove(ky)   
       
       
 #####################################################################################################
 def subsg(s):
  a= s.split('|')
  if len(a)==1: return s
  rt=''
  l=len(a)
  i=0
  while i< (l-1):
    rt+=a[i]
    i+=1
  return rt 
  
 #####################################################################################################
 #####################################################################################################
 def get_ontology_conditionz(obj1,dt,topicos ): 
  global Zeus_Mode
  if True:
     rts=[]
     collects=[]
     print 'Special get_ontology_condition:',obj1,dt,topicos 
     if obj1 == '$$all$$' or obj1 == '': 
       obj1=None
     if True:
      ps=''
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos]       
      f=False
      ps2=''
      clas=[]
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos] 
      for d in dt:
       cl4 = index.create_index_expression(u'datach', d)
       clas.append(cl4)
      for ds in topicos:
       cl4 = index.create_index_expression(u'topico',ds)
       clas.append(cl4)
      #==============================================================      
      clausec = index.create_index_clause(clas,count=1000000)
      resultSetk=[]
      ant_z=Zeus_Mode
      if Zeus_Mode:
       if obj1 == None:
        resultSetk=tb_object_dt1.get_indexed_slices(clausec)  
       else:
        try:
         resultSetk=[[obj1,tb_object1.get(obj1)]]
        except: 
           resultSetk=tb_object_dt1.get_indexed_slices(clausec) 
       #fnds=False
       #for dk in resultSetk:
       #  fnds=True
       #  break
       #if not fnds :         
       #  resultSetk=tb_object_dt31.get_indexed_slices(clausec)  
       #  for r in resultSetk:
       #    Zeus_Mode=False
       #    break
      else: 
       if obj1 == None:
        resultSetk=tb_object_dt31.get_indexed_slices(clausec)  
       else:
        resultSetk=[[obj1,tb_object31.get(obj1)]]
      #print 'get_ontology_s_p.sql:',sqlc2t
      for ky,cols in resultSetk:
        try:
         obj=cols[u'object']         
        except: 
         try:
          obj=cols[u'objeto']
         except:
          obj=subsg(ky)
        #============
        if obj == None: continue
        if obj not in collects:         
         obj_principal=get_object_by_dataz(obj,obj)        
         obj_principal.get_links('')
         if obj1 != None:
          if obj_principal.name == obj1:
           rts.append(obj_principal)
           collects.append(obj)
         else:
          rts.append(obj_principal)
          collects.append(obj)
  #Zeus_Mode=ant_z
  return rts       
 
 #####################################################################################################
 #####################################################################################################
 ##################################################################################################### 
 
 def get_object_by_dataz(obj,uid):
  if uid != '':
   if Zeus_Mode:
    try:
     resultSet=[[uid,tb_object1.get(uid)]]  
    except: 
     resultSet=[]  
   else: 
    resultSet=[[uid,tb_object31.get(uid)] ]
    
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    if Zeus_Mode:
     resultSet=tb_object1.get_indexed_slices(clausec)  
    else: 
     resultSet=tb_object31.get_indexed_slices(clausec)  
  #
  obj_nm=None
  #uid=None
  cenar=0
  cnts_all_tps=0
  for key1,results in resultSet:
       obj_nm=results[u'objeto'] 
       #uid=key1
       cenar=results[u'cenar']
       cnts_all_tps=results[u'conts_n'] 
       break
  #-----------
  lay=mdNeural.mdLayer ()
  if Zeus_Mode:
   lay.tb=1
  else:
   lay.tb=3  
  if obj_nm == None: obj_nm=obj
  lay.name=obj_nm
  tpc2=lay.set_topico('identificador')
  tpc2.uuid=cenar
  nrc2= lay.set_nr(lay.name)
  nrc2.uuid=cenar
  tpc2.connect_to(lay,nrc2,'Composicao') 
  #print lay.topicos,'....................'
  print 'Read object(g1):',obj,' uid:',uid,',cenar:',cenar
  #-----------
  def cached_dt(objectkey,cnt):
    cached=[]
    if Zeus_Mode:
      rg=gt.get_range(objectkey,tb_object_dt1,1,cnt)
      #rg=tb_object_dt1.get_range(key_ini,key_end)
    else:  
      rg=gt.get_range(objectkey,tb_object_dt31,1,cnt)
      #rg=tb_object_dt31.get_range(key_ini,key_end)
    for ky,cols in rg:
      cached.append([ky,cols])
    return cached  
  if True :
      rows=cached_dt(uid,cnts_all_tps) 
      iterat=iter_cd(rows)
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
           ic=ky
           uuid=ky
           nr= lay.set_nr(DT)
           cnti=int(results[u'cnt'])
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
                   nrc= lay.set_nr(DT)
                   ic2=ky
                   lev=results[u'LEV']
                   uuid=ky
                   nrc.uuid=cenar
                   #print 'Level 2(ind):',lev,TOP,DT
                   if int(results[u'cnt']) <= cnti:
                    ky,results = resultSet1.next()
                    continue
                   
                   if int(lev) != 2:
                     break
                   #==
                   #print 'Level 2(dt) :',nrc.dt
                   nr.connect_to(lay,nrc,'Composicao') 
                   ky,results = resultSet1.next()
                   results = read_dt_level( nrc,3,uid,ic2,lay,results,resultSet1,cenar ) #####                  
  return lay  
 #####################################################################################################
 #####################################################################################################
 ##################################################################################################### 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_ontology_condition_idz(obj,dt,topicos ): 
  if True:
     rts=[]
     collects=[]
     print 'Special get_ontology_condition:',obj,dt,topicos 
     if obj == '$$all$$': 
       obj=None
     if True:
      ps=''
      if type(dt) != type([] ) and type(dt) == type(''):
        dt=[dt] 
      if type(topicos) != type([] ) and type(topicos) == type(''):
        topicos=[topicos]       
      f=False
      ps2=''
      clas=[]
      for d in dt:
       cl4 = index.create_index_expression(column_name=u'datach', value=d)
       clas.append(cl4)
      for ds in topicos:
       cl4 = index.create_index_expression(column_name=u'topico', value=ds)
       clas.append(cl4)
      #==============================================================      
      clausec = index.create_index_clause(clas,count=1000000)
      if Zeus_Mode:
       resultSet=tb_object_dt1.get_indexed_slices(clausec)  
      else: 
       resultSet=tb_object_dt31.get_indexed_slices(clausec)  
      #print 'get_ontology_s_p.sql:',sqlc2t
      for ky,cols in resultSet:
        obj1=cols[u'UID']         
        if obj not in collects:         
         obj_principal=get_object_by_dataz(obj1,obj1)        
         if obj_principal != None:
          if obj1 != None:
           if obj_principal.name == obj:
            rts.append([obj1,obj1])
            collects.append(obj1)
          else:
           rts.append(obj_principal)
           collects.append(obj1)
  return rts 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 class icnt:
   def __init__(self,vl):
      self.valor=vl
   def inc(self):
      self.valor+=1
   def value(self):
      return self.valor     
 def post_object_by_data(layer,cenario,usr,termo,foco,posted_objs,senti,l_p_ant): 
     if layer.name == '' : layer.name ='undef'
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
      if s.uuid > 0 and geral_uuid ==0:
        geral_uuid=s.uuid
        cenario=geral_uuid
        print 'change cenar(geral_uuid):',geral_uuid     
      print 'DT:',s.dt
      fnd_tops=True
      for d in s.sinapses:
       print d.nr.dt
     print '++------------------------------------------'
     
     if not fnd_tops: return
     ky1=nameo #ky1=nameo+' '+str(cenario) 
     nameo=ky1 
     print 'Post-obj:[',nameo,']'
     no_post_o=False
     for [s,st] in posted_objs:
      if s == nameo and st==senti :
         no_post_o=True
     posted_objs.append([nameo,senti])
     #========== 
     #if not no_post_o and len(layer.topicos)>0:
     print 'Insert-OBJ:'
     #==
     print 'Post.Topicos{}:' 
     #==========    ===============================================
     #===============================================     
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
            it={"UID":uid,"topico":tp_Dt,"LEV":str(level),"sin":sn.opcode,"datach":sn_dt.lower(),"id_top":str(id_top),"username":usr,"cnt":str(cnt.value())}
            arr1.append( [ kyl1,it ] )
            cnt.inc()
            #====================================================
            #==========
            post_nr(uid,cnt,arr1,usr,sn.nr,level+1,id_top,True)
       except Exception,e:
        #print 'Error post nr.' ,  e
        log.exception('[Error post nr...]')
     #==========    ===============================================     
     indi=icnt(1)
     arr_post=[]
     for tp in layer.topicos:
      #==========    ===============================================
      print 'Post.nr.num:',indi
      #     
      post_nr(ky1,indi,arr_post,usr,tp)
     #===============================================
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
     def post_alldt(arr):
       #=======================
       b = tb_object_dt.batch(queue_size=len(arr))   
       for k,cols in arr:
        b.insert(str(k),cols) 
       b.send()
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
       colsr={"OBJ_ORIG":ky1,"OBJ_DEST":lnk.lr.name,"OPCODE":lnk.opcode,"USERNAME":usr,"FOCO":foco_o,"FOCO_D":foco_d,"UID":uid};
       #conn.sqlX (sqlc,([ky1,lnk.lr.name+' '+str(cenario),lnk.opcode,usr,foco_o,foco_d,uid]))
       tb_relaction.insert(rky,colsr);       
      except Exception,err: print 'Erro post links:',err
      #===============
      #layer,cenario,usr,termo,foco
      post_object_by_data(lnk.lr,cenario,usr,termo,foco,posted_objs,senti,l_p_ant) 
     #=============== 
     #conn.commit()
 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def post_object_by_dataz(layer,cenario,usr,termo,foco,posted_objs,senti,l_p_ant,Force=False): 
     if layer.name == '' : layer.name ='undef'
     nameo=layer.name
     print 'Post layer:',nameo
     if umisc.trim(nameo) == '' or umisc.trim(nameo) == '\n' :
      if l_p_ant != None:
        nameo=l_p_ant.name
      if umisc.trim(nameo) == '' or umisc.trim(nameo) == '\n' :  
       return
     
     fnd_tops=False
     nameo=umisc.trim(nameo)
     l_p_ant=layer
     geral_uuid=cenario
     print 'POST:LR:',nameo,',cenar(geral_uuid):',geral_uuid
     print '++------------------------------------------'
     for s in layer.topicos:
      if s.uuid > 0 and geral_uuid ==0:
        geral_uuid=s.uuid
        cenario=geral_uuid
        print 'change cenar(geral_uuid):',geral_uuid
      print 'DT:',s.dt      
      fnd_tops=True
      for d in s.sinapses:
       print d.nr.dt
     print '++------------------------------------------'
     
     if not fnd_tops and not Force: return
     ky1=nameo #ky1=nameo+' '+str(cenario) 
     nameo=ky1 
     print 'Post-obj:[',nameo,']'
     no_post_o=False
     for [s,st] in posted_objs:
      if s == nameo and st==senti :
         no_post_o=True
     posted_objs.append([nameo,senti])
     #========== 
     #if not no_post_o and len(layer.topicos)>0:
     print 'Insert-OBJ:'
     #==
     def post_alldt(arr):
       #=======================
       if Zeus_Mode:
        b = tb_object_dt1.batch(queue_size=len(arr))   
       else: 
        b = tb_object_dt31.batch(queue_size=len(arr))   
       for k,cols in arr:
        b.insert(str(k),cols) 
       b.send()
     #=====================
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
            it={"UID":uid,"topico":tp_Dt,"LEV":str(level),"sin":sn.opcode,"datach":sn_dt.lower(),"id_top":str(id_top),"username":usr,"cnt":str(cnt.value())}
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
      print 'Post.nr.num:',indi
      #
      post_nr(ky1,indi,arr_post,usr,tp)
     #===============================================
     print 'Geral.post.layer(Zeus_Mode:',Zeus_Mode,'):',ky1
     if not no_post_o :
      #sql1="insert into SEMANTIC_OBJECT3(username,objeto,cenar,senti) values(?,?,?,?)"
      try:   
       cols={"username":usr,"objeto":ky1,"cenar":str(cenario),"sento":str(senti),"conts_n":str(len(arr_post))}
       if Zeus_Mode:
        tb_object1.insert(ky1,cols)       
       else: 
        tb_object31.insert(ky1,cols)       
       #conn.sqlX (sql1,([usr,nameo,cenario,senti]))
      except Exception,err: print 'Erro ao post(OBJECT):',err
     else: print 'Skip:',nameo,senti
     #=============
     uid=ky1
     #= 
     print 'Post-NRS:'
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
       if lnk.opcode == None: lnk.opcode=''
       rky=lnk.lr.name+'-'+ky1+'-'+lnk.lr.name+'-'+lnk.opcode
       colsr={"obj_orig":ky1,"obj_dest":lnk.lr.name,"opcode":lnk.opcode,"username":usr,"foco":foco_o,"foco_d":foco_d,"uid":uid,"cond":""};
       #conn.sqlX (sqlc,([ky1,lnk.lr.name+' '+str(cenario),lnk.opcode,usr,foco_o,foco_d,uid]))
       if Zeus_Mode:       
        tb_relaction1.insert(rky,colsr)
       else: 
        tb_relaction31.insert(rky,colsr)
        
      except Exception,err: print 'Erro post links:',err
      #===============
      #layer,cenario,usr,termo,foco
      post_object_by_dataz(lnk.lr,cenario,usr,termo,foco,posted_objs,senti,l_p_ant) 
     #=============== 
     #conn.commit()
 #####################################################################################################
 #####################################################################################################
 ##################################################################################################### 
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def valida_topico31_2(purpose,usr,obj,first=True,topico='',index=0,topico_o=0,sinapses_consid1=[]):
   rt=[]
   global Zeus_Mode
   if first: # primeiro topico  
      #print 'start valida.topico:',purpose,index
      ps=purpose[index].lower()    
      #================================================================================  
      if obj == "%" or obj == "":
        obj_dest=None
      else:
        obj_dest=obj
      if True: 
          #===========
          ps2=[]
          if len(ps)> index+1 :
            ps2=[purpose[index+1].lower() ]
            index+=1
          #=========  
          objs1=get_ontology_topic_condition31(obj_dest,ps2,[ps])
          if len(objs1) == 0:
            ant_z=Zeus_Mode
            Zeus_Mode=False
            if obj_dest != None and obj_dest != "":
             obj_r=get_object_by_data2z(obj_dest,obj_dest,False)            
             Zeus_Mode=ant_z            
             for s in sinapses_consid1: # buscar linkados admitidos
              lnks=obj_r.get_links(s)
              for lnk in lnks:
               objs12=get_ontology_topic_condition31(lnk.lr.name,ps2,[ps]) 
               if len(objs12) > 0:
                 objs1=objs12
                 break
          #===========            
      index+=1
      # resultSet -> passaram pela etapa      
      for [ky,tp,dt,lo] in objs1:
        i=ky
        #print 'Start.level:',index
        tp=dt
        rt2c=valida_topico31(purpose,usr,lo,False,tp,index,lo)
        if len(rt2c) > 0 :         
          if lo not in rt:
           rt.append(lo)         
   else: # topico encadeado 
      #print 'start.second.level:',purpose,index 

      #==================== 
      if len(purpose)<=(index):
        return [topico_o]
      ps=purpose[index]
      # 
      rts=get_ontology_topic_condition31(topico_o,[],[topico],index)
      index+=1
      for [ky,TOP,DT,lo] in resultSet:
        tp=DT
        rt2=valida_topico31(purpose,usr,obj,False,tp,index,lo)
        if len(rt2) == 0: return []
        for r in rt2:
          rt.append(r)
        
   return rt   
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 def get_object_by_data2z_cod(obj,uid,parsed):
  if uid != '':
   try:
    resultSet=[[uid,tb_object1.get(uid)  ]]
   except:
    resultSet=[] 
  else:
    cl4 = index.create_index_expression(column_name='objeto', value=obj)
    clausec = index.create_index_clause([cl4],count=1000000)
    resultSet=tb_object1.get_indexed_slices(clausec)  
  #
  obj_nm=None
  #uid=None
  cenar=0
  cnts_all_tps=0
  for key1,results in resultSet:
       obj_nm=results[u'objeto'] 
       #uid=key1
       cenar=results[u'cenar'] 
       cnts_all_tps=results[u'conts_n'] 
       break
  #-----------
  lay=mdNeural.mdLayer ()
  lay.tb=1
  if obj_nm == None: obj_nm=obj
  lay.name=obj_nm
  print 'Read object(g1):',obj,' uid:',uid,',cenar:',cenar
  #-----------
  def cached_dt(objectkey,cnt):
    cached=[]
    rg=gt.get_range(objectkey,tb_object_dt1,1,cnt)
    for ky,cols in rg:
      cached.append([ky,cols])
    return cached  
  if True :
      rows=cached_dt(uid,cnts_all_tps) 
      iterat=iter_cd(rows)
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
                                      
                   if parsed:
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrc=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      nr_top.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrc=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       nr_top.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrc=nr
                    ky,results = resultSet.next()
                    if nrc != None:
                      read_dt_level(nrc,(level+1),uid1,ic1,lay1,results,resultSet,uuid)
                   else: 
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
           ic=ky
           cnti=int(results[u'cnt'])
           uuid=ky
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
           if parsed:            
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrTO=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      tps.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrTO=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       tps.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrTO=nr
            
           else: 
            nrTO= lay.set_nr(DT)
            nrTO.uuid=cenar
            tps.connect_to(lay,nrTO,'Composicao') 
           if True:
              #==     
              # 
              levs=range(0,50)             
              resultSet1=iterat.get_level(levs)             
              # 
              # 
              ky,results = resultSet1.next()
              while results  :
                   DT=results[u"datach"] 
                   TOP=results[u'topico']
                   ic2=ky
                   lev=results[u'LEV']
                   uuid=ky
                   #print 'Level 2(ind):',lev,TOP,DT
                   if int(results[u'cnt']) <= cnti:
                    ky,results = resultSet1.next()
                    continue
                   
                   if int(lev) != 2:
                     break
                   #==
                   if parsed:
                    
                    nrs=[]
                    tmp=''
                    indice_p=0
                    fir=True
                    for d in DT:
                      if d == ',':
                       if fir:
                        nrs.append(tmp)
                        tmp=''
                       else:
                         if DT[indice_p-1] != '\\':
                          nrs.append(tmp)
                          tmp=''          
                         else:tmp+=d
                      else:tmp+=d
                    if tmp != '': nrs.append(tmp) 
                    nrc=None
                    if len(nrs) == 0 :               
                      nr= lay.set_nr(DT)    
                      nrTO.connect_to(lay,nr,'Composicao') 
                      nr.uuid=uuid
                      nrc=nr
                    else:
                      for DT in nrs:
                       nr= lay.set_nr(DT)   
                       nrTO.connect_to(lay,nr,'Composicao') 
                       nr.uuid=uuid
                       nrc=nr
                    ky,results = resultSet1.next()
                    if nrc != None:
                      read_dt_level(nrc,(3),uid,ic2,lay,results,resultSet1,cenar)                    
                   else: 
                    nrc= lay.set_nr(DT)
                    nrc.uuid=cenar
                    #print 'Level 2(dt) :',nrc.dt
                    nrTO.connect_to(lay,nrc,'Composicao')                    
                    ky,results = resultSet1.next()
                    results = read_dt_level( nrc,3,uid,ic2,lay,results,resultSet1,cenar ) #####                  
  return lay 
 ##################################################################################################### 
 ####################################################################################################
 #####################################################################################################
 #####################################################################################################
 #####################################################################################################
 