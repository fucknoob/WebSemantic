#objecto->to->class->grow
#retornar indica get_class_cenario
# coleta definicoes explicidas de classes nos textos minerados
#objecto->to->class->grow(  )

ractionline classofcenario-client-classif
 purpose classify-client
 purpose intern-er
 factname classof(cenario-definidor,object-cenario-cache)
 factname posseof(cenario-definidor,object-cenario-cache)
 factname object-cenario-cache
 factname cenario-definidor
 # post-class-of-cenario -> gravacao, persistencia das informacoes coletadas
 layoutcode post-class-of-cenario

 fact object-cenario-cache
  # identificador object-que-tem-os-identificadores-pertinentes-ao-cenario
  # no caso abaixo, tem o nome do cenario a ser procurar pelas definicoes
  identificador cen-cliente-st

 fact cenario-definidor
  cenary object-que-define-os-elementos-cen

 fact classof
  class $$all$$
  # find path para a lista de objetos gerenciados
  identificador objetos-cenary
  cenary cenario

  
 fact posseof
  posse $$all$$
  identificador objetos-cenary
  cenary cenario

 end

