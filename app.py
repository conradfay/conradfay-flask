import flask, flask.views
import settings

import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, create_session

#Views
from login import Login
from remote import Remote
from music import Music
from main import Main
from show_users import Show_users
from register import Register
from change_password import Change_password
from account_settings import Account_settings

#Create App
app = flask.Flask(__name__)
app.secret_key = settings.secret_key

#Routes
app.add_url_rule('/', 
		view_func=Main.as_view('main'),
		methods=['GET', 'POST'])
app.add_url_rule('/<page>/', 
		view_func=Main.as_view('main'), 
		methods=['GET'])
app.add_url_rule('/login/', 
		view_func=Login.as_view('login'),
		methods=['GET', 'POST'])
app.add_url_rule('/remote/', 
		view_func=Remote.as_view('remote'), 
		methods=['GET', 'POST'])
app.add_url_rule('/music/', 
		view_func=Music.as_view('music'), 
		methods=['GET'])
app.add_url_rule('/show-users/', 
		view_func=Show_users.as_view('show_users'), 
		methods=['GET'])
app.add_url_rule('/register/', 
		view_func=Register.as_view('register'), 
		methods=['GET', 'POST'])
app.add_url_rule('/account-settings/', 
		view_func=Account_settings.as_view('account_settings'), 
		methods=['GET'])
app.add_url_rule('/account-settings/change-password/', 
		view_func=Change_password.as_view('change_password'), 
		methods=['GET', 'POST'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run()
