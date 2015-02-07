from mod_python import apache

import base64
import calendar
import os
import rfc822
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse


def web_search(start,sessao,query,limit,callback):
 opener = urllib2.build_opener()
 #pars='start='+start+"&limit="+limit+"callback="+callback+'&query='+UrlEncode(query)
 pars='start='+start+"&limit="+limit+"&callback="+callback+'&query='+(query)+'&sessao='+sessao
 #pars='q='+UrlEncode(termo)+'&since_id'
 #data_Res = opener.open('http://mind-net.com/mind-net/request_mind.php', pars).read()
 data_Res = opener.open('http://mind-net.com/mind-net/request_mind_ex22.php?'+pars, '' ).read()
 return data_Res


def twitter_search(start,query,limit,callback):
 opener = urllib2.build_opener()
 pars='start='+start+"&limit="+limit+"&callback="+callback+'&query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/request_mind2.php?'+pars, '' ).read()
 return data_Res
 
def facebook_search(start,query,limit,callback):
 opener = urllib2.build_opener()
 pars='start='+start+"&limit="+limit+"&callback="+callback+'&query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/get_facebook.php?'+pars, '' ).read()
 return data_Res

def entry(req,start,sessao,query,limit,callback):
 #return facebook_search(start,query,limit,callback)
 #return twitter_search(start,query,limit,callback)
 query=urllib.quote(query)
 return web_search(start,sessao,query,limit,callback)
 
 
 
 