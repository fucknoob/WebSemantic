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

def init_cenario_ng_cliente(stack):
  p_ass='cen-cliente-g-st-coll'
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
   cen.rcts=['cenario-ecomm-product-classify-elements' ]
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
 cur_cen=init_cenario_ng_cliente(stack)
 for cn in cur_cen:
  for rct in cn.rcts:
   print 'ALias(C):',rct
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
         l.set_nr_ch(nrt,'classify','composicao')
         print 'RCT Ask Call-TO-Process:',l,l.name
         stack.proc_pg.call_process(usr,[l])
   print '--------------------------------------'



