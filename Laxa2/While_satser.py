'''
print("jämna tal från 0-10")
n=0
while n <= 10:
    print(n, end=" ")
    n += 2
'''

'''
fåglar=8000
antal_år=0

print(f" år {antal_år}: antal fåglar: {fåglar}st")
while fåglar >=800:
    fåglar /= 2 
    antal_år += 1
    print(f"år {antal_år} antal fåglar: {fåglar}st")
'''
'''
uppgift 1
s=0
n=0
while s < 100:
    s+=1
    n+=s

print(n)
'''
'''
uppgift 2
s=0
n=0
while s < 99:
    s+=2
    n+=s

print(n)
'''
'''
uppgift 3
n=0
r=0
while n < 100:
    r+=2**(-n)
    n+=1
print (f"{r}")
'''


import random as rnd
rnd.randint(1,100)
n=rnd.randint(1,100)
gissning = float(input("skriv ett heltal mellan 0 och 100"))
while gissning != n:
    print:("ett annat tal")
   



