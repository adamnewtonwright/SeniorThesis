import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

difference = []
for j in range(14,28):
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

angles = [0,5,10,15,20,25,30,35,40,45,50,75,85,90]
difference = np.array(difference)
difference  = difference / 3.91

plt.figure()
plt.plot(angles,difference,'.-')
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity (V/W)')
plt.grid(True)
plt.savefig('FLvsAngle.pdf')
plt.show()

