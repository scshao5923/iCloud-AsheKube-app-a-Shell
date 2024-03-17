import re
import sqlite3
import sys
import mypath
# if sys.platform=='win32':
#     dataPath="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell"
# else:
#     dataPath="/private/var/mobile/Library/Mobile Documents/iCloud~AsheKube~app~a-Shell/Documents"
sql="select distinct stk from trans order by stk"
db=sqlite3.connect(mypath.dataPath+"/db/stk.db")
cursor=db.cursor()
cursor.execute(sql)
result = cursor.fetchall()
db.commit()
db.close()
#print(result)
lst="0000自行輸入"
for x in result:
	lst=lst+","+x[0]
#print(lst)，
print(re.sub(",$","",lst))
#f=open(dataPath+"/tmp/stk.txt","w")
#f.write(re.sub(",$","",lst))
#f.close()
