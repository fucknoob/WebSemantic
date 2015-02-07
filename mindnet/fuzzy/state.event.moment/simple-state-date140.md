fuzzy simple-state-date140
   force_position Y
   madatory Y
   layout_onto state.event.moment
   direction R
   an AN
   sq 4
   pref 
   def 
    dt dia
    sn 
    return 
    direct 
   def 
    dt #day
    sn 
    return [event-data-day,$$data$$,event-data-day]
    direct 
   def 
    dt de
    sn 
    return 
    direct 
   def 
    dt #month
    sn 
    return [event-data-month,$$data$$,event-data-month]
    direct 
   def 
    dt \,,o,a,os,as
    sn 
    return [event-link,,event-link]
    direct 
   suf 
   suf 
end
