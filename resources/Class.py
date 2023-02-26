from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.Class import Class

class ClassResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('lastName', type=str)

    @jwt_required()
    def get(self, name):
        ele = Class.findByName(name)
        if ele:
            return ele.json()    
        return {'message': f'class {name} not found'}, 400

    def post(self, name):
        ele = Class.findByName(name)
        if ele:
            return {'message': f'class {name} allready exist'}, 400
        
        data = self.parser.parse_args()
        ele = Class(name)
        ele.save()
        return ele.json()

    def delete(self, name):
        ele = Class.findByName(name)
        if ele:
            ele.delete()
            return {'message': f'ele {name} deleted successfully'}, 202
        return {'message': f'ele {name} doesn\'t exist'}, 400


class ClassesResource(Resource):
    def get(self):
        return {'classes':[ele.json() for ele in Class.query.all()]}