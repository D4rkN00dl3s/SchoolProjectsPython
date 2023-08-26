A = int(input())

if A != 0 and A**2 < 25:
    A = A*-1
    print(A)
elif A == 0:
    A = 1
    print(A)
else:
    print(A)