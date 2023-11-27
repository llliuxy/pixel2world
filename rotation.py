import numpy as np
import math

T = [0., 0., 1668.]

fuyang = 10.98 / 180 * math.pi
fangxiang = 42.6 / 180 * math.pi

xuanzhuan = 0.2 / 180 * np.pi

x = ([math.cos(fangxiang), -math.sin(fangxiang), 0])
z = ([math.cos(fuyang) * math.sin(fangxiang), math.cos(fuyang) * math.cos(fangxiang), -math.sin(fuyang)])

y = np.cross(z, x)

x_hat = np.array(x) * np.cos(xuanzhuan) + np.array(y) * np.sin(xuanzhuan)
z_hat = z
y_hat = np.cross(z_hat, x_hat)


ux = x_hat / np.linalg.norm(x_hat)
uy = y_hat / np.linalg.norm(y_hat)
uz = z_hat / np.linalg.norm(z_hat)

print(x_hat, y_hat, z_hat)
print(x, y, z)
print(ux, uy, uz)

m = (ux, uy, uz)
mm = np.asmatrix(m)
print(mm)

T_hat = -np.dot(mm, T)

print(T_hat)
