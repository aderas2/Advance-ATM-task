
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
          return False

       except TypeError:
         return False
         
   return False



def account_number_validation(account_number):
   #check if account_number is not empty
   #if account_number is 10 digits
   #if the account_number is an integer
   if account_number:
     try:

       int(account_number)
      
       if len(str(account_number))==10:
         return True

     except ValueError:
        return False

     except TypeError:
       return False
   return False