from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
# DB 설정
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///board'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts/new')
def new():
    return render_template('new.html')

@app.route('/posts/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    
    return render_template('create.html')
    
    