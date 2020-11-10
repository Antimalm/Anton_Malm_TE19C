
'''
while n < 10:
    print(n, end =" ")
    n+=1
'''
'''
s= 0
while n < 50:
    s=s+n
    n+=2
print(f"{s}")
'''
'''
1L mjölk 1500000 bakterier
I rumstemperatur ökar antalet bakterier med 50% varje timme. 
Mjölken blir sur när bakterierna överstiger 10000000 st
Hur många timmar tills den blir sur?
'''
'''
n=1500000
while n < 10000000:
    s = n*1,5
print(f"{n}")
'''

'''
import dandom as rnd

rnd.randint(1,10)
'''
import matplotlib.pyplot as plt

s = [0,10,20,30,40,50,60,70,80,90,100]

t = [0,1.83,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.97,9.69]

v=[0]



for i in range(1,len(t)):
    v_i=(s[i]-s[i-1])/(t[i]-t[i-1])
    v.append(v_i)


plt.plot(t,v)
plt.show()
