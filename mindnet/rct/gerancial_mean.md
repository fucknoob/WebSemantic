#mean (composicao) :
#     ->definicoes nos topicos mean
#      -> get_origems -> capturar objetos com abstracao
#      -> def destino -> procurar objectos com topicos mean que implementem os topicos dos objetos abstratos
#
#      definidor de topicos mean:
#       source -> o que implementar
#       mean -> implementacao
#
#      buscador de abstracao:
#       composicao: caracts a implementar
#
#      collect -> por caracts -> definidor-mean.source in object-implementar.composicao
#      #========================================================
#        object definidor-> identificador == dest
#        object com caracts encontradas em mean -> orig
#
#
#
# 1-achar objectos com abstracao e rastrear layers com definicao de mean para implementar objetos( marcados como __abstract__)
# 1-objetos identificados explicitamente( collect  por alguma caract que identifique abstracao )
# 2-achar objetos marcados como procura-mean e rastrear definicoes
# achar objectos com abstracao e rastrear layers com definicao de mean para implementar objetos
# achar objetos marcados como procura-mean e rastrear definicoes
#
#


# aplica links mean entre objetos que defininam mean e referenciado

# prototipo basico de associacao do objeto definidor de mean( objeto que definem os mean ) , com o objeto que contem as caracts
#  a serem implementadoas( objeto destino )
#
# prototipo medium
#  ponderacao
#  filtros


# modelo 2: rastrear nomes complexos(com mais de 2 extruturas(elementos)) e aplicar as etapas acima, mas em vez de topicos, usar o nome dos objetos para procurar implementacoes

ractionline mean_collects
  # utiliza vb_collect para selecionar os objects que contem abstracoes, com tds as informacoes a processar , aplica os filtros e dispoe esses layers para as demais
  #  acoes(get_orig,....)
  factname app_collect_s_filter

  # colletar por rule, nao por object
  fact app_collect_s_filter
   interface collect_s
   objective
   rule  mean
   quality
   collect_s orig

end

# analizar se existe medicao de aderencia para objetos origem, retornando os mais aderentes(afininity)  entre o dest e os coletados
ractionline pondere_orig
 factname caracts_pondere
 factname rules_min(cenario-rule-min)
 #============
 fact caracts_pondere
  orig $$all$$
 #============
 fact rules_min
  rule orig
  identificador $$all$$
 # analiza aderencia
 raw_afininity

 
end

ractionline g_mean_process_lnk
  factname process_mean
  # process_mean_gerencial -> analises complementares, um trigger pos validador
  layoutcode process_mean_gerencial
  fact process_mean
   # object -> origem do link mean
   identificador $$all$$
   # identificador -> objecto destino(identificador encontradoe em etapas superiores
   orig $$all$$
   # static -> topico fixo de retorno, com o opcode-> opcode de link
   opcode $$all$$
   # condition -> link condicional
   condition $$all$$
   # link-> processe linkagem dos objetos
   link
end



ractionline gerencial_mean

  call mean_collects
  call pondere_orig
  #=================
  
  call g_mean_process_lnk

  


end



