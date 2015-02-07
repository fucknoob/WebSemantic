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



def entry(req,w):
 return '<p>The secret word is <b>'+w+'</b> and your IP is <b>127.0.0.1</b>.</p>'
 
 
 
 