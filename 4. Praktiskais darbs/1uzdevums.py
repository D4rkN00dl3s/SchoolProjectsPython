from math import *
x = int(input("Ievadi x: "))

if x > 0:
    y = sqrt(pow(3*x+2, 3)-24*x)/(3*sqrt(x)-2/sqrt(x))
    print(f"Rezultats: {y:.3f}")
else:
    y = 2*x-(3-x)/4
    print(f"Rezultats: {y:.2f}")