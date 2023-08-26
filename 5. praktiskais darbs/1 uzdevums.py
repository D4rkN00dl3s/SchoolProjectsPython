import math
c = 0
a = int(input())
b = int(input())
N = []

for c in range(a, b+1):
    if c>0:
        N+=[c]
print(N)
print(math.prod(N))