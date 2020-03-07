from app import megaapp

@megaapp.route('/')
@megaapp.route('/index')
def index():
	return "Hello, World!"