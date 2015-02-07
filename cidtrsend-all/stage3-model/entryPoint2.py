# coding: latin-1


import Identify 


   
def entry(param,data_parse):

 l=Identify.prepare_layout('igor.moraes','common-indentify')
 l2=Identify.prepare_layout('igor.moraes','common-indentify')
 onto=Identify.prepare_data_by_ask(l, param,'igor.moraes','common-indentify',[] )
 for dta in data_parse:
  #print 'process data:',dta
  ir=Identify.process_data(l2,dta,onto,'common-indentify','igor.moraes') 
  for topico in ir[0].topicos:
   if len(topico.dt) > 0 :
       print '==========================================='
       print topico.dt
       print 'sins:--'
       def pr(topico):
           for p in topico.sinapses:
            print p.nr.dt
            if p.opcode == 'Relaction': 
             print '?????????????????????????????????'
             pr(p.nr)
             print '?????????????????????????????????'
            elif p.opcode == "cmpp":
             print ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'        
       pr(topico)
       print '-------'
       print '==========================================='

#entry('carro detalhe opções',['vectra é um bom carro com design inteligente, em composto por fibra de carbono restrito em carro de passeio '])
entry('carro detalhe',['carro detalhe'])


#print '--------------------------------------------------------'
#print '--------------------------------------------------------'
#print '--------------------------------------------------------'
#print '--------------------------------------------------------'
#print '--------------------------------------------------------'

#entry('viagens melhores opções',['viagem para o nordeste é muito mais tranquilo, composto por translados mas restrito para criancas '])












 
 
 
 