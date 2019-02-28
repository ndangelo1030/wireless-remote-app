from user import User
from user import NewUser

class LoginRepo:
    def find(self, username, password):
        return User(username,password)
    def add(self, username, password, email, fname, lname):
        return NewUser(username, password, email, fname, lname)
