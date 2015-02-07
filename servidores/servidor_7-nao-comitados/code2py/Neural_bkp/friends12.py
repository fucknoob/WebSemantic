#coding: latin-1
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

#import conn
#conn= conn.conn_mx

import logging
from StringIO import StringIO
import datetime
import time, datetime

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('GET-FACEBOOK->COLLECT')


ch  = logging.StreamHandler ()
lbuffer = StringIO ()
logHandler = logging.StreamHandler(lbuffer)
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")self.logHandler.setFormatter(formatter)

log.addHandler(logHandler) 
log.addHandler(ch) 

import conn
conn= conn.conn_mx


sql_insert_p='insert into fcb_users(user_name,id,u_name) values(?,?,?)'

def insere_usr(user_name,id,u_name): 
 #print 'insert:',[user_name,id,u_name] 
 try:
  conn.sqlX(sql_insert_p,([user_name,id,u_name]))
 except: pass 
     
    
def get_usrs(uid):
    fql='SELECT uid2 FROM friend WHERE uid1 = '+uid
    args = {}
    args["query"], args["format"] , args['access_token'] = fql, "json" ,'323755687729999|p-YAUWo1Sc-2hRYPqi9mHUu6_k0'

    url='http://api.facebook.com/method/fql.query?'+ urllib.urlencode(args)
    file = urllib2.urlopen("https://api.facebook.com/method/fql.query?" + urllib.urlencode(args))
    
    rets=file.read ()
    print rets
    #
    #result = simplejson.load(file)
    #return result
    
    
def get_likes(ids):
    url='https://graph.facebook.com/'+ids+'/likes?access_token=392136580875840|rdRN2UGmcx_eJdJhRFvq_-F9O0Y'
    file = urllib2.urlopen(url)
    dts=file.read ()   
    
    print dts
 
to_ins=[]
 
err=False 
 
def get_feeds(id,cs=0,c_url=''):
    args = {}
    global to_ins
    global err
    
    
    args['access_token'],args['limit'] =  '130873000405995|5N0XoPtYqnfP0LBj8g-oeIO90MI','500'
    
    
    
    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    print 'Process pg:',id
    
    if c_url != '':
     url=c_url
    
    try:
    
      file = urllib2.urlopen(url)
     
     
      #opener = urllib2.build_opener()
      #opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB5')]
      #file = opener.open(url, '' )     
     
    
    except Exception,err1:
     err=True
     print 'Error:',err1
     return
    #dts=file.read ()   
    
    #print dts
    
    
    result = simplejson.load(file)    
        
    r2=result['data']
    pagin=result['paging']
    msg_i=1
    for ch in r2:
     
     try:
      id=ch[u'id']
     except: pass 
     try:
      _from=ch[u'from']
     except: pass 
     try:
      likes=ch[u'likes']
     except: 
      likes=None     
     try:
      message=ch[u'message']
     except: pass 
     try:
      link=ch[u'link']
     except: pass 
     try:
      icon=ch[u'icon']
     except: pass 
     try:
      type=ch[u'type']
     except: pass 
     try:
      status_type=ch[u'status_type']
     except: pass 
     try:
      object_id=ch[u'object_id']
     except: pass 
     try:
      created_time=ch[u'created_time']
     except: pass 
     try:
      updated_time=ch[u'updated_time']
     except: pass 
     try:
      shares=ch[u'shares']
     except: pass 
     try:
      comments=ch[u'comments']
     except: 
      comments=None
       
    
     if comments != None:
       try:
        its=comments[u'data']
        for it in its:
         created_time=it[u'created_time']
         message=it[u'message']
         _from=it[u'from']
         u_name=_from[u'name']
         u_id=_from[u'id']
         #print u_name,u_id
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])
       except Exception,e: 
          pass       
       
     if likes != None:
       try:
        its=likes[u'data']
        for it in its:
         u_name=it[u'name']
         u_id=it[u'id']
         #print u_name,u_id
         to_ins.append(['',u_id.encode('latin-1'),u_name.encode('latin-1')])          
       except Exception,e: 
          pass       
     
     msg_i+=1
     
     
    if cs > 200: return 
    try:
     nova_pagina=pagin['next']     
     print 'get page:',(cs+1)
     get_feeds(id,(cs+1),nova_pagina)
    except: pass
    
    #=======================
    if cs == 0:
     print 'insert rows.id:',len(to_ins)
     for its in to_ins:
       [a,u_id,u_name]=its
       insere_usr('',u_id,u_name)
     to_ins=[]  
     time.sleep( 2 )
    
def obter_toke(id,pwd):
 url='https://graph.facebook.com/oauth/access_token?%20client_id=392136580875840&client_secret=a165cab020b8a99f4a12ef5d8aecdf91&grant_type=client_credentials' 
 
 
def alterat_token(id,pwd):
    url='https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id='+id+'&client_secret='+pwd+'&fb_exchange_token=SHORT_LIVED_ACCESS_TOKEN'
    print url
    file = urllib2.urlopen(url)
    rets=file.read ()
    print rets
        

def get_dist_u():
 cursor = conn.sql("SELECT distinct ID,i from fcb_users where indexed='N' and  rowno < 50 ") 
 p=[]
 isd=[]
 for results in cursor:
    ids=results[0]
    i=results[1]    
    p.append(ids)
    isd.append(i)
 
 return [p,isd]   

 
def index_subs():
 c=0
 while c < 100000 :   
  [usrs,fc]=get_dist_u()
  c2=0  
  for u in usrs:
    print 'Process usr:',u
    try:    
     get_feeds(u)
     print 'Close usr:',usrs[c2]
     if not err:
      conn.sql("update fcb_users set indexed='S' where i= "+str(fc[c2]))
      conn.commit()
     err=False 
    except: pass 
    c2+=1
  c+=1  
  

  
listas_de_enderecos1=["redetelecine","MotorolaBrasil","GuaranaAntarctica","cervejaskol","LOrealParisBrasil","SmirnoffBrasil","hotelurbanobr","programapanico"]  
listas_de_enderecos2=["BrahmaSelecao","BrahmaTimao","BrahmaFla","brahmaoficial","BrahmaSãoPaulo","Brahmapalmeiras","AngelicaProducoes"]  
listas_de_enderecos3=["privaliabrasil","esporteinterativo","CQC","canalfox.br","Globoesporte","RiderOficial","Avenida-Brasil-Novela"]  
listas_de_enderecos4=["AvenidaBrasilNovela","copa2014.comunidade","DomingaoDoFaustao","brunoemarrone","RedeGlobo","NairBello","chxoficial"]  
listas_de_enderecos5=["Jorge-Aragão","cantorDaniel","FabioJrOficial","familiapaulafernandes","RobertoCarlosOficial","TrechosdeMusicasdaPaulaFernandes"]  
listas_de_enderecos6=["MichelTelo","eleicoes2012br","NeimarJrOficial","Neymaroficial","milemamaluuf","LucianoHuck","corinthians","FlamengoOficial"]  
listas_de_enderecos7=["Dafiti","groupon.br","PeixeUrbano","santanderbrasil","AviancaBrasil","voegol","TAMAirlines","familia.gigante.sccp","sitevagalume"]
listas_de_enderecos8=["saopaulofc","sePalmeiras","oficialvasco","ivetesangalo","Kaka","paulocoelho","todopais.paulafernandes","letrasmusbr"]

listas_de_enderecos9=["redegiraffas","oralbbrasil","SedaOficial","axebr","TRIP-LINHAS-AÉREAS-SA","KLMBrasil","TricaeBR","Pompomfraldas","babycombr","johnsonsbabybrasil"]
listas_de_enderecos10=["pampersbrasil","canalfx.br","santanderbrasil","CitiBrasil","McDonaldsBrasil","subwaybrasil","bobsbrasil","BurgerKingBrasil","HabibsOnline","nikefootball"]
listas_de_enderecos11=["HallsBrasil","canalfox.br","bemolonline","CitroenBrasil","RenaultBrasil","volkswagendobrasil","hondaautomoveis","pontofrio","saraivaonline","brasil.universia"]
listas_de_enderecos12=["clickonbr","Lojas.Riachuelo","ClubeDoDescontoBR","UOLEsporte","sportv","itau","Bradesco","chocolatebis","NestleBrasil","DisneyMoviesBrasil","lactaoficial"]


listas_de_enderecos13=["Conselhos-da-Carminha","ritalee.oficial","luansantana","GuaranaAntarctica","unilevervolei","unilever","PepsiBrasil","cocacolazero"]
listas_de_enderecos14=["subwaybrasil","McDonaldsBrasil","LojasRenner","Lojas.Riachuelo","corinthians","saopaulofc","FortalezaCearaBrasil","FacebookBrasil"]
listas_de_enderecos15=["privaliabrasil","AzulLinhasAereas","clicRBS","UOL","TerraBrasil","MercadoLivre","SamsungBrasil","FlamengoOficial","riodejaneirocidademaravilhosa"]
  
listas_de_enderecos16=["CervejaBohemia","sonymusicbrasil","BrahmaSelecao","oboticario","Antarctica","BudweiserBrasil","StellaArtoisBrasil","chicletsbrasil","guaranakuat","PepsiBrasil"]
listas_de_enderecos17=["CacauShow","Netshoes","RisqueOficial","brahmaoficial","olxbrasil","modanapassarela","ceaBrasil","esmaltecolorama","SonyBrasil","centauroesporte","ubisoft.brasil"]
listas_de_enderecos18=["RockInRio","sonhodevalsa","HavaianasBrasil","JohnnieWalkerBrasil","Natura","naturanet","fiatbr","GilletteBrasil","kibonbr","sazonbrasil","Devassa"]
listas_de_enderecos19=["MaxTotalAlimentos","GarnierBrasil","tresemmebr","pantenebrasil","nikecorrebrasil","SadiaOficial","mentosbr","nokiabrasil","ColgateBrasil","hellmannsbrasil"]
listas_de_enderecos20=["CheetosBrasil","MaybellineBrasil","BrasilSorriso","BebeStore","SonyMusicGospel","usereserva","iCarros","SamsungBrasil","RufflesOficial","OfficialMelissa","adorofarm"]
listas_de_enderecos21=["XboxBR","PlayStationBR","doritosbrasil","hvpetcare","NikeSkateboardingBrasil","viamarte","wizard.oficial","SephoraBrasil","meuamigopet","gatoradebrasil"]
listas_de_enderecos22=["SamsungMobileBrasil","novaschin","Olympikus","SKYYVODKAbr","ClubSocialBR","gvtoficial","embratel","SKYBrasil","magazineluiza","tokstok","yahoobrasil"]
listas_de_enderecos23=["RonaldinhoOficial","fgv.oficial","VolvoCarsBR","mercedesbenzbrasil","BMWBrasil","YamahaMotorBrasil","harleydavidsondobrasil","SonheHonda","Pele","spideranderson"]
listas_de_enderecos24=["MSNBrasil","portalr7","BigBrotherBrasil","oficialvasco","santosfc","FluminenseFC","atleticooficial","cruzeirooficial","closeupbrasil","fruittellabrasil"]
listas_de_enderecos25=["subwaybrasil","TricaeBR","ButterToffees","hyundaibr","reebokBr","GarnierBrasil","hondaautomoveis","Decolar","lojamelissa","maggibrasil","schutzoficial"]
listas_de_enderecos26=["volkswagendobrasil","AbsolutBrasil","adesbrasil","OiOficial","BrahmaVasco","bacardibrasil","NikeSurfingBrasil","AmericanasCom","Buscofem","clickonbr","sonymobilebr"]
listas_de_enderecos27=["wellabrasil","voudemarisa","arezzo.oficialvasco","SubmarinoViagensOficial","LojasRenner","Intimusbr","chevroletbrasil","mundofini","Elo7br","activiabrasil"]
listas_de_enderecos28=["TopperBrasil","MasterCardBrasil","ColgatePlaxBrasil","nutellabrasil","sazonbrasil","OBoticarioCapricho","OMelhorDoMundo","ItauUniversitarios","niveabrasil"]



listas_de_enderecos29=["pedala.com.br","descubraariel","AudiBrasil","HondaDreamBrasil","pontofrio","PhilipsImpress","garoto","ClightCodigoX","cifraclub","animalebrasil","CampariBrasil","UseHuck","mundodecomfort"]
listas_de_enderecos30=["MaquiagemNatura","PepsiCoBrasil","RamarimBR","ChilliBeansBR","SchweppesBrasil","ajudareomelhorremedio","saraivaonline","FordBrasil","serenatadeamor","jackdanielsbrasil","ElectroluxBr"]
listas_de_enderecos31=["FusionEnergyDrink","UmbroBrasil","familiaextra","senacsaopaulo","levelupgamesbr","mrvengenharia","delvalletm","Greenvana","MormaiiBrasil","santanderbrasil","kanuibr","WarnerBrosPicturesBrasil"]
listas_de_enderecos32=["portoseguro","GreenpeaceBrasil","pratafina","oppadesign","conversebrasil","airubr","TicTacBrasil","CiaHering","magazineluiza","omobrasil","CupNoodlesBrasil","rio2016","BonafontBrasil","theposhlittlestore"]
listas_de_enderecos33=["CitiBrasil","TintasSuvinil","ampmbrasil","consulbr","Trakinas","VanishBrasil","nissanbrasil","colccioficial","ClubeDosViraLatas","quiksilverbr","iTunesBR","timbrasil","naturatododia","ninhosoleil"]
listas_de_enderecos34=["CervejaKaiser","eudoraoficial","livrariacultura","panasonic.br","InstitutoEmbellezeOficial","BlackBerryBrasil","PostosALE","kabum.com.br","LiptonBrasil","BrahmaSantos","fila.br","philipsbrasil","thefashionera"]
listas_de_enderecos35=["mondainebrasil","H2OHBrasil","peugeotbrasil","i9byPowerade","Devassa","LandRoverBR","bomnegocio","SapatosBottero","ducoco","Fruttarebr","MundoWalmart","ChivasRegalBrasil","NextelBrasil","pizzahutbrasil"]
listas_de_enderecos36=["MoblyBR","meumoveldemadeira","timbeta","grcaixaseguros","lgdobrasil","jacmotors","BrahmaFlu","assimumabrastemp","sandaliasipanemaoficial","valepresente","descomplica.videoaulas","BrahmaCruzeiro"]
listas_de_enderecos37=["groupon.viagens","lenovobr","ItauUniversitarios","savemebr","cepacoloficial","modamercatto","RagazzoOnline","casasbahiacombr","RicardoEletro","SantanderUniversidades","kiamotorsbrasil","hsbrasil"]
listas_de_enderecos38=["buscadescontos.bd","IberiaBR.PT","StarbucksBrasil","cozinhasitatiaia","OnibusMarcopolo"]



listas_de_enderecos39=["dumond.oficial","saldefrutaeno","IberiaBR.PT","InstitutoLP","ViajarBaratoBR","diasupermercado","DrOetkerBrasil","concursopublico","lorealprofessionnelbrasil","loccitane.brasil","pernambucanas","avonbr"]
listas_de_enderecos40=["myshoesoficial","minifazenda","toddybrasil","caixa","SOLDLeiloes","duracellbrasil","TimberlandBrasil","SBCoaching","DanetteBrasil","vestibularfgv","naturaekosbrasil","MaxTotalAlimentos","PiccadillyBR"]
listas_de_enderecos41=["valenobrasil","bancodobrasil","GracoBrasil","CervejariaHeinekenBrasil","CuidadosCasa","qixskate","camiseteria","bareMineralsBrasil","MirabelOficial","alwaysbrasil","DeCaronaComElas","PenaltyBR"]
listas_de_enderecos42=["comprafacil","PayPalBrasil","dzarm.oficial","Polishop","TeletonOficial","mizunobrasil","azaleiaOficial","PostItBR","newerabrasil","galeriadorock","fordnewfiestabrasil","PedigreeAdotar","FutebolFC"]
listas_de_enderecos43=["AviancaBrasil","multiplus","IOBconcursos","TobleroneBrasil","istickfb","bateriasmoura","SearaBrasil","LostBrasil","bolsapravoce","CamaroClubeBrasil","CI.Intercambio","restaurantemanekineko","IvecoBr"]
listas_de_enderecos44=["maquiagemavonoficial","Mundomit","ChocolatesKopenhagen","WSPAbr","baratocoletivo","cafe3coracoes","BrinoxOficial","oficialnutry","GEOEventos","ccbbsp","agulhasnegrasbmw","Ricocomvc","ArcorBrasil"]
listas_de_enderecos45=["RiderOficial","ArnoOficial","PassportScotchBrasil","SundownBrasil","fabercastellbrasil","IgrejaAdventistadoSetimoDia","pagseguro","ypiocaoficial","ShoppVillaLobos","novomaraca","jeepdobrasil"]
listas_de_enderecos46=["chandonbrasil","docemenor","br.estacio","jequiticosmeticos","MelittaWake","DanoneBabyBrasil","euamoomundo","Fiat500Brasil","GrupoRBS","SaudeJaSuplementos","Tecnisa","cafesantaclara","hotel.transamerica"]
listas_de_enderecos47=["rioanilshopping","ibacana.com.br","voesky","HospitalAlbertEinstein","OticasCarol","neutrogenabrasil","adoteumgatinho","shoppingtijuca","doutores","SonyPicturesBrasil","amaissaude","FnacBrasil"]
listas_de_enderecos48=["PlazaShoppingNiteroi","lojaboobebe","iguatemisalvador.page","allianzbrasil","carinhoinspiracarinho","regateio","SaladaBunge","RichesterID","billabongbrasil","salinasmaragogi","gedobrasil"]
listas_de_enderecos49=["NEToficial","projetomedicina","construtoragafisa","MuellerCtba","fgv.oficial","MID-Refresco","LanAirlinesBrasil","nubevagas","BBCHDBrasil","shoppingabc"]


listas_de_enderecos50=["fernandoesorocaba","sorrisomarotooficial","gusttavolimaoficial","jorgeemateus","ClaudiaLeitte","exaltasamba","zezedicamargoeluciano","GusttavoLima01","anacarolinaoficial","somlivre","robertomaiaoficial"]
listas_de_enderecos51=["cantorDaniel","jorgeemateusfcoficial","Jorge-e-Matheus","oficialavioes","grupoeva","Maria-Gadu","RockInRio","JeitoMolequeOficial","NX-Zero","thiaguinhocomth","joaonetoefredericooficial","sertanejoisraelnovaes"]
listas_de_enderecos52=["paranossaalegria","pretagiloficial","Péricles","Munhoz-e-Mariano","rockrestart","JotaQuest","bdsoficial","OficialDiogoNogueira","skank","bandaoito7nove4","turmadopagode","joaoboscoevinicius"]
listas_de_enderecos53=["sertanejouniversitarioorg","capitalinicial","ThaemeeThiago","WSeGarotaSafada","victoreleo","Os-Havaianos","nandoreisoficial","FrasesDePagode6","marisamonteoficial","PadreFabiodeMelo","nxzerooficial"]
listas_de_enderecos54=["DeiixaAcoontecerNaturalmente","faclubeisraelnovaes","VanessaDaMataOficial","Saulo-Fernandes","sitekboing","BeloOficial","alexandrepiresoficial","asusbr","Calçado-Online","shoppingbarramoda","MAPFREbr"]
listas_de_enderecos55=["efacil","oficialgbarbosa","rossiresidencialoficial","acebrasil","LojasTorraTorra","ResultadosDigitais","cravocanelaoficial","naturalmentedoce","SuzukiBR","SonheHonda","BlowtexPreservativos","CanalCCAA"]
listas_de_enderecos56=["assiname","CervejaBavaria","audia1brasil","eDestinos.com.br","fiukoficial","BandaGarotaSafada","osertanejouniversitario","alinebarrosonline","orappa","ChicoBuarque","Djavanoficial","gp.brunakarla"]
listas_de_enderecos57=["PaginaProjota","roupanova","JotaQuest","ZecaPagodinhoOficial","sambooficial","trechosdesertanejos","PaginaBondeDaStronda","FrasesdoBDS","mafia1dbrazil","marcelodedois","naldooficial","CarlinhosBrownOficial"]
listas_de_enderecos58=["Tom.Jobim","ConeCrewDiretoriaCONE","rebeldes","ViciadasEmOneD","umusicbrasil","harmoniaoficial","GusttavoLimaevoce","MariaRitaOficial","zezedicamargoeluciano","oficialfresno","radiojovempan","bandaparangoleII"]
listas_de_enderecos59=["sertanejolove","PretinhodoPoderoficial","SonyMusicGospel","postologoexisto","ArlindoCruzOficial","RacionaisJaofei","djandremarques","fredegustavo","botapagodao","PittyOficial","315303111859239"]
listas_de_enderecos60=["NatirutsOficial","carnafacul","199055170180825","oficialfresno","WSFrases","Empreguetes","VerdadeiramenteAmizade","anapaulavaladao","EmicidaOficial","eduardocostaoficial"]

 
  
  
a=sys.argv[1]
listas_de_enderecosC=[]

if a== '1':
 listas_de_enderecosC=listas_de_enderecos1
if a== '2':
 listas_de_enderecosC=listas_de_enderecos2
if a== '3':
 listas_de_enderecosC=listas_de_enderecos3
if a== '4':
 listas_de_enderecosC=listas_de_enderecos4
if a== '5':
 listas_de_enderecosC=listas_de_enderecos5
if a== '6':
 listas_de_enderecosC=listas_de_enderecos6
if a== '7':
 listas_de_enderecosC=listas_de_enderecos7
if a== '8':
 listas_de_enderecosC=listas_de_enderecos8
if a== '9':
 listas_de_enderecosC=listas_de_enderecos9
if a== '10':
 listas_de_enderecosC=listas_de_enderecos10
if a== '11':
 listas_de_enderecosC=listas_de_enderecos11
if a== '12':
 listas_de_enderecosC=listas_de_enderecos12
if a== '13':
 listas_de_enderecosC=listas_de_enderecos13
if a== '14':
 listas_de_enderecosC=listas_de_enderecos14
if a== '15':
 listas_de_enderecosC=listas_de_enderecos15
if a== '16':
 listas_de_enderecosC=listas_de_enderecos16
if a== '17':
 listas_de_enderecosC=listas_de_enderecos17
if a== '18':
 listas_de_enderecosC=listas_de_enderecos18
if a== '19':
 listas_de_enderecosC=listas_de_enderecos19
if a== '20':
 listas_de_enderecosC=listas_de_enderecos20
if a== '20':
 listas_de_enderecosC=listas_de_enderecos20
if a== '20':
 listas_de_enderecosC=listas_de_enderecos20
if a== '21':
 listas_de_enderecosC=listas_de_enderecos21
if a== '22':
 listas_de_enderecosC=listas_de_enderecos22
if a== '23':
 listas_de_enderecosC=listas_de_enderecos23
if a== '24':
 listas_de_enderecosC=listas_de_enderecos24
if a== '25':
 listas_de_enderecosC=listas_de_enderecos25
if a== '26':
 listas_de_enderecosC=listas_de_enderecos26
if a== '27':
 listas_de_enderecosC=listas_de_enderecos27
if a== '28':
 listas_de_enderecosC=listas_de_enderecos28
if a== '29':
 listas_de_enderecosC=listas_de_enderecos29
if a== '30':
 listas_de_enderecosC=listas_de_enderecos30
if a== '31':
 listas_de_enderecosC=listas_de_enderecos31
if a== '32':
 listas_de_enderecosC=listas_de_enderecos32
if a== '33':
 listas_de_enderecosC=listas_de_enderecos33
if a== '34':
 listas_de_enderecosC=listas_de_enderecos34
if a== '35':
 listas_de_enderecosC=listas_de_enderecos35
if a== '36':
 listas_de_enderecosC=listas_de_enderecos36
if a== '37':
 listas_de_enderecosC=listas_de_enderecos37
if a== '38':
 listas_de_enderecosC=listas_de_enderecos38
if a== '39':
 listas_de_enderecosC=listas_de_enderecos39
if a== '40':
 listas_de_enderecosC=listas_de_enderecos40
if a== '41':
 listas_de_enderecosC=listas_de_enderecos41
if a== '42':
 listas_de_enderecosC=listas_de_enderecos42
if a== '43':
 listas_de_enderecosC=listas_de_enderecos43
if a== '44':
 listas_de_enderecosC=listas_de_enderecos44
if a== '45':
 listas_de_enderecosC=listas_de_enderecos45
if a== '46':
 listas_de_enderecosC=listas_de_enderecos46
if a== '47':
 listas_de_enderecosC=listas_de_enderecos47
if a== '48':
 listas_de_enderecosC=listas_de_enderecos48
if a== '49':
 listas_de_enderecosC=listas_de_enderecos49
if a== '50':
 listas_de_enderecosC=listas_de_enderecos50
if a== '51':
 listas_de_enderecosC=listas_de_enderecos51
if a== '52':
 listas_de_enderecosC=listas_de_enderecos52
if a== '53':
 listas_de_enderecosC=listas_de_enderecos53
if a== '54':
 listas_de_enderecosC=listas_de_enderecos54
if a== '55':
 listas_de_enderecosC=listas_de_enderecos55
if a== '56':
 listas_de_enderecosC=listas_de_enderecos56
if a== '57':
 listas_de_enderecosC=listas_de_enderecos57
if a== '58':
 listas_de_enderecosC=listas_de_enderecos58
if a== '59':
 listas_de_enderecosC=listas_de_enderecos59
if a== '60':
 listas_de_enderecosC=listas_de_enderecos60

 
 
 
for ender in  listas_de_enderecosC:
  try:
    get_feeds(ender)
  except: pass
  conn.commit()
 


 
#get_usrs("100002272680690")

 