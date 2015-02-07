#coding: latin-1
# insere usuarios avulsos


import os
import sys

sys.path.append('./pymongo')  
import pymongo

#import pycassa
#from pycassa.pool import ConnectionPool
#from pycassa import index
#from pycassa.columnfamily import ColumnFamily

#pool2 = ConnectionPool('MINDNET', ['79.143.185.3:9160'],timeout=10000)
#web=pycassa.ColumnFamily(pool2, 'web_cache1')

#obj=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3')
#obj_dt=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3')

#obj3=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT3_1_4')
#obj_dt3=pycassa.ColumnFamily(pool2, 'SEMANTIC_OBJECT_DT3_1_4')
#obj_rl3=pycassa.ColumnFamily(pool2, 'SEMANTIC_RELACTIONS3_1_4')


MONGO_URL='mongodb://mdnet1:acc159753@91.205.172.85:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcb=dbM['fcb_users1']
 


fcb.remove({})
#==========
#web.truncate()
#obj_dt.truncate()
#obj.truncate()
#obj_dt3.truncate()
#obj3.truncate()
#obj_rl3.truncate()


#=======================
def insere_novo(ky,user_name,u_name,tb=1):
 fcb.insert({'user_name':  user_name ,'id':ky , 'u_name':u_name,'indexed':'N','_id':ky,'important':'S'})

 
 
#insere_novo('222977965716','Pontofrio.com','Pontofrio.com')
#insere_novo('127587077302295','casasbahiacombr','casasbahiacombr')
#insere_novo('362752461813','familiaextra','familiaextra')
#insere_novo('194775443140','RicardoEletro','RicardoEletro')
#insere_novo('115244248489160','walmart.com','walmart.com')
#insere_novo('163737793668569','ofertaspank.brasil','ofertaspank.brasil')
#insere_novo('128249847206220','groupon.br','groupon.br')
#insere_novo('259007827634','PeixeUrbano','PeixeUrbano')
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

insere_novo('101036196646365','voudemarisa','voudemarisa')
insere_novo('168235628589','Netshoes','Netshoes')
insere_novo('167799875673','nikefutebol','nikefutebol')
insere_novo('188394007863369','nswbrasil','nswbrasil')
insere_novo('143598718987403','nikecorrebrasil','nikecorrebrasil')
insere_novo('352806884759036','reebokBr','reebokBr')
insere_novo('525738414202280','calvinkleinbrasil','calvinkleinbrasil')
insere_novo('106121679436713','fila.br','fila.br')
insere_novo('110387212341584','Olympikus','Olympikus')
insere_novo('104725456232742','centauroesporte','centauroesporte')
insere_novo('141304895927080','Dafiti','Dafiti')


cnt_users=0
r=fcb.find({})
for c in r:
 c['indexed']='N'
 fcb.update({'_id':c['_id']},c)
 print 'KEY:',c['_id']
 cnt_users+=1
print 'cnt_users:',cnt_users 
 
 
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

 
