fuzzy fz_politica-act-1
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
    dt fazer,conhecer,aprender,saber,votar
    sn 
    return 
    direct 
   def 
    dt eleições,politica,vereador,senador,deputado,federal,estadual,presidente,governador,prefeito,governo,pt,psdb,psb,pv,psdc,prtb,psol,pcb,psc,pco,pstu
    sn 
    return [interaction.get.action,politica,interaction.get.action]
    direct 
   suf  
   suf 

fuzzy fz_politica-act-2
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
    dt em
    sn 
    return 
    direct 
   def 
    dt fazer,conhecer,aprender,saber,votar
    sn 
    return 
    direct 
   def 
    dt eleições,politica,vereador,senador,deputado,federal,estadual,presidente,governador,prefeito,governo,pt,psdb,psb,pv,psdc,prtb,psol,pcb,psc,pco,pstu
    sn 
    return [interaction.get.action,politica,interaction.get.action]
    direct 
   suf  
   suf 
end
