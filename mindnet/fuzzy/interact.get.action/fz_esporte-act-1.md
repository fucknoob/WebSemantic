fuzzy fz_esporte-act-1
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt quero,vou,exercer,como,penso,gosto,sonho
    sn 
    return 
    direct 
   def 
    dt fazer,conhecer,aprender,saber,praticar,jogar
    sn 
    return 
    direct 
   def 
    dt futebol,bola,cricket,tenis,hóquei,volei,rugby,basquete,baseball,golf
    sn 
    return [interaction.get.action,esporte,interaction.get.action]
    direct 
   suf  
   suf 


fuzzy fz_esporte-act-2
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt quero,vou,exercer,como,penso,gosto,sonho
    sn 
    return 
    direct 
   def 
    dt fazer,conhecer,aprender,saber,praticar,jogar
    sn 
    return 
    direct 
   def 
    dt futebol
    sn 
    return
    direct 
   def 
    dt americano 
    sn 
    return [interaction.get.action,esporte,interaction.get.action]
    direct 
   suf  
   suf 
end
