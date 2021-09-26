x = int(input("Kérem adja meg az első kiválaszott számot!:  "))
y= int(input("Kérem adja meg az második kiválaszott számot!:  "))

if(x<y):
    print("Az első szám ("+str(x)+") az kisebb ('<') mint a második ("+str(y)+") szám.")
elif(x==y):
     print("A két szám ("+str(x)+" és "+str(y)+") egyenlő.")
else:
 print("Az első szám ("+str(x)+") az nagyobb ('>') mint a második megadott ("+str(y)+") szám.")