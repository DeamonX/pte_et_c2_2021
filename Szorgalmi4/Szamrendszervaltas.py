import math

def InputAlapSzam():
    loop =True
    while loop:
        try:
            alapszamh = int(input("Kérem adja meg az alapértelmezett számrendszert!:   "))
            if alapszamh<2 or alapszamh>36:
                print("A program erre nem képes.")
            else:
                loop=False
        except ValueError:
            print("Számot szeretnék kérni!")
    return alapszamh

def InputSzam():
    alapszam = input("Kérem adja meg az előbb említett számrendszerben lévő számot!:   ")
    return alapszam

def InputUjSzamH():
    loop =True
    while loop:
        try:
            ujszamh = int(input("Kérem adja meg az új alapértelmezett számrendszert!:   "))
            if ujszamh<2 or ujszamh>36:
                print("A program erre nem képes.")
            else:
                loop=False
        except ValueError:
            print("Számot szeretnék kérni!")
    return ujszamh

def AtvaltRegirolTizre(regiszamh,szam):
    if regiszamh>10:
        szamertekek=[]
        x=65
        while x<(65+regiszamh-10):
            szamertekek.append(chr(x))
            x+=1
    szamTizesbe=0
    i = len(str(szam))
    k=0
    while k<i:
        try:
            if int(szam[k])>-1 and int(szam[k])<10:
                szamTizesbe+=math.pow(regiszamh,i-(k+1))*int(szam[k])
                print(str(math.pow(regiszamh,i-(k+1))*int(szam[k])))
        except:
            szamTizesbe+=math.pow(regiszamh, i-(k+1))*(szamertekek.index(szam[k])+10)
            print(str(math.pow(regiszamh, i-(k+1))*szamertekek.index(szam[k])+10)+"\n"+str(szamertekek.index(szam[k])+10))
        k+=1
    return str(szamTizesbe)

    ujszamTizesbe=AtvaltRegirolTizre(regiszamh,szam)

    return ujszamTizesbe
    
alapSzamH= InputAlapSzam()
alapSzam= InputSzam()
UjSzamH= InputUjSzamH()

print("\n"+Atvaltas(alapSzamH,alapSzam,UjSzamH))
