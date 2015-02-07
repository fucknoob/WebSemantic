import MySQLdb


conn= MySQLdb.connect(host='dbmy0020.whservidor.com', user='mdnetsearc' , passwd='acc159753',db='mdnetsearc')
print 'Connected...'
cursor = conn.cursor ()
cursor.execute ('select url_id,sval from urlinfo where url_id not in( select just_processed from pg_processed  ) and sname = \'body\' order by url_id  LIMIT 1,1') 
print 'sql executed!!'
resultSet = cursor.fetchall()
for results in resultSet:     
    id= results[0]
    pg= results[1]
    print 'id:',id
