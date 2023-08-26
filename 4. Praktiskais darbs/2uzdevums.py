print("Ievadi skaitlu starp 1 un 5")
while True:
    try:
        x = int(input("-> "))
        if x in range (1, 6):
            print("Skaitlis ir", x)
        else:
            print("Nepareiz skaitlis, ievadi velreiz.")
    except:
        print("Tas nav skaitlis")