fuzzy simple-state-moment-new.13
   force_position Y
   madatory N
   layout_onto state.event.moment.4
   direction R
   an AN
   sq 50
   pref 
   def 
    dt na
    sn 
    return 
    direct 
   def 
    dt $$all$$
    sn 
    return 
    direct 
   def 
    dt semana
    sn 
    return [interact.state.moment.date,$week-in-month,interact.state.moment.date]
    direct 
   def 
    dt de
    sn 
    return 
    direct 
   def 
    dt $$all$$
    sn 
    return [interact.state.moment.daterel,$$data$$,interact.state.moment.daterel]
    direct 
   suf 
end
