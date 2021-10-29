import math

x = int(input("Adja meg a kör sugarát! : "))
print("A kör kerülete: "+str(round(2*x*math.pi,3))+"\nA kör területe: "+str(round(math.pow(x,2)*math.pi,3)))