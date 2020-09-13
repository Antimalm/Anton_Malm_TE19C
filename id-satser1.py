# jämt eller udda
tal = int(input ("Ange ett heltal:"))


(tal%2) 
if tal%2 == 1:
    print("0jämt tal")
else:
    print("Jämnt tal")

vinkel = float(input("Ange en vinkel v i grader där 0 <= v<=360  "))
#spetsig: 0<v<90
#rät: v=90
#trubbig: 90<v<180

if vinkel >=0 and vinkel < 90: 
    print("spetsig vinkel.")
elif vinkel == 90:
    print("rät vinkel")
elif vinkel > 90 and vinkel <180:
    print("Trubbig")
else:  
    print("vinkeln är inte spetsig, rät eller trubbig")
    
