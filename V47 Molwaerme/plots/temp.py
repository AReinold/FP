import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

R1=ufloat(22, 0.1)
R2=ufloat(26.2, 0.1)
R3=ufloat(30, 0.1)
R4=ufloat(33.3, 0.1)
R5=ufloat(37, 0.1)
R6=ufloat(40.8, 0.1)
R7=ufloat(44.4, 0.1)
R8=ufloat(48.0, 0.1)
R9=ufloat(51.7, 0.1)
R10=ufloat(55.4, 0.1)
R11=ufloat(59.3, 0.1)
R12=ufloat(63.1, 0.1)
R13=ufloat(66.7, 0.1)
R14=ufloat(70.3, 0.1)
R15=ufloat(73.8, 0.1)
R16=ufloat(77.5, 0.1)
R17=ufloat(81.1, 0.1)
R18=ufloat(84.3, 0.1)
R19=ufloat(87.6, 0.1)
R20=ufloat(91, 0.1)
R21=ufloat(93.6, 0.1)
R22=ufloat(96.3, 0.1)
R23=ufloat(100.5, 0.1)
R24=ufloat(104.8, 0.1)
R25=ufloat(107.8, 0.1)
R26=ufloat(109.9, 0.1)

T1=0.00134*R1**2+2.296*R1+30.13
T2=0.00134*R2**2+2.296*R2+30.13
T3=0.00134*R3**2+2.296*R3+30.13
T4=0.00134*R4**2+2.296*R4+30.13
T5=0.00134*R5**2+2.296*R5+30.13
T6=0.00134*R6**2+2.296*R6+30.13
T7=0.00134*R7**2+2.296*R7+30.13
T8=0.00134*R8**2+2.296*R8+30.13
T9=0.00134*R9**2+2.296*R9+30.13
T10=0.00134*R10**2+2.296*R10+30.13
T11=0.00134*R11**2+2.296*R11+30.13
T12=0.00134*R12**2+2.296*R12+30.13
T13=0.00134*R13**2+2.296*R13+30.13
T14=0.00134*R14**2+2.296*R14+30.13
T15=0.00134*R15**2+2.296*R15+30.13
T16=0.00134*R16**2+2.296*R16+30.13
T17=0.00134*R17**2+2.296*R17+30.13
T18=0.00134*R18**2+2.296*R18+30.13
T19=0.00134*R19**2+2.296*R19+30.13
T20=0.00134*R20**2+2.296*R20+30.13
T21=0.00134*R21**2+2.296*R21+30.13
T22=0.00134*R22**2+2.296*R22+30.13
T23=0.00134*R23**2+2.296*R23+30.13
T24=0.00134*R24**2+2.296*R24+30.13
T25=0.00134*R25**2+2.296*R25+30.13
T26=0.00134*R26**2+2.296*R26+30.13

print(T1)
print(T2)
print(T3)
print(T4)
print(T5)
print(T6)
print(T7)
print(T8)
print(T9)
print(T10)
print(T11)
print(T12)
print(T13)
print(T14)
print(T15)
print(T16)
print(T17)
print(T18)
print(T19)
print(T20)
print(T21)
print(T22)
print(T23)
print(T24)
print(T25)
print(T26)
