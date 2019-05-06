##################################################
# Filename: RvsT.py
# Objective: Plot Resistance versus temperature for BBO crystal thermistor 
##################################################

import matplotlib.pyplot as plt
import numpy as np

# Temperature in ˚C
T = [23.8,23.0,23.5,24.0,24.9,25.2,26.0,26.3,27.0,28.0,28.8,29.5,30.5,32.0,33.5,34.8,36.0,39.5,41.0,42.0,44.0,46.0]

# Current in A
I = [0.0,.10,.25,.3,.5,.6,.75,.8,1.0,1.1,1.25,1.3,1.5,1.6,1.75,1.8,2.0,2.1,2.25,2.3,2.5,2.6]

# Resistance in kΩ
R = [444.6,443.9,442.1,440.1,436.4,433.5,430.0,426.8,423.6,419.7,415.1,411.7,406.4,397.5,391.6,386.4,379.3,369.3,362.5,354.4,347.4,337.4]

# Plot Resistance versus temperaure
plt.figure()
plt.plot(T,R,'.')
plt.xlabel('Temperature (˚C)')
plt.ylabel('Resistance (kΩ)')
plt.grid(True)
plt.show()


# Plot Temperature versus current
plt.figure()
plt.plot(I,T,'.')
plt.ylabel('Temperature (˚C)')
plt.xlabel('Current (A)')
plt.grid(True)
plt.show()
