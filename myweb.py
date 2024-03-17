from flask import \
    Flask, flash, request, redirect, url_for, send_from_directory, \
    render_template
from werkzeug.utils import secure_filename
from markupsafe import escape
from health import cardiology
from stk import qrystk
import os, sys, time
import mypath

# if sys.platform=='win32':
#     UPLOAD_FOLDER="C:/Users/scsha/iCloudDrive/iCloud~AsheKube~app~a-Shell/uploads"
# else:
#     UPLOAD_FOLDER="/private/var/mobile/Library/Mobile Documents/iCloud~AsheKube~app~a-Shell/Documents/uploads"

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = mypath.dataPath+"/uploads"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    h=vars(request)
    h={k: h[k] for k in sorted(h)}
    print()
    print(os.urandom(40))
    for k in h:
        print(k,':',h[k])
    print(request.files)
    print()
    if request.method == 'POST':
        print('request.form:'+str(request.form))
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('Not allowed file:'+file.filename)
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template("upload.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route("/getheart")
def getHeart():
	return cardiology.get_heart()

@app.route("/qrystk")
def qryStk():
    whereTy = request.args.get('whereTy', '')
    data=request.args.get('data','')
    orderTy=request.args.get('orderTy','')
    return qrystk.qry(whereTy,data,orderTy)

@app.route("/test/<path:tmpstr>")
def showTmpstr(tmpstr):
    return f'tmpstr {escape(tmpstr)}'

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()

