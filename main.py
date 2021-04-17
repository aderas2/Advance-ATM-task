#register
#log-in


#initializing the system
import random

database = {}
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

    is_valid_account_number = account_number_validation(accountNumberFromUser)

    if is_valid_account_number:
      password = input('What is your password? \n')

      for accountNumber,userDetails in database.items():
        if accountNumber==int(accountNumberFromUser):
          if(userDetails[3]==password):
            bankOperation(userDetails)
            
        else:
          print('Invalid account or password')
          login()
    else:
      init()



def register():
  
  print('******** Register ********')
  email = input('What is your email address? \n')
  first_name = input('What is your first name? \n')
  last_name = input('What is your last name? \n')
  password = input('please create a password. \n')



  try:

    accountNumber = generateAccountNumber()

  except ValueError:
    print('Account generation failed due to internet connection')
    init()



  database[accountNumber] = [first_name,last_name,email,password]

  print('Your account has been created')
  print('==== ======= ====== ======= =====')
  print('Your account number is: %d' %accountNumber)
  print('Make sure you keep it safe')
  print('==== ======= ====== ======= =====')

  login()

 

def bankOperation(user):
    print('Welcome %s %s' %(user[0],user[1]))    

    selectedOption = (input('What would you like to do? (1) deposit (2) Withdrawal (3) Logout (4) exit \n'))
    is_valid_option = bank_option_validation(selectedOption)

    if is_valid_option:
      if (is_valid_option == 1):      
        depositOperation()

      elif (is_valid_option == 2):      
        withdrawalOperation()

      elif (is_valid_option == 3):
        logout()

      elif (is_valid_option == 4):
        exit()

      else:
        print('Invalid option selected')
        bankOperation(user)
    else:
     bankOperation(user) 



def bank_option_validation(optionspicked):
 #check if account_number is not empty
   #if account_number is 10 digits
   #if the account_number is an integer
   if optionspicked:
     if len(str(optionspicked))==1:

       try:
         int(optionspicked)
         return True
      
       except ValueError:
          print('Invalid Option, Option should be integer')
          return False
       except TypeError:
         print('Invalid Option type')
         return False
     else:
       print('Option cannot be less or more than 1 digits')
       return False
   else:
     print('Option is a required field')
     return False



def account_number_validation(account_number):
   #check if account_number is not empty
   #if account_number is 10 digits
   #if the account_number is an integer
   if account_number:
     if len(str(account_number))==10:

       try:
         int(account_number)
         return True
      
       except ValueError:
          print('Invalid Account Number, account number should be integer')
          return False
       except TypeError:
         print('Invalid account type')
         return False
     else:
       print('Account Number cannot be less or more than 10 digits')
       return False
   else:
     print('Account Number is a required field')
     return False



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