import flask, flask.views
import db
from db import Session
import utils

class Show_users(flask.views.MethodView):
    @utils.login_required
    def get(self):
        session = Session()
        
        user_list = [
        [],
        [],
        [],
        []]
        
        user_entries = -1
        user_entries_length = []
        
        for instance in session.query(db.User).order_by(db.User.id): 
            user_list[0].append(instance.username)
            user_list[1].append(instance.firstname)
            user_list[2].append(instance.lastname)
            user_list[3].append(instance.password)
            user_entries += 1
            user_entries_length.append(user_entries)
        return flask.render_template('show_users.html',
                                     user_entries_length=user_entries_length,
                                     user_list=user_list
                                     )