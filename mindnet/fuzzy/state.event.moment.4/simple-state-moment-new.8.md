fuzzy simple-state-moment-new.8
   force_position Y
   madatory N
   layout_onto state.event.moment.4
   direction R
   an AN
   sq 60
   pref 
   def 
    dt todo
    sn 
    return 
    direct 
   def 
    dt dia
    sn 
    return 
    direct 
   def 
    dt $day
    sn 
    return [interact.state.moment.daterel,$$data$$,interact.state.moment.daterel]
    direct 
   def 
    dt de
    sn 
    return 
    direct 
   def 
    dt cada
    sn 
    return 
    direct 
   def 
    dt mês,mes
    sn 
    return [interact.state.moment.date,$every-day-month,interact.state.moment.date]
    direct 
   suf 
end
