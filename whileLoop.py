responses = {}

polling_active = True

while polling_active:
    
    name = input("\n what is ur name? ")
    
    
    response = input("which mountain would you like to climb someday ?")
    
    responses[name] = response #set the response as a part of the dict with key name
    
    
    repeat = input("would you like to let another person respond? (yes/no)")
    
    
    if repeat == 'no':
        
        polling_active = False
        
print("poll results")


for name, response in responses.items():
    
    print(name + "would you like to climb " + response + ".")
        
        
        
        
        
    
    
    
    
    
    
