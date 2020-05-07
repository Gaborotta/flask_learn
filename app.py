#%%
import os
import json
from flask import Flask, session
from flask import render_template, url_for, redirect, flash
from flask import request
from flask import make_response
from werkzeug.utils import secure_filename
from random import random

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String #DBのテーブルの型をインポート
# from flask_wtf.csrf import CSRFProtect

# from form import Thema_form, Sub_Thema_form

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.sqlite' # DBへのパス
# csrf = CSRFProtect(app)

db = SQLAlchemy(app)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# メインページ
@app.route('/main', methods=["GET", "POST"])
def main_page():
    if request.method == 'POST':
        main_thema = request.form['main_thema']
        response = make_response(render_template('sub.html', main_thema=main_thema))
        response.set_cookie('main_thema', main_thema)
        return response    
    return render_template('main.html')

# サブテーマページ
@app.route('/sub', methods=["GET", "POST"])
def sub_page():
    if request.method == 'GET':
        main_thema = request.cookies.get('main_thema')
        if main_thema:
            return render_template('sub.html', main_thema=main_thema)
        else:
            return render_template('main.html')
    elif request.method == 'POST':
        main_thema = request.cookies.get('main_thema')
        # print(request.form)       
        response = make_response(render_template('whole.html', main_thema=main_thema, sub_themas=request.form.to_dict()))
        response.set_cookie('sub_themas', value=json.dumps(request.form.to_dict()) )
        return response    

# マンダラートページ
@app.route('/whole', methods=["GET", "POST"])
def whole_page():
    if request.method == 'GET':
        main_thema = request.cookies.get('main_thema')
        sub_themas = json.loads(request.cookies.get('sub_themas'))
        if sub_themas:
            return render_template('whole.html', main_thema=main_thema, sub_themas=sub_themas)
        elif main_thema:
            return render_template('sub.html', main_thema=main_thema)
        else:
            return render_template('main.html')
    elif request.method == 'POST':
        # if len([i for i in request.form.items() if i != ""]) < 8:
        #     response = make_response(render_template('whole.html', main_thema=main_thema, sub_themas=sub_themas))
        #     response.set_cookie('ideas', value=json.dumps(request.form.to_dict()) )
        #     return response
        main_thema = request.cookies.get('main_thema')
        sub_themas = json.loads(request.cookies.get('sub_themas'))
        
        print(request.form)       
        response = make_response(render_template('finish.html', main_thema=main_thema, sub_themas=sub_themas, ideas=request.form.to_dict()))
        response.set_cookie('ideas', value=json.dumps(request.form.to_dict()) )
        return response    

# 完成ページ
@app.route('/finish', methods=["GET", "POST"])
def finish_page():
    if request.method == 'GET':
        main_thema = request.cookies.get('main_thema')
        sub_themas = json.loads(request.cookies.get('sub_themas'))
        ideas = json.loads(request.cookies.get('ideas'))       
        return render_template('finish.html', main_thema=main_thema, sub_themas=sub_themas, ideas=ideas)
    elif request.method == 'POST':
        twitter = request.cookies.get('main_thema')
        return

### 下記勉強

@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.form['name'] and request.files['image']:
        f = request.files['image']
        file_path = 'static/' + secure_filename(f.filename)
        f.save(file_path)
        return render_template('result.html', name=request.form['name'], image_url=file_path)

@app.route('/login', methods=['GET'])
def rende_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template(
            'check.html', 
            email= request.form['email'],
            username= request.form['username']
        )
    else:
        return render_template('error.html')

@app.route('/search')
def search():
    q = request.args.get('q', '')
    return f'{q}'

@app.route('/user/<int:user_id>')
def user_id(user_id):
    return f'{user_id}'

@app.route('/title/<title>')
def title(title):
    return render_template('index.html',title=title)

@app.route('/hoge',methods=['GET'])
def hoge():
    return 'hoge'

@app.route('/hoge',methods=['POST'])
def Hoge():
    return 'Hoge'

# %%
## おまじない
if __name__ == "__main__":
    app.run(debug=True)