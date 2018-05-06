from mpl_toolkits.mplot3d import Axes3D
from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10.001, 1.0)
y1 = 3*x - 2
y2 = 3*x + 10
fig, ax = plt.subplots()
#ax = fig.gca()
# ax.set_xticks(np.arange(-4, 5, 1))
# ax.set_yticks(np.arange(-81,36 ,1))

lines = plt.plot(x, y1, x, y2, antialiased=True)
l1, l2 = lines
plt.setp(l1, linewidth=2, color='r', linestyle='-')
plt.setp(l2, linewidth=2, color='b', linestyle='-')

plt.xlabel('x')
#plt.ylabel('f(x) = ')
plt.annotate('$y_1$ = $3x-2$', xy=(5,13 ), xytext=(7, 13),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.annotate('$y_2$ = ??', xy=(5,25), xytext=(7,25),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

#plt.setp(lines, color='r', linewidth=2.0)
#plt.plot(x, y,'k' ,y1, 'k')
plt.grid()
plt.show()

"""
circle = plt.Circle((0,0), 1, fill=False)

fig, ax = plt.subplots()

ax.add_artist(circle)

plt.ylim(-1, 1)
plt.xlim(-1, 1)

plt.grid()

plt.show()

points = np.array([[0,0,0],
                  # [0,0,1],
                   [0,1,0],
                   [1,0,0],
                   [1,1,0]])
                   #[1,0,1],
                   #[0,1,1],
                   #[1,1,1]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
r = [0,1]

X, Y = np.meshgrid(r, r)

#ax.plot_surface(X,Y,1, alpha=0.5)
ax.plot_surface(X,Y,0, alpha=0.5)
#ax.plot_surface(X,0,Y, alpha=0.5)
#ax.plot_surface(X,1,Y, alpha=0.5)
#ax.plot_surface(1,X,Y, alpha=0.5)
#ax.plot_surface(0,X,Y, alpha=0.5)

ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()"""
