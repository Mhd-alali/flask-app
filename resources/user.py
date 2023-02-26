from flask_restful import Resource, Api, reqparse
from models.user import User

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)

    def post(self):
        data = self.parser.parse_args()
        if User.findByUsername(data['username']):
            return {'message': f'user {data["username"]} allready exist'}, 400
        user = User(**data)
        user.save()
        return user.json()
