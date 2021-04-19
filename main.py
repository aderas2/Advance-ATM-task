#register
#log-in


#initializing the system
import random
import validation
import database
from getpass import getpass



def init():

    
    print('Welcome to bank php')
  
    haveAccount = int(input('Do you have account with us : 1 (yes) 2 (No) \n'))
    if (haveAccount == 1):
      login()

    elif (haveAccount == 2):        
      register()

    else:
      print('You have selected invalid option')
      init()


def login():
    print('********* login ******')
   
    accountNumberFromUser = (input('What is your account Number? \n'))

    is_valid_account_number =validation. account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

      password = getpass('What is your password \n')

      user= database.authenticated_user(accountNumberFromUser,password)

      if user:
        bankOperation(user)

      print('Invalid account or password')
      login()
      
    else:
      print('Account number Invalid, check that you have up to 10 digit and only integers')
      init()



def register():
  
  print('******** Register ********')
  email = input('What is your email address? \n')
  first_name = input('What is your first name? \n')
  last_name = input('What is your last name? \n')
  password = getpass('please create a password. \n')
  



  accountNumber = generateAccountNumber()

  is_user_created = database.create(accountNumber, first_name, last_name ,email, password)

  if is_user_created:

    print('Your account has been created')
    print('==== ======= ====== ======= =====')
    print('Your account number is: %d' %accountNumber)
    print('Make sure you keep it safe')
    print('==== ======= ====== ======= =====')

    login()

  else:

    print('Something went wrong, please try again')
    register()


 

def bankOperation(user):
    print('Welcome %s %s' %(user[0],user[1]))    

    selectedOption = int((input('What would you like to do? (1) deposit (2) Withdrawal (3) Logout (4) exit \n')))

    if (selectedOption == 1):      
        depositOperation()

    elif (selectedOption == 2):      
        withdrawalOperation()

    elif (selectedOption == 3):
        logout()

    elif (selectedOption == 4):
        exit()

    else:
        print('Invalid option selected')
        bankOperation(user)

     




def withdrawalOperation():
  print('Withdrawal')

def depositOperation():
  print('Deposit')

def logout():
  login()



def generateAccountNumber():
    return random.randrange(1111111111,9999999999)





### Actual Banking system ###
#print(generateAccountNumber())
init()