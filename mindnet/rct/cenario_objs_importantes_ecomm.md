ractionline cenario_objs_importantes_ecomm  factname cenario_objs_importantes_ecomm1  factname cenario_objs_importantes_ecomm21  factname cenario_objs_importantes_identification
  # cada fact implementa um conjunto de caracteristicas, elementos para identificar um tipo de object
  #  assim varios facts podem implementar varios search por objetos diferentes
  fact cenario_objs_importantes_ecomm1   purp-destin $rule-destination-for-objects   rule defs>pacote   rule defs>de   rule defs>viagem   tag by.ce/002
  fact cenario_objs_importantes_ecomm21    purp-destin $rule-destination-for-objects    rule defs>interaction.get.action>viagem    rule defs>interaction.get.action>internacional    #rule defs>dos    #rule defs>Anéis    tag by.ce/002    tag enderenco-002.2end
# manifesto de algumas marcasractionline lay_manifesto_marcas  factname lay_manifesto_marcas_fct1  fact lay_manifesto_marcas_fct1   purp-destin $marca   rule hering
end
# manifesto de identificacao de defs de produtosractionline layer_obj_index_model
end# contem os defs para identificar uma categoriaractionline layer_obj_index_model_class
end
#manifesto para cenarios de assuntosractionline layt_manif_esporte
end
ractionline layt_manif_profissao
end
ractionline layt_manif_viajens
end


