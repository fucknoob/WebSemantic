fuzzy simple-act-1.party
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt ir,iremos,vou,vai,vão,vao,irei,irão,foram,fui,foi
    sn 
    return 
    direct 
   def 
    dt ver,assistir,ao,pra,pro,para
    sn 
    return 
    direct 
   def 
    dt balada,festa,discoteca,dance,noite,festa,balada,aniversario,casamento,viagem,musica,ir pra noite,formatura,teatro,opera,cinema
    sn 
    return [interaction.get.action,party.dance,interaction.get.action]
    direct 
   suf 
end
