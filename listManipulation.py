

def main():
    
    evens = [2,4,6,8,10,12,16,18,20]
    odds = [1,3,5,7,9,11,13,15,17,19]
    
    evenSquared = list(map(lambda e: e**2, filter(lambda e: e > 4 and e<16, evens))) #imagine map (y,x)
    
    print(evenSquared)
    
    evenSquared = [e ** 2 for e in evens]  #list manipuation [y for x in ]
    
    print(evenSquared)
    
    oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]
    
    print(oddSquared)
    
    
    
    
if __name__ == "__main__":
    
    main()
    
    
    
    
    
    
