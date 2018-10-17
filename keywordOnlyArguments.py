"""
functions that use keyword-only arguments - positions don't matter

TO DO: find more examples 
    
"""



def print_something(name = "name", age = "unknown"):
    
    print("My name is",name,",and my age is ",age)
    
    
print_something(age=26,name = "V") #keyword-only function
