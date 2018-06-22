import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.umath import sqrt
from uncertainties import ufloat
import math
t, c, fehler = np.genfromtxt('cvplot.txt', unpack=True)

x=np.linspace(70, 300, 1000)

plt.plot(t, c, 'rx', label='Messwerte für $C_V$')

plt.xlabel(r"$T$ in $\mathrm{K}$")
plt.ylabel(r"$C_{\mathrm{V}}$ in $\mathrm{JK}^{-1}\mathrm{mol}^{-1}$")
plt.errorbar(t, c, fehler, fmt='none')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('cvplot.pdf')
