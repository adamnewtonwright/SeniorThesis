import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd
from scipy.optimize import curve_fit
 ##################################################
 # saturation intensity for diode laser in CW
 ##################################################
 

power = [0,0.25,0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.25,2.50,2.75,3.00,3.25]
fl =    [0,14.4,24.8,41.6,48.8,54.5,60.8,68.0,72.8,76.8,82.4,84.8,89.6,93.6]
power = np.array(power) / 1000 #milliwatts -> watts
fl = np.array(fl)
area = np.pi * (2e-3)**2
intensity = power / area

error = [abs(fl[i]) * np.sqrt((.2/fl[i])**2 + (.2/np.max(fl))**2) for i in range(0,len(fl))]

def sigmoid(x, x0, k, a):
     y = a / (1 + np.exp(-k*(x-x0)))
     return y

def sat(I,A,Isat,C):
    y = A / (1+I/Isat) + C
    return y

popt, pcov = curve_fit(sat, intensity, fl)
print(popt)

y = sat(power, *popt)

plt.figure()
plt.errorbar(intensity,fl,yerr = error,fmt = '.', label = 'Data')
plt.plot(intensity,y, label = 'Sigmoid Best Fit')
plt.xlabel('Power (mW)')
plt.ylabel('Fluorescence (dV)')
plt.grid(True)
plt.legend(loc = 4)
plt.savefig('SatCont.pdf')
plt.show()

