import random
arr = [random.randint(-5, 15) for i in range(10)]
def neg():
    negVal=arr[0]
    index = 0
    for i in range(1,len(arr)):
        # -1 ir vislielākais negatīvais skaitļis, tāpēc nevājag parbaudīt tālak 
        if negVal == -1:
            break
        # Nesalīdzinam ar pozitiviem skaitļiem
        if arr[i] >= 0:
            continue
        # Ja negatīvie skaiļi ir vienadi, tad saglābt pirmo atrāsto indeksu
        if negVal == arr[i]:
            continue
        # Salidzīnat divus negatīvu skaitļu modulus un saglābt mazako
        if abs(arr[i])<abs(negVal):
            negVal=arr[i]
            index=i
            continue
        # Ja negVal ir 0 vai lielaks, tad parbaudīt to ar negativo skaitļu, lai negVal butu negativs
        if arr[i] > negVal:
            negVal = arr[i]
            index = i
            
    print("Lielākais negatīvais masīva elements un to indeks:", negVal, ",", index)
    
print(arr)
neg()

