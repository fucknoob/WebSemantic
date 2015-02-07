
import simplejson
import urllib
import os
import sys
import urllib2
import umisc
import gc
import thread
import time

import logging
from StringIO import StringIO
import datetime
import time, datetime


def post_msg(id,msg,token):
    args = {}    
    args['access_token'],args['message'] ,args['METHOD']=  token,msg,'POST'

    url='https://graph.facebook.com/'+id+'/feed?' + urllib.urlencode(args)
    
    print url
    
    #file = urllib2.urlopen(url)



post_msg("1773861276","teste app",'AAAESh5j8VvwBAOSkw4eTYvqjZBzzsdutjnCDA4WnT0EqL775OJhpat2A1OFd3ezSQX2nVRLxYFIfhKU3KQmrjZBkIZCvs1pMLcB5tJVUyHQZA3cnERAr')