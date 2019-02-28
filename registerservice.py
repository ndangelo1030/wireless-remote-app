from user import User
from loginrepo import LoginRepo

class RegisterService:
    def __init__(self,repository):
        self.repository = repository
        
    def register_user(self, username, password, email, fname, lname):
        register = self.repository.add(username, password, email, fname, lname)
        return register
