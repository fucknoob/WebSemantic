fuzzy simple-collect-accept
   force_position N
   madatory Y
   layout_onto simple-search-interact
   direction R
   an OR
   sq 0
   pref 
   def 
    dt aporte,aplicação,aplicar,investir
    sn 
    return [interact,apply-money,interact]
    direct 
   def 
    dt retirada,receb
    sn 
    return [interact,receive-money,interact]
    direct 
   def 
    dt ,conectividade,conectar
    sn 
    return [interact,connect,interact]
    direct 
   suf eu,er,s
   suf 
end
