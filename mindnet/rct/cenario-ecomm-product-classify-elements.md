# obs: criar os objetos representando os produtos disponiveis

ractionline get_category_ecomm_from_product  factname  get_category_ecomm_from_product_1  layoutcode create_object_by_data_classify_products  fact get_category_ecomm_from_product_1    interface category,defs,interact.classify2,interact.genero,interact.mode.mark,interact.mode.collection,interact.mode.news,interact.mode.purpose,defs.preco.atual,defs.preco.base,identificador    mandator category,defs,identificador    category $$all$$    defs $$all$$    interact.classify2 $$all$$    interact.genero $$all$$    interact.mode.mark $$all$$    interact.mode.collection $$all$$    interact.mode.purpose $$all$$    interact.mode.news $$all$$    defs.preco.atual $$all$$    defs.preco.base $$all$$    identificador $$all$$
end
ractionline get_classify_ecomm_from_product  factname  get_classify_ecomm_from_product1.12  layoutcode create_object_by_data_classify_products  fact get_classify_ecomm_from_product1.12    class $$all$$    identificador $$all$$
end
ractionline cenario-ecomm-product-classify-elements  purpose cenario-ecomm-classify-products-elements-get  call get_classify_ecomm_from_product  call get_category_ecomm_from_product
end
