ractionline fz_event_start
   purpose state-process
   factname fz_event_fz1

   fact fz_event_fz1
    fzlayout interact.happen
    fzlayout interact.news
    # actions padroes
    fzlayoutCh interact.get.action
    fzlayoutCh interact.exchange.action
    fzlayoutCh interact.move.action
    fzlayoutCh interact.stay.action
    fzlayoutCh interact.persony.base.action
    fzlayoutCh interact.check.action
    
    event-start
    event-finish
    interact.dest

end

