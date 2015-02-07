# colect objects
# pondere adenrecias


ractionline filter_collects

  factname apps_collect_s_filter
  layoutcode appfs_collects_class_printresult
  # colletar por obj+ filter + refer(links)
  fact apps_collect_s_filter
   interface identificador,rename,filter
   identificador $$all$$
   #rename identificador,object
   # criar alias de class como alis( topico a ser filtrado  )
   #rename class,alias
   # criar alias de except(exessao)
   #rename except,refer
   refer class
   alias
   filter

end


ractionline ask-aswer-classif-response
  #coletar class links , class definitions sobre um obj

  call filter_collects


  
end






