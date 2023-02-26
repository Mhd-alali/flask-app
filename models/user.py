from db import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def findByUsername(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def findById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'id':self.id,
            'username':self.username,
            'password':self.password
        }
