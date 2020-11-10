import numpy as np
import matplotlib.pyplot as plt

s = [10,20,30,40,50,60,70,80,90,100]

t = [1.83,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.97,9.69]

v= [10/1.83, 20/2.87, 30/3.78, 40/4.65, 50/5.5, 60/6.32, 70/7.14, 80/7.96, 90/8.97, 90/9.69]



plt.plot (s,v, '*-')
plt.ylabel("hastighet(m/s)")
plt.xlabel("sträcka(m)")
plt.title("Usain bolts värdldsrekord")
plt.grid()
plt.show()





