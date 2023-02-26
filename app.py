# py -m app
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from classes.security import identity, authenticate

from resources.user import UserResource
from resources.student import StudentResource, StudentsResource
from resources.Class import ClassResource,ClassesResource

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'abcd'

jwt = JWT(app, authenticate, identity) # /auth

api = Api(app)

api.add_resource(StudentResource, '/student/<string:name>')
api.add_resource(StudentsResource, '/students')

api.add_resource(ClassResource, '/class/<string:name>')
api.add_resource(ClassesResource, '/classes')

api.add_resource(UserResource, '/signin')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
