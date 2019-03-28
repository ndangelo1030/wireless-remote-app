from user import User
#from loginrepo import LoginRepo

class RegisterService:
    def __init__(self,repository)
        self.repository = repository
        
    def register_user(self, username, password, email, fname, lname):
        register = self.repository.add(username, password, email, fname, lname)
        return register
class QueryRegister:
    def __init__(self,repository)
        self.repository = repository
    def find(self, username, password, email)
        return RegUser(username, password, email)
class RemoveUser:
    def __init__(self,repository)
        self.repository = repository
    def remove(self,username,password,email)
        rmuser = self.repository.remove(username,password,email)
class CopyExisting:
    def __init(self,repository)
        self.repository = repository
    def copy(self,username,password,email,fname,lname)
        cpuser = self.repository.copy(username,password,email,fname,lname)
    
