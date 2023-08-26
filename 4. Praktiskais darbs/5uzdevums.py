a = int(input("Ievadi nogriežņa a garumu: "))
b = int(input("Ievadi nogriežņa b garumu: "))
c = int(input("Ievadi nogriežņa c garumu: "))

if a < b+c and b < a+c and c < b+a:
    print("Var izveidot trijsturu")
else:
    print("Nevar izveidot trijsturu")