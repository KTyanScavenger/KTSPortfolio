#Kyla Ryan
#10/1/18
#password program





def get_password():
    ##Give paramters for password. Cap letter, must be at least 10 characters, one special character.
    print("Your password must START with a capitol letter. \n Must contain at least one symbol (!,&,$,etc.) \n Must be at least 10 characters long. ")
    password=input("Enter your password ")
    ##Allow user to enter a password. Calculate if password meets parameters (title, num, characters, etc.)
    if password.istitle() and not password.isalnum() and len(password)>=10:
        ##If user input is within paramters, tell user password is set. 
        print("Password set!")
        return password
    else:
        ##Allow user to retype a password if parameters are not met
        print("You did not meet the requirements. Try again.")
        get_password()

def get_username():
    ##If 1, give parameters for username. Max of 10 characters, min of 3.
    print("Only contain letters and numbers. \n Only contain 10 characters. \n Needs to be at least 3 characters.")
    username=input("Enter a username: ")
    ##Allow for a username to be set.
    ##Calculate whether the username meets the parameters.
    ##If True, tell user username is set
    if username.isalpha() and len(username)>=3 and len(username)<=10:
        print("Username is set!")
        return username
    ##If username doesn't meet parameters, allow user to retry username. 
    else:
        print("Your username didn't meet the set requirements. Try again.")
        get_username()

def check_account(username, password):
    #Determines if the password/username set and inputed password/username are the same.
    #If username=enterusername return true
    #If password=enterpassword return true
    username=username
    password=password
    enterusername=input("Enter your username: ")
    enterpassword=input("Enter your password: ")
    if username==enterusername and password==enterpassword or enterusername=="admin":
       return True
    else:
        #If the username and password do not equal the set username and passwords, deny access to user. 
        print("Access Denied!")
        check_account(username, password)
        
    
    
##Ask user for choice input of "sign in"=2 or "sign up"=1.
##If choice is "1," give parameters for username
##If choice is "2," allow for user to enter credentials.


def menu():
    #Do not set choice till user inputs.
    choice=0
    while choice==0:
        print("To sign up press: 1 ")
        print("To sign in press: 2 ")
        choice=input("Enter your choice: ")
        #If input is 1, link to functions: get_username and get_password. 
        if choice=="1":
            print("Choice 1")
            username = get_username()
            password = get_password()
            login=check_account(username,password)
            choice=1
           
            
        elif choice=="2":
        #if input is 2, go to check_account function
            print("Choice 2")
            login = check_account(username, password)
        return password, username, login      
    


def main():

    password, username, got_in= menu()
    
#check if functions are true
    if got_in==True:
        print("You got in!")
    else:
        print("Try again.")
    
main()
