from flask import render_template
from app import megaapp

@megaapp.route('/')
@megaapp.route('/index')
def index():
	user = {'username':'Tuan'}
	return render_template('index.htm',title='Home Page',user=user)
