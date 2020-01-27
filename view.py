import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from gpx2geojson import convert

UPLOAD_DIR = os.getenv('UPLOAD_DIR')
ALLOWED_EXTENSIONS = {'gpx'}

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html', flg=None, alert='アップロードするファイルを選択し、送信してください')
    if request.method == 'POST':
        if 'inputFile' not in request.files:
            return render_template('index.html', flg=False, alert='アップロードするファイルが指定されていません')
        file = request.files['inputFile']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_DIR'], secure_filename(file.filename))
            file.save(filename)
            convert(filename)
            return render_template('index.html', flg=True, alert='ファイル　%s をアップロードしました' % filename)
        else:
            return render_template('index.html', flg=False, alert='.gpxファイル以外は処理できません')

if __name__=='__main__':
    app.run(debug=True)
