fuzzy simple-state-moment-new.29
   force_position Y
   madatory N
   layout_onto state.event.moment.4
   direction R
   an AN
   sq 50
   pref 
   def 
    dt daqui,em
    sn 
    return 
    direct 
   def 
    dt $$all$$
    sn 
    return  [interact.state.moment.daterel,$$data$$,interact.state.moment,daterel]
    direct 
   def 
    dt semana,semanas
    sn 
    return 
    direct 
   def 
    dt na,no
    sn 
    return 
    direct 
   def 
    dt $$data$$
    sn 
    return [interact.state.moment.date,$next-week-dayfixed,interact.state.moment.date]
    direct 
   def 
    dt segunda,terca,terça,quarta,quinta,sexta,sábado,sabado,domingo
    sn 
    return [interact.state.moment.daterel2,$$data$$,interact.state.moment.daterel2]
    direct 
   suf 
end
