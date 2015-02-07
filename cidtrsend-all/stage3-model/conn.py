# conexao

import sys

sys.path.append('c:/python25/mxdb')

import maxdb

user = 'MIND'
#user = 'MIND2'
pwd = 'MIND'

#host = '192.168.18.20'
host = 'localhost'
dbname = 'AS4'

#dbname = 'mindnet'
#host = '109.235.146.89:3306'


print 'Connecting to knowledge cluster(1)....[',dbname,host,']'
conn_mx = maxdb.connect (user, pwd, dbname, host)
print 'MxDb.Connected.'
