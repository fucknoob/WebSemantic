# conexao

import sys

sys.path.append('c:/python25/mxdb')

import maxdb

user = 'MIND'
pwd = 'MIND'

host = '91.205.172.85'
dbname = 'MINDNET'

print 'Connecting to knowledge cluster(2)....'
conn_mx = maxdb.connect (user, pwd, dbname, host)
print 'Connected(2).'
