import flask, flask.views
import db
from db import Session

users = {'admin':'123apples'}

class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('login.html')

    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            flask.flash('logout successful')
            return flask.redirect(flask.url_for('login'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('login'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        
        #Session and username/password gets added to dictionary
        session = Session()
        for instance in session.query(db.User).order_by(db.User.id): 
            users[instance.username]=instance.password
            print users
        
        if username in users and users[username] == passwd:
            flask.session['username'] = username
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('login'))
