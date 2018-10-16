    
def filterFunc(x):
    if x % 2 == 0: #if x mod 2 == 0, is an even num
        return False
    return True

def filterFunc2(x):
    #take only lower case letters
    if x.isupper(): 
        return False
    return True

def squareFunc(x):
    return x**2
    

def toGrade(x):
    
    if (x >= 90):
        return "A"
    elif (x >= 80 and x< 90):
        return "B"
    elif (x >= 70 and x<80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"
    
    

def main():
    
    #define some sample sequences to use
    
    nums = (1,2,3,4,5,6,7,77,8,4,3)
    
    chars = "IPython 6.1.0 -- An enhanced Interactive Python."
    
    grades = (81, 89, 94, 78, 61, 66, 99, 74)
    
    #filtering out odd numbers from tuple
    
    odds = list(filter(filterFunc,nums)) # syntax = filter(by booleans, object)
    print(odds)
    
    #filtering lower case letters

    lowers = list(filter(filterFunc2,chars)) 
    print(lowers)    
    
    #squaring 
    
    squares = list(map(squareFunc,nums))
    print(squares)
    
    #sorting & mapping for letter grades
    
    grades = sorted(grades) #sorting; ascending
    
    letters = list(map(toGrade,grades)) # syntax : map(function, object)
    print(letters)


if __name__== "__main__":
    
    main()
  
