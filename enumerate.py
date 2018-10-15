# list out lists using enumerate to assist in index creation



def main():

    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"] # day in French
    
    
    #use regular iteration over the days
    
    for m in range(len(days)):
        print(m+1,days[m])
        
        
    #use enumerate to get an index

    for i,m in enumerate(days,start=1):
        print(i,m)
        
    #use zip to pack multiple list and enumarte to help with the index
    
    for m in zip(days, daysFr):
        print(m)
        
        
    for i, m in enumerate(zip(days,daysFr),start=1):
        print(i,m[0],"=",m[1],"in French")
    
    

if __name__ == "__main__":
    main()
