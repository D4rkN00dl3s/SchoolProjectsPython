import random
array = [random.randint(-10, 10) for i in range(20)]
print(array)
#Funkcija aprēķina pirmo 10 elementu summu
def count():
    S=0
    n=0
    for n in range(10):
        S+=array[n]
    print(f'Pirmo 10 elementu summa: {S}')
#Funkcija aprēķina pēdējo 10 elementu reizinājumu    
def mult():
    for n in range(10,len(array)):
        if n == 10:
            S = array[n]
            continue
        S*=array[n]
    print(f'Pēdējo 10 elementu reizinājums: {S}')
#Funkcija parbauda cik ir pozitivus skaitlus masiva    
def check():
    n=0
    array_a=[]
    for n in range(20):
        if array[n]>0:
            array_a.append(array[n])
    print(f'Pozitīvu elementu skaits: {len(array_a)}')
    
print()        
count()
print()
mult()
print()
check()
