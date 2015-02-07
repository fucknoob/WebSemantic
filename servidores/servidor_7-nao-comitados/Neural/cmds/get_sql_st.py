import sys
sys.path.append('/home/mdnetsearc/public_html/Neural/MySQLdb')
        
import MySQLdb 



sql="SELECT url,rec_id FROM  url WHERE url LIKE  '%Moip%' LIMIT 0 , 20"
#conn3= MySQLdb.connect(host='200.98.197.245', user='esyns1' , passwd='acc159753', db='esyns1') 
conn3= MySQLdb.connect(host='200.98.197.232', user='esyns1_1' , passwd='acc159753', db='esyns1_1') 

cursor = conn3.cursor ()
cursor2 = conn3.cursor ()
cursor.execute (sql) 
resultSet = cursor.fetchall()

file = open("cc.txt", "w")

for results in resultSet:     
  file.write(str(results[1])+'->'+results[0] +"\n") 
  file.write("==========================\n") 
  
  sql2="SELECT sname,sval FROM  urlinfo WHERE url_id = " + str(results[1])
  cursor2.execute (sql2) 
  resultSet2 = cursor2.fetchall()
  for results2 in resultSet2:
   file.write( results2[0] + ":" +results2[1] )
   file.write("\n")
 
  file.write("==========================\n") 

file.close()