#EXEC
import mdER
import mdNeural

class stack_base:
 def __init__(self):
  self.cenarios=[]
  self.assinat=''

class base_cenario_client:
 def __init__(self):
  self.rcts=[]
  self.perfil=[]

def init_stack(stack):
   stack=stack_base()

def init_cenario_class_cliente(stack):
  p_ass='cen-cliente-st'
  fnd=False
  stck=None
  for s in stack.stack:
   if s.assinat == p_ass:
    fnd=True
    stck=s
    return stck.cenarios
  if not fnd:
   cen=base_cenario_client()
   #==============
   #cen.rcts=['ask-aswer-classif-response','ask-aswer-aderency-product-response' ]
   cen.rcts=['ask-aswer-aderency-product-response2' ]
   cen.ojects_findp=[]        #define objects de findpath
   cen.defs_findp=[] #definicoes diretas de find-path
   cen.perfil=[]
   b=stack_base()
   b.assinat=p_ass
   b.cenarios.append(cen)
   stack.stack.append(b)
   return b.cenarios
  #========================
  print '----------------------------------------------------------------------'
  print len(stack.stack),':-->stack'
  print '----------------------------------------------------------------------'

def run( layers,relactionado,startL,usr,stack):
 print 'Start compile cenary:----------'
 cur_cen=init_cenario_class_cliente(stack)
 ids=[]
 master_id=''
 for k in layers:
   for tp in k.topicos:
    if 'identificador' in tp.dt or 'object' in tp.dt:
     for tp2 in tp.sinapses:
      #print 'identificador.master(ids):',tp2.nr.dt
      master_id=tp2.nr.dt[0]
     ids.append(tp)
 stack.kstermo=[]
 stack.kstermo.append(None)
 stack.kstermo.append(None)
 stack.kstermo.append(master_id)
 for cn in cur_cen:
  for rct in cn.rcts:
   print 'ALiass:',rct
   second_Rcts=mdER.get_RactionLines2C(rct,usr)
   print 'len.rcts(O) [',len(second_Rcts),']'
   print '......................................'
   for s in second_Rcts:
    #print 'S:',s
    for l in s:
     if type(l).__name__ == 'instance':
      if l.__class__.__name__ == 'mdLayer':
         print 'RCT-fnd:',l.name
         nrt=l.set_topico('purpose')
         l.set_nr_ch(nrt,'interact.need','composicao')
         #===================
         #lr_rct1_Arr=l.get_raw_object_code(['apps_aderencia_with_cenario'],usr)
         linksl=l.get_links('CALL')
         print 'Coll.fact.call:',linksl
         for ln2 in linksl:
          #if ln2.lr.name.upper() != 'process_aderencia_filter2'.upper(): continue
          fcts=ln2.lr.get_links('FACT')
          print 'get.fcts(2):',fcts
          for l2 in  fcts:
           ln=l2
           print 'Cenario.set.rule->getob():',l2.lr.name
           #if  ln.lr.name.upper() != 'apps_aderencia_with_cenario'.upper() : continue
           #print 'dmpc1.:'
           #ln.lr.dump_layer()
           if False: # se false, implementa por find-path, se true, diretamente
            lr_rct1=ln.lr
            nrt=lr_rct1.get_topico('rule') # caract ponderante para o rct [ask-aswer-aderency-product-response], que vai definir quais rules coletar
            print 'cenar->set_rule():',nrt
            if nrt != None:
             nrt.sinapses=[]
             lr_rct1.set_nr_ch(nrt,'Senhor','Composicao')
             lr_rct1.set_nr_ch(nrt,'dos','Composicao')
             lr_rct1.set_nr_ch(nrt,'An\xe9is','Composicao')
           for idk in ids:
              lr_rct1=ln.lr
              lr_rct1=l
              nrt=lr_rct1.set_topico_nr(idk)

         print 'RCT Ask Call-TO-Process:',l,l.name
         #print 'dump.l:',l.dump_layer()
         stack.proc_pg.call_process(usr,[l],True)
   print '--------------------------------------'



