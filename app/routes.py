<<<<<<< HEAD
from flask import render_template, flash, redirect, url_for
from app import megaapp
from app.forms import LoginForm
=======
from app import megaapp
>>>>>>> 30213821a289cdfe467137d6d5a99e7f3a218aeb

@megaapp.route('/')
@megaapp.route('/index')
def index():
<<<<<<< HEAD
    user = {'username':'Tuan'}
    posts=[{'author': {'username': 'John'},'body': 'Beautiful day in Portland!'},{'author': {'username': 'Susan'},'body': 'The Avengers movie was so cool!'}]
    return render_template('index.htm', title='Home', user=user, posts=posts)


@megaapp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me= {}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.htm', title='Sign In', form=form)
=======
	return "Hello, World!"
>>>>>>> 30213821a289cdfe467137d6d5a99e7f3a218aeb
