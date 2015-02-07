# conexao

import sys

sys.path.append('/Neural/mxdb')

import maxdb

user = 'MIND'
pwd = 'MIND'

#host = '192.168.18.20'
#dbname = 'AS4'

dbname = 'mindnet'
host = '127.0.0.1'


print 'Connecting to knowledge cluster....'
conn_mx = maxdb.connect (user, pwd, dbname, host)
print 'Connected.'
