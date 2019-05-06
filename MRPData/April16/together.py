import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd



##################################################
# circular light
##################################################

#rep 700 kHz, current = .12, with compensation coils
dvr = [26.8,26.8,26.8,26.6,26.6,26.2,26.4,26.2,26.4,26.2,26.2,26.2,26.2,26.0]
dvr = np.array(dvr)
powerr = 1.7

effr = dvr/powerr
reperr = [abs(effr[i]) * np.sqrt((.2/dvr[i])**2 + (.03/powerr)**2) for i in range(0,len(effr))]

# continuous light
dvc = [27.4,27.2,27.0,26.6,26.2,25.8,25.4,24.8,24.4,24.0,23.0,22.4,22.0,22.0]
dvc = np.array(dvc)
powerc = 1.7

effc = dvc / powerc
conerr = [abs(effc[i]) * np.sqrt((.2/dvc[i])**2 + (.03/powerc)**2) for i in range(0,len(effc))]

angler = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]
anglec = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]

plt.figure()
plt.errorbar(anglec, effc, yerr = conerr,label= 'Continuous Circular', fmt = '.')
plt.errorbar(angler, effr,yerr = reperr, label = '700 kHz Circular', fmt = '.')

##################################################
# linear light
##################################################

angles = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]

# Rep 700 kHz
dvr = [24.2,24.2,24.2,24.4,24.4,24.6,24.4,24.6,24.8,24.8,25.0,24.8,24.8,24.8]
powerr = 1.7
dvr = np.array(dvr)
effr = dvr/powerr
effrerror = [abs(effr[i]) * np.sqrt((.1/dvr[i])**2 + (.05/powerr)**2) for i in range(0,len(effr))]


# Continuous Light
dvc = [23.6,23.6,23.8,23.8,23.8,23.8,23.8,23.8,24.0,23.8,23.8,24.0,24.0,24.0]
powerc = 1.7
dvc = np.array(dvc)
effc = dvc/powerc
effcerror = [abs(effc[i]) * np.sqrt((.1/dvc[i])**2 + (.05/powerc)**2) for i in range(0,len(effc))]

plt.errorbar(angles,effr,yerr = effrerror,label = '700 kHz Linear', fmt = '.')
plt.errorbar(angles,effc,yerr = effcerror,label = 'Continuous Linear', fmt = '.')


plt.xlabel('Angle (degrees)')
plt.ylabel('Return Efficiency (dv/W)')
plt.grid(True)
plt.legend()
plt.savefig('together.pdf')
plt.show()



##################################################
# Scale everything to first dv/W of rep circular
##################################################
##################################################
# circular
##################################################

#scale factor = 26.8/1.7
scf = 26.8/1.7

#osc averaging 4 frames
#rep 700, current = .12, with compensation coils
dvr = [26.8,26.8,26.8,26.6,26.6,26.2,26.4,26.2,26.4,26.2,26.2,26.2,26.2,26.0]
dvr = np.array(dvr)
powerr = 1.7

effr = dvr/powerr
effrscaled = effr/effr[0]
reperr = [abs(effr[i]) * np.sqrt((.2/dvr[i])**2 + (.03/powerr)**2) for i in range(0,len(effr))]
reperrscaled = [abs(effrscaled[i]) * np.sqrt((reperr[i]/effr[i])**2 + (reperr[0]/effr[0])**2) for i in range(0,len(effr))]

# cont
# continuous light
dvc = [27.4,27.2,27.0,26.6,26.2,25.8,25.4,24.8,24.4,24.0,23.0,22.4,22.0,22.0]
dvc = np.array(dvc)
powerc = 1.7

effc = dvc / powerc
effcscaled = effc/effc[0]
conerr = [abs(effc[i]) * np.sqrt((.2/dvc[i])**2 + (.03/powerc)**2) for i in range(0,len(effc))]
conerrscaled = [abs(effcscaled[i]) * np.sqrt((conerr[i]/effc[i])**2 + (conerr[0]/effc[0])**2) for i in range(0,len(effc))]

angler = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]
anglec = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]

plt.figure()
plt.errorbar(anglec, effcscaled, yerr = conerrscaled,label= 'Continuous Circular', fmt = '.')
plt.errorbar(angler, effrscaled,yerr = reperrscaled, label = '700 kHz Circular', fmt = '.')

##################################################
# linear
##################################################

angles = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]

dvr = [24.2,24.2,24.2,24.4,24.4,24.6,24.4,24.6,24.8,24.8,25.0,24.8,24.8,24.8]
powerr = 1.7
dvr = np.array(dvr)
effr = dvr/powerr
effrscaled = effr/effr[0]
effrerror = [abs(effr[i]) * np.sqrt((.1/dvr[i])**2 + (.05/powerr)**2) for i in range(0,len(effr))]
reperrscaled = [abs(effrscaled[i]) * np.sqrt((effrerror[i]/effr[i])**2 + (effrerror[0]/effr[0])**2) for i in range(0,len(effr))]


# Continuous Light
dvc = [23.6,23.6,23.8,23.8,23.8,23.8,23.8,23.8,24.0,23.8,23.8,24.0,24.0,24.0]
powerc = 1.7
dvc = np.array(dvc)
effc = dvc/powerc
effcscaled = effc/effc[0]
effcerror = [abs(effc[i]) * np.sqrt((.1/dvc[i])**2 + (.05/powerc)**2) for i in range(0,len(effc))]
conerrscaled = [abs(effcscaled[i]) * np.sqrt((effcerror[i]/effc[i])**2 + (effcerror[0]/effc[0])**2) for i in range(0,len(effc))]

plt.errorbar(angles,effrscaled,yerr = reperrscaled,label = '700 kHz Linear', fmt = '.')
plt.errorbar(angles,effcscaled,yerr = conerrscaled,label = 'Continuous Linear', fmt = '.')


plt.xlabel('Angle (degrees)', fontsize = 16)
plt.ylabel('Fluorescence as Percent of Maximum', fontsize = 16)
plt.grid(True)
plt.ylim(.65,1.1)
plt.title('Low Intensity', fontsize = 18)
plt.legend()
plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
plt.savefig('togetherscaled.pdf')
plt.show()

