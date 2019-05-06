import pandas as pd
import matplotlib.pyplot as plt
from seaborn import *
import numpy as np

FLvsI = pd.read_csv("FLvsI_Rep700.csv")
FLvsREP = pd.read_csv('FLvsREP_B11.csv')
FLvsAngleCont = pd.read_csv('FlvsAngle_Continuous_B11.csv')
FLvsAngleRep = pd.read_csv('FlvsAngle_REP700_B11.csv')

FLvsAngleCont2 = pd.read_csv('FlvsAngle_Continuous_B11_2.csv')
FLvsAngleRep2 = pd.read_csv('FlvsAngle_REP700_B11_2.csv')
##################################################
# Fluorescence vs mag
##################################################
current = FLvsI['I']
power  = FLvsI['POWER']
dv  = FLvsI['DV']

eff = dv/power

reperr = [abs(eff[i]) * np.sqrt((1/dv[i])**2 + (.03/power[i])**2) for i in range(0,len(eff))]

plt.figure()
plt.errorbar(current,eff,yerr = reperr, fmt = '.')
plt.xlabel('Current (A)')
plt.ylabel('Return Efficiency (dV/W)')
plt.grid(True)
plt.savefig('EfficiencyCurr.pdf')
plt.show()


##################################################
# Fluorescence vs rep
##################################################
rep = FLvsREP['REP']
power = FLvsREP['POWER']
dv = FLvsREP['DV']

eff = dv/power
reperr = [abs(eff[i]) * np.sqrt((2/dv[i])**2 + (.03/power[i])**2) for i in range(0,len(eff))]

plt.figure()
plt.errorbar(rep,eff,yerr = reperr, fmt = '.')
plt.xlabel('Repetition Rate (kHz)')
plt.ylabel('Photon Return (Intensity/mW)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/EfficiencyRep.pdf')
plt.show()

##################################################
# Fluorescence vs angle
##################################################
angle = FLvsAngleCont['ANGLE']
powercont = FLvsAngleCont['POWER']
dvcont = FLvsAngleCont['DV']
powerrep = FLvsAngleRep['POWER']
dvrep = FLvsAngleRep['DV']

conteff = dvcont/powercont
repeff = dvrep/powerrep

yconterr = [abs(conteff[i]) * np.sqrt((2/dvcont[i])**2 + (.03/powercont[i])**2) for i in range(0,len(conteff))]
yreperr = [abs(repeff[i]) * np.sqrt((2/dvrep[i])**2 + (.03/powerrep[i])**2) for i in range(0,len(repeff))]

plt.figure()
plt.errorbar(angle,conteff,yerr = yconterr,label = 'Continuous', fmt = '.')
plt.errorbar(angle,repeff,yerr = yreperr,label = '700 kHz rep. rate', fmt = '.')
plt.xlabel('Angle (degrees)')
plt.ylabel('Photon Return (Intensity/mW)')
plt.grid(True)
plt.legend()
plt.savefig('../Thesis/FullPaper/Images/FluorescencevAngle.pdf')
plt.show()


##################################################
# Fluorescence vs angle
##################################################
angle2 = FLvsAngleCont2['ANGLE']
powercont2 = FLvsAngleCont2['POWER']
dvcont2 = FLvsAngleCont2['DV']
powerrep2 = FLvsAngleRep2['POWER']
dvrep2 = FLvsAngleRep2['DV']

conteff2 = dvcont2/4.05
repeff2 = dvrep2/1.67

yconterr2 = [abs(conteff2[i]) * np.sqrt((2/dvcont2[i])**2 + (.03/powercont2[i])**2) for i in range(0,len(conteff2))]
yreperr2 = [abs(repeff2[i]) * np.sqrt((2/dvrep2[i])**2 + (.03/powerrep2[i])**2) for i in range(0,len(repeff2))]

plt.figure()
plt.errorbar(angle2,conteff2, yerr = yconterr2,label = 'Continuous', fmt = '.')
plt.errorbar(angle,repeff2,yerr = yreperr2,label = '700 kHz rep. rate', fmt = '.')
plt.xlabel('Angle (degrees)')
plt.ylabel('Photon Return (Intensity/mW)')
plt.grid(True)
plt.legend()
plt.savefig('FluorescencevAngle2.pdf')
plt.show()
