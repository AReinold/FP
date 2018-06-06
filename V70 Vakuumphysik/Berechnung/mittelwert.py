import matplotlib.pyplot as plt
import math
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

x=np.sqrt((95.86-94.28)**2+(92.23-94.28)**2+(94.75-94.28)**2)
a=np.sqrt((1)/(3*(2)))
y=a*x

#x=np.array([95.86,92.23,94.75])
#y=np.std(x)/unp.sqrt(len(x))

print(y)
