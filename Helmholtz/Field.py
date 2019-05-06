import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd

##################################################
# half amp
##################################################
axialhalf = pd.read_csv("FieldAxialMiddlehalfamp.csv")
radialhalf = pd.read_csv("FieldRadialMiddlehalfamp.csv")

##################################################
# one amp
##################################################
axialone = pd.read_csv("FieldAxialMiddle1amp.csv")
radialone = pd.read_csv("FieldRadialMiddle1amp.csv")

##################################################
# Field vs current
##################################################
fieldvcurrent = pd.read_csv('FieldvsCurrent.csv')

one = [1 for i in axialhalf['position (cm)']]
plt.figure()
lineup, = plt.plot(axialhalf['position (cm)'],axialhalf['mag. field (gauss)'],'.',label = "0.5 A")
linedown, = plt.plot(axialone['position (cm)'],axialone['mag. field (gauss)'],'.',label = '1 A')
plt.axvline(x=1.5)
plt.axvline(x=11.5)
plt.xlabel('Axial Distance (cm)', fontsize = 16)
plt.ylabel('Magnetic Field (Gauss)', fontsize = 16)
plt.ylim(5,16)
plt.xlim(0,15)
plt.legend(handles=[lineup, linedown],bbox_to_anchor=(.8, .15))
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/FieldAxial.pdf')
plt.show()
plt.close()


plt.figure()
lineup, = plt.plot(radialhalf['position (cm)'],radialhalf['mag. field (gauss)'],'.',label = "0.5 A")
linedown, = plt.plot(radialone['position (cm)'],radialone['mag. field (gauss)'],'.',label = '1 A')
plt.axvline(x=9)
plt.xlabel('Radial Distance from Center (cm)', fontsize = 16)
plt.ylabel('Magnetic Field (Gauss)', fontsize = 16)
plt.ylim(5,16)
plt.xlim(0,12)
plt.legend(handles=[lineup, linedown],bbox_to_anchor=(.8, .15))
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/FieldRadial.pdf')
plt.show()


plt.figure()
plt.plot(fieldvcurrent['current'],fieldvcurrent['field'],'.')
a,b = np.polyfit(fieldvcurrent['current'],fieldvcurrent['field'],1)
x = np.arange(np.min(fieldvcurrent['current']),np.max(fieldvcurrent['current']),.01)
plt.plot(x,b + a*x,'r')
print('slope = ',a)
print('intercept =',b)
plt.xlabel('Current (A)')
plt.ylabel('Magnetic Field (Gauss)')
plt.grid(True)
plt.savefig('../Thesis/FullPaper/Images/FieldvCurrent.pdf')
plt.show()

