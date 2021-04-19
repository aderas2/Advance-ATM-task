#create record
#update record
#read record
#delete record
#CRUD
#find user
import os
import validation


user_db_path = 'data/user_record/'

def create(user_account_number,first_name, last_name ,email, password ):
  print('Create a new user record')
  #create file
  #name of the file would be account_number.txt
  #add the user details in the File
  #return True
  #if saving to file fails, delete created file
  user_data = first_name + ',' +last_name+ ',' + email + ',' + password + ',' + str(0)

  if does_account_exist(user_account_number):
    return False

  if does_email_exist(email):
    print('User already Exist')
    return False

  
  completion_state = False

  try:
    f = open(user_db_path +str(user_account_number)+ '.txt','x')

  except FileExistsError:
    does_file_contain_data = read(user_db_path +str(user_account_number)+ '.txt')
    if not does_file_contain_data:
      delete(user_account_number)


  else:
    f.write(str(user_data))
    completion_state = True
  
  finally:
    f.close()
    return completion_state


def read(user_account_number):
#find user with account number
#fetch content of the file 

  is_valid_account_number = validation.account_number_validation(user_account_number)


  try:

    if is_valid_account_number:
      f = open(user_db_path +str(user_account_number)+ '.txt','r')
    
    else:
       f = open(user_db_path + user_account_number ,'r')
  
  except FileNotFoundError:
    print("User not found")
  
  except FileExistsError:
    print("user doesn't exist")

  except TypeError:
    print('Invalid account number format')

  else:
    return f.readline()

  return False






def update(user_account_number):
  print('update user record')
  #find user with account account_number
  #fetch the content of the File
  #update the content of the file
  #safe the file  
  #return True



def delete(user_account_number):
  #find user with account account_number
  #delete the user record (file)

  is_user_deleted = False

  if os.path.exists(user_db_path + str(user_account_number) + '.txt'):

    try:

      os.remove(user_db_path + str(user_account_number) + '.txt')
      is_user_deleted = True

    except FileNotFoundError:

      print('user not found')
    
    finally:

      return is_user_deleted 
  



def does_email_exist(email):
  all_user = os.listdir(user_db_path)
  for user in all_user:
    user_list = str.split(read(user),',')
    if email in user_list:
      return True
  return False


def does_account_exist(account_number):
  all_user = os.listdir(user_db_path)
  for user in all_user:
    if user == str(account_number) + '.txt':
      return True

  return False



def authenticated_user(account_number, password):
  if does_account_exist(account_number):
    user = str.split(read(account_number),',')
    if password == user[3]:
      return user
  
  return False

  print('')


#does_email_exist()
#print(read(3643152778))