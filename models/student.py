import sqlite3
from db import db


class Student(db.Model):
    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastName = db.Column(db.String(50))

    classId = db.Column(db.Integer, db.ForeignKey('Class.id'))
    Class = db.relationship('Class')

    def __init__(self, name, lastName, classId):
        self.name = name
        self.lastName = lastName
        self.classId = classId

    @classmethod
    def findByStudentName(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def exist(cls, name):
        return bool(cls.findByStudentName(name))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastName': self.lastName,
            'classId': self.classId
        }
