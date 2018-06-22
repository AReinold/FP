import matplotlib.pyplot as plt
import math
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

x=np.sqrt((437.8-516.28)**2+(451.0-516.28)**2+(464.7-516.28)**2+(491.1-516.28)**2+(504.2-516.28)**2+(525.4-516.28)**2+(545.0-516.28)**2+(563.9-516.28)**2+(581.2-516.28)**2+(598.5-516.28)**2)
a=np.sqrt(1)/90
y=a*x

#x=np.array([95.86,92.23,94.75])
#y=np.std(x)/unp.sqrt(len(x))

print(y)
