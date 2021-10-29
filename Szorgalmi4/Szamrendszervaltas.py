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
        except:
            szamTizesbe+=math.pow(regiszamh, i-(k+1))*(szamertekek.index(szam[k])+10)
        k+=1
    return szamTizesbe

def AtvaltTizesrolUjra(tizesSzam,ujHalmaz):
    szamertekek=[]
    if ujHalmaz>10:
        x=65
        while x<(65+ujHalmaz-10):
            szamertekek.append(chr(x))
            print(chr(x))            
            x+=1
    vegsoSzam=""
    UjhalmazSzama=[]
    while tizesSzam!=0:
        if tizesSzam%ujHalmaz <10:
            UjhalmazSzama.append(tizesSzam%ujHalmaz)
        else:
            UjhalmazSzama.append(szamertekek.index(chr(int((tizesSzam%ujHalmaz)+10))))
        tizesSzam//=ujHalmaz
    
    i=len(UjhalmazSzama)-1
    while 0 <= i:
        vegsoSzam = str(vegsoSzam)+str(int(UjhalmazSzama[i]))
<<<<<<< Updated upstream
        i=i-1
=======
        i-=1
>>>>>>> Stashed changes
    return vegsoSzam

def Atvaltas(regiszamh,szam,ujszamh):
    ujszamTizesbe=AtvaltRegirolTizre(regiszamh,szam)
    UjHalmazos=AtvaltTizesrolUjra(ujszamTizesbe,ujszamh)
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

    return UjHalmazos
    
alapSzamH= InputAlapSzam()
alapSzam= InputSzam()
UjSzamH= InputUjSzamH()

print("\n"+str(alapSzamH)+" alapból, "+str(alapSzam)+" értékkel, és az új számhalmazzal, ami "+str(UjSzamH)+" az új, átkonvertált számunk: "+str(Atvaltas(alapSzamH,alapSzam,UjSzamH)))
