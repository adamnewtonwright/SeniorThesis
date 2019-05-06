import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd

df = pd.read_csv("SatIntensity.csv")
dfA = pd.read_csv("SatIntensityAbs.csv")

power = df['power']
fluor = df['dv']

powerA = dfA['power']
abs = dfA['dv']

plt.figure()
plt.plot(power,fluor,'.')
#plt.title()
plt.xlabel('Power (mW)')
plt.ylabel('Fluorescence (mV)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/SatInt.png')
plt.show()

plt.figure()
plt.plot(powerA,abs,'.')
#plt.title()
plt.xlabel('Power (mW)')
plt.ylabel('Absorption (mV)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/SatIntAbs.png')
plt.show()

