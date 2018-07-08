import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import sem
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as stds



def E_00(d,I_0,d_0, omega):
    return I_0*np.exp( -2*( (d-d_0)/omega )**2 )
def E_10(d, I_01, d_01, omega_1, I_02, d_02, omega_2):
    return I_01 * np.exp( -2 * ( (d-d_01) / omega_1 )**2 )+ I_02 * np.exp( -2 * ( ( d-d_02) / omega_2 )**2 )
def polarisation( phi, I_0, phi_0):
    return I_0*( np.cos(phi-phi_0) )**2
###################
# Auswertung T_00 #
###################
print('\n\n\n-----------------------------------------------------------\n','Auswertung der Grundmode T_00', '\n', '-----------------------------------------------------------\n\n\n')
r_00, I_00=np.genfromtxt('Messwerte\Grundmode.txt',unpack=True)
params_I_00, cov_I_00 = curve_fit(E_00,r_00,I_00 )
error_I_00= np.sqrt(np.diag(cov_I_00))


amplitude_I_00 = ufloat(params_I_00[0],error_I_00[0])
verschiebung_I_00 = ufloat( params_I_00[1], error_I_00[1])
omega_I_00 = ufloat( params_I_00[2], error_I_00[2])

print('Amplitude: ', amplitude_I_00,'\n')
print('Verschiebung ', verschiebung_I_00,'\n')
print('Frequenz ', omega_I_00, '\n')

# Plotten
d_00=np.linspace(r_00[0],r_00[-1],10000)

plt.plot(r_00, I_00, '.', label='Messwerte')
plt.plot(d_00, E_00(d_00, params_I_00[0], params_I_00[1], params_I_00[2]), label='Fit')
plt.legend()
plt.xlabel(r'$r \, / \, mm $')
plt.ylabel(r'$ I_{\mathrm{p}}\, / \, \mu A$')
plt.grid()
plt.savefig('plots\T_00.png')
#plt.show()


###################
# Auswertung T_10 #
###################
print('\n\n\n-----------------------------------------------------------\n','Auswertung der Grundmode T_10', '\n', '-----------------------------------------------------------\n\n\n')

r_10, I_10=np.genfromtxt('Messwerte\erstemode.txt',unpack=True)



I_max_left=max(I_10[1:10])
I_max_right=max(I_10[10:-1])
null=np.where(I_10<0.04)[0][0]
r_left_max=r_10[np.where(I_10==I_max_left)[0][0]]
r_right_max=r_10[np.where(I_10==I_max_right)[0][0]]

omega_guess_left=8*sem( I_10[1:13])
omega_guess_right=8*sem( I_10[13:-1])
print(omega_guess_left)
print('Verwendete Startwerte für den T_10 Fit: \n')
print('I_1 ',I_max_left)
print('d_1 ', r_left_max)

print('\n I_2 ',I_max_right)
print('d_2 ', r_right_max)



params_I_10, cov_I_10 = curve_fit(E_10,r_10,I_10,p0=[I_max_left, r_left_max, 1, I_max_right, r_right_max,1])
error_I_10= np.sqrt(np.diag(cov_I_10))

amplitude_I_01 = ufloat(params_I_10[0],error_I_10[0])
verschiebung_d_01 = ufloat( params_I_10[1], error_I_10[1])
omega_1 = ufloat( params_I_10[2], error_I_10[2])

amplitude_I_02 = ufloat(params_I_10[3],error_I_10[3])
verschiebung_d_02 = ufloat( params_I_10[4], error_I_10[4])
omega_2 = ufloat( params_I_10[5], error_I_10[5])


print('Amplitude 1: ', amplitude_I_01,'\n')
print('Verschiebung 1: ', verschiebung_d_01,'\n')
print('Frequenz 1: ', omega_1, '\n')

print('Amplitude 2: ', amplitude_I_02,'\n')
print('Verschiebung 2: ', verschiebung_d_02,'\n')
print('Frequenz 2: ', omega_2, '\n')


# Plotten
d_10=np.linspace(r_10[0],r_10[-1],10000)
plt.clf()
plt.plot(r_10, I_10, '.', label='Messwerte')
plt.plot(d_10, E_10( d_10,params_I_10[0], params_I_10[1], params_I_10[2], params_I_10[3], params_I_10[4], params_I_10[5]), label='Fit')
plt.legend()
plt.xlabel(r'$r \, / \, mm $')
plt.ylabel(r'$ I_{\mathrm{p}}\, / \, \mu A$')
plt.grid()
#plt.show()
plt.savefig('plots\T_10.png')



### Polarisationsmessung ###

# winkel = Q_(np.linspace(0, 360, 37), 'degree') #in deg
#
# I_pol = Q_(np.array([0.116, 0.067, 0.034, 0.011, 0.001, 0.004, 0.020, 0.049, 0.086,
# 0.137, 0.187, 0.238, 0.281, 0.307, 0.308, 0.288, 0.251, 0.198, 0.137, 0.083, 0.040,
# 0.013, 0.001, 0.005, 0.024, 0.053, 0.094, 0.146, 0.208, 0.264, 0.295, 0.296, 0.279,
# 0.252, 0.214, 0.167, 0.111]), 'mA') #in mA

#winkel, I_pol=np.genfromtxt('polarisation.txt',unpack=True)
#winkel=np.deg2rad(winkel)
#print(max(winkel))

#params_pol, covariance_pol = curve_fit(polarisation,winkel, I_pol)

#winkel_fit = np.linspace(-0.1, 2 * np.pi + 0.1, 1000)

#plt.clf()
#plt.plot(winkel_fit, polarisation(winkel_fit, *params_pol), 'r-', label=r'Fit')
#plt.plot(winkel, I_pol, 'bx', label=r'Messdaten')
#plt.xlabel('$\phi$ in rad')
#plt.xlim(-0.1, 2 * np.pi + 0.1)
#plt.ylabel('$I(\phi)$ in µA')
#plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           #[r"$0$", r"$\frac{1}{2}\pi$", r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
#plt.tight_layout()
#plt.legend(loc = 'best')
#plt.show()
#plt.savefig('polarisation.pdf')

#print('Parameter Fit Polarisation:(I_0, phi_0) ', *params_pol, '\n')
#print('Parameter Fehler Fit Polarisation: ', np.sqrt(np.diag(covariance_pol)), '\n')
#print(np.rad2deg(params_pol[1]))
