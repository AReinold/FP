import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
x=ufloat(-0.000873, 0.000004)
y=ufloat(0.00001941, 0.00000003)

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

C1=ufloat(11.5, 0.4)
C2=ufloat(10.5, 0.4)
C3=ufloat(14.6, 0.6)
C4=ufloat(15.1, 0.6)
C5=ufloat(14.1, 0.5)
C6=ufloat(14.6, 0.6)
C7=ufloat(15.2, 0.6)
C8=ufloat(15.0, 0.6)
C9=ufloat(15.3, 0.6)
C10=ufloat(14.5, 0.5)
C11=ufloat(14.9, 0.6)
C12=ufloat(15.6, 0.6)
C13=ufloat(15.6, 0.6)
C14=ufloat(16.2, 0.7)
C15=ufloat(15.2, 0.6)
C16=ufloat(15.6, 0.6)
C17=ufloat(17.5, 0.8)
C18=ufloat(17.0, 0.7)
C19=ufloat(18.0, 0.8)
C20=ufloat(23.5, 0.3)
C21=ufloat(24.7, 0.3)
C22=ufloat(15.8, 0.6)
C23=ufloat(15.4, 0.5)
C24=ufloat(22.0, 0.1)
C25=ufloat(26.1, 0.8)

a2=(x/T2)+y
a3=(x/T3)+y
a4=(x/T4)+y
a5=(x/T5)+y
a6=(x/T6)+y
a7=(x/T7)+y
a8=(x/T8)+y
a9=(x/T9)+y
a10=(x/T10)+y
a11=(x/T11)+y
a12=(x/T12)+y
a13=(x/T13)+y
a14=(x/T14)+y
a15=(x/T15)+y
a16=(x/T16)+y
a17=(x/T17)+y
a18=(x/T18)+y
a19=(x/T19)+y
a20=(x/T20)+y
a21=(x/T21)+y
a22=(x/T22)+y
a23=(x/T23)+y
a24=(x/T24)+y
a25=(x/T25)+y
a26=(x/T26)+y

kappa=140
V0=0.000007092

CV1=(C1)-(9*(a2**2))*(kappa)*(V0)*(T2)
CV2=(C2)-(9*(a3**2))*(kappa)*(V0)*(T3)
CV3=(C3)-(9*(a4**2))*(kappa)*(V0)*(T4)
CV4=(C4)-(9*(a5**2))*(kappa)*(V0)*(T5)
CV5=(C5)-(9*(a6**2))*(kappa)*(V0)*(T6)
CV6=(C6)-(9*(a7**2))*(kappa)*(V0)*(T7)
CV7=(C7)-(9*(a8**2))*(kappa)*(V0)*(T8)
CV8=(C8)-(9*(a9**2))*(kappa)*(V0)*(T9)
CV9=(C9)-(9*(a10**2))*(kappa)*(V0)*(T10)
CV10=(C10)-(9*(a11**2))*(kappa)*(V0)*(T11)
CV11=(C11)-(9*(a12**2))*(kappa)*(V0)*(T12)
CV12=(C12)-(9*(a13**2))*(kappa)*(V0)*(T13)
CV13=(C13)-(9*(a14**2))*(kappa)*(V0)*(T14)
CV14=(C14)-(9*(a15**2))*(kappa)*(V0)*(T15)
CV15=(C15)-(9*(a16**2))*(kappa)*(V0)*(T16)
CV16=(C16)-(9*(a17**2))*(kappa)*(V0)*(T17)
CV17=(C17)-(9*(a18**2))*(kappa)*(V0)*(T18)
CV18=(C18)-(9*(a19**2))*(kappa)*(V0)*(T19)
CV19=(C19)-(9*(a20**2))*(kappa)*(V0)*(T20)
CV20=(C20)-(9*(a21**2))*(kappa)*(V0)*(T21)
CV21=(C21)-(9*(a22**2))*(kappa)*(V0)*(T22)
CV22=(C22)-(9*(a23**2))*(kappa)*(V0)*(T23)
CV23=(C23)-(9*(a24**2))*(kappa)*(V0)*(T24)
CV24=(C24)-(9*(a25**2))*(kappa)*(V0)*(T25)
CV25=(C25)-(9*(a26**2))*(kappa)*(V0)*(T26)

print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)
print(a9)
print(a10)
print(a11)
print(a12)
print(a13)
print(a14)
print(a15)
print(a16)
print(a17)
print(a18)
print(a19)
print(a20)
print(a21)
print(a22)
print(a23)
print(a24)
print(a25)
print(a26)

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(CV1)
print(CV2)
print(CV3)
print(CV4)
print(CV5)
print(CV6)
print(CV7)
print(CV8)
print(CV9)
print(CV10)
print(CV11)
print(CV12)
print(CV13)
print(CV14)
print(CV15)
print(CV16)
print(CV17)
print(CV18)
print(CV19)
print(CV20)
print(CV21)
print(CV22)
print(CV23)
print(CV24)
print(CV25)
