import flask, flask.views
import utils
import db
from db import Session

class Change_password(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('change_password.html')
    
    @utils.login_required
    def post(self):
        session = Session()
        
        #get current user entry
        for u in session.query(db.User).filter(db.User.username==flask.request.form['username']):  
            user = u
        

        
        #check if old password is right
        if flask.request.form['old_password'] != user.password:
            flask.flash('incorrect old password!')
            return flask.redirect(flask.url_for('account_settings'))
        #check if two passwords match
        elif flask.request.form['new_password'] != flask.request.form['new_password_2']:
            flask.flash('two passwords do not match!')
            return flask.redirect(flask.url_for('account_settings'))
        #append new password to the user
        else:
            user.password = flask.request.form['new_password']
            flask.flash('password successfully updated')
            session.commit()
            return flask.redirect(flask.url_for('login'))
            
        
    





























