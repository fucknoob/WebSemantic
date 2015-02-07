#coding: latin-1
import sys

sys.path.append('/Neural/simplejson')

import simplejson

import umisc
from datetime import datetime
import logging
from StringIO import StringIO
import urllib
import urllib2
import cookielib

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('publica_relacionamentos')

import bson
import pymongo


MONGO_URL='mongodb://mdnet1:acc159753@91.205.172.85:27017/mdnet'
connM = pymongo.Connection(MONGO_URL) 
dbM=connM.mdnet
fcbM=dbM['fcb_users1']


base_ids=['222977965716','127587077302295','362752461813','194775443140','115244248489160','163737793668569','128249847206220','259007827634',\
          '133481940001233','267796029913881','140871914508','162523134477','218694078173902','127110964018134','141466772559841',\
          '123874468062','114278431986431','194839529381','101036196646365','168235628589','167799875673','188394007863369',\
          '143598718987403','352806884759036','525738414202280','106121679436713','110387212341584','104725456232742','141304895927080']

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
                    ('Content-Type', 'application/x-www-form-urlencoded'),
                    ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]



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

def addInteracaoEstatistica(empresa, tipo, valor, data):
    global est_tbl
    e=est_tbl.find_one({'_id':empresa})
    arr=e['interacoes']
    arr.append({'tipo':tipo,'valor':valor,'data':data});
    est_tbl.update({'_id':empresa},{'$set':{'interacoes':arr}},upsert=True)
    inserirAtividade(empresa, tipo, valor);

def inserirAtividade(empresa, tipo, valor):
    global ativ_tbl
    e=ativ_tbl.find_one({'id_empresa':empresa})
    d=datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    if( e!=None and e['visualizado']==0 ):
        valor+=e['qtd']
    ativ_tbl.update({'id_empresa': empresa, 'tipo': tipo}, {'$set':{'qtd':valor, 'visualizado':0, 'datahora':d, 'datahoracad': d}}, upsert=True)

    
    
def addRelacionamento(id_empresa, id_produto, fbid, nome_usuario, link_perfil, link_thumb, link_comment, gerou_ads, datahora, comment):
   global rel_tbl, prod_tbl
   r = rel_tbl.insert({
      'id_empresa':id_empresa,
      'id_produto':'',
      'desc_produto':'like',
      'fbid':fbid,
      'nome_usuario':nome_usuario,
      'link_perfil':link_perfil,
      'link_thumb':link_thumb,
      'datahora':datahora,
      'datahoracad':datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
   })
   addInteracaoEstatistica(id_empresa, 'relacionamentos', 1, datetime.now().strftime("%d-%m-%Y")) 
   
   
rel_tbl.remove({})   
#insert relactionamentos
clients=fcbM.find({})
for cli_id in clients:
    if cli_id in base_ids: continue
    try:
        cfile = urllib2.urlopen('http://graph.facebook.com/'+cli_id['_id'])
        result = simplejson.load(cfile)
        id_user=cli_id['_id']
        name_user=result['name']
        #==
        url_picture_large='http://graph.facebook.com/'+id_user+'/picture?width=140&height=140'
        usock = opener.open(url_picture_large)
        finalurl = usock.geturl()  
        #============
        addRelacionamento('submarino', 0, id_user, name_user, 'http://facebook.com/'+id_user, finalurl, '', 'N', datetime.now().strftime("%Y-%m-%d"), '')
        #============
    except: 
        log.exception("ERROR:===")  
    
    
    
    
