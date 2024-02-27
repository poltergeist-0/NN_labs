import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-8, 8, 100)
plt.xlabel('u1', fontsize=16)
plt.ylabel('u2', fontsize=16)
plt.plot(x,(-2*x-3),"black",label='original functions')
plt.plot(x,(x+5),"black")

u1_training = np.array([3, 3, 2, -6, 7, 7, 1, -1, 4, 5, -3, 7, 1, 8, -1, -8, 0, -5, -6, 4, -6, -3, -1, -5] )
u2_training = np.array( [6, -4, 6, -1, -4, -2, 3, 3, 1, -8, 8, 8, 8, 4, -2, 4, -1, -8, 1, -2, 8, -3, 5, 3])
plt.plot(u1_training,u2_training,"ok",markersize = 3,label='training data')

plt.plot(x,((15*x+8)/(-6)),"grey")
plt.plot(x,((-5*x-26)/(-4)),"grey",label='output functions')

u1_wrong_testing = np.array([-3])
u2_wrong_testing = np.array([5])
plt.plot(u1_wrong_testing,u2_wrong_testing,"+r",markersize = 13,label='incorrect test results')

u1_right_testing = np.array([-3, -5, -4, -3, 3])
u2_right_testing = np.array([7, 3, 3, -6, -5])
plt.plot(u1_right_testing,u2_right_testing,"+g",markersize = 13,label='correct test results')

plt.legend(fontsize=10)
plt.show()
