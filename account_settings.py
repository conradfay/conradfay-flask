import flask, flask.views
import db
from db import Session
import utils

class Account_settings(flask.views.MethodView):
    @utils.login_required
    def get(self):
        session = Session()
        
        user_info = []
        
        for instance in session.query(db.User).order_by(db.User.id): 
            user_info.append(instance.username)
            user_info.append(instance.firstname)
            user_info.append(instance.lastname)
            user_info.append(instance.password)
        return flask.render_template('account_settings.html',
                                     user_info=user_info
                                     )