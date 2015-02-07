#encoding: latin-1
# atualizar:
# variancy
# filter + get_Reverse_links
# $stack
# return
# write
import os
import umisc
import logging
from StringIO import StringIO
import datetime
import time, datetime
import mdFuzzy
import mdTb
from operator import itemgetter, attrgetter
import mg

import pycassa
from pycassa.pool import ConnectionPool
from pycassa import index
from pycassa.columnfamily import ColumnFamily

def start_db(pool2):
  mdTb.start_db(pool2)

 
kstermo=None


type_coll='0' # 0->get_object,1->get_object2



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
def collect_objs_orig( i,usr,mdlayer):
 objs_r=[]
 objs_r2=[] 
 objs_r22=[]
 if mdlayer.tb == 1:  
  #cl4 = index.create_index_expression(column_name='obj_orig', value=str(i))
  #
  #clausec = index.create_index_clause([cl4],count=1000000)
  #resultSet=mdTb.tb_relaction1.find({'obj_orig':str(i)})
  resultSet=mg.obj_get_Range([mdTb.tb_relaction1],[['obj_orig',str(i)]])
  for ky,resultsC in resultSet: 
   ido=resultsC[u'obj_dest']
   ido2=resultsC[u'opcode']
   ido3=resultsC[u'foco']
   ido4=resultsC[u'foco_d']
   ido5=resultsC[u'cond']
   ido6=int(resultsC[u'cntk'])
   #===
   if ido2  == None:
    ido2=''
   if ido3  == None:
    ido3=''
   if ido4  == None:
    ido4=''
   if ido5  == None:
    ido5=''
   #===
   objs_r2.append([ido,ido2,ido3,ido4,ido5,ido6])  
  #============== 
 objs_r22=sorted(objs_r2, key=itemgetter(5), reverse=False) 
 objs_r2=[]
 for [ido,ido2,ido3,ido4,ido5,ido6] in objs_r22:
    objs_r.append([ido,ido2,ido3,ido4,ido5])
 return objs_r 
#===--------------------------------------
def collect_objs_orig_obj2( i,usr,mdlayer):
 objs_r=[]
 if mdlayer.tb ==2 : # 2 -> semantic_object3        
  resultSet=mg.obj_get_Range([mdTb.tb_relaction],[['obj_orig',str(i)]])
  for ky,resultsC in resultSet: 
   ido=resultsC[u'obj_dest']
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
   #===
   objs_r.append([ido,ido2,ido3,ido4,ido5])
 elif mdlayer.tb == 3: # 3 -> semantic_object3_1_4:
  resultSet=mg.obj_get_Range([mdTb.tb_relaction31],[['obj_orig',str(i)]])
  for ky,resultsC in resultSet: 
   ido=resultsC[u'obj_dest']
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
   #===
   objs_r.append([ido,ido2,ido3,ido4,ido5])
 return objs_r 
#===--------------------------------------
def collect_objs_dest( i,usr,mdlayer):
 objs_r=[]
 if mdlayer.tb == 1:
  objs_r2=[] 
  #cl4 = index.create_index_expression(column_name='obj_dest', value=str(i))
  #clausec = index.create_index_clause([cl4],count=1000000)
  resultSet=mg.obj_get_Range([mdTb.tb_relaction1],[['obj_dest',str(i)]])
  #resultSet=mdTb.tb_relaction1.find({'obj_dest':str(i)})
  for resultsC in resultSet: 
   ido=resultsC[u'obj_orig']
   ido2=resultsC[u'opcode']
   ido3=resultsC[u'foco']
   ido4=resultsC[u'foco_d']
   ido5=resultsC[u'cond']
   ido6=int(resultsC[u'cntk'])
   #===
   if ido2  == None:
    ido2=''
   if ido3  == None:
    ido3=''
   if ido4  == None:
    ido4=''
   if ido5  == None:
    ido5=''
   if ido6  == None:
    ido6=''
   #===
   objs_r2.append([ido,ido2,ido3,ido4,ido5,ido6])  
  objs_r22=sorted(objs_r2, key=itemgetter(5), reverse=False) 
  for [ido,ido2,ido3,ido4,ido5,ido6] in objs_r22:
    objs_r.append([ido,ido2,ido3,ido4,ido5])   
  #================================================ 
 elif mdlayer.tb == 2: # semantic_object3
  resultSet=mg.obj_get_Range([mdTb.tb_relaction],[['obj_dest',str(i)]])
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
   #===
   objs_r.append([ido,ido2,ido3,ido4,ido5])   
 elif mdlayer.tb == 3: # semantic_object3_1_4
  resultSet=mg.obj_get_Range([mdTb.tb_relaction31],[['obj_dest',str(i)]])
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
   #===
   objs_r.append([ido,ido2,ido3,ido4,ido5])   
 return objs_r 
#===--------------------------------------
def collect_objs_dest_obj2( i,usr,mdlayer):
 objs_r=[]
 if mdlayer.tb == 2:
  resultSet=mg.obj_get_Range([mdTb.tb_relaction],[['obj_dest',str(i)]])
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
   #===
   objs_r.append([ido,ido2,ido3,ido4,ido5])   
 elif mdlayer.tb > 2:
  resultSet=mg.obj_get_Range([mdTb.tb_relaction31],[['obj_dest',str(i)]])
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
   #===
   objs_r.append([ido,ido2,ido3,ido4,ido5])   
 return objs_r 
#===--------------------------------------

def pr_par(s):
 rt=[]
 tmp=''
 for a in s:
  if a == ',':
   rt.append(tmp)
   tmp=''
  else:
   tmp+=a
 #=====================  
 return rt    

def collect_links(obj_principal2,i2,usr):
 
 c1=collect_objs_orig(i2,usr,obj_principal2)
 if len(c1) == 0:
  c1=collect_objs_orig_obj2(i2,usr,obj_principal2)
 #==----------------------------------------
 for c in c1:
  obj_id=c[0]
  opc=c[1]
  foco=pr_par(c[2])
  foco_d=pr_par(c[3])
  cond=pr_par(c[4])  
  if obj_principal2.tb == 1:#semantic_object
   obj_k=get_object_by_data(obj_id,obj_id)
  elif obj_principal2.tb == 2:#semantic_object3
   obj_k=mdTb.get_object_by_data(obj_id,obj_id)
  elif obj_principal2.tb == 3:#semantic_object3_1_4
   antz=mdTb.Zeus_Mode
   mdTb.Zeus_Mode=False
   obj_k=mdTb.get_object_by_data2z(obj_id,obj_id,True)
   mdTb.Zeus_Mode=antz
  obj_principal2.set_link_ds(obj_k,opc,foco,foco_d,cond)
 

def collect_links2(obj_principal2,i2,usr):
 
 c1=collect_objs_dest(i2,usr,obj_principal2)
 if len(c1) == 0:
  c1=collect_objs_dest_obj2(i2,usr,obj_principal2)
 rt=[] 
 #==----------------------------------------
 for c in c1:
  obj_id=c[0]
  opc=c[1]
  foco=pr_par(c[2])
  foco_d=pr_par(c[3])
  cond=pr_par(c[4])  
  obj_k=get_object_by_data(obj_id,usr)
  #================
  mc=mdDynamicLayerLink(obj_k,opc,cond)
  mc.foco_o=foco
  mc.foco_d=foco_d
  rt.append(mc)
 
 return rt



import get_object
import get_object2 


 

def get_object_by_data2(obj,usr):
  if type_coll == '0':
   return get_object.get_object_by_data2(obj,usr)
  else: 
   return get_object2.get_object_by_data2(obj,usr)
 
def get_object_by_data29(obj,usr,max_purposes):
  if type_coll == '0':
   return get_object.get_object_by_data29(obj,usr,max_purposes)
  else: 
   return get_object2.get_object_by_data29(obj,usr,max_purposes)
 
 
def get_object_by_data23(obj,usr):
  if type_coll == '0':
   return get_object.get_object_by_data23(obj,usr)
  else: 
   return get_object2.get_object_by_data23(obj,usr)

  

def get_object_by_data22(obj,usr,plus):
  if type_coll == '0':
   return get_object.get_object_by_data22(obj,usr,plus)
  else: 
   return get_object2.get_object_by_data22(obj,usr,plus)

 

 
def get_object_by_data223(obj,usr,plus):
  if type_coll == '0':
   return get_object.get_object_by_data223(obj,usr,plus)
  else: 
   return get_object2.get_object_by_data223(obj,usr,plus)
  
 
 
def clear_obj(usr,name ):
  if type_coll == '0':
   return get_object.clear_obj(usr,name )
  else: 
   return get_object2.clear_obj(usr,name )

 
 
def post_object_by_data_es(layer,usr): 
  #if type_coll == '0':
  # return get_object.post_object_by_data_es(layer,usr)
  #else: 
  # return get_object2.post_object_by_data_es(layer,usr)
  return get_object2.post_object_by_data_es(layer,usr) 

def get_ontology_s2s(aliases,opcode,usr): 
  if type_coll == '0':
   return get_object.get_ontology_s2s(aliases,opcode,purposes,usr )
  else: 
   return get_object2.get_ontology_s2s(aliases,opcode,purposes,usr )
 
def get_ontology(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None 
  if type_coll == '0':
   return get_object.get_ontology(aliases,purposes,usr )
  else: 
   return get_object2.get_ontology(aliases,purposes,usr )

  
 
 
 
def get_ontology_s(aliases,purposes,destinats,usr ): #  considera os purposes nos filtros quando alias == None 
  if type_coll == '0':
   return get_object.get_ontology_s(aliases,purposes,destinats,usr )
  else: 
   return get_object2.get_ontology_s(aliases,purposes,destinats,usr )
   
def get_ontology_s_p(aliases,purposes,destinats,usr ): #  considera os purposes nos filtros quando alias == None 
  return get_object2.get_ontology_s_p(aliases,purposes,destinats,usr )
  
 
 
def get_ontology_ponderate(aliases,min_purposes,max_purposes,usr,dfin=[],sinapses_consid=[] ): # min_purposes=mandatory, max_purposes=max ideal 
  if type_coll == '0':
   return get_object.get_ontology_ponderate(aliases,min_purposes,max_purposes,usr,dfin,sinapses_consid )
  else: 
   return get_object2.get_ontology_ponderate(aliases,min_purposes,max_purposes,usr,dfin,sinapses_consid )
  
 
 
def get_ontology2(aliases,purposes,usr ): #  considera os purposes nos filtros quando alias == None 
  if type_coll == '0':
   return get_object.get_ontology2(aliases,purposes,usr )
  else: 
   return get_object2.get_ontology2(aliases,purposes,usr )

   

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
   self.kstermo=kstermo
   self.tmp=[]


GlobalStack=CGlobalStack ()

   
#===================
def get_typ(obj,usr2):
  # 
  typ=0
  #=======================
  resultSet=mdTb.tb_py.get(obj)
  typ=int(resultSet[u'TYP'])
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
  #
  try:  
   resultSet=mdTb.tb_py_code.get(dt)
  except: 
   resultSet=[] 
  # 
  if True:
    results = resultSet
    typ=get_typ(dt,usr)
    o=clean_s_k(results[u'CODE'])
    code=(o)
    sr_int_cmd_param=dts
    relactional=relactionate
    startL=layer_Start
    usuario=usr
    GlobalStack.kstermo=kstermo
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
     log.exception( 'Exec Error:['+ dt +']') 
     post_error(usr)
     print 'Code:\n',code
    if typ == 1: #executavel
     # adicionar ao codes_Result o retorno_srt(lines->[endereco,dados] ) 
     if retorno_srt != None:
      codes_Result.append( retorno_srt )
 #===================
 return codes_Result 

def get_object_by_data(obj,usr): 
 print 'get.all.obj.for:',obj
 return mdTb.get_object_by_data2z_cod(obj,obj,True)

def get_object_by_data_o22(obj,usr,obj_caller): 
 is_rct=False
 if obj_caller != None:
   is_rct=obj_caller.rct
 if mdTb.Zeus_Mode or is_rct:
  lay=mdTb.get_object_by_data(obj_nm,'')   
 else: 
  try: 
   #resultSet=[[ alia, mdTb.tb_object1.get(alia) ]] 
   #resultSet=[[obj,mg.tb_get([mdTb.tb_object],obj)]]
   resultSet=[[alia,mg.tb_get([mdTb.tb_object1],alia)]]
  except:
   resultSet=[]  
  for ky,resultsC in resultSet: 
       obj_nm=results[u'objeto'] 
  #-----------
  lay=mdLayer ()
  if obj_nm == None: obj_nm=obj
  lay.name=obj_nm
  lay=mdTb.get_object_by_data(obj_nm,'')
  #-----------
 return lay   

 
def get_object_by_name(aliases,usr,caller=None): 
 tree_h=[]
 is_rct=False
 if caller != None:
   is_rct=caller.rct
 for alias in aliases:
  if mdTb.Zeus_Mode or is_rct:
     #alia=alias.upper ()
     alia=alias
     # 
     try:
      #resultSet=[[ alia, mdTb.tb_object1.get(alia) ]] 
      resultSet=[[ alia, mg.tb_get([mdTb.tb_object1],alia) ]]
     except: continue  
     #print 'Get.obj.by.name:',alia,usr
     for ky,results in resultSet:
        i=ky
        #====
        avaliable_objs=[]
        #===--------------------------------------
        obj_principal=get_object_by_data(i,usr)
        tree_h.append(obj_principal)
        #===        
  else: 
     alia=alias
     rt=get_object_by_data_o22(alia,usr,caller)   
     tree_h.append(rt)
   
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
   nrr.uuid=nr.uuid
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
  self.uuid=0
 def connect_toi(self,lr,nr,opcode,index):
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
   self.sinapses.insert(index,sn)
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

 
 def mont_return_data2(self):
    ow=self
    if  True : 
        sn1=None
        for s in ow.dynsinap:
         if s.opcode =='Compare-DYN':          
          sn1=s.nr
          print 'mont_return_data2================'
          print 'Found:DynSinap:',s.opcode,', Ob:',ow.dt
          print 'Sn1:',sn1.dt
          print '================================='
          r= self.translate_dts(ow,sn1) 
          #ow.dynsinap.remove(s)
          return r
    return ow      
 
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
   def __init__(self,lr,opcode,opcode_seg=[]):
    mdLayerLink.__init__(self,lr,opcode,opcode_seg)
    self.foco_o=[]   
    self.foco_d=[]

class mdLayer: #mantem a ontologia do conhecimento montada
  def dump_layer_file(self):
   def spaces(n):
    r=''
    i=1
    while i<=n:
     r+=' ' 
     i+=1
    return r
   #===========================   
   fil=open("c:\\python24\\kk.txt","wr")
   def print_s(nr,lev=1):
    if lev > 1:
     fil.write(spaces(lev)+'DT:'+str(nr.dt)+','+str(nr)+'\n')
    if len(nr.sinapses) > 0 :
     fil.write( spaces(lev)+'sub-level:-----' +'\n')
     for d in nr.sinapses:
       print_s(d.nr,lev+1)
     fil.write( spaces(lev)+'sub-level------'+'\n' )
   #=====================
   fil.write( 'dump-layer:'+self.name+'\n' )
   for s in self.topicos:
    fil.write(  'TOP:'+str(s.dt)+','+str(s)+'\n' )
    print_s(s)
   fil.write( 'dump-layer--------------------------'+'\n' )
   fil.close()
  #=  
  def dump_layer(self):
   def spaces(n):
    r=''
    i=1
    while i<=n:
     r+=' ' 
     i+=1
    return r
   #===========================    
   def print_s(nr,lev=1):
    if lev > 1:
     print spaces(lev)+'DT:',nr.dt,nr
    if len(nr.sinapses) > 0 :
     print spaces(lev)+'sub-level:-----'
     for d in nr.sinapses:
       print_s(d.nr,lev+1)
     print spaces(lev)+'sub-level------'
   #=====================
   print 'dump-layer:',self.name
   for s in self.topicos:
    print  'TOP:',s.dt,s
    print_s(s)
   print 'dump-layer--------------------------'
   
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
  def s_get_ontology_ponderate_caracts(self,aliases,min_purposes,max_purposes,usr,purpose,top_considers=[] ,dfin=[],sinapses_consid=[]):
    print 'get_ontology_ponderate_Caracts.get_ontology_ponderate():',aliases,min_purposes,[],usr
    rts=get_ontology_ponderate(aliases,min_purposes,[],usr,dfin,sinapses_consid )
    rts_o=[]
    print 'Ponderate found:',rts
    for [mx,obj] in rts:
     print 'Ponderate min(',obj.name,'):',len(max_purposes)
     attr=[]      
     try:
      for cons in top_considers:  
            print 'Considere:',cons           
            pass 
     
      alss=obj.get_all()
      print 'Ponderate found:',len(alss)
      alls2=max_purposes
      fnds=0
      for nr_atu in alss:      
       found_k=False
       for n_ca in alls2:
        if umisc.trim(n_ca) == '':continue
        print 'Ponderate Get_ontology-start{',n_ca,'}'
        rets_onto=self.s_get_ontology_ponderate(n_ca,[],[],usr )
        print 'Ponderate Get_ontology{',n_ca,'},result:',rets_onto
        for [attr,o] in rets_onto:
          print 'Ponderate found obj:',o,o.name 
          rts_n_c=o.get_all()
          print 'Ponderate found obj->tops:',rts_n_c
          for n_c in rts_n_c:
           nrt_oc_comp=nr_atu.clone_nr(nr_atu)
           #===========
           for cons in top_considers:             
            if self.s_compare_dt(nrt_oc_comp,cons):
              nrt_oc_comp.dt=['$$all$$']
           #===========
           print 'Ponderate compare topico:',nrt_oc_comp.dt,n_c.dt            
           chk_i=self.compare_dt_depend(usr,purpose,nrt_oc_comp,n_c,[])
           if chk_i:
             fnds+=1
             found_k=True
             break
     except Exception,e:
      print 'Error pondete funcion:',e
      log.exception("======================")      
     print 'Ponderate min:',len(max_purposes),' ,found:',fnds
     if fnds >=  len(max_purposes):
      print 'Ponderate found collected:',obj
      rts_o.append([attr,obj])
      
    return rts_o 
     
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
     for ap in apub:
       if self.s2_compare_dt(s,ap):
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
      for apu in apub:
       if self.s2_compare_dt(s,apu):
         if s not in self.published:
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
      #for d in s.sinapses:
      # sins.append(d.nr)
    if not f:
     sins.append(s)   
   return sins
   
   
  def get_all_raw(self,row_trans): 
   #row_trans=[]  
   areturn=[]
   #===
   apub=[]
   nrs_d_cmp=self.topicos
   ind_cmp=0
   for spr in nrs_d_cmp:
    fnd_tr=False
    for [s2,s3] in row_trans:
     #print 'row_Trans compare from:',s2.dt,',to:',s3.dt,'nr:',s2,',nr2:',spr
     if spr ==  s2:
      print 'row_Trans from:',s2.dt,',to:',s3.dt 
      fnd_tr=True
      break
    if fnd_tr:
     apub.append(s3)   
    else:    
      if self.compare_nr_Dt( 'interface' ,  spr ) :
        for snc in spr.sinapses:
          apub.append(snc.nr)
      else:
        apub.append(spr)    
   #=====================================        
   if len(apub) > 0 :
     areturn = apub
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
      #for d in s.sinapses:
      # sins.append(d.nr)
    if not f:
     sins.append(s)   
   return sins   
   
  def get_all_static(self): 
   #row_trans=[]  
   areturn=[]
   #===
   apub=[]
   #=====================================        
   if len(apub) > 0 :
     areturn = apub
   elif len(self.topicos)>0:
     areturn = self.topicos   
   else:
     areturn = self.nrs
     
   sins=[]
   for s in areturn:
    f=False
    for d in s.dt:
     if d=='tstatic':
        sins.append(s) 
        break
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
    self.tb=1 # 1->semantic_object, 2->semantic_object3, 3->semantic_object3_1_4
    self.rct=False
  #== 
  def update_links(self):
   collect_links(self,self.name,self_usr)
  def get_Reverse_links(self):
   return collect_links2(self,self.name,self_usr)
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
  def get_links_raw(self):
   rts=[]
   if len(self.links   ) == 0 :
    self.update_links()
   for s in self.links:
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
  def set_link(self,lr,opcode,opcode_seg=[]):
    mc=mdLayerLink(lr,opcode,opcode_seg)
    self.links.append(mc)
  def set_link_ds(self,lr,opcode,foco_o=[],foco_d=[],opcode_seg=[]):
    mc=mdDynamicLayerLink(lr,opcode,opcode_seg)
    mc.foco_o=foco_o
    mc.foco_d=foco_d
    self.links.append(mc)
  def set_link_d(self,d):
    self.links.append(d)
  def get_topico_s(self,dt):
    ns=[]
    for n in self.topicos:
     for d in n.dt:
       if d.upper () == dt.upper():
         ns.append( n )
    return ns
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
  def set_topico_aq(self,dts):
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
  def set_nr_ch_a2(self,top,ch,opcode):
    nr=ch
    top.connect_to(self,nr,opcode)
    return nr
  def set_nr(self,dt):
    nr=mdNeuron(self)
    nr.dt.append(dt)
    self.nrs.append(nr)
    return self.nrs[len(self.nrs)-1]
  def set_nr_arr(self,dt):
    nr=mdNeuron(self)
    nr.dt=(dt)
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
  def get_raw_object_code(self,nm,usr):
     return get_object_by_name(nm,usr,self)
  def get_all_it(self,nm,usr):
     objc2=get_object_by_name([nm],usr,self)
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
       #if d1.upper () ==  d2.upper () or d1.lower()=='$$all$$' or self.compare_data_h(d1,d2) :
       #if mdFuzzy.compare_n(d1,d2) > 0 or mdFuzzy.compare(d1,'$$all$$') > 0 or self.compare_data_h(d1,d2) :
       if mdFuzzy.compare_n(d1,d2) > 0 or d1.lower()=='$$all$$' or self.compare_data_h(d1,d2) :
        afnd=True
        break
       for ex in expand:         
         #if d1.upper () ==  ex.upper () or d1.lower()=='$$all$$':
         #if mdFuzzy.compare_n(d1,ex) > 0 or mdFuzzy.compare(d1,'$$all$$') > 0 :
         if mdFuzzy.compare_n(d1,ex) > 0 or d1.lower()=='$$all$$':
           afnd=True
           break
       if afnd: break       
      #elif d1.upper () ==  d2.upper () or d1.lower()=='$$all$$':
      #elif mdFuzzy.compare_n(d1,d2) > 0 or mdFuzzy.compare(d1,'$$all$$') > 0 :
      elif mdFuzzy.compare_n(d1,d2) > 0 or d1.lower()=='$$all$$' :
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
      if d1.lower()=='dlink':
       lnks=nr2.owner.get_links(d2)
       if len(lnks) > 0 :
        afnd= True   
        break
      #==============================================
      #==============================================            
      if len(expand) > 0 :
       #print 'Compare:',d1.upper(),' with:',expand 
       #if d1.upper () ==  d2.upper () or d1.lower()=='$$all$$'  or self.compare_data_h(d1,d2) :
       #if mdFuzzy.compare_n(d1,d2) > 0 or mdFuzzy.compare(d1,'$$all$$') > 0 or self.compare_data_h(d1,d2) :
       if mdFuzzy.compare_n(d1,d2) > 0 or d1.lower()=='$$all$$' or self.compare_data_h(d1,d2) :
        afnd=True
        break
       for ex in expand:
         #if d1.upper () ==  ex.upper () or d1.lower()=='$$all$$':
         #if mdFuzzy.compare_n(d1,ex) > 0  or  mdFuzzy.compare(d1,'$$all$$') >0 :
         if mdFuzzy.compare_n(d1,ex) > 0  or  d1.lower()=='$$all$$':
           afnd=True
           break
       if afnd: break      
      #elif d1.upper () ==  d2.upper () or d1.lower()=='$$all$$':
      #elif mdFuzzy.compare_n(d1,d2) > 0  or  mdFuzzy.compare(d1,'$$all$$') > 0 :
      elif mdFuzzy.compare_n(d1,d2) > 0  or  d1.lower()=='$$all$$' :
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

  def s2_compare_dt(self,nr,dt):
      for s in nr.dt:
       if dt.upper () == s.upper():
         return True
      return False          
   
  def get_find_path(self,layer,dt,usr,purpose,owner): #   
   def get_all_dt(lay,topico):
    rts=[]
    if True:
     d=lay.get_topico(topico)
     if d!=None:
        for rs in d.sinapses:
          for drs in rs.nr.dt:
            rts.append(drs)
    return rts        
      
   def get_all_dt_raw(lay):
    rts=[]
    for d in lay.topicos:
     #d=lay.get_topico(topico)
     if d!=None:
        for rs in d.sinapses:
          for drs in rs.nr.dt:
            rts.append(drs)
    return rts        
   
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
   def parse1(dt):
    rt=[]
    tmp=''
    for s in dt:
      if s==' ' or s == ',' or s == ')' or s == '(' or s==';' or s == '{' or s == '}':
       rt.append(tmp)
       tmp=''
      else: tmp+=s
    if tmp!='': rt.append(tmp)
    rt2=[]
    for r in rt:
     rtsc=r.split('@') # object@dest-topico
     if len(rtsc) > 1 and len(rtsc) < 3:
       rt2.append(rtsc)
    return rt2
   #========================    
   def parse2(dt):
    rt=[]
    tmp=''
    for s in dt:
      if s==' ' or s == ',' or s == ')' or s == '(' or s==';' or s == '{' or s == '}':
       rt.append(tmp)
       tmp=''
      else: tmp+=s
    if tmp!='': rt.append(tmp)
    rt2=[]
    for r in rt:
     rtsc=r.split('@') # object@opcode-link@dest-topico
     if len(rtsc) > 2 and len(rtsc) < 4  :
       rt2.append(rtsc)
    return rt2
   #========================    
   def parse3(dt):
    rt=[]
    tmp=''
    for s in dt:
      if s==' ' or s == ',' or s == ')' or s == '(' or s==';' or s == '{' or s == '}':
       rt.append(tmp)
       tmp=''
      else: tmp+=s
    if tmp!='': rt.append(tmp)
    rt2=[]
    for r in rt:
     # // get_ontology_s(s[0],s[1],topico_read,usr ): #  considera os purposes nos filtros quando alias == None //get_ontology_s(aliases,purposes,destinats,usr )
     rtsc=r.split('@') # object-@topico-relevante-remote@topico-read(p/ competar dt)@dest-topico  
     if len(rtsc) > 3:
       if rtsc[0] == '?': rtsc[0] = None
       rt2.append(rtsc)
    return rt2
   #  
   print 'Get find-path for :',layer.name,'[',dt,']',' Owner:',owner.name
   #==
   layer.release_filter ()   
   nrs=layer.get_all ()
   if True:
    '''  em cada dt=[a,b,c,...] é um nome de um fact, onde vai ter os topicos implementados. nesses, procurar object->object implementador ou no cenario.objects.find-path=>nome dos objetos pelo apelido passado, ou cenario.objects.find-paths.defs -> definicoes direto no cenario  '''
    all_dt=parse1(dt)  
    all_dt2=parse2(dt) 
    all_dt3=parse3(dt) 
    print 'FdPath:',dt,all_dt
    facts_defs=[]
    lnks=owner.get_links('FACT')
    #print 'lnks:', len(lnks)
    search=[]
    search2=[]
    search3=[]
    if True:
     ln=layer
     for [al,dest] in all_dt:
       tps_a=layer.get_topico(dest)
       search.append( [tp_a,al] )
        #====
    if True:
     for [atp,adt] in all_dt2:
       search2.append( [atp,adt] )
    if True:
     for atp in all_dt3:
       search3.append( atp )
     
    if len(search2) > 0 : # procura por objetos linkados ao obj_orig
     print 'find-path search.2:',search2
     for [obj_orig,opcode_links,dest_topico] in search2:#
        lrse=get_ontology_s2s(obj_orig,opcode_links,usr) # procura por links
        for lr in lrse:
          tp=layer.get_topico(dest_topico)
          if tp != None:
           nr=layer.set_nr(lr.name)
           tp.connect_to(layer,nr,opcode) 
           owner.set_link(lr,opcode_links)
                           
                        
                        
    if len(search3) > 0 :
     print 'find-path search.3:',search3
     #{3}
     for sc in search3:
       #object-@topico-relevante-remote@topico-read(p/ competar dt)@dest-topico
       #
       topico=layer.get_topico(sc[3])
       topico_tag=layer.get_topico('tag') # se houver pedido de identificacao
       if topico_tag !=None:
         topico_tag.sinapses=[]       
       #=======================================
       if topico == None : continue
       topico_read=sc[1]
       #lrs=get_ontology(d,purpose,usr)
       dts_conf=get_all_dt(layer,sc[2])
       ant_z=mdTb.Zeus_Mode=True
       lrs=get_ontology_s(sc[0],dts_conf,[topico_read],usr ) 
       #print 'Get.get_ontology_s_p():'
       mdTb.Zeus_Mode=False
       lrs_1=get_ontology_s(sc[0],dts_conf,[topico_read],usr ) 
       mdTb.Zeus_Mode=ant_z        
       #print 'find.get_obj():(',sc[0],dts_conf,[topico_read],usr,')->',lrs_1,'.',lrs
       for l in lrs_1:
         lrs.append(l)
       #====================================================
       fpaths=[]
       rts=[]
       indc=-1
       for lr in lrs:
         indc+=1
         fpaths=lr.get_all ()
         f_integra=False
         for f in fpaths:
          if self.s_compare_dt(f,'f-sub'):#substituto, remove o topico anterior
           f_integra=True
         rts=fpaths  
         '''
         print 'fpaths:',f_integra
         for p in rts:
           print '.dt:',p.dt
           for a in p.sinapses:
            print '.sin:',a.nr.dt
         print 'caller:',topico.dt
         '''
         #=============
         remote_tag=[]
         if len(rts):
           for p in rts:
            if self.compare_nr_Dt( 'tag' ,  p ) :
               if p not in remote_tag:
                remote_tag.append(p)                
         inserid_tag=False    
         sp1=None         
         #=============
         for t in rts:
            if not self.compare_nr_Dt( topico.dt[0] ,  t ) :continue
            # confere tag
            if not inserid_tag and topico_tag!=None:
              if len(remote_tag)==0:
                 if sp1==None:
                  #set_nr_ch(self,top,dt,opcode) 
                  sp1=topico_tag.owner.set_nr_ch(topico_tag,'tag','Composicao')
                 s2=sp1.owner.set_nr_ch(sp1,'NODEF','Comosicao')
                 print 'set.tag:',s2.dt
                 inserid_tag=True
              for s in remote_tag:
                for s1 in s.sinapses:
                 if sp1==None:
                  sp1=topico_tag.owner.set_nr_ch(topico_tag,'tag','Composicao')
                 sp1.connect_to(topico_tag.owner,s1.nr,'Composicao')
                 print 'set.tag:',s1.nr.dt
                 inserid_tag=True
            #            
            for k in t.sinapses:
             if not f_integra:              
              #print 'tpc:',k.nr.dt
              if indc > 0 :
               topico.connect_to(topico.owner,k.nr,'Composicao'+str(indc))
              else:
               topico.connect_to(topico.owner,k.nr,'Composicao') 
              #for a in topico.sinapses:
              # print '.sin2:',a.nr.dt
             else: 
              layer.add_filter(k.nr) # foca apenas os substitutos
              
         #print 'dump.lr:',layer.dump_layer()                  
    if len(search) > 0 :
     print 'find-path search.1:',search
     for [tps,d] in search:  
       topico=layer.get_topico(tps)
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
         
  def process_Call_RCT(self,data_c,ontology,usr,purpose,relactionate,have_collected):
   print 'Enter.to.call.links.CALL:',self.name
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
      print 'Identify RCT:',node.name
      node.process_RCT(data_c,ontology,usr,purpose,relactionate,have_collected,True )
     else:
      # generic é um objeto que simboliza a chamada de outros, descrevendo em seus destinations os dests a serem procurads em rcts nao likadas, mas q implementem essas destinations    
      rcts=get_ontology(None,generics,usr)
      print 'Identify.2.0 RCT:',rcts
      for r in rcts:
        print 'Identify RCT.2:',r.name
        r.process_RCT(data_c,ontology,usr,purpose,relactionate,have_collected,True )    
   
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
       tps=ev.get_topico_s('destination')
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
                   
  def clone_layer(self):
   rt=mdLayer()
   rt.name=self.name   
   for s in self.topicos:
    nr2 = mdNeuron(rt)
    nr2=nr2.clone_nr(s)
    rt.set_topico_nr(nr2)
   return rt 
    
  #runask(usr,purpc,identif,type_S)   
  def runask(usr,purpose_vocabulario,code,typeS):
    codes=''
    for c in code:
     codes+=( c + ' ')
    cmd = 'python \wamp\www\neural\SemaIndexerStage2.py "'+usr+'" "'+codes+'" "'+purpose_vocabulario+'" "'+typeS+'" '
    os.system(cmd)
    
   
    
  def process_RCT(self,layers,ontology,usr,purpose,relactionate=False,have_collected=[],aj_c=False):        
   # ractionline
   # verbos a serem processados
   #  compare(with need/way/mean)
   #  behaviour(with need/way/mean)
   #  inferencia preditiva(causa-efeito)
   #  inferencia reativa( acao-reacao)    
   #  --------  detectar need/mean/way automatico
   # 
   #obs: get_find_path -> opera nas implementacoes de rct
   #     process_inter_find_path -> opera em objectos, tanto nas rct quanto no paremetro de input "layers", a cada chamada do get_all()
   '''
      formato:
       topico->findpath para cada fact
       links-layer -> cada fact
   '''   
   def get_fct_links():
    rt=[]
    nodes=self.get_links('FACT')
    print 'Layers FACTS:',len(nodes)
    for n in nodes:
     n2=n.lr.clone_layer()
     n.lr=n2
     rt.append(n)
    return rt 
   adm_return=True
   self.rct=True
   print 'Start Call RCT:',self.name , ' ,len buff(' ,len(layers), ')' 
   print 'Cache:[',self.name,']'
   print 'Buffer:[',layers,']'
   for lc1 in layers:
    print '.el:',lc1.name
    #lc1.dump_layer()
   print '===================='
   print 'All-L:len:',len(layers),' ,def:',layers
   aj_return=[]   
   aj_param=[]
   if aj_c:
    for a in layers:
     aj_param.append(a)
   print 'RCT->facts(',self.name,'):'
   for layer_Atu_r in layers:
    print 'RUn layer-cd:================================================================================================================='
    #
    layers_collect=[]    
    layer_Atu_r=layer_Atu_r.clone_layer()
    layers_collect_s=[]    
    rtp=mdLayer ()
    nore=mdLayer ()   
    filtered=[]
    dyned=[]
    nodes=get_fct_links()
    #===
    for ns in nodes:
      print '[',ns.lr.name,']'
    topicos_fpath=self.topicos
    idcx=0
    nodek=[]
    _nds2=[]
    node_cmps=[]
    for node in nodes:
     node=node.lr
     node=node.clone_layer()
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
     nodek.append(node)    
     #_nds2=nodek.get_all_raw(node_cmps)     
     print 'NDS:======','[',node.name,']'
     for n1 in nds:
      print '---------'
      if self.s_compare_dt(n1,'source') or self.s_compare_dt(n1,'destination') or \
        self.s_compare_dt(n1,'compare') or \
        self.s_compare_dt(n1,'autoask') or \
        self.s_compare_dt(n1,'no_return') or \
        self.s_compare_dt(n1,'behavior') or \
        self.s_compare_dt(n1,'raw_afininity') or \
        self.s_compare_dt(n1,'preditive') or \
        self.s_compare_dt(n1,'reactive') or \
        self.s_compare_dt(n1,'link') or \
        self.s_compare_dt(n1,'rename') or \
        self.s_compare_dt(n1,'link-nr') or \
        self.s_compare_dt(n1,'filter') or \
        self.s_compare_dt(n1,'collect') or \
        self.s_compare_dt(n1,'collect_s') or \
        self.s_compare_dt(n1,'collect_apr')or\
        self.s_compare_dt(n1,'gravity')or\
        self.s_compare_dt(n1,'refuzzy')or\
        self.s_compare_dt(n1,'interface'):
          continue
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
     #== 
     for n1 in nds:
      if self.s_compare_dt(n1,'source') or self.s_compare_dt(n1,'destination') or \
        self.s_compare_dt(n1,'compare') or \
        self.s_compare_dt(n1,'no_return') or \
        self.s_compare_dt(n1,'autoask') or \
        self.s_compare_dt(n1,'behavior') or \
        self.s_compare_dt(n1,'raw_afininity') or \
        self.s_compare_dt(n1,'preditive') or \
        self.s_compare_dt(n1,'reactive') or \
        self.s_compare_dt(n1,'link') or \
        self.s_compare_dt(n1,'rename') or \
        self.s_compare_dt(n1,'link-nr') or \
        self.s_compare_dt(n1,'filter') or \
        self.s_compare_dt(n1,'collect') or \
        self.s_compare_dt(n1,'collect_s') or \
        self.s_compare_dt(n1,'interface')or\
        self.s_compare_dt(n1,'gravity')or\
        self.s_compare_dt(n1,'refuzzy')or\
        self.s_compare_dt(n1,'collect_apr') or\
        \
        self.s_compare_dt(n1,'interface') :
          pass
      else: 
       need_s+=1 
     #==========    
     tps_len=0
     '''
       ==================================================
       ==================================================
     '''
     
     
     indckl=1     
     if True:
      l=layer_Atu_r
      #get_all() -> l.process_inter_find_path()
      print 'def-L:',l,',n:',indckl
      indckl+=1
      dyned.append(l)
      l.process_inter_find_path(purpose)
      nds2=l.get_all ()      
      #print 'dump.nds2-----------------------------------------------------'
      #l.dump_layer()
      print 'NDS2:======[',l.name,']'
      for n1 in nds2:
       print '----------'
       print n1.dt
       for snds in n1.sinapses:
        print '++++++++++++++'
        print snds.nr.dt
        print '++++++++++++++'
       print '----------'
      print '==========='
      colect_gr=[]
      tps_len=0
      rt=mdLayer ()
      print 'NDS-LEN:',len(nds) ,'================='
      if len(nds)>0: print 'nds[0].owner:',nds[0].owner.name
      for d in nds:
       print d.dt,'<<'
      print '======================================'      
      for nr_atu in nds:
        _nds2=[]
        verbo_compl=[] # dados complementares do filtro
        for e in nodek:
         _nds22=e.get_all_raw(node_cmps)
         for _nd in _nds22 :
          _nds2.append(_nd)
        #=== 
        verbo='vbNoDef'      
        if self.s_compare_dt(nr_atu,'no_return'):
         verbo='vb_no_return'
        if self.s_compare_dt(nr_atu,'compare'):
         verbo='vb_compare'
        if self.s_compare_dt(nr_atu,'autoask'):
         verbo='vb_auto_ask'
        if self.s_compare_dt(nr_atu,'behavior'):
         verbo='vb_behavior'
        if self.s_compare_dt(nr_atu,'raw_afininity'):
         have_collected.append(True)
         verbo='vb_afininity_raw'
        if self.s_compare_dt(nr_atu,'preditive'):
         verbo='vb_preditiva'
        if self.s_compare_dt(nr_atu,'reactive'):
         verbo='vb_reactive'
        if self.s_compare_dt(nr_atu,'link'):
         verbo='vb_link'
        if self.s_compare_dt(nr_atu,'rename'):
         verbo='vb_rename'
        if self.s_compare_dt(nr_atu,'link-nr'):
         verbo='vb_link_nr'
        if self.s_compare_dt(nr_atu,'filter'):
         verbo='vb_filter'
        if self.s_compare_dt(nr_atu,'collect'):
         have_collected.append(True)
         verbo='vb_collect'
        if self.s_compare_dt(nr_atu,'collect_s'):
         have_collected.append(True)
         verbo='vb_collect_s'
        if self.s_compare_dt(nr_atu,'collect_apr'):
         have_collected.append(True)
         verbo='vb_collect_apr'
        if self.s_compare_dt(nr_atu,'gravity'):
         verbo='vb_gravity'
        if self.s_compare_dt(nr_atu,'refuzzy'):
         verbo='vb_refuzzy'
        if verbo !=  'vbNoDef':
         for s in nr_atu.sinapses:
          for ds in s.nr.dt:
           verbo_compl.append(ds)
        #=============================================   
        if verbo=="vb_auto_ask":
         identif=[]
         type_S="1"
         purpc=purpose
         for nr_t in _nds2:
          if self.s_compare_dt(nr_t,'composicao'):
           for s in nr_t.sinapses:
            for d in s.nr.dt:
             identif.append(d)
          if self.s_compare_dt(nr_t,'datatype'):
           for s in nr_t.sinapses:
            for d in s.nr.dt:
             type_S=(d)
             break
          if self.s_compare_dt(nr_t,'destination'):
           for s in nr_t.sinapses:
            for d in s.nr.dt:
             purpc=(d)
             break
         if len(identif) > 0 :
           runask(usr,purpc,identif,type_S)         
        #======================================== 
        if verbo == 'vb_no_return':
          adm_return=False
        if verbo=='vb_compare':
         print 'Run.(',verbo,')'
         # achar identificador
         # achar dest
         # gerar comparativo
         # anotar igualdades
         # anotar diferencas
         for nr_t in _nds2:
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
        #==============================
        if verbo=='vb_refuzzy': # 
         if len(verbo_compl) > 1:
          refz=[]
          s=verbo_compl[0] 
          purp2=''
          if len(verbo_compl)>1:
            purp2=verbo_compl[1] 
          for nr_t in _nds2:          
              if self.s_compare_dt(nr_t,s):
               for ss in nr_t.sinapses:
                for d in ss.nr.dt:
                 refz.append(d)
          if len(refz) > 0 :
            import reFuzzy
            #entry(['groupon classe'], ['simple-search-classify'],'igor.moraes')
            rts=reFuzzy.entry(refz,purp2)
            if len(rts) > 0 :
              layers=[]
            for r in rts:
              layers_collect_s.append(r)
        #==============================
        if verbo=='vb_gravity': # collect aproux -> collect em cima de caracts mencionadas         
         direction=verbo_compl[0]
         opcode='refer-C'
         if len(verbo_compl) > 1:
          opcode=verbo_compl[1]
         #
         print 'Gravity point(',direction,',',opcode,',',colect_gr,')==========================='
         if direction == "L":
          tpsd=[]
          for k in nds2:
           print 'Proces nr gravity:',k.dt,k
           ntin=False
           fnd_tps=None
           for [t1,t2] in colect_gr:
            #print 'Nr.gravity:',k,',nr.collect:',t1
            if t1 == k:
              ntin=True 
              fnd_tps=t1             
           if not ntin:          
            tpsd.append(k)
           else:            
            if fnd_tps  :
             tp=fnd_tps
             for cos in tpsd:
                print 'Gravity:from',tp.dt,' to:',cos.dt
                #=== 
                tp.connect_to(cos.owner,cos,opcode)
            tpsd=[]             
            
         if direction == "R":
          topk=None
          foundCK=False
          for k in nds2:      
           dtsk=[]
           if topk != None:
            dtsk=topk.dt
           print 'Proces nr gravity:',k.dt,k,foundCK,topk,dtsk,',tps_len:',tps_len
           ntin=False
           fnd_tps=None
           for [t1,t2] in colect_gr:
            #print 'Nr.gravity:',k,',nr.collect:',t1
            if t1 == k:
              ntin=True 
              fnd_tps=t1  
              foundCK=False              
           if (not ntin) and foundCK and topk != None:   
            print 'Gravity:from',topk.dt,' to:',k.dt  
            topk.connect_to(topk.owner,k,opcode)
           elif ntin:            
            if tps_len > 0 and fnd_tps != None :
             topk=fnd_tps
             if topk == k:
              #if foundCK:
              # break
              foundCK=True
          
         print 'End.Gravity point==========================='
           
 
        #==============================
        if verbo=='vb_collect_apr': # collect aproux -> collect em cima de caracts mencionadas
          #usado para gerar relacao de layers a processar para o call de outra ractionline, fazer coleta de objetos com determinadas caracts
          print 'Run.(',verbo,')' 
          identif=[] # objects  
          referencia=[]
          purpose2=[]
          for nr_t in _nds2:
              if self.s_compare_dt(nr_t,'objective'):
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
          for nr_t in _nds2:
              if self.s_compare_dt(nr_t,'objective'):
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
           print 'Collect->result(',id,',',referencia,',',purpose2,',',usr,').[',ob,']'
           for [mx,obs] in ob:
            layers_collect.append(obs)
          
        if verbo=='vb_afininity_raw':# collect by two objects caracts
          print 'Run.(',verbo,')'
          identif=[] # objects  
          referencia=[]
          purpose2=[]
          dfin=[]
          tag_S=[]
          sinapses_consid=[]
          for nr_t in _nds2:
              #print 'Nr-C-COLL',nr_t.dt
              # identificador -> object atual com as carats a implementar
              if self.s_compare_dt(nr_t,'identificador') or self.s_compare_dt(nr_t,'ids2'):
               puc=''
               for s in nr_t.sinapses:
                for d in s.nr.dt: 
                 puc+=' '+d
               puc=umisc.trim(puc) 
               if puc != '':
                purpose2.append(puc)
              if self.s_compare_dt(nr_t,'rule'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 r=None
                 for [title,refs] in referencia:
                   if title == s.opcode :
                     r=refs  
                 if r==None:
                   referencia.append([s.opcode,[]])
                   r=referencia[len(referencia)-1][1]
                 if umisc.trim(d) != '':  
                  r.append(d)
              #source ==> objects collected to compar   
              if self.s_compare_dt(nr_t,'plus'): #plus, adicionam para ponderar
               for s in nr_t.sinapses:
                 for d in s.nr.dt:               
                  identif.append(d)
              #========================================    
              if self.s_compare_dt(nr_t,'dfin'):  
               for s in nr_t.sinapses:
                 for d in s.nr.dt:               
                  dfin.append(d)
              #========================================    
              if self.s_compare_dt(nr_t,'sins'):  
               for s in nr_t.sinapses:
                 for d in s.nr.dt:               
                  sinapses_consid.append(d)
              if self.s_compare_dt(nr_t,'tag'):  
               for s in nr_t.sinapses:
                  print 'collect.tag_s:',s.nr.dt
                  if len(s.nr.dt) > 0 :
                   if s.nr.dt[0] != '':
                    tag_S.append(s.nr)                  
                   
          if len(purpose2) <= 1:
            #conferir se orig => none, usar os ja coletados como name
            f1=False
            if len(purpose2) ==1:
              if purpose2[0] == '$cache':
                f1=True
            else:
               purpose2.append('')
            if f1:
                purpose2=[]
                for lc2 in layers:
                 purpose2.append(lc2.name)  
                 for lc22 in lc2.get_links_raw(): 
                  purpose2.append(lc22.lr.name)           
          for id in purpose2:
           print 'Purpose.1:',id   
           inds_tag=-1           
           if id == '$$all$$': id=''
           for [sinapse,referencia2] in referencia:
            inds_tag+=1
            print 'tag_S.len(',len(tag_S),')'
            if len(tag_S) > inds_tag:
              print 'tag_S(',inds_tag,'):',tag_S[inds_tag]
            #===           
            print 'Collect_raw->result==>params:','{',id,'}',referencia2,identif,usr,purpose,referencia2,dfin,sinapses_consid
            ob=self.s_get_ontology_ponderate_caracts(id,referencia2,identif,usr,purpose,referencia2,dfin,sinapses_consid )
            print 'Collect_raw->result(',id,',',referencia2,',',identif,',',usr,').{',ob,'}'           
            for [mx,obs] in ob:
             d1=''
             if len(verbo_compl) > 0 :
              d1=verbo_compl[0]
             print 'layers_collect_s:',[obs,d1]            
             layers_collect_s.append([obs,d1])  
             if obs!= None:
               print 'Input.process:',obs.name 
               layers=[]
               if len(tag_S) > inds_tag:
                print 'connect.tags.'
                tags = tag_S[inds_tag]
                obs.set_topico_nr(tags)               
               obs.dump_layer()
            
          
        if verbo=='vb_collect_s': # collect  -> collect em ponderacao
          #usado para gerar relacao de layers a processar para o call de outra ractionline, fazer coleta de objetos com determinadas caracts
          print 'Run.(',verbo,')'
          identif=[] # objects  
          referencia=[]
          purpose2=[]
          for nr_t in _nds2:
              #print 'Nr-C-COLL',nr_t.dt
              if self.s_compare_dt(nr_t,'objective'):
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
          
          if len(identif) == 0 :
           ob=[]
           if len(referencia) > 0  or len(purpose2) > 0 :
            ob=self.s_get_ontology_ponderate(None,referencia,purpose2,usr )
           print 'Collect->result(',None,',',referencia,',',purpose2,',',usr,').{',ob,'}'           
           for [mx,obs] in ob:
            d1=''
            if len(verbo_compl) > 0 :
             d1=verbo_compl[0]
            #print 'layers_collect_s:',[obs,d1]
            layers=[]
            layers_collect_s.append([obs,d1])    
          
          for id in identif:
           ob=self.s_get_ontology_ponderate(id,referencia,purpose2,usr )
           print 'Collect->result(',id,',',referencia,',',purpose2,',',usr,').{',ob,'}'           
           for [mx,obs] in ob:
            d1=''
            if len(verbo_compl) > 0 :
             d1=verbo_compl[0]
            #print 'layers_collect_s:',[obs,d1]
            layers_collect_s.append([obs,d1]) 
            layers=[]
            
        #==============================     
        if verbo=='vb_filter': 
          # usado para criar um publish( filtro de nrs em cadeia que sobem p topicos, dentro de uma chamada de rct)
          print 'Run.(',verbo,')'
          
          identif=[] # objects 
          alias=[]
          refer=[] # links
          for nr_t in _nds2:          
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'alias'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 alias.append(d)
              if self.s_compare_dt(nr_t,'refer'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 refer.append(d)

          
          fnd_al=False
          if len(alias) > 0:
           for nr_t in _nds2:
            for al in alias:           
              if self.s_compare_dt(nr_t,al):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 fnd_al=True
          
          if len(alias) > 0 and fnd_al:
           identif=[] # desconsidera identificador

                 
          if len(alias) > 0:
           for nr_t in _nds2:
            for al in alias:           
              if self.s_compare_dt(nr_t,al):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
                 
          print 'Params:','[',identif,'],[', alias,'],[' ,refer ,']' 
          
             
          for id in identif:
           ob=get_ontology( id,purpose,usr )
           # capturar filtros 
           for obh in ob:
            print 'Filter.obj:',obh,obh.name,'==============='
            for tps in obh.topicos:
             print tps.dt
            print 'Filter.obj.end:',obh,obh.name,'===========(',type_coll,')'
           objs_lnk=[]
           for fl in refer:
            for obj in ob:
             obj.update_links()
             print 'Ob.links-len:',len(obj.links)
             for lk in obj.links :
              print 'Ob.links:',lk.opcode
              if lk.opcode.upper() == fl.upper():
               objs_lnk.append([lk.lr,fl])
           #===============
           if True:
            for o in ob:
             d1=''
             if len(verbo_compl) > 0 :
              d1=verbo_compl[0]
             #==   
             
             print 'Filter.do(',o.name,',',refer,')'             
             filtered.append(o)
             
             for [oc,opcode_f] in objs_lnk:   
              print 'Get.onto:',oc.name
              oc2=get_ontology( oc.name,purpose,usr ) 
              for oc in oc2:               
               print 'Filter.links(',oc.name,',tops:',oc.topicos,')'               
               #==  
               if len(oc.topicos) > 0:
                ntp=o.set_topico('reference')
                nr2=o.set_nr(oc.name)
                ntp.connect_to(o,nr2,'Composicao')
                #o.set_nr_ch(ntp,nr2,'Composicao')
                ntp=o.set_topico('reference2')
                nr2=o.set_nr(opcode_f)
                ntp.connect_to(o,nr2,'Composicao')
                #======================
               for t in oc.topicos:
                #print 'Filter.append:',t.dt
                o.set_topico_nr(t)
              
             print 'o.do_filter:',o.name 
             o.do_filter(verbo_compl)
             layers=[]
             layers_collect_s.append([o,d1]) 
        #=============================================================       
        if verbo=='vb_rename': # so opera nos layers_collect
          # linkar objetos, 'referencia' -> 'identificador' em 'purpose' -> motivo
          print 'Run.(',verbo,')->rnm'
          print 'Params:','[',verbo_compl,'],[', layers_collect,'],[',layers_collect_s,']' 
          if len(verbo_compl) > 1:
           for nr in nds2:
            old=verbo_compl[0]
            new=verbo_compl[1]
            if self.s_compare_dt(nr,old):
              print 'VB-rename :',old,', to:',new
              nr.dt[0]=new
              pass
    
               
        #=============================================================        
        if verbo=='vb_link':
          # linkar objetos, 'referencia' -> 'identificador' em 'purpose' -> motivo
          print 'Run.(',verbo,')'
          identif=[] # objects  
          referencia=[]
          purposes=[]
          foco=[]
          condition=[]
          for nr_t in _nds2:
              if self.s_compare_dt(nr_t,'identificador'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 identif.append(d)
              if self.s_compare_dt(nr_t,'orig'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 referencia.append(d)
              if self.s_compare_dt(nr_t,'opcode'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 purposes.append(d)
              if self.s_compare_dt(nr_t,'foco'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 foco.append(d)
              if self.s_compare_dt(nr_t,'condition'):
               for s in nr_t.sinapses:
                for d in s.nr.dt:
                 condition.append(d)
          
          print 'Params:',identif,referencia, purposes ,foco ,condition,have_collected   
          #####
          #have_collected=[]          
          #####
          for id in identif:
           ob=get_ontology( id,purpose,usr )
           print 'Onto:',ob
           for o in ob:
            ob2=[]
            if len(have_collected) == 0:
             for id2 in referencia:
              ob22 = get_ontology( id2,purpose,usr )
              print 'Onto-REF:',id2,purpose,usr,'->',ob22
              for o22 in ob22:
               ob2.append(o22)
            else:
              ob2=layers   
              print 'Collected used:',have_collected,layers
              for s in layers:
               print '[',s.name,']'
            for o2 in ob2:
              #=============
              if umisc.trim(o2.name) == ''  or umisc.trim(o2.name) == '__TST__' : continue
              focus_o=[]
              focus_d=[]
              linkds=False
              if len(foco) > 0 :
               for foc in foco :
                tps=o.get_topico(foc)
                foco_o.append(tps)
               for foc in foco :
                tps=o2.get_topico(foc)
                foco_d.append(tps)
               for p in purposes:
                print 'Process link(1):',o.name,o2.name
                o.set_link_ds(o2,p,foco_o,foco_d,condition) 
                linkds =True
              else:             
               for p in purposes:
                print 'Process link(2):',o.name,o2.name
                o.set_link_ds(o2,p,[],[],condition)                 
                linkds=True
              # save presistable
              if linkds:
               print 'Post linked layer:',o.name
               post_object_by_data_es(o,usr)
               #post_object_by_data_es(o2,usr) 
        #==========================        
        if verbo=='vb_link_nr':
          print 'Run.(',verbo,')'
          # linkar objetos, 'referencia' -> 'identificador' em 'purpose' -> motivo
          identif=[] # objects  
          referencia=[]
          purposes=[]
          for nr_t in _nds2:
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
           ob=get_ontology( id,purpose,usr )
           for o in ob:
            for id2 in referencia:
             ob2 = get_ontology( id2,purpose,usr )
             for o2 in ob2:
              #=============
              nr1=o.get_all () # considerando filter ativo
              nr2=o2.get_all ()
              for n1 in nr1:
               for n2 in nr2:
                for p in purposes:
                 nr1.connect_to(n1.owner,n2,p)
             # persist layers
             #post_object_by_data_es(ob,usr): 
             #post_object_by_data_es(ob2,usr): 
          
            
        if verbo=='vb_behavior': #( discreta(em foco), intermitente(sem referencia),mutacao fact(actions aplicados/historico de acoes) )
          # procurar mutacoes em caracts de 'identificador'
          # procurar mutacoes em foco -> 'referencia'
          # mutacoes, sequencias de actions -> facts 
          print 'Run.(',verbo,')'          
          identif=[] # objects  
          referencia=[]
          action=[]
          for nr_t in _nds2:
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
           # 
           ####node_cmps.append([nr_atu,nr_atu.mont_return_data2() ])
           node_cmps.append([nr_atu,n_c ])           
           ###
           rt.set_topico_nr(n_c)                                 
           #print 'compare:',nr_atu.dt,n_c.dt,' result:',fnd_comp   
           colect_gr.append([n_c,nr_atu]) 
        if fnd_comp:         
         tps_len+=1           
         ###rt.set_topico_nr(nr_atu)                                                 
        else:
         nore.set_topico_nr(nr_atu)        
         
         
      #=======================          
      
      '''
      tps=rt.topicos
      rt.topicos=[]
      for r in tps:
       r2=mdNeuron(r.owner)
       r2=r.mont_return_data(tps,foco) 
       if r2!=None:               
        rt.set_topico_nr(r2)
      '''
      
      print 'NEED:',need_s,',FOUND:',tps_len
      if tps_len >= need_s :
       ''' adicionar  os not inface , se tiver '''       
       nrs=node.get_all_no_interface ()
       nrs_static=node.get_all_static()
       dt_ts=[]
       def dump_t(nr):
        r=[]
        r.append(nr.dt)
        r.append('sins-----')
        for d in nr.sinapses:
         i=dump_t(d.nr)
         for a in i:
          r.append(i)
        return r 
       for s in rt.topicos:
        s=dump_t(s)
        for a in s:
         dt_ts.append(a)
        
       print 'RCT->interface(1):',nrs,len(nrs),rt.topicos,'->>' #,dt_ts
       print 'RCT->STATIC:',nrs_static,',foco:',layers_collect_s
       for [ob_atu,vb] in layers_collect_s:
        for n in nrs_static: 
         for n2 in n.sinapses: 
          ob_atu.set_topico_nr(n2.nr)
        #print 'dump.coll...'
        #ob_atu.dump_layer()        
       #rt.dump_layer()
       if len(nrs) > 0:
        # so retorna os n interface.nos q tem interface declarada, usa eles p conferencia e complemento(find-path),etc... mas n retorna as interfaces
        rt.topicos=[]
       for n in nrs:
         rt.topicos.append(n)
       '''adicionar no rtp'''
       for n in nrs_static: 
         rt.topicos.append(n)       
       for ts in rt.topicos:
        rtp.set_topico_nr(ts)
       #=====================
       rt=None   
      else : pass
    if len(nodes) == 0 and len(rtp.topicos) <= 0:
      i_ls=layers
      #print 'Prepare to call-inter-rtc(1)[',self.name,']:' ,layers_collect_s,i_ls,layers_collect
      print 'Prepare to call-inter-rtc(1)[',self.name,']:' ,layers_collect_s
      #process_Call_RCT(self,data_c,ontology,usr,purpose,relactionate)
      if len(layers_collect_s) > 0 and len(i_ls) > 0:
       for [ll,top_s] in layers_collect_s:
        s2=ll.name
        lr=i_ls[0]
        lr.set_topico_aq([top_s,s2])
        
      if len(layers_collect) > 0:
       i_ls=layers_collect
       
      if len(layers_collect_s) > 0:
       if len(layers_collect) == 0:
        i_ls=[]
       for l in layers_collect_s:
        i_ls.append(l)
      for ass in i_ls:
       if ass  not in aj_param:
        aj_param.append( ass )      
      
    
    if len(rtp.topicos) > 0 :
      print 'Call Layout-Code from:',self.name
      layout_codes=self.get_links('LAYOUT-CODE')
      #===
      i_ls=[rtp]
      #print 'Prepare to call-inter-rtc(2):' ,layers_collect_s,i_ls
      print 'Prepare to call-inter-rtc(2):' ,layers_collect_s
      if len(layers_collect_s) > 0 and len(i_ls) > 0:
       for [ll,top_s] in layers_collect_s:
        s2=ll.name
        print 'Call-layout-name:',s2,layers
        if len(layers) > 0 :
         lr=layers[0]        
         lr.set_topico_aq([top_s,s2])   
        else:
         i_ls.append(l) 
      #====================================  
      if len(layers_collect) > 0:
       i_ls=layers_collect   
       
      if len(layers_collect_s) > 0:
       if len(layers_collect) == 0:
        i_ls=[]
       for l in layers_collect_s:
        i_ls.append(l)
      #================
      nms=[]      
      for d in layout_codes:
       nms.append(d.lr.name)
      print 'Prepare to call layouts-code---{',nms,'}'
      rtps=[rtp]
      for d in layers_collect:
       rtps.append(d)
      for d in layers_collect_s:
       rtps.append(d[0])
      print 'Collect objects:',layers_collect,layers_collect_s 
      prepare_search_customlayouts(self,nms,rtps,usr,relactionate) #purposes,dts,usr
      layers_collect = []
      layers_collect_s =[]
      print 'layouts-code executed. ---'
      #print 'Lr:n',rtp.name
      #===
      #process_Call_RCT(self,data_c,ontology,usr,purpose,relactionate)
      #======================================== 
      for ass in i_ls:
       if ass  not in aj_param:
        aj_param.append( ass )      
      
      #self.process_Call_RCT(i_ls,ontology,usr,purpose,relactionate)
      for s in dyned:
       s.release_din_sinapse()
      for s in filtered:
         s.release_filter ()
      aj_return.append( [rtp,nore] )
      
      continue
    for s in filtered:
     s.release_filter ()
    for s in dyned:
     s.release_din_sinapse()
    #aj_return.append( [None,None] )
    continue
    #====    
   if len(layers) == 0 and len(get_fct_links()) == 0: # se rct fazia e sem nodes, pode ser entry point
    print 'Process call empty rct.'    
    self.process_Call_RCT([],ontology,usr,purpose,relactionate,have_collected)
     
   if len(aj_param) and adm_return :
    #print 'layers:',layers  
    if aj_c:
     for a in aj_param:
      if type(a) == type([]):
       if a[0] not in layers :
        layers.append(a[0])             
      else:
       if a not in layers:
        layers.append(a)
    #print 'aj_param:',layers  
    #print 'aj_param(2):',aj_param
    print 'Process call lrs len(',len(aj_param),')'
    self.process_Call_RCT(aj_param,ontology,usr,purpose,relactionate,have_collected)
   if len(aj_return):
    al1=mdLayer()
    al2=mdLayer()
    print 'aj_return:',aj_return
    for [l1,l2] in aj_return:
      for a1 in l1.topicos:
       al1.set_topico_nr(a1)
    for [l1,l2] in aj_return:
      for a2 in l2.topicos:
       al2.set_topico_nr(a2)
    #==========================  
    return [al1,al2] 
   return [None,None]    
    
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
      '''
      tps=rt.topicos
      rt.topicos=[]
      for r in tps:
       r2=mdNeuron(r.owner)
       r2=r.mont_return_data(tps,foco) 
       if r2!=None:
        rt.set_topico_nr(r2)
      '''  
      print 'NEED:',need_s,' FOUND:',tps_len
      if tps_len >= need_s :
       ''' adicionar  os not inface , se tiver '''       
       nrs=node.get_all_no_interface ()
       print 'RCT->interface(2):',nrs,len(nrs),rt.topicos
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
  

    
    
    