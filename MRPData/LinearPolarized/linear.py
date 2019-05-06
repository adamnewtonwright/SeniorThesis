import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd

angles = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]

dvr = [44.8,44.8,45.0,45.4,45.6,45.6,45.8,45.6,45.6,45.8,46.0,46.2,46.2,46.4]
powerr = 1.7 
dvr = np.array(dvr)
effr = dvr/powerr
effrerror = [abs(effr[i]) * np.sqrt((.1/dvr[i])**2 + (.05/powerr)**2) for i in range(0,len(effr))]


dvc = [88.3,88.5,88.6,88.8,89.2,89.4,89.8,91.0,91.2,91.6,92.0,92.6,93.0,93.6]
powerc = 3.7
dvc = np.array(dvc)
effc = dvc/powerc
effcerror = [abs(effc[i]) * np.sqrt((.1/dvc[i])**2 + (.05/powerc)**2) for i in range(0,len(effc))]

plt.figure()
plt.errorbar(angles,effr,yerr = effrerror,label = 'Rep Rate 700 kHz')
plt.errorbar(angles,effc,yerr = effcerror,label = 'Continuous')
plt.xlabel('Angles (degrees)')
plt.ylabel('Return Effeciency (dv/W)')
plt.grid(True)
plt.legend()
plt.savefig('FlvsAngleLinear.pdf')
plt.show()

##################################################
# scaled
##################################################
effrscaled = effr / effr[0]
effcscaled = effc / effc[0]

effrerrorscaled = [abs(effrscaled[i]) * np.sqrt((effrerror[i]/effr[i])**2 + (effrerror[0]/effr[0])**2) for i in range(0,len(effr))]

effcerrorscaled = [abs(effcscaled[i]) * np.sqrt((effcerror[i]/effc[i])**2 + (effcerror[0]/effc[0])**2) for i in range(0,len(effc))]

plt.figure()
plt.errorbar(angles,effrscaled,yerr = effrerrorscaled,label = 'Rep Rate 700 kHz')
plt.errorbar(angles,effcscaled,yerr = effcerrorscaled,label = 'Continuous')
plt.xlabel('Angles (degrees)')
plt.ylabel('Return Effeciency (dv/W)')
plt.grid(True)
plt.legend()
plt.savefig('FlvsAngleLinearScaled.pdf')
plt.show()
