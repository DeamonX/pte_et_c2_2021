def UsageInput():
    loop = True
    while(loop):
        try:
            usage= float(input("\nKérem adja meg, hogy hány liter üzemanyagot emészt meg az autó 100km-en!:  "))
            loop=False
        except ValueError:
            print("Ajánlatos számot megadni felénk.")
    return usage

def PrecentInput():
    loop = True
    while(loop):
        try:
            precent= float(input("\nKérem adja meg, hogy hány százaléknyi üzemanyag van jelenleg benne (0-100)!:  "))
            if precent < 0 or precent > 100:
                print("0 és 100 közötti érték lehet csak.")
            else:
                loop=False
        except ValueError:
            print("Ajánlatos számot megadni felénk és tizedes esetén ponttal elválasztani.")
    return precent

def GasInput():
    loop = True
    while(loop):
        try:
            gas= float(input("\nKérem adja meg, hogy hány liter üzemanyag fér a tarályba!:  "))
            loop=False
        except ValueError:
            print("Ajánlatos számot megadni felénk és tizedes esetén ponttal elválasztani.")
    return gas

def DistanceInput():
    loop = True
    while(loop):
        try:
            distace= float(input("\nKérem adja meg, hogy milyen messze van a következő benzinkút (km-ben):  "))
            loop=False
        except ValueError:
            print("Ajánlatos számot megadni felénk és tizedes esetén ponttal elválasztani.")
    return distace

gas = GasInput()
precent = PrecentInput()
usage = UsageInput()
distace = DistanceInput()

if gas*(precent/100) <= usage*(distace/100):
    print("Most kell tankoljon.")
else:
    print("Ráér akkor is.")