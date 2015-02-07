# Note, am using two-legged auth here.
# needs http://drupal.org/node/1336974 for two-legged and http://drupal.org/node/1337718 if using a nonstandard port.
#
# there's a couple of approaches here.  One uses xmlrpclib, one doesn't.  Both use oauth2 - but could probably be worked with oauth
#
# services_endpoint needs to be something like (serialiazed as I've pulled it from database and there's no form yet):
#  a:1:{s:14:"services_oauth";a:3:{s:13:"oauth_context";s:n:"CONTEXT GOES HERE";s:11:"credentials";s:8:"consumer";s:13:"authorization";s:n:"DEFAULT SECURITY LEVEL GOES HERE";}}
# Don't forget to fix for 'CONTEXT GOES HERE' and 'DEFAULT SECURITY LEVEL GOES HERE' (and fix 'n' to be the right number)
import oauth2
import time
import urllib2
import xmlrpclib
host_key = 'PUT A KEY HERE'
host_secret = 'PUT A SECRET HERE'
# this is the endpoint.
host = 'https://api-ssl.bitly.com'
class OAuthTransport(xmlrpclib.SafeTransport):
    def __init__(self, host, verbose = None, use_datetime=0):
        xmlrpclib.SafeTransport.__init__(self)
        self.verbose = verbose
        self._use_datetime = use_datetime
        self.host = host
    def oauth_request(self, url, moreparams={}, body=''):
        params = {
            'oauth_version': "1.0",
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': int(time.time())
            }
        consumer = oauth2.Consumer(key=host_key,secret=host_secret)
        params['oauth_consumer_key'] = consumer.key
        params.update(moreparams)
        req = oauth2.Request(method='POST', url=url, parameters=params, body=body)
        signature_method = oauth2.SignatureMethod_HMAC_SHA1()
        req.sign_request(signature_method, consumer, None)
        return req
    def single_request(self, host, handler, request_body, verbose=0):
        if (verbose):
            print(host)
            print(handler)
            print(request_body)
        # the parameters call for host + handler - but they've dropped the method (eg:https)
        request = self.oauth_request(url=self.host, body=request_body)
        req = urllib2.Request(request.to_url())
        req.add_header('Content-Type', 'text/xml')
        req.add_data(request_body)
        f = urllib2.urlopen(req)
        return(self.parse_response(f))
def build_request(url, moreparams={}, body=''):
    params = {
        'oauth_version': "1.0",
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time())
    }
    consumer = oauth2.Consumer(key=host_key,secret=host_secret)
    params['oauth_consumer_key'] = consumer.key
    params.update(moreparams)
    req = oauth2.Request(method='POST', url=url, parameters=params, body=body)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, None)
    return req
trans = OAuthTransport(host)
server = xmlrpclib.ServerProxy(host, transport=trans)
if (1):
    try:
        for method in server.system.listMethods():
            print method
            # it would be really nice if introspection works.  Currently it doesn't.
#            print '\n'.join(['  ' + x for x in server.system.methodHelp(method).split('\n')])
#            print
    except xmlrpclib.Fault, err:
        print "A fault occurred"
        print "Fault code: %d" % err.faultCode
        print "Fault string: %s" % err.faultString
if (1):
    req_body = '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
    request = build_request(url=host, moreparams={}, body=req_body)
    u = urllib2.urlopen(request.to_url(), req_body)
    print u.readlines()
# note that it returns a lot of extra information.   Suspect node.retrieve unfinished.
try:
    print server.node.retrieve(3, ['nid','title'])
except xmlrpclib.Fault, err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString
req_body = '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
request = build_request(url=host, moreparams={}, body=req_body)
u = urllib2.urlopen(request.to_url(), req_body)
print u.readlines()