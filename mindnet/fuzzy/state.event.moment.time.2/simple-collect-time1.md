fuzzy simple-collect-time1
   force_position N
   madatory Y
   layout_onto state.event.moment.time.2
   direction R
   an OR
   sq 0
   pref 
   def 
    dt antes
    sn 
    return [time,before,time]
    direct 
   def 
    dt depois,posterior,posteriormente
    sn 
    return [time,after,time]
    direct 
   suf o,a,as,amos,am
   suf 
end
