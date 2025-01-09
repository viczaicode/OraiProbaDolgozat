import random

def SorozatosfeladatSzamKiiras():
    print("II/A,B,C")

def SorozatosSzamGeneralas():
    szamok = []
    for i in range(0,5):
        randomszam = random.randint(10, 20)
        szamok.append(randomszam)
    return szamok

def SorozatosSorbaRendezes(elvalaszto, szamok):
    kimenet = ""
    for i in range(len(szamok)):
        kimenet += str(i)
        if i < len(szamok) - 1:
            kimenet += elvalaszto
    return kimenet



def SorozatosKisebbSzamolas(szamok):
    hanyDBKisebb = 0
    for i in range(len(szamok)-1):
        if i > szamok[i+1]:
            hanyDBKisebb += 1
    return hanyDBKisebb

def SorozatosFajlbaKiiras(hanyDBKisebb):
    fajlom = open("vegeredmeny.txt", "w", encoding="utf-8")
    fajlom.write("II/F:\n")
    fajlom.write(f"Kisebb számok száma: {hanyDBKisebb}.\n")

def sorozatKiiras(kimenet):
    print(kimenet)



