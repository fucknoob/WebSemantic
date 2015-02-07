# colect objects
# pondere aderencias


ractionline filter_collects_pr

  factname apps_collect_s_filterc

  # colletar por obj+ filter + refer(links)
  fact apps_collect_s_filterc
   interface identificador,rename,filter
   identificador $$all$$
   #rename identificador,object
   # criar alias de class como alis( topico a ser filtrado  )
   #rename class,alias
   # criar alias de except(exessao)
   #rename except,refer
   refer sugest
   alias
   filter

end

# so para pegar os names object
ractionline fil_get_ids_ow_r
  factname get_ide_from_obj_r
  
  fact get_ide_from_obj_r
   object $$all$$
   rename object,identificador
   no_return

end

ractionline process_aderencia_filter
  # pps_aderencia_with_cenario normal, dependendo depassar pela geracao de cenario as caracts a serem testadas
  #factname apps_aderencia_with_cenario
  #1.->object@dest-topico
  #2.->object@opcode-link@dest-topico
  #3.->object-@topico-relevante-remote@topico-read(p/ competar dt)@dest-topico
  # diretamente de um obj
  #factname apps_aderencia_with_cenario(obj_rule_objs@rule@rule)
  # por destination
  factname apps_aderencia_with_cenario($$all$$@purp-destin@dest@rule)
  layoutcode apps_collects_products_printresult
  
  fact apps_aderencia_with_cenario
     interface  raw_afininity,identificador
     # id => $cache, pois vai usar os coletados na rct filter_collects_pr ou diretamente o identificador dos objetos coletados
     # se inibir o identificador, a busca sera mais ampla e nao por usuario
     identificador $$all$$
     # dest -> tipo de destination(purpose) a procurar para identificar os objetos em questao
     dest $rule-destination-for-objects
     # adicional plus
     #plus
     # rule vai ser fornecido pelo cenario, ou por find-path, onde vai determinar as caracts para coletar
     rule
     # dfin simbolo para 'explode'/'parser' de um topico em varios do parametro rule
     dfin >
     # sins-> sinapses do fpath, o seja, dos links dos objetos que podem ser percorridos quando identificador fornecidor, para encontrar layers likados e conferir
     sins sugest,need,guess
     raw_afininity

end


ractionline ask-aswer-aderency-product-response
  #coletar class links , class definitions sobre um obj

  call filter_collects_pr
  call fil_get_ids_ow_r
  call process_aderencia_filter


end







