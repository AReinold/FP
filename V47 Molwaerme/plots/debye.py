import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

T1=ufloat(91.21, 0.24)
T2=ufloat(100.22, 0.24)
T3=ufloat(108.07, 0.24)
T4=ufloat(116.92, 0.24)
T5=ufloat(126.04, 0.24)
T6=ufloat(134.71, 0.24)
T7=ufloat(143.43, 0.24)
T8=ufloat(152.41, 0.24)
T9=ufloat(161.44, 0.24)
T10=ufloat(170.99, 0.25)

D1=4.8
D2=4.5
D3=4.3
D4=4.2
D5=4.0
D6=3.9
D7=3.8
D8=3.7
D9=3.6
D10=3.5

d1=T1*D1
d2=T2*D2
d3=T3*D3
d4=T4*D4
d5=T5*D5
d6=T6*D6
d7=T7*D7
d8=T8*D8
d9=T9*D9
d10=T10*D10

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8)
print(d9)
print(d10)
