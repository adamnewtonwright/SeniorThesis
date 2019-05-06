##################################################
# filename: efficiency.py
# objective: Measure efficiency of the bbo conversion
# current = 5 A
##################################################

import numpy as np
import csv
import matplotlib.pyplot as plt

# total amount of light was 15,500

green = []
res = []
efficiency = []

with open('efficiency.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        green.append(row['green'])
        res.append(float(row['res']))
res = np.array(res)
green = np.array(green)
res = res.astype(float)
green = green.astype(float)


for each in green:
	e = each/15500 * 100
	efficiency.append(float(e))
efficiency = np.array(efficiency)
##################################################
# Resistance versus time
##################################################
plt.figure()
plt.plot(res,efficiency,'.')
#plt.title('Efficiency of BBO Crystal versus Resistance of Thermistor')
plt.xlabel('Resistance (kΩ)')
plt.ylabel('Efficiency (%)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/efficiency.pdf')
plt.show()


##################################################
# Curve fit
##################################################
from scipy.optimize import curve_fit
def exponenial_func(x, a, b, c):
    return a-b*np.exp(-x/c)


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

