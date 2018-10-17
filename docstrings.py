    
"""

TO DO: storing info about functions, modules, classes, etc.


"""
    
    
"""
best practices

all in triple quotes

first line - summarize the functionality

for modules - list important classes, functions, exceptions 
for functions - list parameters & explain each per line

list return values if any

list exceptions if any

"""




def myFunction(arg1,arg2 = None) #function parameters

"""myFunction(arg1,arg2 = None) --> this functions does x

Parameters:
    arg1: the first argument is ...
    arg2: the 2nd argument is ...
    
"""
    print(arg1,arg2)
    
    
def main():
    print(myFunction.__doc__)
    
    
if __name__ == "__main__":
    
    main()

