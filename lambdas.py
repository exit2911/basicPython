"""use lambdas : anonymous functions
   for readability if the function is short

"""
 


import math

def sqrt(x):
    return math.sqrt(x)



def cuberoot(x):
    
    return x**(1/3)


def main():
    
    x = [1,4,5,6,2,33,4]
    
    
    #regular functions
    
    print(list(map(sqrt,x))) #map(f,x)
    print(list(map(cuberoot,x)))


    # use lambdas


    print(list(map(lambda t: math.sqrt(t), x)))
    print(list(map(lambda t: t**(1/3),x)))
    
if __name__ == "__main__":

    main()
    
    
    
