##################################################
# filename: TRFluctuations.py
# objective: measure the fluctuations of temperature and resistance at fixed current
# current = 5A
##################################################

import numpy as np
import csv
import matplotlib.pyplot as plt

# Our time was incremented in steps of 15 seconds
time = np.arange(0,70*15,15)

Res = []
Temp = []

with open('RTfluctuations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Res.append(row['Resistance'])
        Temp.append(row['Temperature'])
Res = np.array(Res)
Temp = np.array(Temp)
time.astype(float)
time = np.array(time)
Res = Res.astype(float)
Temp = Temp.astype(float)

##################################################
# Resistance versus time
##################################################
plt.figure()
plt.plot(time,Res,'.')
plt.title('Resistance vs Time of Thermistor (I = 5A)')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (kΩ)')
plt.grid(True)
plt.show()


##################################################
# Curve fit
##################################################
from scipy.optimize import curve_fit
def exponenial_func(x, a, b, c):
    return a-b*np.exp(-x/c)


popt, pcov = curve_fit(exponenial_func, time, Temp, p0=(47,50,500))
print(popt)
##################################################
# Temperature versus Time
##################################################
plt.figure()
plt.plot(time,Temp,'.')
plt.plot(time,popt[0]-popt[1]*np.exp(-time/popt[2]))
plt.title('Temperature vs Time of Thermistor (I = 5A)')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (˚C)')
plt.grid(True)
plt.show()

