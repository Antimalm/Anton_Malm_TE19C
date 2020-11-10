'''
Mjölkuppgift - while


1L mjölk 1 500 000 bakterier i rumstemp
 bakterier ökar med 50% per timme i rumstemp.
Mjölk surnar vid 10 000 000 st
Hur många timmar?
'''
import matplotlib.pyplot as plt
import numpy as np

bakterier = 1.5e6
surt = 1e7
faktor = 1.5
timmar = 0

y_bakterier = [bakterier]

while bakterier < surt:
    bakterier= faktor*bakterier
    y_bakterier.append(bakterier)
    timmar +=1

x_timmar = np.arange(timmar+1)


print(x_timmar)
print (f"Antal tillar tills mjölken surna är {timmar} timmar rumstemperatur.")
print(y_bakterier)

plt.plot(x_timmar, y_bakterier)
plt.xlabel("timmar")
plt.ylabel("antal bakterier")
plt.title("bakterietillväxt för  mjölki rumstemp")
plt.show()