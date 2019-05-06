import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd

power = np.arange(1,4.5,.25)

# Change in fluorescence from 0 to 90 divided by initial
dvchange = [2.4/20.2,2.4/22.2,2.2/23.8,2.8/28.8,2.4/31,4/34.4,4.2/37.4,6/43.2,6.4/46,5.6/49.6,3.2/52,6.4/52.4,8.4/58.4,8/58.4]
dvchange = np.array(dvchange)

plt.figure()
plt.plot(power,dvchange/power)
plt.xlabel('Power (mw)')
plt.ylabel('Fluorescence Change (dv/initial)')
plt.grid(True)
plt.savefig('flchangevpower.pdf')
plt.show()

