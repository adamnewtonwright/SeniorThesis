import numpy as np
import matplotlib.pyplot as plt

##################################################
# fluorescence versus angle
##################################################

#osc averaging 4 frames
#rep 700, current = .12, with compensation coils
dvr = [52,52,52,52.8,52.8,53.6,53.6,53.6,53.6,53.6,53.6,53.8,53.6]
dvr = np.array(dvr)
powerr = 1.78

effr = dvr/powerr
reperr = [abs(effr[i]) * np.sqrt((.2/dvr[i])**2 + (.03/powerr)**2) for i in range(0,len(effr))]

# cont
dvc = [56.8,56.8,56.8,65.6,67.2,71.2,73.6,76,78.4,81.6,82.4,83.2,84]
dvc = np.array(dvc)
powerc = 4.1

effc = dvc / powerc
conerr = [abs(effc[i]) * np.sqrt((.2/dvc[i])**2 + (.03/powerc)**2) for i in range(0,len(effc))]

angler = [90,85,80,45,40,35,30,25,20,15,10,5,0]
anglec = [90,85,80,45,40,35,30,25,20,15,10,5,0]

plt.figure()
plt.errorbar(anglec, effc, yerr = conerr,label= 'Continuous', fmt = '.')
plt.errorbar(angler, effr,yerr = reperr, label = '700 kHz Rep. Rate', fmt = '.')
plt.xlabel('Angle between Beam and Magnetic Field (degrees)')
plt.ylabel('Return Efficiency (dV/W)')
plt.grid(True)
plt.legend()
plt.savefig('FLvsAngle_4.pdf')
plt.show()

##################################################
# scaled data
##################################################
effcperc = effc / effc[-1]
effrperc = effr / effr[-1]
plt.figure()
plt.plot(anglec,effcperc,label = 'Continuous')
plt.plot(angler,effrperc,label = 'Rep Rate 700 kHz')
plt.xlabel('Angle (degrees)')
plt.ylabel('Fluorescence as Percent of Maximum')
plt.grid(True)
plt.legend()
plt.savefig('FLvsAngleScaled.pdf')
plt.show()


##################################################
# fluorescence versus rep rate
##################################################
dvrep = [38.4,38.6,39.2,40,40,40,40,39.2,39.6,41.6,43.2,42.4,40.4,40.2,39.8,39.2,37.8,37.2,37,36.4,36,35.2,35.2]
power = 1.8

dvrep = np.array(dvrep)

effrep = dvrep/power

reps = np.arange(500,960,20)
reperr = [abs(effrep[i]) * np.sqrt((1/dvrep[i])**2 + (.03/power)**2 + (.1/reps[i])**2) for i in range(0,len(effrep))]


plt.figure()
plt.errorbar(reps,effrep,yerr = reperr,fmt = '.')
plt.xlabel('Repetition Rate (kHz)')
plt.ylabel('Return Efficiency (dv/W)')
plt.grid(True)
plt.savefig('FLvRep.pdf')
plt.show()


