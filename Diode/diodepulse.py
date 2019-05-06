##################################################
# filename: TRFluctuations.py
# objective: Measure the fluctuations in resistance and temperature
# current = 5 A
##################################################

import numpy as np
import csv
import matplotlib.pyplot as plt


time1 = []
volts1 = []

with open('WaveData20.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        volts1.append(str(row['volt']))
        time1.append(row['time'])
time1 = np.array(time1)
volts1 = np.array(volts1)
time1 = time1.astype(float)
volts1 = volts1.astype(float)

##################################################
# Resistance versus time
##################################################
plt.figure()
plt.plot(time1,volts1)
#plt.title('Pulse of Diode Laser')
plt.xlabel('Time (s)')
plt.ylabel('Intensity (mV)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/diodepulse.pdf')
plt.show()


time2 = []
volts2 = []

with open('WaveData22.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        volts2.append(str(row['volt']))
        time2.append(row['time'])
time2 = np.array(time2)
volts2 = np.array(volts2)
time2 = time2.astype(float)
volts2 = volts2.astype(float)

##################################################
# Resistance versus time
##################################################
plt.figure()
plt.plot(time2,volts2)
#plt.title('Pulse of Diode Laser')
plt.xlabel('Time (s)')
plt.ylabel('Intensity (mV)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/diodepulse2.pdf')
plt.show()
###################################################
## Curve fit
###################################################
#from scipy.optimize import curve_fit
#def exponenial_func(x, a, b, c):
#    return a-b*np.exp(-x/c)
#
#
#popt, pcov = curve_fit(exponenial_func, time, Temp, p0=(47,50,500))
#print(popt)
###################################################
## Temperature versus Time
###################################################
#plt.figure()
#plt.plot(time,Temp,'.')
#plt.plot(time,popt[0]-popt[1]*np.exp(-time/popt[2]))
#plt.title('Temperature vs Time of Thermistor (I = 5A)')
#plt.xlabel('Time (s)')
#plt.ylabel('Temperature (˚C)')
#plt.grid(True)
#plt.show()
#
