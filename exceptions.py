
while True:
    
    
    try:
        a = int(input("enter the first number \n enter exit to quit"))
       
        if a == "exit":
            break
        else:
        
            b = int(input("enter the 2nd number "))
        answer = a + b
    
    except ValueError:
            
        msg = "please enter numbers"
        
        print(msg)  
                
    else:
        
        print(answer)
        
