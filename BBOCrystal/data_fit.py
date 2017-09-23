import matplotlib.pyplot as plt # This allows us to make nice plots.
import numpy as np # Allows us to manipulate lists and arrays, and imports trigonometric functions. 
import os # This will allow us to run the file import on both windows and macs.
from lmfit import minimize, Parameters, Parameter, report_fit, fit_report # This is the actual meat of the program: The fit routine.
from math import e, cos # Allows us to use e^... when we calculate stuff.


# Temperature in ˚C
T = [23.8,23.0,23.5,24.0,24.9,25.2,26.0,26.3,27.0,28.0,28.8,29.5,30.5,32.0,33.5,34.8,36.0,39.5,41.0,42.0,44.0,46.0]

# Current in A
I = [0.0,.10,.25,.3,.5,.6,.75,.8,1.0,1.1,1.25,1.3,1.5,1.6,1.75,1.8,2.0,2.1,2.25,2.3,2.5,2.6]

# Resistance in kΩ
R = [444.6,443.9,442.1,440.1,436.4,433.5,430.0,426.8,423.6,419.7,415.1,411.7,406.4,397.5,391.6,386.4,379.3,369.3,362.5,354.4,347.4,337.4]

'''FIT DATA WITH LINE
############################################'''
def fit_fc(params, x, data): 
    y0 = params['y0'].value 
    slope0 = params['slope0'].value  
    model =  slope0 * np.array(x) + y0
    return model - data



params = Parameters()
params.add('y0', value = 500.0, min = 400.0 , max = 650.0)
params.add('slope0', value = 0, min = -20, max = 20)

leastsq_kws={"ftol":1e-22, "xtol":1e-22, "gtol":1e-22, 'maxfev': 500000} # This tells Python what we consider a good enough fit. 
result = minimize(fit_fc, params, args=(T, R), method = 'leastsqr', **leastsq_kws) # Here we're telling it to use the least-square fitting method.

report_fit(result.params, show_correl = True, min_correl = 1e-3) # This reports the fitting results.
print(fit_report(result, min_correl = 1e-10)) # Print out the final report, including uncertainty.

xplot = T # An elegant way to set up the x-axis.
yplot = np.array(result.params['slope0']) * xplot + result.params['y0'] # NOTE that the np.array is SUPER IMPORTANT!! OTherwise it dies with a cryptic error message!

plt.yticks(fontsize=16)    
plt.xticks(fontsize=16) 

xdiff = np.max(T) - np.min(T)
ydiff = np.max(R) - np.min(R)
plt.xlim(np.min(T)-np.sqrt(xdiff),np.max(T)+np.sqrt(xdiff))
plt.ylim(np.min(R)-np.sqrt(ydiff),np.max(R)+np.sqrt(ydiff))

plt.title('Resistance versus Temperature for BBO thermistor')
plt.xlabel('Temperature (˚C)')
plt.ylabel('Resistance (kΩ)')

plt.plot(xplot, yplot) # Show the fit as well as the original data.
plt.plot(T, R,'ro')
plt.grid(True)
plt.show()
