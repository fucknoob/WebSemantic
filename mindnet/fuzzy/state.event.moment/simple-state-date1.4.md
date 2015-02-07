fuzzy simple-state-date1.4
   force_position Y
   madatory N
   layout_onto state.event.moment
   direction R
   an AN
   sq 20
   pref 
   def 
    dt dia,data,em
    sn 
    return 
    direct 
   def 
    dt #day
    sn 
    return [event-data-day,$$data$$,event-data-day]
    direct 
   def 
    dt /
    sn 
    return 
    direct 
   def 
    dt #month
    sn 
    return [event-data-month,$$data$$,event-data-month]
    direct 
   def 
    dt /
    sn 
    return 
    direct 
   def 
    dt #year
    sn 
    return [event-data-year,$$data$$,event-data-year]
    direct 
   suf 
end
