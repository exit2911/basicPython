import json

def get_stored_username():
    
    filename = 'username.json'
    
    
    try:
        
        with open(filename) as f_obj:
            username = json.load(f_obj)
            
    except ValueError: #JSONDecodeError is subclass of ValueError
    
        
        
        username = input("what is your name? ")
        filename = 'username.json'
        
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            
    else:
        return username
    
def greet_user():
    
    username = get_stored_username()
  
    print("is your name " ,username)
    
    answer = input("enter y or n ")
    
    if answer == "y":
        print("hi " + username)
        
    elif answer == "n":
        username = input("what is your name? ")
        filename = 'username.json'
        
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print('hi '+ username)


greet_user()           
