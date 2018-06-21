import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

m=0.342
M=0.063546

U2=ufloat(13.27, 0.01)
U3=ufloat(13.26, 0.01)
U4=ufloat(13.25, 0.01)
U5=ufloat(13.28, 0.01)
U6=ufloat(13.30, 0.01)
U7=ufloat(13.29, 0.01)
U8=ufloat(13.32, 0.01)
U9=ufloat(13.33, 0.01)
U10=ufloat(13.34, 0.01)
U11=ufloat(13.34, 0.01)
U12=ufloat(13.35, 0.01)
U13=ufloat(13.35, 0.01)
U14=ufloat(13.35, 0.01)
U15=ufloat(13.36, 0.01)
U16=ufloat(13.37, 0.01)
U17=ufloat(13.37, 0.01)
U18=ufloat(13.37, 0.01)
U19=ufloat(13.38, 0.01)
U20=ufloat(13.38, 0.01)
U21=ufloat(13.38, 0.01)
U22=ufloat(13.38, 0.01)
U23=ufloat(13.39, 0.01)
U24=ufloat(13.40, 0.01)
U25=ufloat(13.40, 0.01)
U26=ufloat(13.41, 0.01)

I2=ufloat(0.1531, 0.00001)
I3=ufloat(0.1542, 0.00001)
I4=ufloat(0.1548, 0.00001)
I5=ufloat(0.1640, 0.00001)
I6=ufloat(0.1738, 0.00001)
I7=ufloat(0.1703, 0.00001)
I8=ufloat(0.1785, 0.00001)
I9=ufloat(0.1815, 0.00001)
I10=ufloat(0.1863, 0.00001)
I11=ufloat(0.1866, 0.00001)
I12=ufloat(0.1868, 0.00001)
I13=ufloat(0.1869, 0.00001)
I14=ufloat(0.187, 0.00001)
I15=ufloat(0.1889, 0.00001)
I16=ufloat(0.1891, 0.00001)
I17=ufloat(0.1893, 0.00001)
I18=ufloat(0.1894, 0.00001)
I19=ufloat(0.1894, 0.00001)
I20=ufloat(0.1895, 0.00001)
I21=ufloat(0.1896, 0.00001)
I22=ufloat(0.1896, 0.00001)
I23=ufloat(0.1896, 0.00001)
I24=ufloat(0.1897, 0.00001)
I25=ufloat(0.1898, 0.00001)
I26=ufloat(0.1898, 0.00001)

T1=ufloat(81.29,0.24)
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
T26=ufloat(298.64,0.26)

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

z1=ufloat(302, 3)
z2=ufloat(250, 3)
z3=ufloat(300, 3)
z4=ufloat(330, 3)
z5=ufloat(360, 3)
z6=ufloat(360, 3)

C1=(M*U2*I2*z1)/(m*t1)
C2=(M*U3*I3*z2)/(m*t2)
C3=(M*U4*I4*z3)/(m*t3)
C4=(M*U5*I5*z4)/(m*t4)
C5=(M*U6*I6*z3)/(m*t5)
C6=(M*U7*I7*z3)/(m*t6)
C7=(M*U8*I8*z3)/(m*t7)
C8=(M*U9*I9*z3)/(m*t8)
C9=(M*U10*I10*z3)/(m*t9)
C10=(M*U11*I11*z3)/(m*t10)
C11=(M*U12*I12*z3)/(m*t11)
C12=(M*U13*I13*z3)/(m*t12)
C13=(M*U14*I14*z3)/(m*t13)
C14=(M*U15*I15*z3)/(m*t14)
C15=(M*U16*I16*z3)/(m*t15)
C16=(M*U17*I17*z3)/(m*t16)
C17=(M*U18*I18*z3)/(m*t17)
C18=(M*U19*I19*z3)/(m*t18)
C19=(M*U20*I20*z4)/(m*t19)
C20=(M*U21*I21*z4)/(m*t20)
C21=(M*U22*I22*z6)/(m*t21)
C22=(M*U23*I23*z6)/(m*t22)
C23=(M*U24*I24*z6)/(m*t23)
C24=(M*U25*I25*z6)/(m*t24)
C25=(M*U26*I26*z3)/(m*t25)

print(C1)
print(C2)
print(C3)
print(C4)
print(C5)
print(C6)
print(C7)
print(C8)
print(C9)
print(C10)
print(C11)
print(C12)
print(C13)
print(C14)
print(C15)
print(C16)
print(C17)
print(C18)
print(C19)
print(C20)
print(C21)
print(C22)
print(C23)
print(C24)
print(C25)
