from user import User
from user import NewUser
from loginrepo import LoginRepo
from registerservice import RegisterService
from loginservice import LoginService

def main():
    
    login_service = LoginService(LoginRepo()) #uses to call to LoginRepo class
    user = login_service.login_user(input("Enter username: "), input("Enter Password: ")) #prompts user for username / password
    print("the username is: ", user.username) #prints the username that was provided (checks for now)
    print("the password is: ", user.password) #prints the password that was provided (checks for now)
    register_service = RegisterService(LoginRepo())
    reguser = register_service.register_user(input("Enter username: "), input("Enter Password: "), input("Enter Email: "), input("Enter First Name: "), input("Enter Last Name: "))
    print("the username is: ", reguser.username) #prints the username that was provided (checks for now)
    print("the password is: ", reguser.password) #prints the password that was provided (checks for now)
    print("The users name is: ", reguser.fname, reguser.lname)
    print("the users email is: ", reguser.email)
if __name__ == "__main__":
    main()
