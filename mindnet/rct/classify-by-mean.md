# considera os links de class,group,dominio (sinapse) criadas pela rct de 'relacionar'

ractionline classify-by-mean
 purpose classify
 purpose mean

 factname class-link-mean (cenarios,object-cenario-cache)

 # considera objetos linkados como class,group,dominio + foco(items de foco no objeto referencial )
 # achado, retorna os  objetos, com identificador id
 layoutcode bylink-class-group-dominio

 fact class-link-mean
  identificador id
  cenary cenario



end
