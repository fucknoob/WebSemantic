fuzzy simple-state-date11
   force_position Y
   madatory Y
   layout_onto state.event.moment
   direction R
   an AN
   sq 5
   pref 
   def 
    dt em
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
    dt \,
    sn 
    return [event-link,,event-link]
    direct 
   suf 
end
