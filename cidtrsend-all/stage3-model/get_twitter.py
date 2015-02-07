from mod_python import apache
import simplejson
import twitter

import base64
import calendar
import os
import rfc822
import simplejson
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse


def UrlEncode(s):
    r = ''
    for c in s:
        o = ord(c)
        if (o >= 48 and o <= 57) or \
            (o >= 97 and o <= 122) or \
            (o >= 65 and o <= 90) or \
            o == 36 or o == 45 or o == 95 or \
            o == 46 or o == 43 or o == 33 or \
            o == 42 or o == 39 or o == 40 or \
            o == 41 or o == 44:
            r += c
        else:
            r += '%' + CleanCharHex(c)
    return r

def twitter_info(usr):
   k='<html><body>'
   api=twitter.Api()
   statuses=api.GetUserTimeline(usr)
   for d in statuses:
      k+= ( '<font size="2" color="red">'+d.created_at+'</font>'+":"+ d.text  +'<br>' )
   return k+'</body></html>'

def entry(req,usr):
 return twitter_info(usr)
 
 
 
 