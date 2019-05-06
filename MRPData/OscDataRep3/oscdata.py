import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

difference = []
for j in range(1,18):
    if j <10:
        data = pd.read_csv('TEK000'+str(j)+'.CSV',names = ['time','voltage','that'])
        voltage = data['voltage']
        max = np.max(voltage)
        min = np.min(voltage)
    elif j >=10:
        data = pd.read_csv('TEK00'+str(j)+'.CSV',names = ['time','voltage','that'])
        voltage = data['voltage']
        max = np.max(voltage)
        min = np.min(voltage)
        for i in voltage:
            if i >= max:
                max =i
            if i<= min:
                min = i
    print(max, min, abs(max)+abs(min))
    difference.append(abs(max) + abs(min))

angles = np.arange(0,90,90/len(difference))
difference = np.array(difference)
difference  = difference / 3.91

plt.figure()
plt.plot(angles,difference,'.-')
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity (V/W)')
plt.grid(True)
plt.savefig('FLvsAngle.pdf')
plt.show()

