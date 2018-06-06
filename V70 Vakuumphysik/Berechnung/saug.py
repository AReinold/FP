import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

p=ufloat(0.0002, 0.00002)
V=ufloat(10.0,0.8)
m=ufloat(0.000436, 0.000012)
S=(V/p)*m

print(S)
