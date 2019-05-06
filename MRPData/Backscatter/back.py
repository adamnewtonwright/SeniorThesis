import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd

cont90 = 234
cont0 =  286
powerc = 3.4

rep90 = 106 
rep0 = 108
powerr = 1.7

plt.figure()
plt.plot([0,90],[cont0/powerc,cont90/powerc],'--.',markersize = 15,label = 'Continuous')
plt.plot([0,90],[rep0/powerr,rep90/powerr],'--.',markersize = 15,label = 'Rep Rate 700 kHz')
plt.xlabel('Angle (degrees)', fontsize = 16)
plt.ylabel('Backscatter Return (dV/W)', fontsize = 16)
plt.grid(True)
plt.legend()
plt.savefig('backscatter.pdf')
plt.show()

##################################################
# scaled
##################################################

plt.figure()
plt.plot([0,90],[cont0/powerc * (powerc/cont0),cont90/powerc * (powerc/cont0)],'--.',markersize = 15,label = 'Continuous')
plt.plot([0,90],[rep0/powerr * (powerr/rep0),rep90/powerr * (powerr/rep0)],'--.',markersize = 15,label = 'Rep Rate 700 kHz')
plt.xlabel('Angle (degrees)', fontsize = 16)
plt.ylabel('Backscatter Return Percentage', fontsize = 16)
plt.grid(True)
plt.legend()
plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
plt.savefig('backscatterScaled.pdf')
plt.show()
