from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.student import Student

class StudentResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('lastName', type=str)
    parser.add_argument('classId', type=int)

    @jwt_required()
    def get(self, name):
        if Student.exist(name):
            return Student.findByStudentName(name).json()
        return {'message': f'student {name} not found'}, 400

    def post(self, name):
        if Student.exist(name):
            return {'message': f'student {name} allready exist'}, 400
        
        data = self.parser.parse_args()
        student = Student(name,data['lastName'],data['classId'])
        student.save()
        return student.json(), 201

    def delete(self, name):
        if Student.exist(name):
            student = Student.findByStudentName(name)
            student.delete()
            return {'message': f'student {name} deleted successfully'}, 202
        return {'message': f'student {name} doesn\'t exist'}, 400

    def put(self, name):
        data = self.parser.parse_args()
        student = Student(name,data['lastName'],data['classId'])
        student.save()
        return student.json(), 201


class StudentsResource(Resource):
    def get(self):
        return {'students':[student.json() for student in Student.query.all()]}