fuzzy simple-state-date134
   force_position Y
   madatory Y
   layout_onto state.event.moment
   direction R
   an AN
   sq 4
   pref 
   def 
    dt em
    sn 
    return 
    direct 
   def 
    dt #month
    sn 
    return [event-data-month,$$data$$,event-data-month]
    direct 
   def 
    dt de
    sn 
    return 
    direct 
   def 
    dt #year
    sn 
    return [event-data-year,$$data$$,event-data-year]
    direct 
   def 
    dt o,o,os,as
    sn 
    return [event-link,,event-link]
    direct 
   suf 
   suf 
end
