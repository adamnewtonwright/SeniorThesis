##################################################
# filename: TRFluctuations.py
# objective: Measure the fluctuations in resistance and temperature
# current = 5 A
##################################################

import numpy as np
import csv
import matplotlib.pyplot as plt


Res = []
time = []
Temp = []

with open('RTFluctuations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Res.append(row['Resistance'])
        time.append(float(row['Time']))
        Temp.append(row['Temperature'])
Res = np.array(Res)
Temp = np.array(Temp)
#time.astype(float)
time = np.array(time)
Res = Res.astype(float)
Temp = Temp.astype(float)

##################################################
# Resistance versus time
##################################################
plt.figure()
plt.plot(time,Res,'.')
#plt.title('Resistance vs Time of Thermistor (I = 5A)')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (kΩ)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/ResFluct.pdf')
plt.show()


##################################################
# Curve fit
##################################################
from scipy.optimize import curve_fit
def exponenial_func(x, a, b, c):
    return a-b*np.exp(-x/c)


popt, pcov = curve_fit(exponenial_func, time, Temp, p0=(30,20,400))
print(popt)
##################################################
# Temperature versus Time
##################################################
plt.figure()
plt.plot(time,Temp,'.')
plt.plot(time,popt[0]-popt[1]*np.exp(-time/popt[2]))
#plt.title('Temperature vs Time of Thermistor (I = 5A)')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (˚C)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/TempFluctFit.pdf')
plt.show()

