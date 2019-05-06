import numpy as np
import matplotlib.pyplot as plt

#rep 700, current = .12, with compensation coils
dvr = [41.6,41.6,41.6,41.6,41.6,41.6,41.6,42.4,42.4,41.2,41.6,41.6,41.6]
dvr = np.array(dvr)
powerr = 1.63

effr = dvr/powerr
reperr = [abs(effr[i]) * np.sqrt((.5/dvr[i])**2 + (.03/powerr)**2) for i in range(0,len(effr))]

# cont
dvc = [82.4,82.4,82.4,85.6,85.6,86.4,86.4,92.8,94.4,94.4,95.2,95.2,96,96]
dvc = np.array(dvc)
powerc = 3.87

effc = dvc / powerc
conerr = [abs(effc[i]) * np.sqrt((.5/dvc[i])**2 + (.03/powerc)**2) for i in range(0,len(effc))]

angler = [90,85,80,45,40,35,30,25,20,15,10,5,0]
anglec = [90,85,80,75,45,40,35,30,25,20,15,10,5,0]

plt.figure()
plt.errorbar(anglec, effc, yerr = conerr,label= 'Continuous')
plt.errorbar(angler, effr,yerr = reperr, label = '700 kHz Rep. Rate')
plt.xlabel('Angle between Beam and Magnetic Field (degrees)')
plt.ylabel('Intensity / Power (dV/W)')
plt.grid(True)
plt.legend()
plt.savefig('FLvsAngle_3.pdf')
plt.show()
