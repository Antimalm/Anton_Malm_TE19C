# if-satser
#1
t = float(input("Skriv ett valfritt tal"))
if t<0: 
    print("talet är negativt")
elif t>0: 
    print("talet är positivt")
else: 
    print: ("talet är 0")

#upg 2.
t = float(input("Skriv vilket tal du vill"))
if t%2 == 1:    
    print("talet är ojämnt")
else:
    print("talet är jämnt")
if t%5 ==0:
    print("Talet är delbart med 5")

#upg 3. 
t1=float(input("Skriv tal 1"))
t2=float(input("skriv tal 2"))


if t1>t2:
    print(t1,"som är ditt första tal är det törsta talet")
else:
    print(t2,"som är ditt andra tal, är det största talet")

#upg 4
vinkel = float(input("Ange en vinkel v i grader där 0 <= v<=360  "))

if vinkel >=0 and vinkel < 90: 
    print("spetsig vinkel.")
elif vinkel == 90:
    print("rät vinkel")
elif vinkel > 90 and vinkel <180:
    print("Trubbig")
elif vinkel == 180:
    print("rak vinkel")
elif vinkel > 180 and vinkel <360:
    print("konvex vinkel")
elif vinkel==360:    
    print("print hel vinkel")
