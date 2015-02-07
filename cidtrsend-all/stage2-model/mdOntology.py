# coding: latin-1

'''
fuzzy:
[elemento-principal], [limite(elementos-ini-fim)] ,[elementos-aceitos] ,[stop-words-elementos-sem-valor]
procura os items que cercam o elemento-principal, determinando pelos elementos aceitos o tipo de relacao com o elemento principal

importante:
controle de fatos:
->o que(acao) {vb}->facts
->com quem(agentes,pacientes) {identificador}
->com o que(elemento interventores, influenciadores)  {agrupador,anexo}{com nós|eles|eu|tu|ele,mais o|a(s),tambëm o|a(s), junto, comigo,conosco,com nós, com eles }
-para que(proposito,objetivo,destinacao)  {destinacao}
'''

import mdER
import mdNeural

def start_db(pool2):
 mdNeural.start_db(pool2)



    
class mdBaseOntology:
  #process_input_model->usado no purpose de layout-out(complemento para layout)
  #process_input_filter->usado no purpose de layout-out(input data por layout)
  #================================
  def __init__(self,usr,purpose):
    inpt_word=mdNeural.mdLayer () # interpretacao de palavras
    #==
    [self.nodesER,self.all_purpouses]=mdER.get_RactionLines(purpose,usr)
    
  def process_ER(self,lay,purpose,usr):
    fnds=False
    run_nod=None
    print 'Start ER:',len(self.nodesER),'------------------------'
    for nod in self.nodesER:      
      #print 'Prepare stream(1):',lay
      [r1,r2]=nod.process_RCT(lay,self,usr,purpose)
      print 'nod->process_RCT():{',nod.name,purpose,usr,'}','->',r1
      if r1 != None:
        lay=r1
        run_nod=nod
        fnds=True
        break
    if fnds: 
     return [lay,run_nod]
    return [None,None]
    #======    
    
  def process_ERc(self,lay,purpose,usr,relactionate):
    fnds=False
    run_nod=None
    print 'Start ER:',len(self.nodesER),lay,'------------------------'
    for nod in self.nodesER:      
      #print 'Prepare stream(2):',lay
      [r1,r2]=nod.process_RCT(lay,self,usr,purpose,relactionate)
      print 'nod->process_RCT():{',nod.name,purpose,usr,'}','->',r1
      if r1 != None:
        lay=r1
        run_nod=nod
        fnds=True
        break # encontrou uma rct que tem retorno, stop execussao. Assim as de maior prioridade estaram sempre rodando primeiro, se nao retornarem, processa as demais      
    if fnds: 
     return [lay,run_nod]
    return [None,None]
    #======    
  
  def process( self,lays,purpose,usr ):
   ret1=self.process_ER(lays,purpose,usr)
   return ret1
   
  def processc( self,lays,purpose,usr,relactionate ):
   print 'Start ERC(1):'
   ret1=self.process_ERc(lays,purpose,usr,relactionate)
   return ret1

   
   
class mdAbstractBaseOntology:
  #process_input_model->usado no purpose de layout-out(complemento para layout)
  #process_input_filter->usado no purpose de layout-out(input data por layout)
  #================================
  def __init__(self ):
    inpt_word=mdNeural.mdLayer () # interpretacao de palavras
    #==
    [self.nodesER,self.all_purpouses]=[ [],[] ]
    
  def process_ER(self,lay,purpose,usr):
    fnds=False
    run_nod=None
    print 'Start ER:',len(self.nodesER),'------------------------'
    for nod in self.nodesER:      
      #print 'Prepare stream(3):',lay
      [r1,r2]=nod.process_RCT(lay,self,usr,purpose)
      print 'nod->process_RCT():{',nod.name,purpose,usr,'}','->',r1
      if r1 != None:
        lay=r1
        run_nod=nod
        fnds=True
        break
    if fnds: 
     return [lay,run_nod]
    return [None,None]
    #======    
    
  def process_ERc(self,lay,purpose,usr,relactionate):
    fnds=False
    run_nod=None
    print 'Start ER.1:',len(self.nodesER),'------------------------'
    for nod in self.nodesER:      
      #print 'Prepare stream(4):',lay
      [r1,r2]=nod.process_RCT(lay,self,usr,purpose,relactionate)
      print 'nod->process_RCT(ER.1):{',nod.name,purpose,usr,'}','->',r1
      if r1 != None:
        lay=r1
        run_nod=nod
        fnds=True
        break
    if fnds: 
     return [lay,run_nod]
    return [None,None]
    #======    
  
  def process( self,lays,purpose,usr ):
   ret1=self.process_ER(lays,purpose,usr)
   return ret1
   
  def processc( self,lays,purpose,usr,relactionate ):
   print 'Start ERC(2):'
   ret1=self.process_ERc(lays,purpose,usr,relactionate)
   return ret1   
   
