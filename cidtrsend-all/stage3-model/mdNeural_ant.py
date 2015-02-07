#encoding: latin-1
import umisc
import logging
from StringIO import StringIO
import datetime
import time, datetime

conn=None
conn3=None
conn4=None


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('DYNAMIC-CODE-ENGINE->mdNeural')


self_usr=''

ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 

#===--------------------------------------
def collect_objs_orig( i,usr):
 objs_r=[]
 if True:        
  resultSet = conn.sqlX ("SELECT trim(OBJ_DEST),OPCODE FROM  SEMANTIC_RELACTIONS where OBJ_ORIG = ?  and USERNAME = ?  order by i",([i,usr]))   
  for resultsC in resultSet:
   ido=resultsC[0]
   ido2=resultsC[1]
   objs_r.append([ido,ido2])
 return objs_r 
#===--------------------------------------
def collect_objs_dest( i,usr):
 objs_r=[]
 if True :
  resultSet = conn.sqlX ("SELECT trim(OBJ_ORIG),OPCODE FROM  SEMANTIC_RELACTIONS where OBJ_DEST = ? and USERNAME = ?  order by i ",([i,usr]))   
  for resultsC in resultSet:
   ido=resultsC[0]
   ido2=resultsC[1]
   objs_r.append([ido,ido2])
 return objs_r 
#===--------------------------------------


def collect_links(obj_principal2,i2,usr):
 
 c1=collect_objs_orig(i2,usr)
 #==----------------------------------------
 for c in c1:
  obj_id=c[0]
  opc=c[1]
  obj_k=get_object_by_data(obj_id,usr)
  obj_principal2.set_link(obj_k,opc)
 
 '''
 #==
 c12=collect_objs_dest(i2,usr)
 #==----------------------------------------
 for c in c12:
  obj_id=c[0]
  opc=c[1]
  obj_k=get_object_by_data(obj_id,usr)
  obj_k.set_link(obj_principal2,opc)
 '''



def get_object_by_data2(obj,usr):
 sql='select objeto,i from SEMANTIC_OBJECT3_1_4 where objeto=? and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 if True :
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO) from SEMANTIC_OBJECT_DT3_1_4 where UID = ' + str(uid) )
     obj_nm=None
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          #----
          tps=lay.set_topico(TOP)
          tps.connect_to(lay,nr,'Composicao') 
 return lay 
 
def get_object_by_data29(obj,usr,max_purposes):
 sql='select objeto,i from SEMANTIC_OBJECT3_1_4 where objeto=? and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 if True :
     rattings=0
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO) from SEMANTIC_OBJECT_DT3_1_4 where UID = ' + str(uid) )
     obj_nm=None     
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          #----
          tps=lay.set_topico(TOP)
          tps.connect_to(lay,nr,'Composicao') 
          
          for d in max_purposes:
           if TOP.lower() == d.lower():
             rattings+=1
             break
          
 return [lay,rattings]  
 
def get_object_by_data23(obj,usr):
 sql='select objeto,i from SEMANTIC_OBJECT3_4_1 where objeto=? and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 if True :
     resultSet = conn3.sql ( 'select trim(DT),trim(TOPICO) from SEMANTIC_OBJECT_DT3_4_1 where UID = ' + str(uid) )
     obj_nm=None
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          #----
          tps=lay.set_topico(TOP)
          tps.connect_to(lay,nr,'Composicao') 
 return lay  

def get_object_by_data22(obj,usr,plus):
 
 sql='select objeto,i from SEMANTIC_OBJECT3_1_4 where objeto=? and USERNAME = ? '
 resultSet =conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 plus_fnd=0
 if True :
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO) from SEMANTIC_OBJECT_DT3_1_4 where UID = ' + str(uid) )
     obj_nm=None
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          plusf=False
          for sd in plus:
           if TOP == 'way' and DT == sd:
            plusf=True
          if plusf:
            plus_fnd+=1
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          #----
          tps=lay.set_topico(TOP)
          tps.connect_to(lay,nr,'Composicao') 
 return [lay,plus_fnd]  

 
def get_object_by_data223(obj,usr,plus):
 
 sql='select objeto,i from SEMANTIC_OBJECT3_4_1 where objeto=? and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
 obj_nm=None
 uid=None
 for results in resultSet:
      obj_nm=results[0] 
      uid=results[1] 
      break
 #-----------
 lay=mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 plus_fnd=0
 if True :
     resultSet = conn3.sql ( 'select trim(DT),trim(TOPICO) from SEMANTIC_OBJECT_DT3_1_4 where UID = ' + str(uid) )
     obj_nm=None
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          plusf=False
          for sd in plus:
           if TOP == 'need' and DT == sd:
            plusf=True
          if plusf:
            plus_fnd+=1
          #tps=lay.get_topico(TOP)
          #if tps == None:
          # tps=lay.set_topico(TOP)
          #----
          tps=lay.set_topico(TOP)
          tps.connect_to(lay,nr,'Composicao') 
 return [lay,plus_fnd]
 
 
 
def clear_obj(usr,name ):
 
 
 try:
  conn.sqlX ('delete from SEMANTIC_RELACTIONS3_1_4 where username=? and obj_orig=? ',([usr,name]) )
  #================
  conn.sqlX ('delete from SEMANTIC_OBJECT_DT3_1_4 where username=? and \"UID\"  in ( select I from SEMANTIC_OBJECT3_1_4 where username=? and objeto=? ) ',([usr,name]) )
  #================
  conn.sqlX ('delete from SEMANTIC_OBJECT3_1_4 where username=? and objeto=? ',([usr,name])  )
  #==============
 except Exception,e: 
  print 'Error delete clean_obj_(2):',e 
 
 conn.commit()
 
def post_object_by_data_es(layer,usr): 
 nameo=layer.name
 nameo=umisc.trim(nameo)
 clear_obj(usr,nameo)
 print 'Post LR:',nameo,',len:',len(nameo),', usr:',usr
 sql1="insert into SEMANTIC_OBJECT3_1_4(username,objeto,CENAR,SENTI) values(?,?,0,0)"
 conn.sqlX (sql1,([usr,nameo]))
 for tp in layer.topicos:
  #==========    ===============================================
  def post_nr(usr,tp,level=1):
   tp_Dt=''
   for d in tp.dt:
    tp_Dt+=d
   tp_name=tp_Dt
   for sn in tp.sinapses:
    sn_dt=''
    for s1 in sn.nr.dt:
     sn_dt+=s1
    sql1="insert into SEMANTIC_OBJECT_DT3_1_4(username,object,dt,topico,LEV) values(?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,nameo,tp_Dt,sn_dt,level]))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
    #==========
    post_nr(usr,sn.nr,level+1)
  #==========    ===============================================
  def post_nr2(usr,topdt,new_dt,sin_dt,level):
    sql1="insert into SEMANTIC_OBJECT_DT3_1_4(username,object,dt,topico,LEV) values(?,?,?,?,?)"
    try:
     conn.sqlX (sql1,([usr,topdt,new_dt,sin_dt,level]))
    except:
     print 'Erro ao post:',topdt,new_dt,sin_dt,level
  
  #==========    ===============================================
   
  post_nr(usr,tp)
 
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  SEMANTIC_RELACTIONS3_1_4(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D,\"UID\") values(?,?,?,?,?,?,?)' 
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
  conn.sqlX (sqlc,([nameo,lnk.lr.name,lnk.opcode,usr,foco_o,foco_d,0]))
  #===============
  post_object_by_data_es(lnk.lr,usr)   
 
def get_special_ontology(need,restriction,plus,usr):
 if True:
     rts=[]
     if True:
      ps=''
      ps2=''
      f=False
      for d in need:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
      f=False
      for d in restriction:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
     resultSet = conn.sqlX ("SELECT trim(OBJETO),i,cenar FROM  SEMANTIC_OBJECT3_1_4 where  USERNAME = ? and i in ( select iud from semantic_object_dt3 where topico ='way' and dt in ("+ps+")  ) and i not in ( select iud from semantic_object_dt3 where topico ='restriction' and dt in ("+ps2+")  )    ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        cenar=results[2]
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
        [obj_principal,plus_score_pr]=get_object_by_data22(i,usr,plus)
        #if len(obj_principal.topicos) > 0 :
        rts.append([obj_principal,plus_score_pr])
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
         [obj_k,plus_score]=get_object_by_data22(obj_id,usr,plus)
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
         [obj_k,plus_score]=get_object_by_data22(obj_id,usr,plus)
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
 return rts  

 
def get_special_ontology_w(need,restriction,plus,usr):
 if True:
     rts=[]
     if True:
      ps=''
      ps2=''
      f=False
      for d in need:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
      f=False
      for d in restriction:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
     resultSet = conn.sqlX ("SELECT trim(OBJETO),i,cenar FROM  SEMANTIC_OBJECT3 where  USERNAME = ? and i in ( select iud from semantic_object_dt3 where topico ='need' and dt in ("+ps+")  ) and i not in ( select iud from semantic_object_dt3 where topico ='restriction' and dt in ("+ps2+")  )    ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        cenar=results[2]
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
        [obj_principal,plus_score_pr]=get_object_by_data223(i,usr,plus)
        #if len(obj_principal.topicos) > 0 :
        rts.append([obj_principal,plus_score_pr])
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
         [obj_k,plus_score]=get_object_by_data223(obj_id,usr,plus)
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
         [obj_k,plus_score]=get_object_by_data223(obj_id,usr,plus)
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
 return rts 
 
def get_ontology(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None 
 if True:
     rts=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None:
      ps=''
      f=False
      for d in purposes:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT where  USERNAME = ? and i in ( select iud from semantic_object_dt where topico ='destination' and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT where OBJETO like ?  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        obj_principal=get_object_by_data2(i,usr)
        #if len(obj_principal.topicos) > 0 :
        rts.append(obj_principal)
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
         obj_k=get_object_by_data2(obj_id,usr)
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
         obj_k=get_object_by_data2(obj_id,usr)
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
 return rts  
 
 
 
def get_ontology_s(aliases,purposes,destinats,usr ): #  considera os purposes nos filtros quando alias == None 
 if True:
     rts=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None:
      ps=''
      f=False
      ps2=''
      for d in purposes:
       if f: ps+=','
       ps+="'"+d+"'"
      f=False
      for ds in destinats:
       if f: ps2+=' or '
       ps2+=" topico like '%"+ds+"%' "
       f=True
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT where  USERNAME = ? and i in ( select iud from semantic_object_dt where ("+ps2+") and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT where OBJETO like ?  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  SEMANTIC_RELACTIONS where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        obj_principal=get_object_by_data2(i,usr)
        #if len(obj_principal.topicos) > 0 :
        rts.append(obj_principal)
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
         obj_k=get_object_by_data2(obj_id,usr)
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
         obj_k=get_object_by_data2(obj_id,usr)
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
 return rts   
 
 
 
 
def get_ontology_ponderate(aliases,min_purposes,max_purposes,usr ): # min_purposes=mandatory, max_purposes=max ideal 
 if True:
     rts=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None:
      ps=''
      f=False
      for d in min_purposes:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT3_1_4 where  USERNAME = ? and i in ( select iud from semantic_object_dt where topico ='destination' and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT3_1_4 where OBJETO like ?  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
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
        [obj_principal,ratting]=get_object_by_data29(i,usr,max_purposes)
        #if len(obj_principal.topicos) > 0 :
        rts.append([ratting,obj_principal])
        rts.sort()
        #===
        c1=collect_objs_orig(min_purposes,i,usr)
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
         obj_k=get_object_by_data2(obj_id,usr)
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
        c12=collect_objs_dest(min_purposes,i,usr)
        #==----------------------------------------
        for c in c12:
         obj_id=c[0]
         opc=c[1]
         fco=c[2]
         fcd=c[3]
         obj_k=get_object_by_data2(obj_id,usr)
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
 return rts   
 
 
def get_ontology2(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None 
 if True:
     rts=[]
     alias = aliases
     if alias == None:
      alias='%'
     if aliases == None:
      ps=''
      f=False
      for d in purposes:
       if f: ps+=','
       ps+="'"+d+"'"
       f=True
      resultSet = conn3.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT3 where  USERNAME = ? and i in ( select iud from semantic_object_dt3 where topico ='destination' and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn3.sqlX ("SELECT trim(OBJETO),i FROM  SEMANTIC_OBJECT3 where OBJETO like ?  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
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
        obj_principal=get_object_by_data23(i,usr)
        #if len(obj_principal.topicos) > 0 :
        rts.append(obj_principal)
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
         obj_k=get_object_by_data23(obj_id,usr)
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
         obj_k=get_object_by_data23(obj_id,usr)
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
 return rts  

def post_error(usr):

 sql = ' insert into  status_err ( USERNAME,MSG ) values( ? , ? ) ' 
 serr= lbuffer.getvalue ()   
 now = datetime.datetime.now ()
 dts=str(now) 
 serr=serr.replace('File','') 
 serr=serr.replace('\"/wamp/www/neural/mdNeural.py\",','' )
 serr=serr.replace('exec(code, locals(), locals())','')
 serr=serr.replace('line 112, in run_layout_parser','')
 serr=serr.replace('\"<string>\",','')
 serr='Dt:'+dts+' '+serr
 print '---------------------------------------'
 print serr
 try:
  conn.sqlX (sql,([usr,serr]))
 except Exception,e:
   print 'Erro post err:',e 
 print '---------------------------------------'

class CGlobalStack:
  def __init__(self):
   self.stack=[]
   self.proc_pg=None


GlobalStack=CGlobalStack ()

   
#===================
def get_typ(obj,usr2):
  resultSet =conn.sql ("select TYP from DATA_BEHAVIOUR_PY where OBJETO='"+obj+"' and USERNAME='"+usr2+"' order by i") 
  typ=0
  for results in resultSet:
    typ=results[0]
  return  typ
#=============================================== 

def clean_s_k(strc2):
   k=''
   if (type(strc2).__name__) == 'SapDB_LongReader':
     strc=strc2.read()
   else:  
     strc=''+strc2
   #===  
   for ss in strc:
     if ss.lower () in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','y','w',
                       '0','1','2','3','4','5','6','7','8','9', 
                       '~','`','!','@','#','$','%','^','&','*','(',')','{','}','[',']','\'','"',':',';','/','?','<',',','>','.','\\','|','-','_','=','+',' ','\n']:     
      k+=(ss)
   return k
  

def prepare_search_customlayouts(layer_Start,purposes,dts,usr,relactionate):
 
 #====================================================================================================
 #chamar os codigos 
 codes_Result=[]
 for dt in purposes:
  resultSet = conn.sql ("select CODE from DATA_BEHAVIOUR_CODE_PY where OBJETO='"+dt+"' and USERNAME='"+usr+"' and objeto in (select objeto from DATA_BEHAVIOUR_PY where USERNAME='"+usr+"') order by i") 
  for results in resultSet:
    typ=get_typ(dt,usr)
    o=clean_s_k(results[0])
    code=(o)
    sr_int_cmd_param=dts
    relactional=relactionate
    startL=layer_Start
    usuario=usr
    stack=GlobalStack
    print 'call onto-layout:',dt,'.........................'
    if typ == 1: #executavel
     code+=' \n\nretorno_srt=run(sr_int_cmd_param,relactional,startL,usuario,stack)'
    else: # executa somente o codigo
     pass
    #================================== 
    try:
     exec(code, locals(), locals())
    except Exception,e:
     #print 'Exec Error:',e 
     log.exception( 'Exec Error:' ) 
     post_error(usr)
     print 'Code:\n',code
    if typ == 1: #executavel
     # adicionar ao codes_Result o retorno_srt(lines->[endereco,dados] ) 
     if retorno_srt != None:
      codes_Result.append( retorno_srt )
 #===================
 return codes_Result 

def get_object_by_data(obj,usr): 
 sql='select trim(objeto) from SEMANTIC_OBJECT where \"OBJETO\"=? and USERNAME = ? '
 resultSet =conn3.sqlX (sql,[obj,usr])
 obj_nm=None
 for results in resultSet:
      obj_nm=results[0] 
 #-----------
 lay=mdLayer ()
 if obj_nm == None: obj_nm=obj
 lay.name=obj_nm
 #-----------
 sql='select trim(DT),trim(TOPICO )from SEMANTIC_OBJECT_DT where OBJECT=? and USERNAME = ? '
 resultSet = conn.sqlX (sql,([obj,usr]))
 for results in resultSet:
      DT=results[0] 
      TOP=results[1]
      nr= lay.set_nr(DT)
      #==
      '''
      tps=lay.get_topico(TOP)
      if tps == None:
       tps=lay.set_topico(TOP)
      ''' 
      #==
      tps=lay.set_topico(TOP)
      #==
      tps.connect_to(lay,nr,'Composicao') 
 return lay   
 
def get_object_by_name(aliases,usr): 
 tree_h=[]
 for alias in aliases:
     alia=alias.upper ()
     resultSet = conn3.sqlX ("SELECT trim(OBJETO) FROM  SEMANTIC_OBJECT where upper(OBJETO) = ?  and USERNAME = ?  ",([alia,usr]))
     for results in resultSet:
        i=results[0] 
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(i,usr):
         objs_r=[]
         if True:
          resultSet =conn.sqlX ("SELECT trim(OBJ_DEST),trim(OPCODE) FROM  SEMANTIC_RELACTIONS where OBJ_ORIG = ?  and USERNAME = ? ",([i,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           pr=resultsC[1]
           objs_r.append([ido,pr])
         return objs_r 
        #===--------------------------------------
        def collect_objs_dest(i,usr):
         objs_r=[]
         if True:
          resultSet = conn.sqlX ("SELECT trim(OBJ_ORIG),trim(OPCODE) FROM  SEMANTIC_RELACTIONS where OBJ_DEST = ? and USERNAME = ? ",([i,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           pr=resultsC[1]
           objs_r.append([ido,pr])
         return objs_r 
        #===--------------------------------------
        obj_principal=get_object_by_data(i,usr)
        tree_h.append(obj_principal)
        #===
        c1=collect_objs_orig(i,usr)
        #==----------------------------------------
        for c in c1:
         obj_id=c[0]
         opc=c[1]
         obj_k=get_object_by_data(obj_id,usr)
         obj_principal.set_link(obj_k,opc)
        #==
        c12=collect_objs_dest(i,usr)
        #==----------------------------------------
        for c in c12:
         obj_id=c[0]
         opc=c[1]
         obj_k=get_object_by_data(obj_id,usr)
         obj_k.set_link(obj_principal,opc)  
 return tree_h  


class mdNeuron:
 class mdSinapse:
   def __init__(self):   
    self.lr=None
    self.nr=None
    self.opcode=None
    self.dyn=False
 class mdDynSinapse(mdSinapse):
   def __init__(self):   
    self.dyn=True
 def clone_nr(self,nr):
   nrr=mdNeuron(nr.owner)
   nrr.dt=nr.dt
   for s in nr.sinapses:
    sd=self.mdSinapse ()
    sd.opcode=s.opcode
    sd.lr=s.lr
    sd.nr=self.clone_nr(s.nr)
    nrr.sinapses.append(sd)
   return nrr    
 def compare(self,nr):
  pass
 def get_all(self):
  return self.sinapses
 def __init__(self,_owner):
  self.dt=[]
  self.owner=_owner
  self.sinapses=[]
  self.dynsinap=[]
  self.reactive=True # se marcado com reactive, esta preparado para responder find-path e comparacoes
  self.Mandatory=True
  self.dyn=False
 def connect_to(self,lr,nr,opcode):
  sn=self.mdSinapse ()
  sn.lr=lr
  sn.nr=nr
  sn.opcode=opcode
  have_found=False
  for s in self.sinapses:
   if s.nr == nr:
    have_found=True
    break
  if not have_found:
   self.sinapses.append(sn)
 #==========  
 def connect_to_dyn_c(self,lr,nr,opcode):
  sn=self.mdDynSinapse ()
  sn.lr=lr
  sn.nr=nr
  sn.opcode=opcode
  have_found=False
  for s in self.dynsinap:
   if s.nr == nr:
    have_found=True
    break
  if not have_found:
   self.dynsinap.append(sn)   
 #============  
 def connect_to_dyn(self,lr,nr,opcode):
  sn=self.mdDynSinapse ()
  sn.lr=lr
  sn.nr=nr
  sn.opcode=opcode
  have_found=False
  for s in self.sinapses:
   if s.nr == nr:
    have_found=True
    break
  if not have_found:
   self.sinapses.append(sn)
 #====================================================================

    
 def translate_dts(self,one,two):
   afnd=False
   one=one.clone_nr(one)
   nrr=one
   for d1 in one.dt:
      d2 = two.dt
      if d1.lower()=='$$all$$':
        nrr.dt=d2 
        afnd=True
        break
      
   indc=0
   for sn in one.sinapses:   
    try:   
      for sn2 in two.sinapses:
       one.sinapses[indc].nr=self.translate_dts( sn.nr,sn2.nr )
       break
    except Exception,e:
     print e,':', sn.opcode   
 
   if afnd: 
    print 'From :', one.dt, ',TO:',nrr.dt
    one=nrr
    
   return one 

 
 def mont_return_data(self,ows,foco):
    ow=self
    print 'Mount->foco()',foco 
    if len(foco) == 0 : 
        sn1=None
        for s in ow.dynsinap:
         if s.opcode =='Compare-DYN':
          sn1=s.nr
          print 'Found:DynSinap:',s.opcode,', Ob:',ow.dt
          ow.dynsinap.remove(s)
          #break
          print 'Sn1:',sn1.dt
          return self.translate_dts(ow,sn1)
          #return ow
      
    #=  
    for s in ows:
     fnd=False
     for s2 in foco:
      for dt in s.dt:
       for dt2 in s2.nr.dt:
        if dt.upper () == dt2.upper () or dt2.upper == "$$ALL$$":
          fnd=True
          md1=s
          if  len( s2.nr.sinapses) <= 0 :  # se nao tem verif menor
           ow.connect_to(ow.owner,md1,s2.opcode)
          else: 
           fcs=[]
           for s3 in s2.nr.sinapses:
            fcs.append(s3)
           ow.mont_return_data(ows,fcs)
        break   
     if fnd:
       pass
     else:
       pass
    return ow 
     
class mdLayerLink:
  def __init__(self,lr,opcode,opcode_seg=[]):
    self.opcode=opcode
    self.lr=lr   
    self.opcode_seg=opcode_seg # usado para segundo opcode( ex. relactions(opcode)->determina relacao + tipo-relacao(opcode_Seg) ->define a relacao 
  def getCl(self):
    return self.__class__.__name__  
    
class mdDynamicLayerLink(mdLayerLink):
   def __init__(self,lr,opcode):
    mdLayerLink.__init__(self,lr,opcode)
    self.foco_o=[]   
    self.foco_d=[]

class mdLayer: #mantem a ontologia do conhecimento montada
  def s_compare_dt(self,nr,dt):
      for s in nr.dt:
       if dt.upper () == s.upper():
         return True
      return False   
  def s_post_object_by_data_es(self,layer,usr):
   return post_object_by_data_es(layer,usr)
  def s_get_ontology_s(self,aliases,purposes,destinats,usr):
   return get_ontology_s(aliases,purposes,destinats,usr)
  #== 
  def s_get_ontology_ponderate(self,aliases,min_purposes,max_purposes,usr ):
    return get_ontology_ponderate(aliases,min_purposes,max_purposes,usr )
  #==============================================
  def release_din_sinapse(self):
   def check_syns(n):
    for s in n.sinapses:
     if s.dyn:
      n.sinapses.remove(s)
   #usada p fazer o release das sinapses temporarias por process_inter_find_path
   for s in self.topicos:
    check_syns(s)
   for d in self.dyns:
    check_syns(d)
    self.topicos.remove(d)
    
    
  def release_filter(self):
   self.published=[]
  def add_filter(self,nr):
   self.published.append(nr)
  def do_filter(self,dts):
   def do_filter_ch(nr,dt):
       if len(dts) > 0 :
        tp=dts[0]
        f=False
        passi=[]
        for t in dts:
         if f:
          passi.aapend(t)
         f=True
        #==
        ch=nr.sinapses
        for c in ch:
         if self.s_compare_dt(c.nr,tp) or tp == '$$all$$':
          do_filter_ch(c.nr,passi)
       else:
         nr.owner.published.append(nr)
   if len(dts) > 0 :
    tp=dts[0]
    f=False
    passi=[]
    for t in dts:
     if f:
      passi.aapend(t)
     f=True
    #==
    ch=self.get_all ()
    for c in ch:
     if self.s_compare_dt(c,tp) or tp == '$$all$$':
      do_filter_ch(c,passi)
   
  def _get_ontology(self,aliases,purposes,usr):
   return get_ontology(aliases,purposes,usr)
   
  def compare_nr_Dt(self,dt,nr):
      for s in nr.dt:
       if dt.upper () == s.upper():
         return True
      return False          
  
  def get_all_f(self):
   rts_f=[]
   nrs_d_cmp=self.topicos
   for spr in nrs_d_cmp:
      if self.compare_nr_Dt( 'interface-res' ,  spr ) :
       for d in spr.sinapses:
          rts_f.append(spr)
   #====================================
   return rts_f 
    
  def get_all_no_interface(self):
   #===
   apub=[]
   apubs=[]
   ind_cmp=0
   nrs_d_cmp=self.topicos
   for spr in nrs_d_cmp:
      if self.compare_nr_Dt( 'interface' ,  spr ) or self.compare_nr_Dt( 'interface-res' ,  spr ) :
        for snc in spr.sinapses:
         for d in snc.nr.dt:
          apub.append(d)
   if len(apub) > 0 :
    for s in self.topicos:
      if self.s2_compare_dt(s,apub):
        apubs.append(s)      
   #===
   if len(apubs) > 0 :
    aret=[]
    for s in self.topicos:
     fnds=False
     for d in apubs:
      if s == d:
        fnds=True
     if not fnds :
       aret.append(s)
    return aret       
   return []
  
  def get_all(self):   
   areturn=[]
   #===
   apub=[]
   nrs_d_cmp=self.topicos
   ind_cmp=0
   for spr in nrs_d_cmp:
      if self.compare_nr_Dt( 'interface' ,  spr ) :
        for snc in spr.sinapses:
         for d in snc.nr.dt:
          apub.append(d)
   if len(apub) > 0 :
    for s in self.topicos:
      if self.s2_compare_dt(s,apub):
        self.published.append(s)      
   #===
   if len(self.published)>0:
     areturn = self.published
   elif len(self.topicos)>0:
     areturn = self.topicos   
   else:
     areturn = self.nrs
     
   sins=[]
   for s in areturn:
    f=False
    for d in s.dt:
     if d=='tstatic':
      f=True
    if not f:
     sins.append(s)   
   return sins
   
  
  def put_publish(self,n):
   fnd=False
   for d in self.published:
    if n == d:
      fnd=True
   if not fnd:
    self.published.append(topico)   
  
  def set_foco(self,foco):
    for fc in foco:
     for n in self.topicos:
      for dt in n.dt:
       for f in fc.dt:
        if f.upper () == dt.upper():
         self.put_publish(n)      
  def __init__(self):
    self.nrs=[]
    self.topicos=[]
    self.name=''
    self.published=[]
    self.links=[]
    self.cache=[]   
    self.dyns=[]
  #== 
  def update_links(self):
   collect_links(self,self.name,self_usr)
  #== 
  def get_links_nm(self,opcode,dst):
   rts=[]
   if len(self.links   ) == 0 :
    update_links()
   for s in self.links:
    if s.opcode.upper () == opcode.upper () or opcode=='':
     fnd=False
     #----------------------
     parcial_foco=[]
     if la.getCl () == 'mdDynamicLayerLink':
       parcial_foco=la.foco_d 
     for d1 in dst:
      ifnd=False
      for p in parcial_foco:
       for d in dst.dt:
        for pd in p.dt:
         if d.upper () == pd.upper():
           ifnd=True
      if not fnd:
       for p in parcial_foco:
        d=la.name
        for pd in p.dt:
         if d.upper () == pd.upper():
           ifnd=True
     if len(parcial_foco) ==0:
       fnd=True
     elif ifnd:
       fnd=True     
     #----------------------
     if fnd:
      rts.append(s)
   return rts
  def get_links(self,opcode):
   rts=[]
   if len(self.links   ) == 0 :
    self.update_links()
   for s in self.links:
    if s.opcode.upper () == opcode.upper () or opcode=='':
     rts.append(s)
   return rts
  def get_links_o2(self,opcodes,nrfoco):
   rts=[]
   if len(self.links   ) == 0 :
    self.update_links()
   for opcode in opcodes:
    [link,topico,sinret]=opcode
    for s in self.links:
     fnd=False
     if s.opcode.upper () == link.upper () or link=='':
      tps=None
      if nrfoco != None:
       tps=nrfoco.owner.get_topico(topico)
      for o in s.foco_o:
       if (o == nrfoco or nrfoco == None) or tps == o:
         fnd=True
     if fnd: 
      opcodes.pop ()
      rts2=get_links_o2(opcodes,None) 
      if len(rts2 ) > 0 :
       for rt1 in rts2:
         rts.append(rt1)
      else:
       rts.append(s)
   return rts
  def get_links_o(self,opcode,foco,sin=None):
   rts=[]
   if len(self.links   ) == 0 :
    self.update_links()
   for s in self.links:
    fnd=False
    if s.opcode.upper () == opcode.upper () or opcode=='':
     for o in s.foco_o:
      if o == foco:
       kfnd=True
       if sin != None: 
         kfnd=False
         for sins_s in o.sinapses:
          if sins_s.opcode.upper () == sin.upper () :
            fnd=True
       if kfnd:
        fnd=True
    if fnd: 
     rts.append(s)
   return rts
  def set_link(self,lr,opcode):
    mc=mdLayerLink(lr,opcode)
    self.links.append(mc)
  def set_link_ds(self,lr,opcode,foco_o,foco_d):
    mc=mdDynamicLayerLink(lr,opcode)
    mc.foco_o=foco_o
    mc.foco_d=foco_d
    self.links.append(mc)
  def set_link_d(self,d):
    self.links.append(d)
  def get_topico(self,dt):
    for n in self.topicos:
     for d in n.dt:
       if d.upper () == dt.upper():
         return n
    return None
  def get_last_topico(self,dt):
    n2=None
    for n in self.topicos:
     for d in n.dt:
       if d.upper () == dt.upper():
         n2=n
    return n2
  def set_topico_a(self,dts):
    if len(dts) > 0 :
     nr=mdNeuron(self)
     nr.dt.append(dts[0])
     self.topicos.append(nr)
     top= self.topicos[len(self.topicos)-1]
     f=True
     for ds in dts:
      if not f:
        top=self.set_nr_ch(top,ds,'Composicao')
      f=False
    return None 
  def set_topico(self,dt):
    nr=mdNeuron(self)
    nr.dt.append(dt)
    self.topicos.append(nr)
    return self.topicos[len(self.topicos)-1]
  def set_topico_a(self,dt):
    nr=mdNeuron(self)
    nr.dt=(dt)
    self.topicos.append(nr)
    return self.topicos[len(self.topicos)-1]
  def set_topico_nr(self,nr):
    fnd=False
    foco=None
    for s in self.topicos:
     if nr == s:
      fnd=True
      foco = s
      break
    if not fnd:  
     self.topicos.append(nr)
     return self.topicos[len(self.topicos)-1]
    else:
     return foco    
  def set_topico_nr_fir(self,nr):
    self.topicos.insert(0,nr)
    return self.topicos[len(self.topicos)-1]
  def set_nr_ch(self,top,dt,opcode):
    nr=mdNeuron(self)
    nr.dt.append(dt)
    top.connect_to(self,nr,opcode)
    return nr
  def set_nr_ch_a(self,top,dt,opcode):
    nr=mdNeuron(self)
    nr.dt=(dt)
    top.connect_to(self,nr,opcode)
    return nr
  def set_nr(self,dt):
    nr=mdNeuron(self)
    nr.dt.append(dt)
    self.nrs.append(nr)
    return self.nrs[len(self.nrs)-1]
  def set_nr_nr(self,nr):
    self.nrs.append(nr)
    return self.nrs[len(self.nrs)-1]
    
  def compare_dt(self,nr1,nr2):
   for d1 in nr1.dt:
    for d2 in nr2.dt:
      if d1.upper () ==  d2.upper():
        return True
   #=======================================
   for sn in nr1.sinapses:   
    try:   
     if sn.opcode.upper () in ['MEAN'] :
      for sn2 in nr2.sinapses:
       if sn2.opcode.upper () in ['MEAN'] :
        if self.compare_dt(sn.nr,sne.nr) :
         return True
    except Exception,e:
     print e,':', sn.opcode   
   return False     
  
  def get_all_it(self,nm,usr):
     objc2=get_object_by_name([nm],usr)
     if objc2 == None: return []
     for objc in objc2:
      krt= objc.topicos
      if len(krt) > 0: return krt
     return []
     
  def expand_cache(self,dt):  
   def parse(dt):
    rt=[]
    tmp=''
    for s in dt:
      if s==' ' or s == ',' or s == ')' or s == '(' or s==';' or s == '{' or s == '}':
       rt.append(tmp)
       tmp=''
      else: tmp+=s
    if tmp!='': rt.append(tmp)
    return rt
   #========================    
   fnd=False
   for [sld,itens] in self.cache:
     if sld == dt:
      return itens
   dt=umisc.trim(dt)
   if dt.find(' ') > -1 :
    new_d=parse(dt)
    self.cache.append([dt,new_d])
    return new_d
      
   return []
   
  def compare_dt_depend1(self,usr,purpose,nr1,nr2,consider_items=[],debug=False):
   afnd=False
   for d1 in nr1.dt:
    for d2 in nr2.dt:
      expand=self.expand_cache(d2)
      if len(expand) > 0 :
       #print 'Compare:',d1.upper(),' with:',expand 
       if d1.upper () ==  d2.upper () or d1.lower()=='$$all$$' or self.compare_data_h(d1,d2) :
        afnd=True
        break
       for ex in expand:
         if d1.upper () ==  ex.upper () or d1.lower()=='$$all$$':
           afnd=True
           break
       if afnd: break
      elif d1.upper () ==  d2.upper () or d1.lower()=='$$all$$':
        #print d1.upper(),d2.upper(),len(nr1.sinapses),'....................................................................'
        afnd= True   
        break   
   return afnd
   
  def compare_Date_del(self,t_format,dt):
    #timestring = "2005-09-01 12:30:09"
    #time_format = "%Y-%m-%d %H:%M:%S"
    #datetime.datetime.fromtimestamp(time.mktime(time.strptime(mytime, time_format)))
    rt=False
    try:
     r=datetime.datetime.fromtimestamp(time.mktime(time.strptime(dt, t_format)))
     return True
    except:
     pass
    return False
  
   
  def compare_data_h(self,dt1,dt2):
   d1=dt1
   d2=dt2
   if d1.lower() == '#month':
     if d2.lower() in ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']:
       return True
   #===================
   if d1.lower() == '#day':
    try:
     if int(d2) in  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,28,30,31]:
       return True     
    except: 
      pass
   #==   
   if d1.lower() == '#year':
    try:
      if int(d2) > 0 :
        return True
    except Exception,e:
     #print 'Err:Year:',e
     pass     
   #=========================  
   if d1.lower() == '#time':
    try:
      #def compare_Date_del(self,t_format,dt):
      #  timestring = "2005-09-01 12:30:09"
      #  time_format = "%Y-%m-%d %H:%M:%S"
      if self.compare_Date_del('%H:%M:%S',d2) :
        return True
    except:
     pass
   #=========================  
   if d1.lower() == '#date':
    try:
      #def compare_Date_del(self,t_format,dt):
      #  timestring = "2005-09-01 12:30:09"
      #  time_format = "%Y-%m-%d %H:%M:%S"
      if self.compare_Date_del('%Y-%m-%d',d2) :
        return True
    except:
     pass
   if d1.lower() == '#datetime':
    try:
      #def compare_Date_del(self,t_format,dt):
      #  timestring = "2005-09-01 12:30:09"
      #  time_format = "%Y-%m-%d %H:%M:%S"
      if self.compare_Date_del('%Y-%m-%d %H:%M:%S',d2) :
        return True
    except:
     pass
    #======================================= 
    return False  
   
  def compare_dt_depend(self,usr,purpose,nr1,nr2,consider_items=[],debug=False):
   afnd=False
   for d1 in nr1.dt:
    for d2 in nr2.dt:
      expand=self.expand_cache(d2)
      if len(expand) > 0 :
       #print 'Compare:',d1.upper(),' with:',expand 
       if d1.upper () ==  d2.upper () or d1.lower()=='$$all$$'  or self.compare_data_h(d1,d2) :
        afnd=True
        break
       for ex in expand:
         if d1.upper () ==  ex.upper () or d1.lower()=='$$all$$':
           afnd=True
           break
       if afnd: break
      elif d1.upper () ==  d2.upper () or d1.lower()=='$$all$$':
        #print d1.upper(),d2.upper(),len(nr1.sinapses),'....................................................................'
        afnd= True   
        break
   
   
   have_sn_app=True
   have_sn_app_allw=False
   #== 
   for sn in nr1.sinapses:   
    try:   
     if sn.opcode.upper () in ['MEAN'] :
      for sn2 in nr2.sinapses:
       if sn2.opcode.upper () in ['MEAN'] :
        if self.compare_dt(sn.nr,sne.nr) :
         return True
     else:
      for sn2 in nr2.sinapses:
       #if afnd:
       #  print 'Now-compare:',sn.nr.dt,sn2.nr.dt,len(sn.nr.sinapses),len(sn2.nr.sinapses)
       rt_sf=self.compare_dt_depend(usr,purpose,sn.nr,sn2.nr,consider_items,True)
       if len(sn.nr.sinapses)==0: # se nao tem mais sinapses filhas, considerar modalidade 'or'
         if rt_sf:
           have_sn_app_allw=True
       if not rt_sf :
         have_sn_app=False
       if have_sn_app_allw:
        have_sn_app=True
       #if afnd:
       #  print 'Now-compared:',sn.nr.dt,sn2.nr.dt,len(sn.nr.sinapses),len(sn2.nr.sinapses),' result:',have_sn_app
         
     #=================     
    except Exception,e:
     print e,':', sn.opcode   
   #===
   #if afnd:
   # print 'All-cmp:',have_sn_app,afnd
   
   if have_sn_app and afnd: 
    return True
   #===
   return False     
   
   
  def compare_sub_dt(self,nr1,nr2):
   def compare_dt_s(self,nr1,nr2):
    for d1 in nr1.dt:
     for d2 in nr2.dt:
       if d1.upper () ==  d2.upper():
         return True
    for sn in nr1.sinapses:    
      for sn2 in nr2.sinapses:
        if self.compare_dt_s(sn.nr,sne.nr) :
         return True
    return False
   #=============================      
   for sn in nr1.sinapses:    
     for sn2 in nr2.sinapses:
       if self.compare_dt_s(sn.nr,sne.nr) :
        return True
   return False     

  def s2_compare_dt(nr,dt):
      for s in nr.dt:
       if dt.upper () == s.upper():
         return True
      return False          
   
  def get_find_path(self,layer,dt,usr,purpose,owner): #   
   def parse(dt):
    rt=[]
    tmp=''
    for s in dt:
      if s==' ' or s == ',' or s == ')' or s == '(' or s==';' or s == '{' or s == '}':
       rt.append(tmp)
       tmp=''
      else: tmp+=s
    if tmp!='': rt.append(tmp)
    return rt
   #========================    
   #  
   print 'Get find-path for :',layer.name,'[',dt,']',' Owner:',owner.name
   #==
   layer.release_filter ()   
   nrs=layer.get_all ()
   if True:
    '''  em cada dt=[a,b,c,...] é um nome de um fact, onde vai ter os topicos implementados. nesses, procurar object->object implementador ou no cenario.objects.find-path=>nome dos objetos pelo apelido passado, ou cenario.objects.find-paths.defs -> definicoes direto no cenario  '''
    all_dt=parse(dt)  
    print 'FdPath:',dt,all_dt
    facts_defs=[]
    lnks=owner.get_links('FACT')
    #print 'lnks:', len(lnks)
    search=[]
    for ln in lnks:
     for al in all_dt:
      if ln.lr.name == al:
        tps_node=ln.lr.get_all()
        impl=False 
        for tp_a in nrs:
         for ps in tps_node: 
          if self.compare_dt_depend1(usr,purpose,ps,tp_a,[]) :
           for s in ps.sinapses:
            for d in s.nr.dt:
             search.append( [tp_a,d] )
           break
        #====
     
    if len(search) > 0 :
     print 'find-path search:',search
     for [topico,d] in search:  
       lrs=get_ontology(d,purpose,usr)
       if len(lrs) == 0: 
        # procurar no cenario na lista de objects de conhecimentos previos e globais
        for sclient in GlobalStack.stack:     
          #print 'cmp.fdp:',sclient.assinat.lower(),d.lower()        
          if sclient.assinat.lower()==d.lower(): # 
           for cen in sclient.cenarios:
            for defs in cen.defs_findp:
             #print 'cmp.fdp.run:',topico.dt,defs[0]       
             if self.s_compare_dt(topico,defs[0]) : # compara a implementacao    
                nrk=topico.owner.set_nr(defs[1])
                topico.connect_to(topico.owner,nrk,'Composicao') # linka ao resultado            
        #==        
        continue
        #==        
       fpaths=[]
       rts=[]
       for lr in lrs:
         fpaths=lr.get_all ()
         f_integra=False
         for f in fpaths:
          if self.s_compare_dt(f,'f-sub'):#substituto, remove o topico anterior
           f_integra=True
         rts=fpaths  
         #=============
         for t in rts:
           if self.s_compare_dt(t,'composicao') or self.s_compare_dt(t,'definicao') or self.s_compare_dt(t,'composition') or self.s_compare_dt(t,'definition'):
            for k in t.sinapses:
             if not f_integra:
              topico.connect_to(topico.owner,k.nr,'Composicao')
             else: 
              layer.add_filter(k.nr) # foca apenas os substitutos
             
  
  def process_Call_RCT(self,data_c,ontology,usr,purpose,relactionate):
  
   nodes=self.get_links('CALL')
   for node_R in nodes:
     node=node_R.lr
     dests=[]
     #========
     nds=node.get_all ()
     generics=[]
     to_gen=False
     for n1 in nds:
      if self.s_compare_dt(n1,'destination'): 
        for d in n1.sinapses:
         if self.s_compare_dt(n1,'generic'):
          to_gen=True
         elif to_gen:
          for ds in d.dt:
           generics.append(ds)           
      
     if not to_gen:
      #print 'Identify RCT:',node.name
      node.process_RCT(data_c,ontology,usr,purpose,relactionate )
     else:
      # generic é um objeto que simboliza a chamada de outros, descrevendo em seus destinations os dests a serem procurads em rcts nao likadas, mas q implementem essas destinations    
      rcts=get_ontology(None,generics,usr)
      for r in rcts:
        r.process_RCT(data_c,ontology,usr,purpose,relactionate )    
   
  def es_compare_dt(self,nr,dt):
      for s in nr.dt:
       if dt.upper () == s.upper():
         return True
      return False          
    
  def compare_objs(self,identif,dest,foco,usr,purpose):
   def set_foco(lr,foco):
    for s in foco:
     for n in lr.topicos:
      if self.compare_nr_Dt(s,n):
       lr.published.append(n)
     for n in lr.nrs:
      if self.compare_nr_Dt(s,n):
       lr.published.append(n)
   rt=[]
   rt1=[]
   rt2=[]
   for id in identif:
    obj=get_ontology2(id,purpose,usr)
    for des in dest:
     obj2=get_ontology2(des,purpose,usr)
     if len(obj) > 0  and len(obj2) > 0 :
      if len(foco) > 0:
       set_foco(obj[0],foco)
       set_foco(obj2[0],foco)
      #
      [r,r2]=obj[0].process_raw_RCT(obj2,ontology,usr,purpose)
      if r!= None :
        for c in r.topicos:
         rt1.append(c)
        for c in r2.topicos:
         rt2.append(c)
      #=============
   if len(rt1) or len(rt2):
    rt=[rt1,rt2]
   return rt
  
  def process_behavior(self,identif,referencia, action,purpose,usr):
   changes=[]
   for id in identif:
     obs=get_ontology2(id,purpose,usr)
     for ob in obs:
      lr_atu=ob
      #
      if len(referencia) > 0 : # foco
       ob.set_foco(referencia)
      changes.append([id,[]])
      # changes = [ id-layer [ [refencia,referencia], [  math=[dt,dt,dt,dt,dt,dt],nomath=[dt,dt,dt,dt,dt]  ]  ]  # referencia -> ex.tempo,distancia.etc.. referncial q organiza o historico
      # actions
      # caracts -> get_all ()      
      eventos=ob.get_links('history') # facts de historico ( caracts,actions )
      for ev in eventos:
       nds=ev.lr.get_all ()   
       #
       # destinatio of evento indicate purpose of link(indica o refenrecial do historio-ex.tempo,distancia,.... ) 
       tps=ev.get_topico('destination')
       refer=[]
       for r in tps:
        for s in r.sinapses:
         for d in s.nr.dt:
          refer.append(d)
       #       
       [rtmath,rtnomath]=nr_atu.process_raw_RCT(nds)
       retmath=[] # considerar os math actions, pois influem em behavior fact
       for tr in rtmath: 
        if self.s_compare_dt(tr,'action'):
         retmath.append(tr)
       for tr in rtnomath: 
        if self.s_compare_dt(tr,'action'):
         retmath.append(tr)
       itc=changes[ len(changes)-1 ]       
       itc[1].append( [  refer  , [rtmath,rtnomath,retmath] ])
       nr_atu=nds
   #
   rt=[]
   for it in changes:
    lr=mdLayer ()
    nm=it[0]
    m=lr.set_topico('math')
    #==
    iden=lr.set_topico('identificador')
    lr.set_nr_ch(iden,nm,'Composicao')
    #==
    n=lr.set_topico('no-math')
    a=lr.set_topico('action')
    rt.append([math,nomath,a])
    for tps in it[1]:
     refer=tps[0]
     [math,nomath,act]=tps[1]
     for r in refer:
       lr.set_nr_ch(n,r,'referencia')
       lr.set_nr_ch(m,r,'referencia')
       lr.set_nr_ch(a,r,'referencia')
     #==========================================
     for ma in math:
      lr.set_nr_ch(m,ma,'Composicao')
     for nma in nomath:
      lr.set_nr_ch(n,nma,'Composicao')
     for a in act:
      lr.set_nr_ch(n,a,'Composicao')
   # rt=> neuron identify + match-nomath topico mas childs de cada um   
   return rt  
 
    
   
  def process_inter_find_path(self,opcode_condition):
   # processar os find-path por linklayer
   nodes=self.get_links('find-path')
   for n in nodes:
    foco_o= n.foco_o
    foco_d= n.foco_d
    opcode=n.opcode_seg
    #==========
    foco_origem=[]
    foco_destino=[]
    #==============
    #opcode = purpose
    #==============
    ps=False
    if opcode_condition == opcode or opcode_condition == "$$all$$" or opcode == "$$all$$":
     # $$all$$-> incondicional
     ps=True
    
    if not ps : return
    
    just_foco=False
    foco_inc=False
    if opcode == 'just-foco':
     just_foco=True
    elif opcode == 'foco-inc':
     foco_inc=True
    #=========================================================================================================================    
    foco_orig=False
    s1=n.get_all()    
    if len(foco_o) == 0 : # se nao tem foco obrigatorio, verificacao=True
     foco_orig=True
    #=================  
    ifound=0
    for s_c2 in foco_o:
     for s_c in s1:
      if self.compare_dt_depend1(s_c,s_c1) :
       ifound+=1
       foco_origem.append(s_c)
       break
    if ifound >=  len(s_c2):
     foco_orig=True
    #=========================================================================================================================    
    foco_dest=False
    s2=self.get_all()    
    if len(foco_d) == 0 : # se nao tem foco obrigatorio, verificacao=True
     foco_dest=True
    #=================  
    ifound=0
    for s_c2 in foco_o:
     for s_c in s2:
      if self.compare_dt_depend1(s_c,s_c1) :
       ifound+=1
       foco_destino.append(s_c)
       break
    if ifound >=  len(s_c2):
     foco_dest=True
     
    if foco_orig and foco_dest:
        # se obedecidos os focos, analisar os opcodes:
        if  len(foco_destino) > 0 :
          # coletar informacoes de cada foco, complementando o foco dest
          for d in foco_destino:  
           if len(foco_origem) > 0 :          
            for o in foco_origem:
             for s in o.sinapses:
              d.connect_to_dyn(d.owner,s.nr,'Composicao')           
           else:
            ak=n.get_all()
            for a in ak:
             d.connect_to_dyn(d.owner,a,'Composicao')           
           
        else:
          ak=n.get_all()
          for a in ak:
           fs1=False
           for o in foco_origem:
            if o==ak: 
             fs1=True
             break
           if not fs1:
            self.dyns.append(a)
            self.set_topico_nr(a)
                   
     
    
  def process_RCT(self,layers,ontology,usr,purpose,relactionate=False):        
    # ractionline
    # verbos a serem processados
    #  compare(with need/way/mean)
    #  behaviour(with need/way/mean)
    #  aderencia
    #  afinidade
    #  inferencia preditiva(causa-efeito)
    #  inferencia reativa( acao-reacao)    
    #  --------  detectar need/mean/way automatico
    
    #obs: get_find_path -> opera nas implementacoes de rct
    #     process_inter_find_path -> opera em objectos, tanto nas rct quanto no paremetro de input "layers", a cada chamada do get_all()
    '''
      formato:
       topico->findpath para cada fact
       links-layer -> cada fact
    '''   
    print 'Start Call RCT:',self.name  
    layers_collect=[]    
    rtp=mdLayer ()
    nore=mdLayer ()
    filtered=[]
    dyned=[]
    nodes=self.get_links('FACT')
    print 'RCT->facts(',self.name,'):'
    for ns in nodes:
      print '[',ns.lr.name,']'
    topicos_fpath=self.topicos
    idcx=0
    for node in nodes:
     node=node.lr
     
     for fpt in topicos_fpath:
      for dtsc in  fpt.dt:
       if node.name.upper () == dtsc.upper():
        dts_fnd=[]
        for sns in fpt.sinapses:
         for dtsn in sns.nr.dt:
           dts_fnd.append(dtsn)
        for dts_fnd1 in dts_fnd:
         #==                dt,usr,purpose
         '''
         'vb_preditiva' # find-path para consideracoes 
         'vb_reactive'  # find-path para consideracoes 
         '''
         self.get_find_path(node,dts_fnd1,usr,purpose,self)#[topico,sinapse,link], retorna os definidores de find-path direto do banco
         node.process_inter_find_path(dts_fnd1)
         #get_all -> 
         
     #=========
     node.process_inter_find_path(purpose)
     dyned.append(node)
     nds=node.get_all ()
     foco=node.get_all_f ()
     print 'NDS:======','[',node.name,']'
     for n1 in nds:
      print '---------'
      print n1.dt
      for snd1 in n1.sinapses:
       print '+++++++++++++++++++++++++++++++++++++'
       print snd1.nr.dt
       print '++++++++++++++++++++++++++++++++++++++'
      print '---------'
     print '=========='
     nds2=self.get_all_it(node.name,usr)
     #==========  
     need_s=0
     for n1 in nds:
      if self.s_compare_dt(n1,'source') or self.s_compare_dt(n1,'destination'): 
       pass
      else: 
       need_s+=1 
     #==========    
     tps_len=0
     '''
       ==================================================
       ==================================================
     '''
     
     print 'All-L:',layers
     for l in layers:
      #get_all() -> l.process_inter_find_path()
      print 'L:',l
      dyned.append(l)
      l.process_inter_find_path(purpose)
      nds2=l.get_all ()
      print 'NDS2:======'
      for n1 in nds2:
       print '----------'
       print n1.dt
       for snds in n1.sinapses:
        print '++++++++++++++'
        print snds.nr.dt
        print '++++++++++++++'
       print '----------'
      print '==========='
      tps_len=0
      rt=mdLayer ()
      verbo='vbNoDef'
      verbo_compl=[] # dados complementares do filtro
      for nr_atu in nds:
        if self.s_compare_dt(nr_atu,'compare'):
         verbo='vb_compare'
        if self.s_compare_dt(nr_atu,'behavior'):
         verbo='vb_behavior'
        if self.s_compare_dt(nr_atu,'aderencia'):
         verbo='vb_aderencia'
        if self.s_compare_dt(nr_atu,'afininity'):
         verbo='vb_afininity'
        if self.s_compare_dt(nr_atu,'preditive'):
         verbo='vb_preditiva'
        if self.s_compare_dt(nr_atu,'reactive'):
         verbo='vb_reactive'
        if self.s_compare_dt(nr_atu,'link'):
         verbo='vb_link'
        if self.s_compare_dt(nr_atu,'link-nr'):
         verbo='vb_link_nr'
        if self.s_compare_dt(nr_atu,'filter'):
         verbo='vb_filter'
        if self.s_compare_dt(nr_atu,'collect'):
         verbo='vb_collect'
        if self.s_compare_dt(nr_atu,'collect_apr'):
         verbo='vb_collect_apr'
        if verbo !=  'vbNoDef':
         for s in nr_atu.sinapses:
          for ds in s.nr.dt:
           verbo_compl.append(ds)
           
        if verbo=='vb_compare':
         print 'Run.(',verbo,')'
         # achar identificador
         # achar dest
         # gerar comparativo
         # anotar igualdades
         # anotar diferencas
         for nr_t in nds2:
          identif=[]
          dest=[]
          foco=[]
          if self.s_compare_dt(nr_t,'identificador'):
           for s in nr_t.sinapses:
            for d in s.nr.dt:
             identif.append(d)
          if self.s_compare_dt(nr_t,'dest'):
           for s in nr_t.sinapses:
            for d in s.nr.dt:
             dest.append(d)
          if self.s_compare_dt(nr_t,'foco'):
           for s in nr_t.sinapses:
            for d in s.nr.dt:
             foco.append(d)
          if len(identif) > 0  and len(dest) > 0 :
           [tfound,tnotfound]=self.compare_objs(identif,dest,foco,usr,purpose)
           if len(tfound) > 0 :
            tps=rt.set_topico('found')
            for r in tfound:
                nr= rt.set_nr(DT)
                tps.connect_to(rt,nr,'Composicao') 
           if len(tnotfound) > 0 :
            tps=rt.set_topico('not-found')
            for r in tnotfound:
                nr= rt.set_nr(DT)
                tps.connect_to(rt,nr,'Composicao') 
           if len(tfound) > 0 or len(tnotfound) > 0 :
            nds2=[]
            fnd_comp=True
            tps_len+=1 
        if verbo=='vb_aderencia': # need->way , caracts-need-entidade=>caracts-way-fornecidas
          # 
          print 'Run.(',verbo,')'
          identif=[] # objects com needs, par linkar candidatos a way
          need=[]
          restrict=[]
          plus=[]  
          for nr_t in nds2:          
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'need'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 need.append(d)
              if self.s_compare_dt(nr_t,'restriction'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 restrict.append(d)
              if self.s_compare_dt(nr_t,'need-plus'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 plus.append(d)
          if len(identif) > 0  and len(need) > 0 :
            # get ontology topico need->way, poderar a mais dadaptada a tds os need+restrictions+need-plus
            objs=get_special_ontology(need,restriction,plus)
            idx=[]
            objs_ret=[]
            for [obj,score_p] in objs:
             # achar os best score, adicionar como primeiros, em layoutcode com maximo e minimo numero de pesquisas, os mais graduados(adaptados) vencem
             fnd=False
             for ds in idx:
              if ds == score_p:
               fnd=True
             if not fnd:
              idx.append(score_p)
             #
            idx.sort ()
            for i in idx:
             for [obj,score_p] in objs: 
              if score_p == i:
               objs_ret.append(obj)
             
            if len(objs_ret) > 0:                  
             tps=rt.set_topico('best')
             for oret in objs_ret:
                    nr= rt.set_nr(oret)
                    tps.connect_to(rt,nr,'Composicao') 
             nds2=[]
             fnd_comp=True
             tps_len+=1 
        
        
        if verbo=='vb_afininity':# way->need
         # caracts-relavantes => way-fornecidos->need-necessarios, purpose/destination->objective
          print 'Run.(',verbo,')'
          # 
          identif=[] # objects com needs, par linkar candidatos a way
          way=[]
          restrict=[]
          plus=[]   
          for nr_t in nds2:          
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'way'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 way.append(d)
              if self.s_compare_dt(nr_t,'restriction'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 restrict.append(d)
              if self.s_compare_dt(nr_t,'way-plus'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 plus.append(d)
          if len(identif) > 0  and len(way) > 0 :
            # get ontology topico way->need, poderar a mais dadaptada a tds os way+restrictions+way-plus
            objs=get_special_ontology_w(way,restriction,plus)
            idx=[]
            objs_ret=[]
            for [obj,score_p] in objs:
             # achar os best score, adicionar como primeiros, em layoutcode com maximo e minimo numero de pesquisas, os mais graduados(adaptados) vencem
             fnd=False
             for ds in idx:
              if ds == score_p:
               fnd=True
             if not fnd:
              idx.append(score_p)
             #
            idx.sort ()
            for i in idx:
             for [obj,score_p] in objs: 
              if score_p == i:
               objs_ret.append(obj)
             
            if len(objs_ret) > 0:                  
             tps=rt.set_topico('best')
             for oret in objs_ret:
                    nr= rt.set_nr(oret)
                    tps.connect_to(rt,nr,'Composicao') 
             nds2=[]
             fnd_comp=True
             tps_len+=1          
        #==============================
        if verbo=='vb_collect_apr': # collect aproux -> collect em cima de caracts mencionadas
          #usado para gerar relacao de layers a processar para o call de outra ractionline, fazer coleta de objetos com determinadas caracts
          print 'Run.(',verbo,')' 
          identif=[] # objects  
          referencia=[]
          purpose2=[]
          for nr_t in nds2:
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'reference'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 referencia.append(d)
              if self.s_compare_dt(nr_t,'purpose'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 purpose2.append(d)
             
          for id in identif:
           ob=get_ontology_s(id,purpose2,referencia,usr )
           #get_ontology_ponderate
           for obs in ob:
            layers_collect.append(obs)
 
        if verbo=='vb_collect': # collect  -> collect em ponderacao
          #usado para gerar relacao de layers a processar para o call de outra ractionline, fazer coleta de objetos com determinadas caracts
          print 'Run.(',verbo,')'
          identif=[] # objects  
          referencia=[]
          purpose2=[]
          for nr_t in nds2:
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'rule'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 referencia.append(d)
              if self.s_compare_dt(nr_t,'quality'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 purpose2.append(d)
             
          for id in identif:
           ob=self.s_get_ontology_ponderate(id,referencia,purpose2,usr )
           print 'Collect->result(',id,',',referencia,',',purpose2,').[',ob,']'
           for [obs,mx] in ob:
            layers_collect.append(obs)
          
        #==============================     
        if verbo=='vb_filter': 
          # usado para criar um publish( filtro de nrs em cadeia que sobem p topicos, dentro de uma chamada de rct)
          print 'Run.(',verbo,')'
          
          identif=[] # objects 
          alias=[]
          for nr_t in nds2:          
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'alias'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 alias.append(d)
                 
          if len(alias) > 0:
           identif=[] # desconsidera identificador
           for nr_t in nds2:
            for al in alias:           
              if self.s_compare_dt(nr_t,al):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
             
          for id in identif:
           ob=get_ontology( id,purpose,usr )
           for o in ob:
            filtered.append(o)
            o.do_filter(verbo_compl)
        #=============================================================                
        if verbo=='vb_link':
          # linkar objetos, 'referencia' -> 'identificador' em 'purpose' -> motivo
          print 'Run.(',verbo,')'
          identif=[] # objects  
          referencia=[]
          purposes=[]
          foco=[]
          for nr_t in nds2:
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'reference'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 referencia.append(d)
              if self.s_compare_dt(nr_t,'purpose'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 purpose2.append(d)
              if self.s_compare_dt(nr_t,'foco'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 foco.append(d)
             
          for id in identif:
           ob=get_ontology( id,purpose )
           for o in ob:
            for id2 in referencia:
             ob2 = get_ontology( id2,purpose )
             for o2 in ob2:
              #=============
              focus_o=[]
              focus_d=[]
              if len(foco) > 0 :
               for foc in foco :
                tps=o.get_topico(foc)
                foco_o.append(tps)
               for foc in foco :
                tps=o2.get_topico(foc)
                foco_d.append(tps)
               for p in purposes:
                o.set_link_ds(o2,p,foco_o,foco_d)                 
        #==========================        
        if verbo=='vb_link_nr':
          print 'Run.(',verbo,')'
          # linkar objetos, 'referencia' -> 'identificador' em 'purpose' -> motivo
          identif=[] # objects  
          referencia=[]
          purposes=[]
          for nr_t in nds2:
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'reference'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 referencia.append(d)
              if self.s_compare_dt(nr_t,'purpose'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 purpose2.append(d)
             
          for id in identif:
           ob=get_ontology( id,purpose )
           for o in ob:
            for id2 in referencia:
             ob2 = get_ontology( id2,purpose )
             for o2 in ob2:
              #=============
              nr1=o.get_all () # considerando filter ativo
              nr2=o2.get_all ()
              for n1 in nr1:
               for n2 in nr2:
                for p in purposes:
                 nr1.connect_to(n1.owner,n2,p)
                 
            
        if verbo=='vb_behavior': #( discreta(em foco), intermitente(sem referencia),mutacao fact(actions aplicados/historico de acoes) )
          # procurar mutacoes em caracts de 'identificador'
          # procurar mutacoes em foco -> 'referencia'
          # mutacoes, sequencias de actions -> facts 
          print 'Run.(',verbo,')'          
          identif=[] # objects  
          referencia=[]
          action=[]
          for nr_t in nds2:
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'reference'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 referencia.append(d)
              if self.s_compare_dt(nr_t,'action'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 action.append(d)   
          irts=self.process_behavior(identif,referencia, action,purpose,usr)
          if len(irts) > 0 :
           for [rmath,rnomath,mathact] in irts:
            rt.set_topico_nr(rmath) # nao mutados 
            rt.set_topico_nr(rnomath) # mutados 
            rt.set_topico_nr(mathact) #-> fact actions
           nds2=[]
        #===============================             
        '''========= 
        ''' 
        fnd_comp=False
        for n_c in nds2:
          #chk_i=self.compare_dt_depend(usr,purpose,nr_atu,n_c,['identificador'])
          chk_i=self.compare_dt_depend(usr,purpose,nr_atu,n_c,[])
          if chk_i:
           fnd_comp=True
           nr_atu.connect_to_dyn_c(nr_atu.owner,n_c,'Compare-DYN') 
          #print 'compare:',nr_atu.dt,n_c.dt,' result:',fnd_comp        
        if fnd_comp:         
         tps_len+=1           
         rt.set_topico_nr(nr_atu)                   
        else:
         nore.set_topico_nr(nr_atu)        
      #=======================          
      
      
      tps=rt.topicos
      rt.topicos=[]
      for r in tps:
       r2=mdNeuron(r.owner)
       r2=r.mont_return_data(tps,foco) 
       if r2!=None:               
        rt.set_topico_nr(r2)
      print 'NEED:',need_s,' FOUND:',tps_len
      if tps_len >= need_s :
       ''' adicionar  os not inface , se tiver '''       
       nrs=node.get_all_no_interface ()
       print 'RCT->interface:',nrs,len(nrs),rt.topicos
       if len(nrs) > 0:
        # so retorna os n interface.nos q tem interface declarada, usa eles p conferencia e complemento(find-path),etc... mas n retorna as interfaces
        rt.topicos=[]
       for n in nrs:
         rt.topicos.append(n)
       '''adicionar no rtp'''
       for ts in rt.topicos:
        rtp.set_topico_nr(ts)
       #=====================
       rt=None       
      else : pass
    if len(nodes) == 0 and len(rtp.topicos) <= 0:
      print 'Prepare to call-inter-rtc():'
      #process_Call_RCT(self,data_c,ontology,usr,purpose,relactionate)
      i_ls=layers
      if len(layers_collect) > 0:
       i_ls=layers_collect
      self.process_Call_RCT(i_ls,ontology,usr,purpose,relactionate)
    
    if len(rtp.topicos) > 0 :
      print 'Call Layout-Code'
      layout_codes=self.get_links('LAYOUT-CODE')
      #===
      nms=[]      
      for d in layout_codes:
       nms.append(d.lr.name)
      print 'Prepare to call layouts-code---{',nms,'}'
      prepare_search_customlayouts(self,nms,[rtp],usr,relactionate) #purposes,dts,usr
      print 'layouts-code executed. ---'
      #===
      print 'Prepare to call-inter-rtc():'
      #process_Call_RCT(self,data_c,ontology,usr,purpose,relactionate)
      i_ls=[rtp]
      if len(layers_collect) > 0:
       i_ls=layers_collect      
      self.process_Call_RCT(i_ls,ontology,usr,purpose,relactionate)
      for s in dyned:
       s.release_din_sinapse()
      for s in filtered:
         s.release_filter ()
      return [rtp,nore]
    for s in filtered:
     s.release_filter ()
    for s in dyned:
     s.release_din_sinapse()
    return [None,None]
    #====    
    
  def process_raw_RCT(self,layers,ontology,usr,purpose,relactionate=False): # nao depende de links facts, executa compare em si mesma
    rtp=mdLayer ()
    nore=mdLayer ()
    nodes=[self]
    idcx=0
    for node in nodes:
     node=node.lr
     #=========
     nds=node.get_all ()
     foco=node.get_all_f ()
     print 'NDS:'
     for n1 in nds:
      print n1.dt
     print '----------'
     nds2=self.get_all_it(node.name,usr)
     #==========  
        
     need_s=0
     for n1 in nds:
      if self.s_compare_dt(n1,'source') or self.s_compare_dt(n1,'destination'): 
       pass
      else: 
       need_s+=1 
     #==========    
     tps_len=0
     for l in layers:
      nds2=l.get_all ()
      print 'NDS2:'
      for n1 in nds2:
       print n1.dt
      print '-----------'
      tps_len=0
      rt=mdLayer ()
      for nr_atu in nds:
        '''========= 
        ''' 
        fnd_comp=False
        for n_c in nds2:
          #chk_i=self.compare_dt_depend(usr,purpose,nr_atu,n_c,['identificador'])
          chk_i=self.compare_dt_depend(usr,purpose,nr_atu,n_c,[])
          if chk_i:
           fnd_comp=True
        if fnd_comp:         
         tps_len+=1  
         rt.set_topico_nr(nr_atu)     
        else:
         nore.set_topico_nr(nr_atu)        
      #=======================
      tps=rt.topicos
      rt.topicos=[]
      for r in tps:
       r2=mdNeuron(r.owner)
       r2=r.mont_return_data(tps,foco) 
       if r2!=None:
        rt.set_topico_nr(r2)
      print 'NEED:',need_s,' FOUND:',tps_len
      if tps_len >= need_s :
       ''' adicionar  os not inface , se tiver '''       
       nrs=node.get_all_no_interface ()
       print 'RCT->interface:',nrs,len(nrs),rt.topicos
       if len(nrs) > 0:
        # so retorna os n interface.nos q tem interface declarada, usa eles p conferencia e complemento(find-path),etc... mas n retorna as interfaces
        rt.topicos=[]
       for n in nrs:
         rt.topicos.append(n)
       '''adicionar no rtp'''
       for ts in rt.topicos:
        rtp.set_topico_nr(ts)
       #=====================
       rt=None       
      else : pass
    if len(rtp.topicos) > 0 :
      layout_codes=self.get_links('LAYOUT-CODE')
      #===
      nms=[]      
      for d in layout_codes:
       nms.append(d.lr.name)
      print 'Prepare to call layouts-code---{',nms,'}'
      prepare_search_customlayouts(self,nms,[rtp],usr,relactionate) #purposes,dts,usr
      print 'layouts-code executed. ---'
      #===
      return [rtp,nore]
    return None
    #====      
  

    
    
    