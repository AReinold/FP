import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

tank =ufloat(9.5,0.8)
lSchlauch = ufloat(0.8,0.1)
kSchlauch=ufloat(0.087,0.011)
Tklein=ufloat(0.013, 0.002)
Tgross=ufloat(0.25, 0.01)
kreuzklein=ufloat(0.016, 0.002)
kreuzgross=ufloat(0.177, 0.09)
ventil1o=ufloat(0.015, 0.002)
ventil1zu=ufloat(0.005, 0.001)
ventil2o=ufloat(0.025, 0.005)
ventil2zu=ufloat(0.0125, 0.0025)
klappeo=ufloat(0.044, 0.004)
klappezu=ufloat(0.022, 0.002)
querschnitt=ufloat(0.067,0.004)

TE=tank+Tgross+kreuzgross+2*(ventil1zu)+klappeo+querschnitt
TL=tank+Tgross+kreuzgross+ventil1o+ventil1zu+klappezu

DE=ventil1o+kreuzgross+kreuzklein+Tgross+Tklein+kSchlauch+lSchlauch+tank+2*(ventil1zu)+ventil2o+klappezu
DL=ventil1o+kreuzgross+kreuzklein+Tgross+Tklein+kSchlauch+lSchlauch+tank+2*(ventil1zu)+klappezu
print(TE)
print(TL)
print(DE)
print(DL)
