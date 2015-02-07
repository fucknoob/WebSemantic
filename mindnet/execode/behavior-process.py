#EXEC
#PROCESSAR BEHAVIOR
#----------------
# processa behavior
# caracts-mutable
# caracts-foco
# action+action
#=============
# resume -> termos(caracts-mutable,caracts-foco,action(s))=>cenario.perfil() -> behavior,behavior


#obs:
# stack.cenarios -> cenarios implementados
# stack.cenario[indicecenario].perfil[indice].classes -> classes definidas
# stack.cenario[indicecenario].perfil[indice].objects -> objectos do cenario.perfil
# stack.cenario[indicecenario].perfil[indice].behaviour -> behaviors monitorados
#

import mdER
import mdNeural

def run(layers,relacionado,startL,usr,stack):
  #ANALIZAR MUTACOES EM CARACTS
  #ANALIZAR ALTERACOES EM CARACTS FOCO
  #CAPTURAR PARAMETROS DE ACTIONS
  for l in layers:
   identificadores=[]
   cenario=''
   actions=[]
   caracts_foco=[]
   #identificador -> objects
   #cenario -> cenario
   #caracts -> foco das caracts
   #actions -> actions envolvidas, link-historico dos objetos
   objects=lr._get_ontology(identificadores,[cenario],usr)
   for o in objects:
    #links historico
    hist=object.get_links('history')
    for j in hist:



