#Funkcija, kura atrod vislielako skaitļu no dotiem
def max1(x,y,z):
    global maxVal
    maxVal= x
    if maxVal<y:
        maxVal=y
    if maxVal<z:
        maxVal=z
    return maxVal
#Funkcija, kura atrod vismazāko skaitļu no dotiem
def min1(x,y,z):
    global minVal
    minVal = x
    if minVal>y:
        minVal=y
    if minVal>z:
        minVal=z
    return minVal

#Lietotajs ievāda x, y un z skaitļus
#Programma parbauda vai lietoja ievāds ir skaitļis vai ne
while True:
    try:
        x = int(input("Ievadi skaitļu x: "))
        break
    except:
        print("Nav pareiz ievads!")
while True:
    try:
        y = int(input("Ievadi skaitļu y: "))
        break
    except:
        print("Nav pareiz ievads!")
while True:
    try:
        z = int(input("Ievadi skaitļu z: "))
        break
    except:
        print("Nav pareiz ievads!")

print()
max1(x,y,z)
min1(x,y,z)
print("Vislielākais skaitlis no dotiem ir: ", maxVal)
print("Vismazākais skaitlis no dotiem ir: ", minVal)

#Izteiksme, kur ievietot šos skaitļus, mes saņemsim rezultatu
Sum = maxVal/maxVal**2 + minVal/minVal**2
print("Rezultāts: ", Sum)
