from loginrepo import LoginRepo
from user import User

class LoginService:
    def __init__(self,repository):
        self.repository = repository

    def login_user(self, username, password):
        login = self.repository.find(username, password)
        
        return login
    def forget_pass(self,username,email,password)
        pwreset = self.repository.clear(password)
    def addnewpass(self,username,password,email)
        newpw = self.repository.add(password)






