import random
def Input():
    loop = True
    while loop:
        chosen = input("Válassz!  Kő-Papír-Olló!:  ").lower()
        if chosen =="papír" or chosen=="olló" or chosen =="kő":
            loop = False
        else:
            print("Hibás input!")
    return chosen
chosen = Input()
valasztek=["kő","papír","olló"]
randomInt = random.randint(0,2)
if chosen == valasztek[randomInt]:
    print("Döntetlen.")
elif chosen=="papír":
    if valasztek[randomInt]=="kő":
        print("Nyertél!")
    elif valasztek[randomInt]=="olló":
        print("Vesztettél!")
elif chosen=="kő":
    if valasztek[randomInt]=="papír":
        print("Vesztettél!")
    elif valasztek[randomInt]=="olló":
        print("Nyertél!")
else:
    if valasztek[randomInt]=="kő":
        print("Vesztettél!")
    elif valasztek[randomInt]=="papír":
        print("Nyertél!")