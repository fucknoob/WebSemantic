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

def init_cenario_class_facebook(stack):
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
   # classify-composicao -> montagem das caracts nos elementos definitivos(SEMANTIC_OBJECT3_1_4)
   # classify-class-> gravar objetos no SEMANTIC_OBJECT3_1_4 e linkar os pertencentes a essa classe com mdlayerlink.opcode=class
   # classify-events -> organizcao de eventos dentro dos objetos definitivos
   #   events-> sao linkados como historico nos objetos envolvidos, destacando os actions e qualificadores envolvidos
   cen.rcts=['gerencial_mean' ]
   cen.ojects_findp=[]        #define objects de findpath
   cen.defs_findp=[['identificador','groupon']] #definicoes diretas de find-path
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
 cur_cen=init_cenario_class_facebook(stack)
 lrK=mdNeural.mdLayer()
 #set_topico_a
 obs_defs=[]
 for l in layers:
  print 'FACE-LR-DUMP:============'
  ids=l.name
  for u in l.topicos :
   #print 'dt:(t):',u.dt,'\n'
   if 'with' in u.dt:
     for d in u.sinapses:
      for dt in d.nr.dt:
        obs_defs.append(dt)
   if 'object' in u.dt:
    u.dt=['identificador']
    lrK.set_topico_nr(u)
    print 'DIS:',u.sinapses
  lrK.name='__TST__'
  print 'FACE-LR-DUMP:(END)========='
  #lrK.set_topico_aq(['quality',''])
  #lrK.set_topico_aq(['rule','mean'])
  
  # inicializar extrutura do cenario a ser procurado no facebook===
  print '[obs_defs]:{',obs_defs,'}'
  obs=[]
  secs=[]
  for nm in obs_defs:
   print 'ALiass(obj-def):',nm
   second_Rcts=mdER.get_RactionLines2C(nm,usr)
   print 'len.rcts(O) [',len(second_Rcts),']'
   print '(obj-def)......................................:)'
   secs.append(second_Rcts)

  if len(secs) ==0:
   return

  to_Search=[]
  to_Search_C=[]
  to_Search_A=[]
  for s1 in secs:
   for s in s1:
     #print 'S:',s
     for l in s:
      if type(l).__name__ == 'instance':
       if l.__class__.__name__ == 'mdLayer':
        print 'LR-FCB-RETURN:',l,l.name
        fcts=l.get_links('FACT')
        for fct in fcts:
         for u in fct.lr.topicos :
           if 'composicao' in u.dt:
             for d in u.sinapses:
               for dt in d.nr.dt:
                to_Search_C.append(dt)
           if 'action' in u.dt:
             for d in u.sinapses:
               for dt in d.nr.dt:
                to_Search_A.append(dt)
         for u in fct.lr.topicos :
           if 'identificador' in u.dt:
             for d in u.sinapses:
               for dt in d.nr.dt:
                if len( to_Search_A ) == 0:
                 for c in to_Search_C:
                  dt2=dt+' '+c + ' brasil'
                  to_Search.append(dt2)
                elif len( to_Search_C ) == 0:
                 for c in to_Search_A:
                  dt2=dt+' '+c + ' brasil'
                  to_Search.append(dt2)
                else:
                 for c2 in to_Search_A:
                  for c in to_Search_C:
                   dt2=dt+' '+c + ' ' + c2 + ' brasil'
                   to_Search.append(dt2)

  import collect_it_fcb

  print 'to_Search:{',to_Search,'}'

  if len(to_Search)==0: return
  
  collect_it_fcb.clean_marcador()
  collect_it_fcb.entry_Sents(to_Search,usr)

  return
  
  
  



