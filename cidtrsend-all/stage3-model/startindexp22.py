# coding: latin-1



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
import socket

def entry(req,logid,q,cn):
 client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client_socket.connect(("localhost", 5005))   
 client_socket.send((logid+'|'+q+'|'+cn+'|'))
 #============================
 return 'CmdOK'
