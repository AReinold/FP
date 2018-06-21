import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
T1=ufloat(81.29, 0.24)
T2=ufloat(91.21, 0.24)
T3=ufloat(100.22, 0.24)
T4=ufloat(108.07, 0.24)
T5=ufloat(116.92, 0.24)
T6=ufloat(126.04, 0.24)
T7=ufloat(134.71, 0.24)
T8=ufloat(143.43, 0.24)
T9=ufloat(152.41, 0.24)
T10=ufloat(161.44, 0.24)
T11=ufloat(170.99, 0.25)
T12=ufloat(180.34, 0.25)
T13=ufloat(189.23, 0.25)
T14=ufloat(198.16, 0.25)
T15=ufloat(206.87, 0.25)
T16=ufloat(216.12, 0.25)
T17=ufloat(225.15, 0.25)
T18=ufloat(233.21, 0.25)
T19=ufloat(241.54, 0.25)
T20=ufloat(250.16, 0.25)
T21=ufloat(256.78, 0.25)
T22=ufloat(263.66, 0.26)
T23=ufloat(274.41, 0.26)
T24=ufloat(285.47, 0.26)
T25=ufloat(293.21, 0.26)
T26=ufloat(298.64, 0.26)


t1=T2-T1
t2=T3-T2
t3=T4-T3
t4=T5-T4
t5=T6-T5
t6=T7-T6
t7=T8-T7
t8=T9-T8
t9=T10-T9
t10=T11-T10
t11=T12-T11
t12=T13-T12
t13=T14-T13
t14=T15-T14
t15=T16-T15
t16=T17-T16
t17=T18-T17
t18=T19-T18
t19=T20-T19
t20=T21-T20
t21=T22-T21
t22=T23-T22
t23=T24-T23
t24=T25-T24
t25=T26-T25

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)
print(t10)
print(t11)
print(t12)
print(t13)
print(t14)
print(t15)
print(t16)
print(t17)
print(t18)
print(t19)
print(t20)
print(t21)
print(t22)
print(t23)
print(t24)
print(t25)
