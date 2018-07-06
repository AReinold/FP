from __future__ import unicode_literals

from numpy import*
from matplotlib.pyplot import *
from scipy.optimize import curve_fit

modpos1,modi1 = loadtxt("messwerte/erstemode.txt",unpack=True)

def I2(r,I_1,I_2,v1,v2,w1,w2):
    return I_1*exp(-2*(r-v1)**2/w1**2)+ I_2*exp(-2*(r-v2)**2/w2**2)

modfit2,modcov2 = curve_fit(I2,modpos1,modi1)

minarray=linspace(5,15,1000)
minsuche = I2(minarray,modfit2[0],modfit2[1],modfit2[2],modfit2[3],modfit2[4],modfit2[5])
i=0
for i in range(0,len(minarray)):
    if minsuche[i] == min(minsuche):
        break
    else:
        i = i+1

minstelle = minarray[i]

modxarray2 = linspace(-5,27,50)
plot(modxarray2-minstelle,I2(modxarray2,modfit2[0],modfit2[1],modfit2[2],modfit2[3],modfit2[4],modfit2[5]))
plot(modpos1-minstelle,modi1,"*")
grid()
xlabel("Abs. zur opt. Achse / mm")
ylabel("Photostrom I / µA")
ylim(-2,60)
xlim(-15,15)
savefig("mode2.pdf")
close()
