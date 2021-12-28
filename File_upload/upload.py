from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)

files = UploadSet('files', ALL)

app.config['UPLOADED_FILES_DEST'] = 'C:/Users/HP/Desktop/test'
configure_uploads(app, files)


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'media' in request.files:
        filename = files.save(request.files['media'])

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
