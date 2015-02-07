#monitorar dominio/posse ->   fornece referencia a classes ou grupos a ser linkados
ractionline abstract_imp_link_o
  purpose  classify
  factname link_o_sources()
  factname link_o_dests()
  factname lnk_purposes()
  
  fact link_o_sources
   source $$all$$
  fact link_o_dests
   dest $$all$$
  fact lnk_purpose
   purpose $$all$$
   
  link

  layoutcode link_to_object_to_class
end
