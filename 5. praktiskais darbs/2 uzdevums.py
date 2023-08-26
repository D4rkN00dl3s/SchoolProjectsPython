n = int(input())
S=0
i=1

for i in range(1, n+1):
    S+=i**i
    
print(S)