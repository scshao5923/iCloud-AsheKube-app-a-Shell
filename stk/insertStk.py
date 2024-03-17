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
qty=int(sys.argv[4])
prc=float(sys.argv[5])
amt=int(round(qty*prc,0))
fee=int(sys.argv[6])
tax=int(sys.argv[7])
if salty=="買":
	net=(amt+fee+tax)*-1
else:
	net=amt-fee-tax
txdat=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mk="B"
cursor=db.cursor()
cursor.execute(
	"insert into trans(dtdat,stk,salty,qty,prc,amt,fee,tax,net,txdat,mk) values(?,?,?,?,?,?,?,?,?,?,?)" 
        ,(dtdat,stk,salty,qty,prc,amt,fee,tax,net,txdat,mk)
)
db.commit()
db.close()
