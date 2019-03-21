from loginrepo import LoginRepo
from Groupuser import FamilyAccountRepo

class FamilyAccountLogin:
    def __init__(familyuser,repository):
        familyuser.repository = repository

def family_login(familyuser, familyusername, familypassword)
family_login= familyuser.repository.find(familyusername, familypassword)

return login
