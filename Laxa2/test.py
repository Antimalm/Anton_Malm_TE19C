#upg 5
radien=float(input("Hur lång är radien?"))
omkrets=radien*3.14
arean= radien*radien*3.14
o= round(omkrets,1)
a= round(arean,1)
if radien >0:
    print(o,"cm är cirklens omkrets och",a,"cm är cirkelns area")
else:
    print("Talet är odefinerat")