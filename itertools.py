#advanced iteration functions in the itertools package


import itertools #iterating elements in a list and spit out a new list of processed items

def testFunction(x):
    
    return x < 40


def main():
    
    #cycle over a list
    
    seq1 = ["heels","computers","books"]
    
    cycle1 = itertools.cycle(seq1)
    
    print(next(cycle1)) #equivalent of seq1[0]
    print(next(cycle1)) #equivalent of seq1[1]
    print(next(cycle1)) #equivalent of seq1[2]
    print(next(cycle1))
    print(next(cycle1))
    
    #use count to create a counter
    
    count1 = itertools.count(100,10) #count upward by 10 from 100
    
    print(next(count1)) 
    print(next(count1)) 
    print(next(count1)) 
    print(next(count1)) 
    
    
    #accumulate creates an iterator that accumualtes values
    
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals,max)
    print(list(acc))
    
    #use chain to connect sequences together
    
    x = itertools.chain("ABCD","1234") 
    print(list(x))
    
    #dropwhile and takewhile will return values that meet certain conditions
    
    
    print(list(itertools.dropwhile(testFunction,vals))) 
    print(list(itertools.takewhile(testFunction,vals)))
    
if __name__ == "__main__":
    
    main() 
   
