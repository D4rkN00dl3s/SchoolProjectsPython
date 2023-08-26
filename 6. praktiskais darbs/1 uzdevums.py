def add(n):
    i=1
    S=0
    while i<=n:
        S+=(-1)**i/i
        i+=1
    print(f"Rezultats: {S:.2f}")
while True:
    try:        
        n = int(input("Ievadi naturalo skaitlu: "))
        if n<0:
            print("Tas nav naturalais skaitlis")
            continue
        add(n)
        break
    except:
        print("Nepareiz ievads")