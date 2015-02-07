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




def get_object_by_data2(obj,usr):
 sql='select objeto,i from '+mdTb.table_object+' where lower(objeto)=lower(?) and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
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
 #-----------
 if True :
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where \"UID\" = ' + str(uid) )
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
 sql='select objeto,i from '+mdTb.table_object+' where lower(objeto)=lower(?) and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
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
 #-----------
 if True :
     rattings=0
     #print 'SQl: conn:','select trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where \"UID\" = ' + str(uid)
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where \"UID\" = ' + str(uid) )
     obj_nm=None     
     for results in resultSet:
          DT=results[0] 
          TOP=results[1]
          nr= lay.set_nr(DT)
          #print '->>:',DT,TOP
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
 sql='select objeto,i from '+mdTb.table_object+' where lower(objeto)=lower(?) and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
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
 #-----------
 if True :
     resultSet = conn3.sql ( 'select trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where "\UID\" = ' + str(uid) )
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
 
 sql='select objeto,i from '+mdTb.table_object+' where lower(objeto)=lower(?) and USERNAME = ? '
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
 #-----------
 plus_fnd=0
 if True :
     resultSet =conn3.sql ( 'select trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where \"UID\" = ' + str(uid) )
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
 
 sql='select objeto,i from '+mdTb.table_object+' where lower(objeto)=lower(?) and USERNAME = ? '
 resultSet = conn3.sqlX (sql,([obj,usr]))
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
 #-----------
 plus_fnd=0
 if True :
     resultSet = conn3.sql ( 'select trim(DT),trim(TOPICO) from '+mdTb.table_dt+' where \"UID\" = ' + str(uid) )
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
  conn.sqlX ('delete from '+mdTb.table_relaction+' where username=? and obj_orig=? ',([usr,name]) )
  #================
  conn.sqlX ('delete from '+mdTb.table_dt+' where username=? and \"UID\"  in ( select I from '+mdTb.table_object+' where username=? and lower(objeto)=lower(?) ) ',([usr,name]) )
  #================
  conn.sqlX ('delete from '+mdTb.table_object+' where username=? and lower(objeto)=lower(?) ',([usr,name])  )
  #==============
 except Exception,e: 
  print 'Error delete clean_obj_(2):',e 
 
 conn.commit()
 
def post_object_by_data_es(layer,usr): 
 nameo=layer.name
 nameo=umisc.trim(nameo)
 clear_obj(usr,nameo)
 print 'Post LR:',nameo,',len:',len(nameo),', usr:',usr
 sql1="insert into "+mdTb.table_object+"(username,objeto,CENAR,SENTI) values(?,?,0,0)"
 conn.sqlX (sql1,([usr,nameo]))
 uid=0
 resultSet2q =conn.sqlX ("select max(I) from "+mdTb.table_object+" where username =? and lower(objeto) = lower(?)   ",([usr,nameo]))
 for results2q in resultSet2q:
      uid=results2q[0] 
      break 
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
    sql1="insert into "+mdTb.table_dt+"(username,\"UID\",dt,topico,LEV,SIN,ID_TOP) values(?,?,?,?,?,'Composicao',1)"
    try:
     conn.sqlX (sql1,([usr,uid,sn_dt,tp_Dt,level]))
    except:
     print 'Erro ao post:',nameo,tp_Dt,sn_dt
     log.exception("--------------------------")
    #==========
    post_nr(usr,sn.nr,level+1)
  #==========    ===============================================
 
   
  post_nr(usr,tp)
 
 #===============================================
 for lnk in layer.links:
  sqlc='insert into  '+mdTb.table_relaction+'(OBJ_ORIG,OBJ_DEST,OPCODE,USERNAME,FOCO,FOCO_D,\"UID\") values(?,?,?,?,?,?,?)' 
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
     resultSet = conn.sqlX ("SELECT trim(OBJETO),i,cenar FROM  "+mdTb.table_object+" where  USERNAME = ? and i in ( select iud from "+mdTb.table_dt+" where topico ='way' and dt in ("+ps+")  ) and i not in ( select iud from "+mdTb.table_dt+" where topico ='restriction' and dt in ("+ps2+")  )    ",([alias,usr]))
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
     resultSet = conn.sqlX ("SELECT trim(OBJETO),i,cenar FROM  "+mdTb.table_object+" where  USERNAME = ? and i in ( select iud from "+mdTb.table_dt+" where topico ='need' and dt in ("+ps+")  ) and i not in ( select iud from "+mdTb.table_dt+" where topico ='restriction' and dt in ("+ps2+")  )    ",([alias,usr]))
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
 print 'get_ontology->(2):---'
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
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where  USERNAME = ? and i in ( select iud from "+mdTb.table_dt+" where topico ='destination' and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object" where lower(OBJETO) like lower(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where  USERNAME = ? and i in ( select iud from "+mdTb.table_dt+" where ("+ps2+") and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where lower(OBJETO) like lower(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
     if aliases == None or umisc.trim(aliases) == '':
      ps=''
      f=False
      for d in min_purposes:
       if f: ps+=','
       ps+="'"+d.lower()+"'"
       f=True
      print 'Collect->get(1)-sql:',ps,alias,usr
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where  USERNAME = ? and i in ( select \"UID\" from "+mdTb.table_dt+" where  lower(topico) in ("+ps+") )  ",([usr]))
     else:     
      print 'Collect->get(2):',alias,usr 
      resultSet = conn.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where lower(OBJETO) like lower(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
          for resultsC in resultSet:
           ido=resultsC[0]
           fco=resultsC[1]
           if fco == None : fco=''
           fcd=resultsC[2]
           if fcd == None: fcd = ''
           objs_r.append([ido,pr,fco,fcd])
         return objs_r 
        #===--------------------------------------
        #print 'get_object_by_data29()->(',i,',',usr,',',max_purposes,')'
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
         return s 
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
      resultSet = conn3.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where  USERNAME = ? and i in ( select iud from "+mdTb.table_dt+" where topico ='destination' and dt in ("+ps+") )  ",([alias,usr]))
     else:     
      resultSet = conn3.sqlX ("SELECT trim(OBJETO),i FROM  "+mdTb.table_object+" where lower(OBJETO) like lower(?)  and USERNAME = ?  ",([alias,usr]))
     for results in resultSet:
        i=results[0] 
        uid=results[1]
        #====
        avaliable_objs=[]
        #===--------------------------------------
        def collect_objs_orig(sins,i,usr):
         objs_r=[]
         for pr in sins:
          resultSet = conn3.sqlX ("SELECT trim(OBJ_DEST),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_ORIG = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
          resultSet = conn3.sqlX ("SELECT trim(OBJ_ORIG),trim(FOCO),trim(FOCO_D) FROM  "+mdTb.table_relaction+" where OBJ_DEST = ? and OPCODE = ? and USERNAME = ? ",([i,pr,usr]))   
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
  
  
 
 

    
    
    