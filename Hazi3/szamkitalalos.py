import random
def CorrectInputLoop():
    RosszInput = True
    while RosszInput:
        try:
            y = int(input("Kérlek add meg az "+str(i+1)+". tipped!:  "))
            if y < int(intervallum[0]) or y> int(intervallum[1]):
                print("Öhm.. az intervallumon kívül tippeltél.. picit gáz de elnézem :D")
            else:
                RosszInput = False
        except ValueError:
            print("Jó próba volt, most már kérlek számot adj meg.")
    return y

def inputSplitToRandomGuess():
    x=""
    while(len(x) !=2):
        x = input("Írj be két számot szóközzel elválasztva az intervallum megadásához!:  ").split(" ")
    if x[0]>x[1]:
        temp = x[0]
        x[0] = x[1]
        x[1] = temp
        print("Értelmesebb lett volna növekvő sorredben, de megoldom..\nAz intervallum a következő: "+str(x))
    else:
        print("Az intervallum a következő!: "+str(x)+"\nSok sikert a tippelgetéshez!\nÖt próbálkozásod lehet!")
    randomNumber = random.randint(int(x[0]),int(x[1]))
    return randomNumber,x
intervallum=""
randomGuess,intervallum= inputSplitToRandomGuess()
i = 0
probalkozhat = True
while i<5 and probalkozhat:
    proba = CorrectInputLoop()
    if proba==randomGuess:
        print("Gratulálok! Sikerült kitalálnod az általam gondolt számot! ("+str(proba)+")!")
        probalkozhat=False
    else:
        i+=1
        if(proba<randomGuess):
            print("Sajnos nem találtad el, de annyit segítek, hogy az általan gondolt szám az nagyobb ennél.\n")
        else:
            print("Sajnos nem találtad el, de annyit segítek, hogy az általan gondolt szám az kisebb ennél.\n")

if probalkozhat and i>=5:
    print("\nSajnos nem sikerült kitalálnod, de azért elmondom az áltatalam gondolt számot: "+str(randomGuess))
