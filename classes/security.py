from models.user import User

def authenticate(username, password):
    user = User.findByUsername(username)
    if user and user.password == password:
        return user


def identity(payload):
    userId = payload['identity']
    return User.findById(userId)
