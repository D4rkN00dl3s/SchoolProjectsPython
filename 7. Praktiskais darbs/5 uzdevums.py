"""
Funkcija, kas lietotaja ievadītajā tekstā atrod vārdu suns un aizstāj to ar vārdu zirgs
un izprinte uz ekrana atjaunotu tekstu.
"""
def aizst(txt):
    jtxt = txt.replace("suns", "zirgs")
    print(jtxt)

#Lietotajs ievāda savu tekstu
txt = input("Ievadi tekstu:")
aizst(txt)