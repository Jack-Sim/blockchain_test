from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import logout_user, current_user, login_user, login_required
from app.forms import *
from app.models import *
from block_class import Block, Chain

chain = Chain(4, "a")

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {"username":"Jack"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        chain.add_block(user)
        print(chain.blocks[-1].to_string())
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
