#%%
from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html', 
        # obj={'title': 'hoge'}, random=random(), 
        # l=['Hoge','Fuga','Foo']
        l= [
            {'name': 'hoge', 'value': '1'},
            {'name': 'fuga', 'value': '2'},
            {'name': 'Foo', 'value': '3'},
        ]
    )

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