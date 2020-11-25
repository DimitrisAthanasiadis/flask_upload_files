#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import math

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploaded_images')
ALLOWED_EXTENSIONS = set(['zip', 'gif', 'jpg', 'png'])
SECRET_KEY = os.urandom(24)

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if not os.path.exists(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('file')
        # if user does not select file, br~owser also
        # submit a empty part without filename
        if len(files) == 0:
            flash('No selected file(s)')
            return redirect(request.url)

        files_size = 0
        for file in files:
            file.seek(0, os.SEEK_END)
            files_size += file.tell()

        # θα εχει περιοριστει ηδη με javascript
        file_size_mb = files_size*math.pow(10, -6)

        if file_size_mb > 25:
            flash('File size too large')
            return redirect(request.url)

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                # zip_ref = zipfile.ZipFile(os.path.join(UPLOAD_FOLDER, filename), 'r')
                # zip_ref.extractall(UPLOAD_FOLDER)
                # zip_ref.close()
        return redirect(url_for('upload_file'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
