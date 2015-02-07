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


def web_search(query):
 opener = urllib2.build_opener()
 pars='query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/request_mind_ex2.php?'+pars, '' ).read()
 return data_Res

def web_search_news(query):
 opener = urllib2.build_opener()
 pars='query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/request_mind_ex_3.php?'+pars, '' ).read()
 return data_Res

def twitter_search(query):
 opener = urllib2.build_opener()
 pars='query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/request_mind2_2.php?'+pars, '' ).read()
 return data_Res
 
def facebook_search(query):
 opener = urllib2.build_opener()
 pars='query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/get_facebook2.php?'+pars, '' ).read()
 return data_Res

def video_search(query):
 opener = urllib2.build_opener()
 pars='query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/request_video.php?'+pars, '' ).read()
 return data_Res

def wiki_search(query):
 opener = urllib2.build_opener()
 pars='query='+(query)
 data_Res = opener.open('http://mind-net.com/mind-net/request_wiki.php?'+pars, '' ).read()
 return data_Res
 
def entry(req,query,t):
 query=urllib.quote(query)
 rt=''
 if t == 'social':
  rt= facebook_search(query)
 elif t == 'web':
  rt= web_search(query)
 elif t == 'news':
  rt= web_search_news(query)
 elif t == 'blog':
  rt=  twitter_search(query)
 elif t == 'video':
  rt=  video_search(query)
 elif t =="wiki":
  rt= wiki_search(query)
 #====
 return rt
 
 
 
 