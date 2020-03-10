#mega = microblog
#from app import app
from app import megaapp, db
from app.models import User,Post

@megaapp.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}