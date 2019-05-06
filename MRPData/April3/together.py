import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd


##################################################
# circular
##################################################

#osc averaging 4 frames
#rep 700, current = .12, with compensation coils
dvr = [27,27]
dvr = np.array(dvr)
powerr = .65

effr = dvr/powerr
reperr = [abs(effr[i]) * np.sqrt((.2/dvr[i])**2 + (.03/powerr)**2) for i in range(0,len(effr))]

# cont
dvc = [26.2,]
dvc = np.array(dvc)
powerc = 1.25

effc = dvc / powerc
conerr = [abs(effc[i]) * np.sqrt((.2/dvc[i])**2 + (.03/powerc)**2) for i in range(0,len(effc))]

angler = [0,90]
anglec = [0,90]

plt.figure()
plt.errorbar(anglec, effc, yerr = conerr,label= 'Continuous Circular')
plt.errorbar(angler, effr,yerr = reperr, label = '700 kHz Circular')

##################################################
# linear
##################################################

angles = [0,90]

dvr = [37.6,40.0]
powerr = 1.25
dvr = np.array(dvr)
effr = dvr/powerr
effrerror = [abs(effr[i]) * np.sqrt((.1/dvr[i])**2 + (.05/powerr)**2) for i in range(0,len(effr))]


dvc = [51,53]
powerc = 1.25
dvc = np.array(dvc)
effc = dvc/powerc
effcerror = [abs(effc[i]) * np.sqrt((.1/dvc[i])**2 + (.05/powerc)**2) for i in range(0,len(effc))]

plt.errorbar(angles,effr,yerr = effrerror,label = '700 kHz Linear')
plt.errorbar(angles,effc,yerr = effcerror,label = 'Continuous Linear')


plt.xlabel('Angle (degrees)')
plt.ylabel('Return Effeciency (dv/W)')
plt.grid(True)
plt.legend()
plt.savefig('together.pdf')
plt.show()

