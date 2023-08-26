#Funkcijas, kas aprēķina x**2, x**3 un x**4 un atgriež rezultātus (x ir funkcijas parametrs, reālais skaitlis).
def pow234(x):
    x1=x
    x2=x
    x3=x
    
    for i in range(1, 2):
        x1=x*x1
    print(f"Kāpinot skaitļu {x}, 2. pakāpē, mes saņēmām: {x1}")
    
    for i in range(1, 3):
        x2=x*x2
    print(f"Kāpinot skaitļu {x}, 3. pakāpē, mes saņēmām: {x2}")
    
    for i in range(1, 4):
        x3=x*x3
    print(f"Kāpinot skaitļu {x}, 4. pakāpē, mes saņēmām: {x3}")
    
"""
Lietotajs ievāda skaitļu x
Programma parbauda vai lietoja ievāds ir skaitļis vai ne
un pēc tam izprinte uz ekrana rezultatus ar pow234 funkcijas palidzibu
"""
while True:
    try:
        for i in range(5):
            x = int(input(f"Ievadi {i+1} skaitļu: "))
            pow234(x)
        break
    except:
        print("Nav pareiz ievads!")
        print()