#coding: latin-1
import sys
import umisc
from datetime import datetime
import logging
from StringIO import StringIO
import urllib
import urllib2

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('vitrines_publish_from_file')

import bson

sys.path.append('./pymongo')

import pymongo

MONGO_URL = 'mongodb://transend:transend1@162.243.69.60:27017/smartdash'
conexao = pymongo.Connection(MONGO_URL)
banco = conexao.smartdash
prod_tbl = banco['produtos']
emp_tbl = banco['empresa']
plan_tbl = banco['planos']
est_tbl = banco['estatistica']
ativ_tbl = banco['atividades']
user_tbl = banco['usuario_empr']
leed_tbl = banco['face_leed']
rel_tbl = banco['relacionamentos']

chaves = banco['chaves']

key='1'

token=chaves.find_one({'key':key})['token']
print 'use token:',token

########################################
 


def post_object(token,obj_id,msg):
     try:
      args = {}    
      args['access_token'],args['message'] ,args['METHOD']=  token,msg,'POST'
      url='https://graph.facebook.com/'+obj_id+'/comments?'
      file = urllib2.urlopen(url,urllib.urlencode(args) )
      print 'Return post:',file.read()
     except:
         print 'Error post:',obj_id 



fil=open('/vitrines/publish_file',"r")
all_text=fil.read()
lines=all_text.split('\2')
for cli in lines:
    elements=cli.split('\1') 
    prodk=elements[1]
    #=====
    msg_k=('Encontramos em seus posts interesses em determinados conteúdos. Tomamos a liberdade de fazer essa conexão entre você e o que pode gostar. Nossas bases identificaram que o post abaixo é interessante para você \n '.decode('latin1').encode('utf8')+prodk.decode('latin1').encode('utf8') )
    #=====
    post_object(token,elements[0],msg_k)  
fil.close() 