import sqlite3
import os
import sys
from flask import render_template
import mypath

# if sys.platform=='win32':
#     dataPath="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell"
# else:
#     dataPath="/private/var/mobile/Library/Mobile Documents/iCloud~AsheKube~app~a-Shell/Documents"

def qry(whereTy,data,orderTy,isClient=False):

    sql="select stk,dtdat,salty,qty,prc,amt,fee,tax,net,txdat from trans "+ \
                "where " +whereTy + " like ? "+ \
                "order by " + \
                orderTy
    db=sqlite3.connect(mypath.dataPath+"/db/stk.db")
    cursor=db.cursor()
    cursor.execute(sql , ('%'+data+'%',))
    result = cursor.fetchall()
    db.commit()
    db.close()
    if isClient:
        import jinja2
        templateLoader = jinja2.FileSystemLoader(searchpath=mypath.dataPath+"/templates/")
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = "stk.html"
        template = templateEnv.get_template(TEMPLATE_FILE)
        return template.render(rows=result)  # this is where to put args to the template renderer    
    else:
        return render_template('stk.html', rows=result)

if __name__ == '__main__':
    print(qry('stk', '2548', 'stk,dtdat'))
