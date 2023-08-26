#Trijstura laukuma aprekinašana pec Hērona formula
import math

a = float(input("Trijstura pirma mala garums: "))
b = float(input("Trijstura otra mala garums: "))
c = float(input("Trijstura treša mala garums: "))
p = a+b+c/2

S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Trijstura laukums ir {S:.2f}")