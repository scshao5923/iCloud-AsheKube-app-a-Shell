import datetime
import sqlite3
import sys
import mypath
# if sys.platform=='win32':
#     dataPath="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell"
# else:
#     dataPath="/private/var/mobile/Library/Mobile Documents/iCloud~AsheKube~app~a-Shell/Documents"

db=sqlite3.connect(mypath.dataPath+"/db/stk.db")
dtdat=sys.argv[1]
ary=dtdat.split("-")
if len(ary[1])==1:
   ary[1]="0"+ary[1]
if len(ary[2])==1:
   ary[2]="0"+ary[2]
dtdat=ary[0]+"-"+ary[1]+"-"+ary[2]
stk=sys.argv[2]
salty=sys.argv[3]
cursor=db.cursor()
cursor.execute(
	"select dtdat,stk,salty,qty,prc,fee,tax from trans where mk='B' and dtdat=? and stk=? and salty=?" 
        ,(dtdat, stk, salty
        )
)
result=""
for row in cursor:
   result=result+\
      "成交日期:"+row[0]+","+\
      "股票:"+row[1]+","+\
      "買賣別:"+row[2]+","+\
      "數量:"+str(row[3])+","+\
      "單價:"+str(row[4])+","+\
      "手續費:"+str(row[5])+","+\
      "稅額:"+str(row[6])+\
      "\n"
db.close()
print(dtdat,stk,salty)
print(result)
