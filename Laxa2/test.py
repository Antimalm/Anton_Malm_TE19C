#upg 7
x=float(input("Skriv in din x-koordinat"))
y=float(input("skriv in din y-koordinat"))

if x>0 and y >0:
    print("dessa koordinater tillhör kvadrant 1")
elif x<0 and y <0:
    print ("dessa koordinater tillhör kvadant 3")
elif x<0 and y>0:
    print("dessa koordinater tillhör kvadrant 4")        
else:
    print("dessa koordinater tillhör kvadrant 2")    
    