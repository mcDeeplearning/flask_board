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
    # posts = Post.query.all()
    # SELECT * FROM posts;
    posts = Post.query.order_by(Post.id.desc()).all()
    # SELECT * FROM posts ORDER BY id DESE;
    return render_template('index.html',posts=posts)

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
    
    return render_template('create.html',post=post)
    
@app.route('/posts/<int:id>')
def read(id):
    post = Post.query.get(id)
    # SELECT * FROM posts WHERE id=1;
    return render_template('read.html',post=post)
    
    