# coding: latin-1
''' controla a aquisicao de dados extruturados, bem como validacao dos mesmos '''
import sys
import os
import umisc

#import sys
#sys.path.append("/home/jean/Programacao/componentes/pycassa")
#sys.path.append("/home/jean/Programacao/Python/componentes")

import logging
 


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('mdER')

# tipos de ER

 

all_posted_objects=0
all_posted_log=[]
 
import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily 

#pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)

pool2 = ConnectionPool('MINDNET', ['localhost:9160'],timeout=10000)



tb_fuzzy = pycassa.ColumnFamily(pool2, 'fuzzy_store') 
tb_fz_store_pref=pycassa.ColumnFamily(pool2,"fz_store_pref")
tb_fz_store_defs=pycassa.ColumnFamily(pool2,"fz_store_defs")
tb_fz_store_sufix=pycassa.ColumnFamily(pool2,"fz_store_sufix")
tb_fz_store_refer=pycassa.ColumnFamily(pool2,"fz_store_refer")
tb_fz_arround_points=pycassa.ColumnFamily(pool2,"fz_arround_points")
 
tb_object = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT') 
tb_object_dt = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT') 
tb_relaction = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS') 


tb_object3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4') 
tb_object_dt3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4') 
tb_relaction3 = pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4') 


tb_py=pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_PY') 
tb_py_code=pycassa.ColumnFamily(pool2, 'DATA_BEHAVIOUR_CODE_PY') 

tb_parse=pycassa.ColumnFamily(pool2, 'knowledge_manager')

is_win=False
if sys.platform == 'win32' or sys.platform == 'win64':
     is_win=True

if is_win:
 PATH_J = "H:\\mindnet\\"
else: 
 PATH_J = "/mindnet/code/"

def process_py():
 global is_win
 tb_py.truncate()
 tb_py_code.truncate()
 #
 import glob
 if is_win:
  rls=glob.glob(PATH_J+"execode\\*.py") 
 else: 
  rls=glob.glob(PATH_J+"execode/*.py") 
 #
 codes=[]
 #
 for rl in rls:
  if is_win:
   nm=rl.replace(PATH_J+"execode\\","")
  else: 
   nm=rl.replace(PATH_J+"execode/","")
  nm=nm.replace(".py","")
  f=open(rl,"r" )
  code=f.read()
  f=open(rl,"r" )
  lines=f.readlines()
  typ="1" # exec
  if len(lines)>0:
   lin=lines[0]
   lin=umisc.trim(lin).replace('\n','').replace('\r','')
   if lin == "#EXEC":
    typ='1'
   elif lin == "#LIB":
    typ='0'
  codes.append([nm,typ,code])  
 # 
 for re in codes:
  obj=re[0]
  usr='igor.moraes'
  TYP=re[1]
  code=re[2]
  code=code.replace('\r','\n')
  params={"USERNAME":usr,"OBJETO":obj,"TYP":str(TYP)}
  tb_py.insert(obj,params)
  #===
  params={"USERNAME":usr,"OBJETO":obj,"CODE":code}
  tb_py_code.insert(obj,params)

 
def process_base_tb():
  #all file in 
  global is_win
  tb_parse.truncate()
  import glob
  if is_win:
   r1s=glob.glob(PATH_J+"know\\*.md")
  else: 
   r1s=glob.glob(PATH_J+"know/*.md")
  cn=1
  for r1 in r1s:
   fil=open(r1,"r")
   lines=fil.readlines()
   ontos=[]
   DT =''
   typ =''
   DEST =''
   layout_onto =''
   start_k=False
   for line in lines:
    line=umisc.trim(line)
    
    if line[:4] =='know' or line[:3] =='end':
     start_k=True
     if DT != '':
      ontos.append([umisc.trim(DT).replace('\n','').replace('\r',''),umisc.trim(typ).replace('\n','').replace('\r',''),umisc.trim(DEST).replace('\n','').replace('\r',''),umisc.trim(layout_onto).replace('\n','').replace('\r','')])
      DT =''
      typ =''
      DEST =''
      layout_onto =''
             
    if start_k:
     if line[:2]=='DT': 
      DT=line[3:]
     elif line[:3]=='typ': 
      typ=line[4:]
     elif line[:4]=='DEST': 
      DEST=line[5:]
     elif line[:11]=='layout_onto': 
      layout_onto=line[12:]
    
      
   if DT != '': 
     ontos.append([umisc.trim(DT).replace('\n','').replace('\r',''),umisc.trim(typ).replace('\n','').replace('\r',''),umisc.trim(DEST).replace('\n','').replace('\r',''),umisc.trim(layout_onto).replace('\n','').replace('\r','')])
   #============================================   
   for r2 in ontos:   
    dt=r2[0]
    #if dt == 'post-layer-classify-product':
    #  print 'kkk'
    username='igor.moraes'
    typ=r2[1]
    dest=r2[2]
    layout_onto=r2[3]
    obj=layout_onto+str(cn)
    cn+=1
    #===========================================
    params={"DT":dt,"typ":str(typ),"DEST":dest,"layout_onto":layout_onto,"USERNAME":username}
    tb_parse.insert(obj,params)
 
 
def get_ractionlines_defs(usr):
 ''' pega o codigo do banco de dados '''
 global is_win
 rt=[]
 import glob
 import os
 if is_win:
  rls1=glob.glob(PATH_J+"rct\\*.md") 
  rls2=os.listdir(PATH_J+"fuzzy\\") 
 else: 
  rls1=glob.glob(PATH_J+"rct/*.md") 
  rls2=os.listdir(PATH_J+"fuzzy/") 
 #===
 for rl in rls1:
  if is_win:
   nm=rl.replace(PATH_J+"rct\\","")
  else: 
   nm=rl.replace(PATH_J+"rct/","")
  nm=nm.replace(".md","")
  f=open(rl,"r" )
  code=f.read()
  rt.append([nm,code])
 #===
 for rsl3 in rls2:
  if os.path.isfile(rsl3):continue
  if rsl3.startswith(".git"): continue
  #==========
  if is_win:
   nmdir=rsl3.replace(PATH_J+"fuzzy\\","")
   cdirs=os.listdir(PATH_J+"fuzzy\\"+nmdir)
  else: 
   nmdir=rsl3.replace(PATH_J+"fuzzy/","")
   cdirs=os.listdir(PATH_J+"fuzzy/"+nmdir)
  #=== 
  for rl in cdirs:
   if is_win:
    nm=rl.replace(PATH_J+"fuzzy\\"+nmdir,"")
    f=open(PATH_J+"fuzzy\\"+nmdir+'\\'+rl,"r" )
   else: 
    nm=rl.replace(PATH_J+"fuzzy/"+nmdir,"")
    f=open(PATH_J+"fuzzy/"+nmdir+'/'+rl,"r" )
   nm=nm.replace(".md","")
   code=f.read()
   rt.append([nm,code])  
 #========
 return rt
 
 
def clear_fz():
  tb_fuzzy.truncate()
  tb_fz_arround_points.truncate()
  tb_fz_store_defs.truncate()
  tb_fz_store_pref.truncate()
  tb_fz_store_refer.truncate()
  tb_fz_store_sufix.truncate()
 
 
def post_rct_object_fz(layer,name,usr):
 fzname=name 
 '''
  linhas:   
   force_position Y/N
   madatory Y/N
   layout_onto lay
   direction R/L
   an AN/OR
   sq 0...
   
   pref prefixo
   pref prefixo
   def data; sn_ret ; dt_ret
   suf [a,b,c]
   suf [a,b,c]
   refer dt
   refer dt
   refer dt
   ctrl-point a;b
   ctrl-point a;b
 '''

 [objs,layouts]=layer
 

 #======================
 force_position='N'
 madatory='Y'
 layout_onto=''
 direction='L'
 an= 'AN'
 sq='0'
 
 pref=[]
 _def=[]
 suf=[]
 refer=[]
 ctrl_point=[]
 
 #======================
 
 k_dt=[]
 k_sn=[]
 k_return=[]
 k_direct=[]
 start_def=False
  
 for ot in objs:
   o=ot[0]
   o2=ot[1]
   #print 'St:',o
   
   if o[:14] == 'force_position':
    force_position=umisc.trim(o2)
    
   if o[:8] == 'madatory' : 
    madatory=umisc.trim(o2)
    
   if o[:11] == 'layout_onto' : 
    layout_onto=umisc.trim(o2)

   if o[:9] == 'direction' : 
    direction=umisc.trim(o2)
    
   if o[:2] == 'an' : 
    an=umisc.trim(o2)
    
   if o[:2] == 'sq' : 
    sq=umisc.trim(o2)
    
   #=== 
   if o[:4] == 'pref' : 
    pref.append(umisc.trim(o2))

   if o[:3] == 'def' :
    if start_def and len(k_dt)>0:
     #post previus def
     _def.append([k_dt,k_sn,k_return,k_direct])
     k_dt=[]
     k_sn=[]
     k_return=[]
     k_direct=[]
    start_def=True
    
   if o[:2] == 'dt' : 
    k_dt.append(umisc.trim(o2))
   if o[:2] == 'sn' : 
    k_sn.append(umisc.trim(o2))
   if o[:6] == 'return' : 
    k_return.append(umisc.trim(o2))
   if o[:6] == 'direct' and o[:9] !='direction': 
    k_direct.append(umisc.trim(o2))
   
 
   if o[:3] == 'suf' : 
    if start_def and len(k_dt)>0:
     #post previus def
     _def.append([k_dt,k_sn,k_return,k_direct])
     k_dt=[]
     k_sn=[]
     k_return=[]
     k_direct=[]
    suf.append(umisc.trim(o2))
    
   if o[:5] == 'refer' : 
    refer.append(umisc.trim(o2))
    
   if o[:10] == 'ctrl-point' : 
    ctrl_point.append(umisc.trim(o2))

 
 #==================================================================== 
 params={"username":usr,"fzname":name,"force_position":force_position,"mandatory":madatory,"layout_onto":layout_onto,"direction":direction,"an":an,"sq":sq}
 tb_fuzzy.insert(str(fzname),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL) 
  
 cnt1=1  
 for prefix in pref:
    params={"username":usr,"fz":name,"pref":prefix}
    tb_fz_store_pref.insert(str(name+'|'+str(cnt1)),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)
    cnt1+=1
 cnt1=1  
 for defs in _def:
   [dt,sin_ret,vl_ret,direct]=defs
   #=== 
   if len(vl_ret)==0: vl_ret.append("")
   if len(direct)==0: direct.append("")
   params={"username":usr,"fz":name,"defs":dt[0],"sin_ret":sin_ret[0],"vl_ret":vl_ret[0],"special_direct":direct[0]}
   tb_fz_store_defs.insert(str( name+"|"+str(cnt1) ),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)
   # 
   cnt1+=1

 cnt1=1
 for sufix in suf:
   params={"username":usr,"fz":name,"sufix":sufix}
   tb_fz_store_sufix.insert(str(name+"|"+str(cnt1)),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL  )
   cnt1+=1
 cnt1=1  
 #==========================================================
 for refers in refer:
   params={"username":usr,"fz":name,"refer":refers}
   tb_fz_store_refer.insert( str(name+"|"+str(cnt1) ),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
   cnt1+=1
 cnt1=1  
 for ctrlp in ctrl_point:
   typ=''
   v_point=''
   tmp=''
   for d in ctrlp:
    if d ==';':
     if typ=='':
      typ=tmp
     elif v_point=='':
      v_point=tmp
     tmp=''
    else:
     tmp+=d
   if tmp != '' :
     v_point=tmp   
   #===
   if typ == '' : typ='0'
   #===   
   params={"username":usr,"fz":name,"typ":typ,"v_point":v_point} 
   tb_fz_arround_points.insert( str(name + "|" + str(cnt1)),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
   cnt1+=1

 
 
 
def post_rct_object_fact(layer,name,usr,storage_data):
 ''' apaga o objeto atual no banco se existir e grava o novo '''
 [objs,layouts]=layer
 global all_posted_objects
 if name == None: return
 
 print 'Post obj:',name
 #
   
 cnt1=1
 for o in objs:
   [topico,childs]=o
   child=''
   for c in childs:
    if child != '' : child+=','
    child+=c
   #========================= 
   indch=0
   lines=[]
   tmp=''
   for ch in child: 
    if ch == '&' and child[indch-1] != '\\':
      lines.append(tmp)
      tmp=''
    else:
      tmp+=ch
   lines.append(tmp)   
   #================== 
   cntd=0
   antdt=None
   for child in lines:
    cntd+=1
    if antdt != None:
       topico=antdt
    params={"username":usr,"datach":child,"topico":topico,"object":name,"LEV":str(cntd),"cnt":str(cnt1)}
    if not storage_data:
     tb_object_dt.insert( name+"|"+str(cnt1),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL  )
    else: 
     tb_object_dt3.insert( name+"|"+str(cnt1),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL  )
    antdt=child
    cnt1+=1
   '''
   child=''
   for c in childs:
    if child != '' : child+=','
    child+=c
   params={"username":usr,"datach":child,"topico":topico,"object":name,"LEV":"1","cnt":str(cnt1)}
   tb_object_dt.insert( name+"|"+str(cnt1),params,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL  )
   cnt1+=1
   '''
 
 for l in layouts:
   params={"username":usr,"datach":l,"topico":"layouts","object":name,"LEV":"1","cnt":str(cnt1)}
   if not storage_data:
    tb_object_dt.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
   else: 
    tb_object_dt3.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
   cnt1+=1
   
 #if name == 'simple-pesq-fct-id':
 #  print 'ver'
 if not storage_data:  
  tb_object.insert( name,{"username":usr,"objeto":name,"cenar":"0","conts_n":str(cnt1)} ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
 else: 
  tb_object3.insert( name,{"username":usr,"objeto":name,"cenar":"0","conts_n":str(cnt1)} ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
 all_posted_log.append('insert:'+name)
 all_posted_objects+=1
 #======================
   
def clear_all_rcts(usr):
 try :
  tb_relaction.truncate()
  tb_object.truncate()
  tb_object_dt.truncate()
  #===
 except: pass
 
 
def post_rct_object_rct(facts,name,purps,usr,r_cts,r_beha,r_layc,priors,storage_data):
 ''' apaga o objeto atual no banco se existir e grava o novo '''
 global all_posted_objects

 cnt1=1
 for o in facts:
   [topico,find_path]=o 
   if umisc.trim(find_path)!= '':
    params={"username":usr,"datach":find_path,"topico":topico,"object":name,"LEV":"1","cnt":str(cnt1)}
    if not storage_data:
     tb_object_dt.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
    else: 
     tb_object_dt3.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
    cnt1+=1
    
   
 for ps in purps:# purpose -> destination
    params={"username":usr,"datach":ps,"topico":'destination',"object":name,"LEV":"1","cnt":str(cnt1)}
    if not storage_data:
     tb_object_dt.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
    else: 
     tb_object_dt3.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
    cnt1+=1
 
 for ps in priors: 
    params={"username":usr,"datach":ps,"topico":'priority',"object":name,"LEV":"1","cnt":str(cnt1)}
    if not storage_data:
     tb_object_dt.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
    else: 
     tb_object_dt3.insert( name+"|"+str(cnt1),params ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
    cnt1+=1

 #print 'Post-RCT(2):',name
 #if name == 'simple-pesq-fct-id':
 #  print 'ver'
 if not storage_data:
  tb_object.insert( name,{"username":usr,"objeto":name,"cenar":"0","conts_n":str(cnt1)} ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
 else: 
  tb_object.insert3( name,{"username":usr,"objeto":name,"cenar":"0","conts_n":str(cnt1)} ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )
 all_posted_log.append('insert:'+name)
 all_posted_objects+=1
 #======================
 cnt1=1 
 for c in r_beha:
   if not storage_data:
    tb_relaction.insert( name+"|"+str(cnt1)+"|"+"BEHAVIOR"+"|"+c,{"username":usr,"obj_orig":name,"obj_dest":c,"opcode":"BEHAVIOR","foco":"","foco_d": "","cond":"","cntk":str(cnt1)  } ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )   
   else: 
    tb_relaction3.insert( name+"|"+str(cnt1)+"|"+"BEHAVIOR"+"|"+c,{"username":usr,"obj_orig":name,"obj_dest":c,"opcode":"BEHAVIOR","foco":"","foco_d": "","cond":"","cntk":str(cnt1)  } ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL )   
   cnt1+=1 
 #============= 
 for c in r_layc:
   tb_relaction.insert( name+"|"+str(cnt1)+"|"+"LAYOUT-CODE"+"|"+c,{"username":usr,"obj_orig":name,"obj_dest":c,"opcode":"LAYOUT-CODE","foco":"","foco_d": "","cond":"","cntk":str(cnt1)   }  ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)   
   cnt1+=1 
   
 for [namec,params] in r_cts:
   if not storage_data:
    tb_relaction.insert( name+"|"+str(cnt1)+"|"+"CALL"+"|"+namec,{"username":usr,"obj_orig":name,"obj_dest":namec,"opcode":"CALL", "foco":params,"foco_d":"" ,"cond":"","cntk":str(cnt1) }  ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)   
   else: 
    tb_relaction3.insert( name+"|"+str(cnt1)+"|"+"CALL"+"|"+namec,{"username":usr,"obj_orig":name,"obj_dest":namec,"opcode":"CALL", "foco":params,"foco_d":"" ,"cond":"","cntk":str(cnt1) }  ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)   
   cnt1+=1 
 #======================
 for o in facts:
   [topico,find_path]=o 
   if not storage_data:
    tb_relaction.insert( name+"|"+str(cnt1)+"|"+"FACT"+"|"+topico,{"username":usr,"obj_orig":name,"obj_dest":topico,"opcode":"FACT","foco":"","foco_d": "" ,"cond":"","cntk":str(cnt1) }  ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)   
   else: 
    tb_relaction3.insert( name+"|"+str(cnt1)+"|"+"FACT"+"|"+topico,{"username":usr,"obj_orig":name,"obj_dest":topico,"opcode":"FACT","foco":"","foco_d": "" ,"cond":"","cntk":str(cnt1) }  ,write_consistency_level=pycassa.cassandra.ttypes.ConsistencyLevel.ALL)   
   cnt1+=1 
 #===  
   
def compile_rct(usr):
 ''' recompila a base de Data Behavior para ractionlines layers-objects '''
 '''   obs:<dependencia> = find-path '''
 ''' 
    formato raction-line:
     ractionline rct
      purpose purp
      [fact-name]
      [fact-name] (dependencia) 
      raction ractionline-to-call (need-fato,need-fat) -> chamada de uma ractionline, passando os fact processados como parametro need-fato
      behavior fact-name
     
	 
     fact 
      use-layout layout,layout,...
      action elemento,...
      object elemento,...
      class elemento,...
      composition elemento,...
      dominio elemento,...
      neeed elemento,...
      way elemento,...
      means elemento,...
 '''
 #==============
 rcts=get_ractionlines_defs(usr)
 #rcts=get_empty_lines(rcts)
 print 'Clear all rcts/facts cache...'
 clear_fz()
 #================ (1)
 clear_all_rcts(usr)
 print 'Compile ',len(rcts),' ractionlines...'
 for r1 in rcts:
  [nome_rct,codigo]=r1
  storage_data=False
  #print 'READ PST:',nome_rct
  #codigo=codigo.replace('\r','')
  #print nome_rct,codigo,'..'
  r_facts=[]
  r_fuzzy=[]
  r_rcts=[]
  r_beha=[]
  r_layc=[]
  ractions=[]
  purps=[]
  rct_name=None
  fct_name=None
  fzName=None
  in_fz=False
  facts=[]
  fzs=[]
  objs=[]
  priors=[]
  layouts_use=[]
  def get_lines(cd):
   r=[]
   tmp=''
   for c in cd:
    if c == '\n' or c == '\r':
     r.append(umisc.trim(tmp) )
     tmp=''
    else:
     tmp+=c
   if tmp != '' :
    r.append(umisc.trim(tmp) )
   return r 
  lns_cod=get_lines(codigo)
  #===================
  for ln in lns_cod:
   ln=ln.replace('\r','')
   ln=ln.replace('\n','')
   ln=umisc.trim(ln)
   if len(ln) > 0 :
    if ln[0]=='#': continue
   if len(ln)==0: continue 
   #============
   if ln[:3].lower () == 'end':
    if len(objs) > 0 :
     if not in_fz:
      facts.append([fct_name,layouts_use,objs])
     else:
      fzs.append([fzName,layouts_use,objs])
     layouts_use=[]
     objs=[]
    # 
    if len(r_facts) > 0 or len(r_rcts) > 0 :      
      ractions.append([rct_name,r_facts,purps,r_rcts,r_beha,r_layc,priors])
      r_facts=[]
      r_rcts=[]
      purps=[]
      priors=[]
      r_beha=[]
      r_layc=[]
    in_fz=False
   #============
   if ln[:11].lower () == 'ractionline':
    #if True  :
    if len(r_facts) > 0 or len(r_rcts) > 0 :
      ractions.append([rct_name,r_facts,purps,r_rcts,r_beha,r_layc,priors])
      r_facts=[]
      priors=[]
      purps=[]
      r_rcts=[]
      objs=[]
    rct_name=umisc.trim(ln[12:])
   elif ln[:7].lower () == 'purpose':
    purp=umisc.trim(ln[8:])
    purps.append(purp) 
   elif ln[:8].lower() == 'priority': 
    ps=umisc.trim(ln[9:])
    priors.append(ps)
   elif ln[:4].lower () == 'call':
    ps=umisc.trim(ln[5:])
    # analizar parametros de chamada -> 
    cal=''
    pars=''
    tmp=''
    for d in ps:
     if d=='(':
      cal=umisc.trim(tmp)
     elif cal != '' and ( d==')' ): 
       pars=(tmp)
     else:
      tmp+=d
    if cal == '' and tmp != '':
     cal=tmp
    r_rcts.append([cal,pars]) 
   #==================================== 
   elif ln[:8].lower () ==  'behavior':
    ps=umisc.trim(ln[9:])
    r_beha.append(ps) 
   elif ln[:10].lower () ==  'layoutcode':
    ps=umisc.trim(ln[11:])
    r_layc.append(ps) 
   elif ln[:12].lower () == 'storage-data':
    storage_data=True    
   elif ln[:8].lower () == 'factname':
    fct=umisc.trim(ln[9:])
    have_depend=False
    fc=fct.find('(')
    if fc > -1 :
     if fct[fc-1] != '\\':
      have_depend=True
      have_depend_p=fc
    fct1=fct
    fct3=''
    if have_depend:
     fc2=fct.find(')')
     fct1=fct[:have_depend_p]
     fct2=umisc.trim(fct[have_depend_p:fc2])
     fct3=fct2[1:]
     fct2=fct3
     fct3=fct2   
    r_facts.append([fct1,fct3])
   elif ln[:4].lower () == 'fact':
    if not in_fz:
        if len(objs) > 0:
         facts.append([fct_name,layouts_use,objs])
         layouts_use=[]
         objs=[]
    else:
        if len(objs) > 0:
         fzs.append([fzName,layouts_use,objs])
         layouts_use=[]
         objs=[]
    fct_name=umisc.trim(ln[4:])
    #if fct_name == 'apps_aderencia_with_cenarioxz3':
    #  print 'kkk'
    in_fz=False
   elif ln[:5].lower () == 'fuzzy':
    if not in_fz:
        if len(objs) > 0:
         facts.append([fct_name,layouts_use,objs])
         layouts_use=[]
         objs=[]
    else:
        if len(objs) > 0:
         fzs.append([fzName,layouts_use,objs])
         layouts_use=[]
         objs=[]
    fzName=umisc.trim(ln[5:])
    in_fz=True
   elif ln[:10].lower () == 'use-layout':
    la=umisc.trim(ln[10:])
    layouts_use.append(la)
   else:
     c=ln
     c1=''
     c2=''
     c4=1
     tmp=''
     fir=True
     for s in c:
      if s == ' ' and fir:
         if umisc.trim(tmp) != '':
          c1=tmp
          tmp=''
          fir=False
          #break
      else: tmp+=s
      c4+=1
     tmp=umisc.trim(tmp)
     if tmp != '':  
       c2=tmp
       if c1 == '': 
        c1=c2
        c2=''
     if umisc.trim(c1) != '':
      c3=[]
      tmpk=''
      fir=True
      indice_p=0
      if in_fz:
       c3=(c2)
      else: 
       for id in c2:
        if id == ',':
         if fir:
          c3.append(tmpk)
          tmpk=''
         else:
           if c2[indice_p-1] != '\\':
            c3.append(tmpk)
            tmpk=''          
           else:tmpk+=id
        else:tmpk+=id
        fir=False
        indice_p+=1
       #======================================== 
       #if tmpk != '': 
       if c1 != 'end':
        c3.append(tmpk) 
      
      if not in_fz:
       #for f in c3:
       if len(c3) > 0 :
        objs.append([c1,c3])
      else:  
        objs.append([c1,c3])
  #=========================
  # registrar os facts e os ractionline como layers  
  print 'Post ',len(fzs),' fzs'
  for f in fzs:
   [name,layouts,objs]=f
   post_rct_object_fz([objs,layouts],name,usr)   
  print 'Post ',len(facts),' facts' 
  for f in facts:
   [name,layouts,objs]=f
   #== (1)
   post_rct_object_fact([objs,layouts],name,usr,storage_data)
   pass
  #========================================================== 
  print 'Post:',len(ractions),' rcts'
  for rc1 in ractions:
    try:
     [rct_name,r_facts,purps,r_cts,r_beha,r_layc,priors]=rc1     
     #print 'Post-RCT:',rct_name,r_facts
     #=== (1)
     post_rct_object_rct(r_facts,rct_name,purps,usr,r_cts,r_beha,r_layc,priors,storage_data)
    except Exception,es:
     print 'Error:',es  
     log.exception("")
 print 'OK'  
 
