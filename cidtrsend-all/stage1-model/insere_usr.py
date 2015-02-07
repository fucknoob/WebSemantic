#coding: latin-1
# insere usuarios avulsos


import os
import sys

sys.path.append('./pymongo')  
import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@ds061938.mongolab.com:61938/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcb=dbM['fcb_users']
web=dbM['web_cache']

obj=dbM['SEMANTIC_OBJECT3']
obj_dt=dbM['SEMANTIC_OBJECT_DT3']


web.remove({})
fcb.remove({})
obj_dt.remove({})
obj.remove({})


#=======================
def insere_novo(ky,user_name,u_name):
 fcb.insert({'user_name':  user_name ,'id':ky , 'u_name':u_name,'indexed':'N','_id':ky,'important':'S'})

#insere_novo('222977965716','Pontofrio.com','Pontofrio.com')
#insere_novo('127587077302295','casasbahiacombr','casasbahiacombr')
#insere_novo('362752461813','familiaextra','familiaextra')
#insere_novo('194775443140','RicardoEletro','RicardoEletro')
insere_novo('115244248489160','walmart.com','walmart.com')
insere_novo('163737793668569','ofertaspank.brasil','ofertaspank.brasil')
insere_novo('128249847206220','groupon.br','groupon.br')
insere_novo('259007827634','PeixeUrbano','PeixeUrbano')
insere_novo('133481940001233','Submarino','Submarino')
insere_novo('267796029913881','AmericanasCom','AmericanasCom')
#insere_novo('140871914508','MotorolaBrasil','MotorolaBrasil')
#insere_novo('162523134477','SamsungBrasil','SamsungBrasil')
#insere_novo('218694078173902','SonyBrasil','SonyBrasil')
#insere_novo('127110964018134','philipsbrasil','philipsbrasil') 
#insere_novo('141466772559841','assimumabrastemp','assimumabrastemp')
#insere_novo('123874468062','nokiabrasil','nokiabrasil')
#insere_novo('114278431986431','sonymobilebr','sonymobilebr')
#insere_novo('194839529381','saraivaonline','saraivaonline')
#insere_novo('101036196646365','voudemarisa','voudemarisa')
#insere_novo('168235628589','Netshoes','Netshoes')

r=fcb.find({})
for c in r:
 c['indexed']='N'
 fcb.update({'_id':c['_id']},c)
 
 
#plano 
#local de prospeccao: [eleger sub-etapas para categorias de produtos, em cada um dos segmentos abaixo]
# - teste com um grupo grande de usuarios de e-commerce para eletro, pra abrir espaco pra nova.com 
# - teste para a parte de viagens, monitorar os grandes de oferta de viagens 
# - teste para esporte e lazer(ex.netshoes)
# - teste para roupas/moda em geral
# - teste para produtoras de conteudo( revistas  e livrarias )
# - teste para cosmetico
# - teste para casa e decoracao
# - teste para brinquedos

#estratégia de prospeccao
# 1-monitorar os grandes e depois q achar possivel LEAD , passar pro perfil desse e indxar algumas msgs. Entrar em contado pra iniciar conversacao no perfil do usuario diretamente
# 2-monitoramento geral da grande base, por idioma e por categoria a ser anunciada para cada empresa fornecedora

 
