import math
def SecInput():
    x=-1
    while x<0 : 
        x=int(input("Kérem adjon meg egy nem negatív értéket!:   "))
    return x

def SecToSplit(x):
    kiir=""
    if x==0:
        kiir="Now."
    else:
        if (x/31536000) > 0:
            ev = math.floor(x/31536000)
            x= x-(ev*31536000)
            if ev>1:
                kiir+="Years: "+str(ev)+", "
            else:
                kiir+="Year: "+str(ev)+", "
        if (x/86400) > 0:
            nap = math.floor(x/86400)
            x= x-(nap*86400)
            if nap>1:
                kiir+="Days: "+str(nap)+", "
            else:
                kiir+="Day: "+str(nap)+", "
        if (x/3600) > 0:
            perc = math.floor(x/3600)
            x= x-(perc*3600)
            if perc>1:
                kiir+="Minutes: "+str(perc)+", "
            else:
                kiir+="Minute: "+str(perc)+", "
        if (x/60) > 0:
            mp = math.floor(x/60)
            x= x-(mp*60)
            if mp>1:
                kiir+="Secounds: "+str(mp)
            else:
                kiir+="Secound: "+str(mp)
    return kiir

    
print(SecToSplit(SecInput()))