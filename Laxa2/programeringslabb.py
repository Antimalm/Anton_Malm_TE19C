import numpy as np
import matplotlib.pyplot as plt
'''
uppgift 1 a) beräkna avståndet från origo till kordinaterna (0.5,0.5)
pythagoras sats: (0,5**2+0,5**2=x^0,5)
jag tar pythagorats sats för att få reda på diagonalen eller hypotenusan till punkterna. Sedan printar jag detta 

'''

'''
y=0.5
x=0.5
s=np.sqrt((y**2)+(x**2))

print(f" avståndet från origo til punkerna (0.5,0.5) är = {s:.2f} längdenheter")
'''
'''
uppgift 1 b) beräkna avståndet från origo till koordinaterna (1,1)
'''
'''
y=1
x=1
s=np.sqrt((y**2)+(x**2))

print(f" avståndet från origo til punkerna (1,1) är = {s:.2f} längdenheter")
'''
'''
uppgift 1 c) beräkna avståndet från origo till kordinaterna (-1,-1)
'''
'''
y=-1
x=-1
s=np.sqrt((y**2)+(x**2))

print(f" avståndet från origo til punkerna (-1,-1) är = {s:.2f} längdenheter")
'''
'''
uppgift 1 d)simulera många punkter mellan (-1,1)
random.uniform (-1,1)
'''
'''
d)
import random as random
for x in range(100):
    x=random.uniform(-1,1)
    print(x)
'''
'''
Enligt mina utträkningar(x^2*pi/x^2=0,25x^2/x^2=0,25pi)
När jar gångrar med fyra får jag pi eftersom cirkelns area tar upp en fjärdedels pi /  1
'''

'''
e)
Jag importerar matplonlib och random, sedan sätter jag antalet punkter inne och ute = 0. För att göra en
måste punkterna vara inom en areaenhet ifrån origo, annars hamnar punkterna utanför mitt koordinatsystem. 
Så om punkterna är innanför så printas dom, och läggs in i koordinatsystem med färgen blått, annars med färgen rött.
Sedan adderar min if-sats 1 per punkt till mina variabler, inne och ute, sedan delar jag antalet innanför
med hela summan för att få reda på andelelen. 
'''
'''
import matplotlib.pyplot as plt

import random as random
inne=0
ute=0
for i in range(100):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)  
    if x**2+y**2 <= 1:
        plt.plot(x,y,'b*')
        inne+=1
    else:
        plt.plot(x,y,'r*')
        ute+=1

print(inne, ute)
andel=inne/i
print("Andelen punkter som hamnar innanför cirkeln är",andel)
plt.grid()
plt.show()


'''



'''
f) Om jag simulerar 10 000 punkter i programmet ovan får jag cirka 78,5% gångrar jag detta med 4 får jag pi
som jag tidigare räknat ut ska stämma. (Enligt mina utträkningar(x^2*pi/x^2=0,25x^2/x^2=0,25pi)
När jar gångrar med fyra får jag pi eftersom cirkelns area tar upp en fjärdedels pi /  1)
'''
'''
h) Om jag testar att ändra x och y:s intervall från -2 till 2 så blir andelen 39% av punkterna innanför. 
Om testar med x och y från -3 till 3 så blir andelen med radien över 3: 26%. Desto större värden jag väljer
desto mindre blir andelen av punkter som är innanför. 
'''
'''
import matplotlib.pyplot as plt

import random as random
inne=0
ute=0
for i in range(1000000):
    x=random.uniform(-7,7)
    y=random.uniform(-7,7)  
    if x**2+y**2 <= 7:
#        plt.plot(x,y,'b*')
        inne+=1
    else:
#        plt.plot(x,y,'r*')
        ute+=1

print(inne, ute)
andel=inne/(i+1)
print("Andelen punkter som hamnar innanför cirkeln är",andel)
#plt.grid()
#plt.show()

'''

'''
'''
'''2a) använder in range satsen och sedan intervallet, 1 för att få ett mellanrum mellan talen
, detta är inte så nödvändigt men om man vill ha varranat tal kan detta var hjälpsamt. 
for n in range (0, 101, 1):
    print(n)
'''

'''
2b) när jag använder range satsen väljer jag vilket intervall mitt n kommer vara i.
När jag sedan använder moduleoperatorn får jag reda på om resten blir 0 och detta gör att
jag kan hitta 5ans multiplar. För talan som inte är multiplar printar de bara de talen mellan 1-100.
'''
'''
for n in range (0, 101, 1):
    if n%5==0:
        print("burr")
    print(n)
'''
'''
2c) samma som förklaring som i 2d. 
'''
'''
n1=float(input("skriv ett valfritt tal mellan 1-100 "))
for n in range (1,101,1):
    if n % n1==0:
        print("burr")
    print(n)
'''
'''
2d) Jag har skapat ett intervall med for i in range satsen och i detta fall mellan 1-100, och om talen som delas 
med talet användaren matade in och resten blir 0 betyder det att det är en multipel och därför printas burr. 
sen har jag lagt in print n sist så att programmet inte printar båda multiplarna och burr. 

'''
'''
n1=float(input("skriv ett valfritt tal mellan 1-100 "))
n2=float(input("skriv ett annat tal mellan 1-100"))
for n in range (1,101,1):
    if n % n1==0:
        print("burr")
    if n % n2==0:
        print("birr")
    else:
        print(n)
'''
'''
2e jag gör som låter användaren mata in ett startvärde och ett slutvärde, om dom till exempel väljer 1 och 100 
kommer programmet printa talen mellan dessa och beroende på vilka 2 tal användaren väljer kommer programmet printa
burr och birr för varje multipel av talen. Jag har lagt in start och slutvärde i min range vilket gör att programmet
förstår vilket intervall användaren vill. 
'''
n4=0
n3=0
start=int(input("skriv ett startvärde"))
slut=int(input("skriv ett slutvärde"))
n1=int(input("skriv ett tal mellan ditt start och slutvärde"))
n2=int(input("skriv ett ANNAT tal mellan ditt start och slutvärde "))
for n in range (start,slut,1):
    if n%n1==0:
        print ("burr")
        n3+=1
    if n%n2==0:
        print("birr")
        n4+=1
    else:
        print(n)
print("antal burr=",n3,"och antal birr=",n4,)
intervall=(slut-start)
print("i ett intervall bestående av", intervall, "siffror")




'''
2f)Ett sätt att utveckla detta program är att räkna antal birr och burr och printa dessa.
Detta gör att koden visar mer information till den som jobbar med koden. Jag beräknar också 
hur stort intervallet är med hjälp av slutvärdet minus startvärdet. 
'''
