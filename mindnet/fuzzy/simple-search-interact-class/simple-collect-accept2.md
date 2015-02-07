fuzzy simple-collect-accept2
   force_position N
   madatory Y
   layout_onto simple-search-interact-class
   direction R
   an OR
   sq 6
   pref 
   def 
    dt lembrar,entender,lembro,lembra,entende
    sn 
    return [interact,understand,interact]
    direct 
   def 
    dt ganhar,receber,ganho,recebe
    sn 
    return [interact,receive,interact]
    direct 
   def 
    dt afastar,perder,fugir
    sn 
    return [interact,away,interact]
    direct 
   def 
    dt cutucar,toque,tocar
    sn 
    return [intearct,toch,interact]
    direct 
   def 
    dt usa,usam,uso,usamos,utiliza,utilizam,utilizamos
    sn 
    return [interact,need-mid,interact]
    direct 
   def 
    dt mensagens,mensagem,e-mail,email,emails,e-mails
    sn 
    return [interact,msg,interact]
    direct 
   def 
    dt processado,processada,agredido,agredida,preso,presa
    sn 
    return [interact,agressao,interact]
    direct 
   suf eu,er,s
   suf 
end
