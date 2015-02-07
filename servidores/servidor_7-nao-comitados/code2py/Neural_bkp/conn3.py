# conexao

import sys

sys.path.append('/Neural/mxdb')

import maxdb

user = 'MIND'
pwd = 'MIND'

host = '91.205.172.85'
dbname = 'MINDNET'

print 'Connecting to knowledge cluster....'
conn_mx = maxdb.connect (user, pwd, dbname, host)
print 'Connected.'
