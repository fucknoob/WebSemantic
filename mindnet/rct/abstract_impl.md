# implementacao dos objetos apartir das buscas, em informacoes com classe,referencia, dependecias,...
#
ractionline  abstr_im_composicao
  factname abs_composicao_im
  layoutcode create_object_by_data
  fact abs_composicao_im
    identificador $$all$$
    composicao $$all$$
end
ractionline abstr_im_refer
  factname referencial_points
  layoutcode create_object_by_data
  fact referencial_points
    identificador $$all$$
    refer $$all$$
end

ractionline abstr_im_needs
  factname abs_needs
  fact abs_need
    identificador $$all$$
    need $$all$$
end
ractionline abstr_im_ways
  factname abs_way
  layoutcode create_object_by_data
  fact abs_way
    identificador $$all$$
    way $$all$$
end
ractionline  abstr_im_meansc
  factname abs_mean
  layoutcode create_object_by_data
  fact abs_mean
    identificador $$all$$
    mean $$all$$
  gravity R
end

ractionline  abstr_im_classes
  # abs_class -> definidores de classe
  factname abs_class
  layoutcode create_object_by_data
  
  fact abs_class
   identificador $$all$$
   class $$all$$



end

ractionline  abstr_im_classes2
  # abs_class -> definidores de classe
  factname abs_class2
  layoutcode create_object_by_data

  fact abs_class2
   identificador $$all$$
   defin $$all$$



end


ractionline abstract_impl
  #coletar definicoes de composicao, classificacao,referencia,....
  purpose  classify


  call abstr_im_composicao
  call abstr_im_refer
  call abstr_im_needs
  call abstr_im_ways
  call abstr_im_means
  call abstr_im_classes
  call abstr_im_classes2

end

