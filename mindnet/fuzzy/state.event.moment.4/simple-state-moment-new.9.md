fuzzy simple-state-moment-new.9
   force_position Y
   madatory N
   layout_onto state.event.moment.4
   direction R
   an AN
   sq 50
   pref 
   def 
    dt para
    sn 
    return 
    direct 
   def 
    dt o
    sn 
    return [interact.state.moment.date,$every-day-month,interact.state.moment.date]
    direct 
   def 
    dt dia
    sn 
    return 
    direct 
   def 
    dt #day
    sn 
    return [interact.state.moment.daterel,$$data$$,interact.state.moment.daterel]
    direct 
   suf 
end
