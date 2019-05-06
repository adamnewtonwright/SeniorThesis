import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

difference = []
for j in range(0,13):
    if j <10:
        data = pd.read_csv('ALL000'+str(j)+'/F000'+str(j)+'CH3.CSV',names = ['time','voltage','that'])
        voltage = data['voltage']
        max = -2000
        min = 2000
        for i in voltage:
            if i >= max:
                max =i
            if i<= min:
                min = i
    elif j >=10:
        data = pd.read_csv('ALL00'+str(j)+'/F00'+str(j)+'CH3.CSV',names = ['time','voltage','that'])
        voltage = data['voltage']
        max = -2000
        min = 2000
        for i in voltage:
            if i >= max:
                max =i
            if i<= min:
                min = i
    print(max, min, abs(max)+abs(min))
    difference.append(abs(max) + abs(min))

angles = [0,5,10,15,20,25,30,35,40,45,50,85,90]
difference = np.array(difference)
difference  = difference / 3.91
voltage = np.array(voltage)

plt.figure()
plt.plot(angles,difference,'.-')
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity (V/W)')
plt.grid(True)
plt.savefig('FLvsAngle.pdf')
plt.show()


