import geometry, procrustes, frechetdist, similarity, icp
from geometry import *
from procrustes import *
from frechetdist import *
from similarity import *
from icp import *

import numpy as np 
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 3, num=20)
y_1 = -2*x**2 + 2*x
y_2 = -2*x**2 + 2*x + 1
y_3 = -2*x**2 + 2*x + 2

z_1 = -2*x**2 + 2*x + 8
z_2 = -2*x**2 + 2*x + 9
z_3 = -2*x**2 + 2*x + 10

poly1 = np.column_stack((x,y_1))
poly2 = np.column_stack((x,y_2))
poly3 = np.column_stack((x,y_3))
poly4 = np.column_stack((x,z_1))
poly5 = np.column_stack((x,z_2))
poly6 = np.column_stack((x,z_3))

traj = np.vstack((poly1, poly2, poly3))
ref = np.vstack((poly4, poly5, poly6))

#poly1 = np.column_stack((x,y_1))
#poly2 = np.column_stack((x,y_2))
similarity = curve_similarity(traj, ref, checkRotation=True, rotate=5)
#T,dist,itera = icp_processing(poly1, poly2, initPose=None, maxIter=50, tol=1e-6)
#poly3 = np.dot(poly1, T[0:2,0:2]) + T[0:2,2]
#print(similarity)

'''
plot output
'''
fig, ax = plt.subplots()
ax.plot(poly1[:,0], poly1[:,1], 'r-*')
ax.plot(poly2[:,0], poly2[:,1], 'r-*')
ax.plot(poly3[:,0], poly3[:,1], 'r-*')
ax.plot(poly4[:,0], poly4[:,1], 'b-*')
ax.plot(poly5[:,0], poly5[:,1], 'b-*')
ax.plot(poly6[:,0], poly6[:,1], 'b-*')

#ax.plot(x, y_3, 'b', label='reference')
# ax.plot(poly3[:,0], poly3[:,1], 'g*', label='matching')
plt.title('The similarity level is:' + str(similarity))
#legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.savefig('output/matching3.jpg')
plt.show()
