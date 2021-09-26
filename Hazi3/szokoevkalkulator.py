def YearInput():
    loop = True
    while(loop):
        try:
            year= int(input("\nKérem adja meg, hogy melyik évről szeretné megtudni, hogy szökőév-e:  "))
            loop=False
        except ValueError:
            print("Hibás input.")
    return year

year = YearInput()
if year % 4 ==0 or (year % 100 ==0 or year % 400 ==0):
    print(str(year)+". év az szökőév!")
else:
    print(str(year)+". év az nem szövőév!")