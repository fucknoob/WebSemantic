fuzzy simple-state-moment-new.42
   force_position Y
   madatory N
   layout_onto state.event.moment.4
   direction R
   an AN
   sq 50
   pref 
   def 
    dt #number
    sn 
    return [interact.state.moment.daterel2,$$data$$,interact.state.moment.daterel2]
    direct 
   def 
    dt dia,dias
    sn 
    return 
    direct 
   def 
    dt após
    sn 
    return [interact.state.moment.date,$next-day-relative,interact.state.moment,date]
    direct 
   def 
    dt segundo
    sn 
    return [interact.state.moment.daterel,$$data$$,interact.state.moment.daterel]
    direct 
   suf 
end
