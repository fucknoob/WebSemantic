fuzzy simple-state-limits
   force_position Y
   madatory Y
   layout_onto state.event.moment
   direction R
   an AN
   sq 1
   pref 
   def 
    dt de
    sn 
    return  [event-data,event-data,event-data]
    direct 
   def 
    dt $$all$$
    sn 
    return [event-data-ini,$$data$$,event-data-ini]
    direct 
   def 
    dt a
    sn 
    return 
    direct 
   def 
    dt #year
    sn 
    return [event-data-end,$$data$$,event-data-end]
    direct 
   def 
    dt .
    sn 
    return [break,break,break]
    direct 
   suf 
end
