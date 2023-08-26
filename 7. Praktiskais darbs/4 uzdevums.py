#Random moduļu  importēšana
from random import *
"""
Funkcija, kas izveido masivu pec lietotāja ievadītu tabulas rindu un kolonnu skaitu,
pēc tam aizpilda tabulu ar nejaušiem skaitļiem intervālā no 0 līdz 20.
"""
def masivs():
    global arr
    arr=[]
    for i in range(rows):
        col=[]
        for j in range(cols):
            col.append(randint(0, 20))
        arr.append(col)
    print("Masivs: ")
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end='\t')
        print()
"""
Funkcija, kas atrod lietotāja norādītās kolonnas šūnu ar mazāko vērtību (kolonnas minimālo vērtību).
"""        
def min1(arr):
    for i in range(cols):
        for j in range(rows):
           if j == 0:
               minVal = arr[j][i]
               continue
           if arr[j][i]<minVal:
               minVal=arr[j][i]
        print(f'Mazakāis skaitlis {i + 1} kolonnā ir {minVal}')
        
#Lietotajs ievāda rindu un kolonnu skaitu.
#Programma parbauda vai lietoja ievāds ir skaitļis vai ne, ka ari vai viņš ir pozitīvs.
        
while True:
    try:
        rows=int(input("Ievadi cik būs rindas: "))
        if rows<0:
            print("Nevar būt negativs rindu skaits!")
            continue
        break
    except:
        print("Nav pareiz ievads!")
while True:
    try:
        cols=int(input("Ievadi cik būs kolonnas: "))
        if cols<0:
            print("Nevar būt negativs kolonnu skaits!")
        break
    except:
        print("Nav pareiz ievads!")
        
#Masiva un kolonnas minimālo vērtību izprintešana uz ekrana.
masivs()
print()
min1(arr)