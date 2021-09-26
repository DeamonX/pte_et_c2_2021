pw = input("Kérem adj meg egy jelszót amit ellenőrizni szeretnél!:  ")
kisbetuk=[]
nagybetuk=[]
szamok=[]
specko=[]
vanKis=False
vanNagy=False
vanSzam=False
vanSpecko = False
i=33
while(i<127):
    if i>=48 and i<=57:
        szamok.append(chr(i))
    elif i>=65 and i<=90:
        nagybetuk.append(chr(i))
    elif i>=97 and i<=122:
        kisbetuk.append(chr(i))
    else:
        specko.append(chr(i))
    i+=1

for i in range(len(kisbetuk)):
    if pw.find(kisbetuk[i]) != -1:
        vanKis=True
for i in range(len(nagybetuk)):
    if pw.find(nagybetuk[i]) != -1:
        vanNagy=True
for i in range(len(szamok)):
    if pw.find(szamok[i]) != -1:
        vanSzam=True
for i in range(len(specko)):
    if pw.find(specko[i]) != -1:
        vanSpecko=True
if len(pw)<5 or not vanKis or not vanNagy or not vanSpecko or not vanSzam:
    print("Gyenge jelszó!")
elif len(pw)>=5 and len(pw)<=9 and vanKis and vanNagy and vanSpecko and vanSzam:
    print("Közepes jelszó!")
elif len(pw)>=10 and vanKis and vanNagy and vanSpecko and vanSzam:
    print("Erős jelszó!")
