#!/usr/bin/env python

#
#	The server that doesn't use the Name Server.
#

import sys, os
import Pyro.core
from Pyro.errors import PyroError


class bc(Pyro.core.ObjBase):
 cc=''
 def __init__(self):
  Pyro.core.ObjBase.__init__(self)
    


class QuoteGen(Pyro.core.ObjBase):
   a=bc()
   def __init__(self):
    	Pyro.core.ObjBase.__init__(self)
   def quote(self):  
        return self.a	
    	
		
Pyro.core.initServer()

daemon = Pyro.core.Daemon()
print
print 'The Pyro Deamon is running on ',daemon.hostname+':'+str(daemon.port)
print '(you may need this info for the client to connect to)'
print

objectName='QuoteGenerator'

uri=daemon.connect(bc(),objectName)
uri=daemon.connect(QuoteGen(),'bc')

# enter the service loop.
print 'QuoteGen is ready for customers. I am not using the Name Server.'
print 'Object name is:',objectName
print 'The URI is: ',uri

daemon.requestLoop()

