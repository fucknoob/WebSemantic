fuzzy simple-act-1.play3
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 10
   pref 
   def 
    dt ir,iremos,vou,vai,v�o,vao,irei,ir�o,foram,fui,foi,vamos,v�o,vao
    sn 
    return 
    direct 
   def 
    dt jogar,praticar,ir,assistir,torcer
    sn 
    return 
    direct 
   def 
    dt jogo
    sn 
    return 
    direct 
   def 
    dt do,da,dos,das,de,no,na
    sn 
    return [interaction.get.action,play,interaction.get.action]
    direct 
   suf 
end

