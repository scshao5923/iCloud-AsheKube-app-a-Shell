import sqlite3
from flask import render_template
import arrow
import sys
import mypath
# if sys.platform=='win32':
#     dataPath="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell"
# else:
#     dataPath="/private/var/mobile/Library/Mobile Documents/iCloud~AsheKube~app~a-Shell/Documents"


def get_heart():
    a = arrow.now()
    beg = a.shift(months=-1).format("YYYY-MM-DD")
    sql = """
select 
    sp, dp, pulse, deg, txdat, km, stepNum 
    from heart
    where txdat > ?
    order by txdat
"""
    db = sqlite3.connect(
        mypath.dataPath+"/db/health.db"
    )
    cursor = db.cursor()
    cursor.execute(sql, (beg,))
    result = cursor.fetchall()
    d = {}

    for rec in result:
        txdat = rec[4][0:10]
        hh = rec[4][11:13]
        if txdat not in d:
            d[txdat] = [None, None]
        if rec[4][11:13] < "18":
            d[txdat][0] = rec
        else:
            d[txdat][1] = rec
    db.commit()
    db.close()
    str = render_template('getHeart.html', h=d)
    f = open(mypath.dataPath+"/temp/cardiology.html", "w", encoding="utf8")
    f.write(str)
    f.close()
    return str


if __name__ == "__main__":
    print(get_heart())
