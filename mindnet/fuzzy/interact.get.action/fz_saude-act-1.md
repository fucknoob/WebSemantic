fuzzy fz_saude-act-1
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt aquir,contrat,melhor,consult,avali,cuid,trat,cur,medic,mediq,sar,fazer,fiz,faç
    sn 
    return 
    direct 
   def 
    dt salubridade,sanidade,bem estar,saúde,doença,insalubridade,insanidade,doente,paciente,dieta,emagrecer,febre,resfriado,gripe,dor
    sn 
    return [interaction.get.action,health,interaction.get.action]
    direct 
   suf ,ir,o,em,emos,irei,iremos,irão,iram,i,iu,ar,amos,a,as,am,ei,aremos,arão,aram,o,eui,ou,eram,emos,ais 
   suf 
end