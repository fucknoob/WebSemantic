#coding: latin-1
import sys
import Pyro.core
import threading
import simplejson
import cookielib
import urllib2
import urllib
import umisc
from datetime import datetime
import logging
from StringIO import StringIO

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('get_vitrines')


#  TOKENS +++++++++++++++++++++++++++++


########################################

atualiza_tab_leeds=True
LOJA='SubMarino'

########################################


base_ids=['222977965716','127587077302295','362752461813','194775443140','115244248489160','163737793668569','128249847206220','259007827634',\
          '133481940001233','267796029913881','140871914508','162523134477','218694078173902','127110964018134','141466772559841',\
          '123874468062','114278431986431','194839529381','101036196646365','168235628589','167799875673','188394007863369',\
          '143598718987403','352806884759036','525738414202280','106121679436713','110387212341584','104725456232742','141304895927080']

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),('Content-Type', 'application/x-www-form-urlencoded'),('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]

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

token_vitrine=chaves.find_one({'key':key})['token']
print 'use token:',token_vitrine


Pyro.core.initClient()

objectName = 'layoutBean'
hostname = '79.143.185.3'
port = '38'

print 'Creating proxy for object',objectName,' on ',hostname+':'+port

if port:
    URI='PYROLOC://'+hostname+':'+port+'/'+objectName
else:	
    URI='PYROLOC://'+hostname+'/'+objectName
print 'The URI is',URI

proxy=Pyro.core.getProxyForURI(URI)

def get_users():
    print 'Getting users...'
    return proxy.get_users()


def post_object(token,obj_id,msg):
     args = {}    
     args['access_token'],args['message'] ,args['METHOD']=  token,msg,'POST'
     url='https://graph.facebook.com/'+obj_id+'/comments?'
     file = urllib2.urlopen(url,urllib.urlencode(args) )
     print file.read()


def post_album(token,album):
     args = {}    
     args['access_token'],args['name'],args['METHOD'],args['message'],args['privacy']=token,album,'POST','Ofertas personalizadas de acordo com perfil - Produtos da Loja Virtual '+LOJA,'{"value":"EVERYONE"}'
     url='https://graph.facebook.com/me/albums?'
     file = urllib2.urlopen(url,urllib.urlencode(args) )
     rt= file.read()
     rt=rt.replace("\"","")
     rt=rt.replace("{","")
     rt=rt.replace("}","")
     rt=rt.replace("id:","")
     return rt     


def post_picture(token,album,foto_url,message_foto):
     args = {}    
     args['access_token'],args['url'],args['message'],args['METHOD'],args['upload file']=token,foto_url,message_foto,'post','false'
     #url='https://graph.facebook.com/'+album+'/photos?access_token='+token+'&message='+message_foto+'&url='+foto_url
     url='https://graph.facebook.com/'+album+'/photos'
     print 'post.url:',url
     
     params = urllib.urlencode(args) # parameters is dicitonar
     req = urllib2.Request(url, params) # PP_URL is the destionation URL
     req.add_header("Content-type", "application/x-www-form-urlencoded")
     file = urllib2.urlopen(req)
     
     #==
     #file = urllib2.urlopen(url,urllib.urlencode(args) )
     rt= file.read()
     rt=rt.replace("\"","")
     rt=rt.replace("{","")
     rt=rt.replace("}","")
     rt=rt.replace("id:","")
     return rt   

usuarios = get_users()

def is_equal(vitr1,vitr2):
    if len(vitr1) != len(vitr2): return False
    n_found=False
    for [n1,rc] in vitr1:
        fnd=False
        for [n2,rc] in vitr2:
            if n1==n2:
                fnd=True
        if not fnd:
            n_found=True
    if n_found: return False
    return True


dist_vitrines=[]
clients=[]

def insert_vitrines(item_prod):
    fnd=False
    indx=0
    for n1 in dist_vitrines:
        if is_equal(n1,item_prod):
            fnd=True
            return indx
        indx+=1
    dist_vitrines.append(item_prod)
    return len(dist_vitrines)-1

for pr in usuarios:
    [client,prods]=pr
    idx=insert_vitrines(prods)
    clients.append([client,idx])


#print dist_vitrines
#print clients 

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


def addFaceLeed(id_empresa, id_produto, fbid, nome_usuario, link_perfil, link_thumb, link_comment, gerou_ads, datahora, comment,descr_produto):
    global leed_tbl, prod_tbl
    #
    prod=bson.Binary(descr_produto)
    usr=bson.Binary(nome_usuario.encode('utf8')) 
    comment=bson.Binary(comment.encode('utf8')) 
    r = leed_tbl.insert({
        'id_empresa':id_empresa,
        'id_produto':id_produto,
        'desc_produto':prod,
        'fbid':str(fbid),
        'nome_usuario':usr,
        'link_perfil':link_perfil,
        'link_thumb':link_thumb,
        'link_comment':link_comment,
        'gerou_ads':gerou_ads,      
        'datahora':datahora,
        'datahoracad':datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"),
        'comment':comment
    })
    addInteracaoEstatistica(id_empresa, 'leeds', 1, datetime.now().strftime("%d-%m-%Y"))   


def addRelacionamento(id_empresa, id_produto, fbid, nome_usuario, link_perfil, link_thumb, link_comment, gerou_ads, datahora, comment):
    global rel_tbl, prod_tbl
    p = buscaProduto(id_produto, id_empresa)
    r = rel_tbl.insert({
        'id_empresa':id_empresa,
        'id_produto':id_produto,
        'desc_produto':p['desc_produto'],
        'fbid':fbid,
        'nome_usuario':nome_usuario,
        'link_perfil':link_perfil,
        'link_thumb':link_thumb,
        'datahora':datahora,
        'datahoracad':datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    })
    addInteracaoEstatistica(id_empresa, 'relacionamentos', 1, datetime.now().strftime("%d-%m-%Y")) 

if atualiza_tab_leeds:
    #insert leads
    indkcs=-1
    to_remove=[]
    for kscli in clients:
        cli=kscli
        indkcs+=1     
        [msg_id,idx]=cli
        url_message='http://graph.facebook.com/'+msg_id
        try:
            cfile = urllib2.urlopen(url_message)
            result = simplejson.load(cfile)
            r2=result['from']
            id_user=r2['id']
            name_user=r2['name']
            comm=result['message']
            #==
            url_picture_large='http://graph.facebook.com/'+id_user+'/picture?width=140&height=140'
            usock = opener.open(url_picture_large)
            finalurl = usock.geturl()  
            #============
            clients[indkcs]=[msg_id,idx, id_user,name_user,finalurl,comm ] 
            if id_user in base_ids:
              to_remove.append(indkcs)    
        except: 
            print 'Error:',msg_id
            to_remove.append(indkcs)
            pass

    # gerar as estatisticas no smartdash 
    indicep=len(to_remove)-1
    while indicep >=0:
        kind=to_remove[indicep]
        del clients [ kind ]
        indicep-=1
    
    
    leed_tbl.remove({'id_empresa':'submarino'})
    for cli in clients:
        if len(cli)>= 6:   
            [msg_id,idx,id_user,name_user,finalurl,comm]=cli
            vitrine=dist_vitrines[idx]
            for item_vitrine in vitrine:
                [cod,rcc]=item_vitrine  
                link_produto=rcc['prod']
                descr=rcc['title']
                #================
                addFaceLeed('submarino', cod, id_user, name_user, 'http://facebook.com/'+id_user, finalurl, 'http://graph.facebook.com/'+msg_id, 'N', datetime.now().strftime("%Y-%m-%d"), comm,descr)
                break
        else:
            print 'Error:',cli
#============================            
#============================            
#============================  
link_albuns=[]
for vitrine in dist_vitrines:
    created_album=False
    link_album=''
    indklc=-1    
    for item_vitrine in vitrine:       
        [cod,rcc]=item_vitrine  
        indklc+=1
        pg=rcc['pg']
        preco_base=''
        preco_atual=''
        preco_total=''
        #============
        lines=pg.split('.')
        for line in lines:
         line=line.replace('\n','')
         line=line.replace('\t','')
         line=umisc.trim(line)   
         if line.startswith('definicao defs preco base ='):
           preco_base=umisc.trim(line.replace('definicao defs preco base =',''))  
         #=============  
         if line.startswith('definicao defs preco atual ='):
           preco_atual=umisc.trim(line.replace('definicao defs preco atual =',''))  
        #============
        if preco_base != '' and preco_atual !='':
            preco_total=' de R$'+preco_base+' por R$'+preco_atual
        elif preco_base != '':
            preco_total='R$'+preco_base
        elif preco_atual != '':    
            preco_total='R$'+preco_atual
        #==================    
        #definicao defs preco base =  299,95. \n  definicao defs preco atual =  209,95.
        if not created_album:
          words=''
          lines=''
          word=''
          lines=pg.split('.')
          if len(lines)>0:
           words=lines[0].split(',')
          if len(words)>1:
           word=words[len(words)-2]+'-'+words[len(words)-1]
          elif len(words)>0:
           word=words[len(words)-1]
          #
          #
          album='Seleção de ofertas de '.decode('latin1').encode('utf8') 
          album+=word.decode('latin1').encode('utf8')
          print 'Create album...' 
          id_a=post_album(token_vitrine,album)
          print 'id.album:',id_a
          id_a=umisc.trim(id_a)
          link_album='https://www.facebook.com/media/set/?set=a.'+ id_a  
          link_albuns.append(link_album)
        #=========== 
        created_album=True
        if rcc['t_image'] != '':
         if indklc % 10 ==0: 
             import time
             time.sleep(3)
         try:   
          post_picture(token_vitrine,id_a,rcc['t_image'],rcc['t_title'].decode('latin1').encode('utf8')+' \n Preco: '+preco_total.decode('latin1').encode('utf8') + ' \n '+rcc['lomadee_url'])
         except: 
             log.exception("")
        # 
        #ft1=post_picture(token_vitrine,id_a,'http://isuba.s8.com.br/produtos/01/00/sku/114480/1/114480196SZ.jpg',' Camisa VR Estampada 		 		- VR \n http://smartsocial.com.br/p.php?p=53873.1'.decode('latin1').encode('utf8'))
        #ft2=post_picture(token_vitrine,id_a,'http://isuba.s8.com.br/produtos/01/00/sku/113626/7/113626763SZ.jpg',' Polo VR Kids Brasao Peito 		 		- VR Kids \n http://smartsocial.com.br/p.php?p=53873.1'.decode('latin1').encode('utf8'))

'''
for cli in clients:
    indkcs+=1     
    [msg_id,idx,id_user,name_user,finalurl,comm]=cli
    #msg_id='1445571722366059_1445599039029994'
    prodk=link_albuns[idx]
    msg_k=('Encontramos em seus posts interesses em determinados conteúdos. Tomamos a liberdade de fazer essa conexão entre você e o que pode gostar. Nossas bases identificaram que o post abaixo é interessante para você \n '.decode('latin1').encode('utf8')+prodk.decode('latin1').encode('utf8') )
    post_object(token_posts,msg_id,msg_k)
'''

fil=open('/vitrines/publish_file',"w")
for cli in clients:
    [msg_id,idx,id_user,name_user,finalurl,comm]=cli 
    prodk=link_albuns[idx] 
    #msg_k=('Encontramos em seus posts interesses em determinados conteúdos. Tomamos a liberdade de fazer essa conexão entre você e o que pode gostar. Nossas bases identificaram que o post abaixo é interessante para você \n '.decode('latin1').encode('utf8')+prodk.decode('latin1').encode('utf8') )
    #=====
    fil.write(msg_id+'\1'+prodk+'\2') 
fil.close() 