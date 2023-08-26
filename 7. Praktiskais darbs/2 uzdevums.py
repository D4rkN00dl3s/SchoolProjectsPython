#Funkcija, kas veic norādītā pozitīvā skaitļa kāpināšanu norādītajā pozitīvajā pakāpē
def kap(x, y):
    x1=x
    for i in range(1, y):
        x1=x*x1
    print(f"Kāpinot skaitļu {x}, {y}. pakāpē, mes saņēmām: {x1}")

#Lietotajs ievāda skaitļu x un pozitīvu pakāpē
#Programma parbauda vai lietoja ievāds ir skaitļis vai ne, ka ari vai pakāpe ir pozitīvaijs skaitļis
while True:
    try:
        x = int(input("Ievadi pozitīvo skaitļu: "))
        break
    except:
        print("Nav pareiz ievads!")
while True:
    try:
        y = int(input("Ievadi pozitīvo pakāpē: "))
    except:
        print("Nav pareiz ievads!")
        continue
    if y<0:
        print("Pakāpē nav pozitīva!")
    else:
        break
#Funkcijas izsaukšana un rezultatu saņemšana
kap(x,y)