import matplotlib.pyplot as plt
import math
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

start=ufloat(8*10**(-3),0.8*10**(-3))
end=ufloat(1.6*10**(-5),0.2*10**(-5))

druck1=ufloat(6*10**(-3),0.6*10**(-3))
druck2=ufloat(3*10**(-3),0.3*10**(-3))
druck3=ufloat(6*10**(-4),0.6*10**(-4))
druck4=ufloat(3*10**(-4),0.3*10**(-4))
druck5=ufloat(6*10**(-5),0.6*10**(-5))
druck6=ufloat(3*10**(-5),0.3*10**(-5))

x=((druck6-end)/(start-end))
ln1=unp.log(x)

print(ln1)
