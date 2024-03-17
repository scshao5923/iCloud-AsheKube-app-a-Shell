import os
from stk import qrystk
import mypath
# dataPath="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell"
p1=input("查詢類型:1股票2成交日:")
p2=input("查詢資料:")
p3=input("排序類型:1股票2成交日:")
try:
    content=qrystk.qry(
        'stk' if p1=='1' else 'dtdat'
        ,p2
        ,'stk,dtdat' if p3=='1' else 'dtdat,stk'
        ,True
    )
except Exception as error:
    print(error)
    input("please press enter to continue....")
f=open(mypath.dataPath+'/temp/result.html','w', encoding='utf-8')
f.write(content)
f.close()
os.system(mypath.dataPath+'/temp/result.html')
