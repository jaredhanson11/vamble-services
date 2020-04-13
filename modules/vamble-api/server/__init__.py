'''
This package contains the Flask REST Api for the Vamble API module.
'''

from vamble_web import flask_setup
from vamble_db.user import User

app = flask_setup.create_app(__name__)
db = flask_setup.create_db(app)
api = flask_setup.create_api(app)
jwt = flask_setup.create_jwt(app)
jwt.load_user = jwt.default_load_user_fn(db.session, User)

# Ugly dependency, but since routes import controller classes
# the api and app objects needs to be available when importing routes
# Attach routes to the Flask-RESTful Resource objects found at controllers/*
from . import routes  # noqa
routes.add_routes(api)
