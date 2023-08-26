izv = int(input())
if izv == 1:
    Tf = int(input())
    
    C=(Tf-32)*5/9
    print(f"{C:.2f}")
        
elif izv == 2:
    C=int(input())
    
    Tf=9*C/5+32
    print(f"{Tf:.2f}")
    

