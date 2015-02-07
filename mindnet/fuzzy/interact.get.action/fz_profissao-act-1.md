fuzzy profissao-act-1
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt quero,vou,cursar,exercer,como,penso,gosto,sonho
    sn 
    return 
    direct 
   def 
    dt fazer,conhecer,aprender,saber,estudar,trabalhar
    sn 
    return 
    direct 
   def 
    dt Agronomia,Ecologia,Educação,Física,Enfermagem,Esporte,Farmácia,Bioquímica,Fisioterapia,Fonoaudiologia,Gastronomia,Gerontologia,Medicina,Medicina,Veterinária,Musicoterapia,Naturologia,Nutrição,Obstetrícia,Oceanografia,Odontologia,Terapia,Ocupacional,Zootecnia,Astronomia,Biotecnologia,Estatística,FísicaGeofísica,Geologia,Matemática,Meteorologia,Química,Administração,Arqueologia,Arquitetura,Urbanismo,Arquivologia,Artes,Audiovisual,Biblioteconomia,Dança,Direito,Educação,Filosofia,Fotografia,Geografia,História,Jornalismo,Pedagogia,Psicologia,Publicidade,Propaganda,Teologia,Turismo,garçon,pedreiro,carpinteiro,eletricista,porteiro,padeiro,secretária,secretário,ator,atriz,artista
    sn 
    return [interaction.get.action,profissao,interaction.get.action]
    direct 
   suf 


fuzzy profissao-act-2
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt quero,vou,cursar,exercer,como,penso,gosto,sonho
    sn 
    return 
    direct 
   def 
    dt Ciências,Engenharia,Gestão,Ciência,Informática,Artes,Desenho,Design,Economia,Doméstica,Estudos,Produção,Relações,Segurança,Serviço,Tecnologia
    sn 
    return 
    direct 
   def 
    dt ,Biológicas,Biomédicas,agrícola,ambiental,Industrial,Gráfico,Doméstica,Literários,Cultural,Editorial,Pública,florestal,ambiental,Aeronáuticas,Aeronáutica,Cartográfica,Civil,Elétrica,Internacionais,Públicas,Social,Têxtil,Física,Mecânica,Mecatrônica,Metalúrgica,Naval,Química,Sanitária,Têxtil,Biomédica,Cênicas,Plásticas,Sociais
    sn 
    return [interaction.get.action,profissao,interaction.get.action]
    direct 
   suf 
end




fuzzy profissao-act-3
   force_position Y
   madatory Y
   layout_onto interact.get.action
   direction R 
   an AN
   sq 0
   pref 
   def 
    dt quero,vou,cursar,exercer,como,penso,gosto,sonho
    sn 
    return 
    direct 
   def 
    dt Ciências,Engenharia,Gestão,Ciência,Design
    sn 
    return 
    direct 
   def 
    dt de,do,das,dos
    sn 
    return 
    direct 
   def 
    dt 
     alimentos,aqüicultura,horticultura,pesca,Computação,Computação,Minas,Petróleo,Gás,Produção,Telecomunicações,Interiores
    sn 
    return [interaction.get.action,profissao,interaction.get.action]
    direct 
   suf 
end

