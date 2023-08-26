#Rinka linijas garumu aprekinašana
d = float(input("Iekšējais diametrs ir: "))
D = float(input("Ārējais diametrs ir: "))
r1 =float(d/2)
r2 =float(D/2)
p = 3.14

S1 = p*r1**2
S2 = p*r2**2
print(f"Iekšēja rinka laukums ir {S1:.2f} ")
print(f"Ārēja rinka laukums ir {S2:.2f} ")