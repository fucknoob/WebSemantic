# call processes in server heroku

import urllib2, cookielib, re, os, sys
import facebook
import urllib
import simplejson


FACEBOOK_APP_ID     = '301848573269756'
FACEBOOK_APP_SECRET = '4a900fa8e641b7057ec9d6ec40e53b96'
FACEBOOK_PROFILE_ID = '1773861276'

API_KEY = '11e517548871c8813a8923b40009a060'


class Facebook:
    def __init__(self, email, password,appid):
        self.email = email
        self.appid=appid
        self.password = password

        self.cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
                            ('Content-Type', 'application/x-www-form-urlencoded'),
                            ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]
        self.opener = opener

    def login(self):
        url = 'https://login.facebook.com/login.php?login_attempt=1'
        
        data = "locale=en_US&non_com_login=&email="+self.email+"&pass="+self.password+"&lsd=20TOl"
        
        usock = self.opener.open('http://www.facebook.com')
        usock = self.opener.open(url, data)
        st=usock.read()
        
        if "Logout" in st:
            #print "Logged in."
            pass
        else:
            #print "failed login"
            print usock.read()
            sys.exit()
            
        #====================================================================    
        url='http://www.facebook.com/desktopapp.php?'
        usock = self.opener.open(url)
        st=usock.read()
        #==============
        #url='https://www.facebook.com/dialog/oauth?client_id=YOUR_APP_ID&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=COMMA_SEPARATED_LIST_OF_PERMISSION_NAMES&response_type=token'
        #user_birthday,read_stream,user_status,publish_stream,user_photos,manage_pages,offline_access
        url='https://www.facebook.com/dialog/oauth?client_id='+self.appid+'&scope=user_birthday,read_stream,user_status,publish_stream,user_photos,manage_pages,offline_access&redirect_uri=https://www.facebook.com/connect/login_success.html&response_type=token'
        usock = self.opener.open(url)
        finalurl = usock.geturl()
        tok=''
        rea=False
        e_i=False
        for s in finalurl:
         if s=='#':
          rea=True
         elif s=='&' and rea:
          e_i=True
         elif rea and not e_i:
           tok+=s
        # retorna o token
        tok=tok[13:]
        return tok        
 

    def get_obj_by_id(self,id,token):
     args = {}
     args['access_token'],args['ids'] =  token,id
     url='https://graph.facebook.com/?'+urllib.urlencode(args)
     file = self.opener.open(url)
     print file.read()
                           
    def get_link_to_object(self,id,token):
     usr_=''
     post_id_=''
     f1=False
     for s1 in id:
      if s1 =='_':   
       f1=True      
      elif not f1:
       usr_+=s1
      elif f1:
       post_id_+=s1      
    
     #url='https://www.facebook.com/permalink.php?story_fbid=623845214298234&id=133481940001233&access_token=436475979759857|y5uRJqX23I4fK0cChHXysiJyVHk&format=json'    
     
     args = {}    
     args['access_token'],args['story_fbid'] ,args['id']=  token,post_id_,usr_
     url='https://www.facebook.com/permalink.php?' ;
     dt=urllib.urlencode(args)    
     file = urllib2.urlopen(url,dt)
     print file.read()

    def get_object(self,token,obj_id):
     args = {}    
     #url='https://graph.facebook.com/1773861276_281599988638309?access_token=AAAAAAITEghMBAItZAGZCDf0hOY7UoLOcb4hTo0l721vwoY3IIP5DwQlWTiNWYNkZCNCghnZCqCuiYvS3CZBdyjDriF4P5ByyzZBDjsyFVjVIlxDIiEB5Mj'
     url='https://graph.facebook.com/'+obj_id+'?access_token='+token
     file = urllib2.urlopen(url)
     print file.read()

    def post_object(self,token,obj_id,msg):
     args = {}    
     args['access_token'],args['message'] ,args['METHOD']=  token,msg,'POST'
     url='https://graph.facebook.com/'+obj_id+'/comments?'
     file = urllib2.urlopen(url,urllib.urlencode(args) )
     print file.read()
     
    def ur_open(self,vl):
     fil=self.opener.open(vl)
     return fil.read()
     

FACEBOOK_APP_ID     = '301848573269756'
FACEBOOK_APP_SECRET = '4a900fa8e641b7057ec9d6ec40e53b96'


def get_app_token():
    oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                      client_secret = FACEBOOK_APP_SECRET,
                      grant_type    = 'client_credentials',
                      scope = 'user_birthday,read_stream,user_status,publish_stream,user_photos,manage_pages,offline_access')                  
                     
                      
    url='https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args) 

    file = urllib2.urlopen(url)

    oauth_response = file.read()

    tt=oauth_response[:12]
    dt=oauth_response[13:]
    return dt

    
#tokenapp= get_app_token()    
    
f = Facebook("contato@transend.com.br", "mind27011982","301848573269756")

token_cli=f.login()

url_app=[]

def run_id(index):
 global f
 global url_app
 return f.ur_open(url_app[index])


id=0
while id <= 100:
 url_app.append(None)

url_app[0]='https://apps.facebook.com/transend_itrack_a/'




