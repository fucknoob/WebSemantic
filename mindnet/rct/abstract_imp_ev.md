# rastreamento de eventos e actions em relacao a referencias(tempo,espaco)
# niveis de rastreamento -> dialog.high,medium,low
# high( dialog.caracts(),... )




ractionline abstract_dialog_high




end


ractionline abstract_dialog_medium
 factname dialog_action(cenario-actions-relevants)

 fact dialog_action
  # pode ser customizado para varias janelas de acoes, ou seja, tipos predefinidosm via find-path
  qualif.action $$all$$

  #qualif.time.when -> ja estraido com os low
  #qualif.state.place -> ja estraido com os low

 fact dialog_destination
   qualif.destination $$all$$

 factname dialog_mode
  qualif.mode.how $$all$$
  
 factname with_elements_people
  qualif.with.people $$all$$

 factname with_elements
  qualif.with.all $$all$$
  
end



ractionline abstract_dialog_low_pos_2
factname fct_event_simple_pos2
fact fct_event_simple_pos2
 state-position $$all$$

layoutcode create_object_by_data_ev

end

ractionline abstract_dialog_low_pos_1
factname fct_event_simple_pos
fact fct_event_simple_pos
 event-place $$all$$

layoutcode create_object_by_data_ev
call abstract_dialog_low_pos_2

end

ractionline abstract_dialog_low_occ_1
factname fct_event_simple_occ
fact fct_event_simple_occ
 event-occurr $$all$$

layoutcode create_object_by_data_ev

end

ractionline abstract_dialog_low_event_1
factname fct_event_simple_event1
fact fct_event_simple_event1
 event $$all$$

layoutcode create_object_by_data_ev

end

ractionline abstract_dialog_low_state_1
factname fct_event_simple_state
fact fct_event_simple_state
 state $$all$$

layoutcode create_object_by_data_ev

end

ractionline abstract_dialog_low_1
factname fct_event_simpledt1
fact fct_event_simpledt1
 event-data $$all$$

layoutcode create_object_by_data_ev

end


ractionline abstract_dialog_low_2
 factname fct_event_simple_data2
 fact fct_event_simple_data2
  event-data-month $$all$$
  event-data-year $$all$$
layoutcode create_object_by_data_ev
end


ractionline abstract_dialog_low_3
 factname fct_event_simple_data_day3
 fact fct_event_simple_data_day3
  event-data-day $$all$$
  event-data-month $$all$$
  event-data-year $$all$$
layoutcode create_object_by_data_ev
end

ractionline abstract_dialog_low_4
 factname fct_event_simple_data_interv4
 fact fct_event_simple_data_interv4
  event-data-ini $$all$$
  event-data-end $$all$$

layoutcode create_object_by_data_ev
end



ractionline abstract_impl_ev
  # low collect
  call abstract_dialog_low_1
  call abstract_dialog_low_2
  call abstract_dialog_low_3
  call abstract_dialog_low_4
  call abstract_dialog_low_pos_2
  call abstract_dialog_low_pos_1
  call abstract_dialog_low_occ_1
  call abstract_dialog_low_event_1
  call abstract_dialog_low_state_1
  # medium level -> state,event,data and other elementos of history
  

end


