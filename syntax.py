#1

K=float(input("Hur varmt är det ute svara i Kelvin."))
Celsius=-K-273.15
print(K, "kelvin är" ,Celsius, "grader celsius")

#2
C=float(input("Hur varmt är det i Celsius"))
K=C-273,15
print(C, "Celsius är",K, "grader i Kelvin")

#3 
Antal=float(input("Hur många gånger åker du buss per dag?"))
Kostnaden=Antal*30
print(Antal, "gånger kostar,",Kostnaden, "kr")
if Antal > 25:print("Köp månadskort istället :)")
if Antal <25:print ("Håll dig till engångsbiljetter :)")