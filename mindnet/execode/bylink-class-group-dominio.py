#EXEC
# implementacao dos layoutout dos classif
# name : bylink-class-group-dominio

import mdER
import mdNeural

def run(layers,relacionado,startL,usr,stack):
 rts=[]
 for lr in layers:
  identif=''
  cenario=''
  # achar cenario + i do lr
  #
  #_get_ontology(self,aliases,purposes,usr)
  objects=lr._get_ontology([identif],[cenario],usr)
  for l in objects:
   layer_r=mdNeural.mdLayer()
   layer_r.name=l.name
   rts.append(layer_r)
   links=l.get_links('REFERENCIAL-CLASS')
   for l in links:
    tps=l.lr.get_all()
    for s in tps:
     layer_r.set_topico_nr(s)
 layers=rts
 
