import datetime
import sqlite3
import sys
import mypath
# if sys.platform=='win32':
#     dataPath="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell"
# else:
#     dataPath="/private/var/mobile/Library/Mobile Documents/iCloud~AsheKube~app~a-Shell/Documents"
db=sqlite3.connect(mypath.dataPath+"/db/health.db")
sp=int(sys.argv[1])
dp=int(sys.argv[2])
pulse=int(sys.argv[3])
deg=int(sys.argv[4])
km=int(sys.argv[5])
stepNum=int(sys.argv[6].replace(',',''))
txdat=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor=db.cursor()
cursor.execute(
	"insert into heart(sp,dp,pulse,deg,txdat,km,stepNum) values(?,?,?,?,?,?,?)" 
        ,(sp,dp,pulse,deg,txdat,km,stepNum)
)
db.commit()
db.close()
