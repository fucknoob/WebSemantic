ractionline compare-obj
 factname cmp-cen-o(cenarios,object-cenario-cache)
 factname mean-analize(mean)
 factname cenario-descript
 factname need-analise
 
 fact cmp-cen-o
   identificador objetos-cenary
   dest id2
   cenary cenario
   # compara id com id2
   compare

 fact mean-analize
   identificador id
   cenary cenario
   mean means
 fact cenario-descript
   cenary cenario
   identificador id
 fact need-analise
   identificador id
   cenary cenario
   need needs
 # analise de dependencias,mean com proposito de cenario+
 call generic(mean-analize,cenario-descript)
 call generic(need-analize,cenario-descript)

end
