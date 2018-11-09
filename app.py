from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *
import os

app = Flask(__name__)
# DB 설정
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///board'
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    # posts = Post.query.all()
    # SELECT * FROM posts;
    posts = Post.query.all()
    # SELECT * FROM posts ORDER BY id DESE;
    return render_template('index.html',posts=posts)

@app.route('/posts/new')
def new():
    return render_template('new.html')

@app.route('/posts/create', methods=["POST"])
def create():
    # title = request.args.get('title')
    title = request.form.get('title')
    # content = request.args.get('content')
    content = request.form.get('content')
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    
    # return render_template('create.html')
    return redirect('/posts/{}'.format(post.id))
    
@app.route('/posts/<int:id>')
def read(id):
    post = Post.query.get(id)
    # SELECT * FROM posts WHERE id=1;
    return render_template('read.html',post=post)
    
@app.route('/posts/<int:id>/delete') 
def delete(id):
    post = Post.query.get(id)
    # DELETE FROM posts WHERE id=3;
    db.session.delete(post)
    db.session.commit()
    
    return redirect('/')
    
@app.route('/posts/<int:id>/edit')
def edit(id):
    post = Post.query.get(id)
    return render_template('edit.html',post=post)
    
@app.route('/posts/<int:id>/update', methods=["POST"])
def update(id):
    post = Post.query.get(id)
    post.title = request.form.get('title')
    post.content = request.form.get('content')
    # post.title = request.args.get('title')
    # post.content = request.args.get('content')
    db.session.commit()
    
    return redirect('/posts/{}'.format(id))