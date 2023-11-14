import numpy
import numpy as np
import math

fuyang = 10.98 / 180 * math.pi
fangxiang = 42.6 / 180 * math.pi

x = ([math.cos(fangxiang), -math.sin(fangxiang), 0])
z = ([math.cos(fuyang) * math.sin(fangxiang), math.cos(fuyang) * math.cos(fangxiang), -math.sin(fuyang)])

y = np.cross(z, x)

ux = x / np.linalg.norm(x)
uy = y / np.linalg.norm(y)
uz = z / np.linalg.norm(z)

print(x, y, z)
print(ux, uy, uz)

m = (ux, uy, uz)
mm = np.asmatrix(m)
print(mm)