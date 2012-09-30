import flask, flask.views
import utils
import db
from db import Session

class Register(flask.views.MethodView):
    def get(self):
        return flask.render_template('register.html')
    
    def post(self):
        session = Session()
        
        new_user = db.User(flask.request.form['username'], flask.request.form['first_name'], flask.request.form['last_name'], flask.request.form['password'])
        session.add(new_user)
        session.commit()
        flask.flash('Welcome! Please log in now!')
        
        return flask.redirect(flask.url_for('login'))
    

