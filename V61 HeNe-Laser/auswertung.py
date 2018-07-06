import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.optimize import curve_fit
########################################################################################################
################################## M O D E  1 0 ########################################################

x, I = np.loadtxt('\messwerte\erstemode.txt', unpack = True)

def f(x, I0, x0, w):
    return I0*(8*((x-x0)/w)**2)*np.exp(-2*((x-x0)/w)**2)

params, cov = curve_fit(f, x, I, p0=[33,20,13])
I0 = params[0]
I0_err = np.sqrt(cov[0][0])
x0 = params[1]
x0_err = np.sqrt(cov[1][1])
w = params[2]
w_err = np.sqrt(cov[2][2])

print(
"""
---------------------------------------------------------------------------------------------------
Parameter der Ausgleichsrechnung: (I0*((8*(x-x0)**2)/(w**2))*np.exp(-((x-x0)**2)/(w**2))) Mode 10
I0 = {}+-{}
x0 = {}+-{}
w = {}+-{}
---------------------------------------------------------------------------------------------------
""".format(I0, I0_err, x0, x0_err, w, w_err))

t = np.linspace(x.min(), x.max(), 1000)
plt.plot(t, f(t, I0, x0, w), 'r-', label='Ausgleichsrechnung')
plt.plot(x, I, 'b.', label='Daten $TEM_{10}$-Mode')
plt.xlim(x.min()-2, x.max()+2)
plt.ylabel(r"Stromstärke $I/$µA")
plt.xlabel(r"Abstand $/mm$")
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig("plot_Mode10.pdf")
plt.close()
