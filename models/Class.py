import sqlite3
from db import db


class Class(db.Model):
    __tablename__ = 'Class'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    students = db.relationship('Student',lazy ='dynamic')

    def __init__(self, name):
        self.name = name

    @classmethod
    def findByName(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'students': [student.json() for student in self.students.all()]
        }