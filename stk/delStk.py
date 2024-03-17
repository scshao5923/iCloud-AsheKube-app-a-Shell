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
	"delete from trans where mk='B' and dtdat=? and stk=? and salty=?" 
        ,(dtdat, stk, salty
        )
)
db.commit()
db.close()
