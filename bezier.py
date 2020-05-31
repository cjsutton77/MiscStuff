import numpy as np
import matplotlib.pyplot as plt

#
# B(n,t) = sum from i=0 to n (Binomial (n,i) * (1-t) ** (n-i) * t ** i * Pi
#

def quad_bezier(p0,p1,p2,t):
    return p0 * (1 - t) ** 2 + 2 * (1 - t) * t * p1 + p2 * t ** 2

def cubic_bezier(p0,p1,p2,p3,t):
    return p0 * (1 - t) ** 3 + 3 * (1 - t) * t * p1 + 3 * p2 * (1 - t)* t ** 2 + p3 * t ** 3

def fourth_bezier(p0,p1,p2,p3,p4,t):
    return p0*(1-t)**4 + 4*p1*t*(1-t)**3+6*p2*(t-t**2)**2+4*p3*(1-t)*t**3+p4*t**4

xc = (0,  .8, 0.25, .4, .6)
yc = (0, .2,   .5, .3, .6)

x2 = quad_bezier(xc[0],xc[1],xc[2],np.arange(0,1,0.01))
y2 = quad_bezier(yc[0],yc[1],yc[2],np.arange(0,1,0.01))
x3 = cubic_bezier(xc[0],xc[1],xc[2],xc[3],np.arange(0,1,0.01))
y3 = cubic_bezier(yc[0],yc[1],yc[2],yc[3],np.arange(0,1,0.01))
x4 = fourth_bezier(xc[0],xc[1],xc[2],xc[3],xc[4],np.arange(0,1,0.01))
y4 = fourth_bezier(yc[0],yc[1],yc[2],yc[3],yc[4],np.arange(0,1,0.01))
plt.scatter(xc, yc, c='red', s=5)
plt.scatter(x2, y2, c='blue',s=1)
plt.scatter(x3, y3, c='green',s=1)
plt.scatter(x4, y4, c='gray',s=1)
plt.show()
