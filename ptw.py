#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#图像像素坐标转世界坐标

import numpy as np
import cv2

camera_parameter = {
    # R
    "R": [[ 0.74367491, -0.66805195,  0.02557765],
 [-0.10296212, -0.15225202, -0.98296395],
 [ 0.66056523,  0.7283721,  -0.18201006]],
    # T
    "T": [ -79.2469824, 1659.1209261, 374.38888501],
    # f/dx, f/dy
    "f": [1949.7414472702515, 1969.9895476198383],
    # center point
    "c": [988.7776800847297, 549.0166325124756]
}


def pixel_to_world(camera_intrinsics, r, t, img_points):

    K_inv = camera_intrinsics.I
    R_inv = np.asmatrix(r).I
    R_inv_T = np.dot(R_inv, np.asmatrix(t))
    world_points = []
    coords = np.zeros((3, 1), dtype=np.float64)
    for img_point in img_points:
        coords[0] = img_point[0]
        coords[1] = img_point[1]
        coords[2] = 1.0
        cam_point = np.dot(K_inv, coords)
        cam_R_inv = np.dot(R_inv, cam_point)
        scale = R_inv_T[2][0] / cam_R_inv[2][0]
        scale_world = np.multiply(scale, cam_R_inv)
        world_point = np.asmatrix(scale_world) - np.asmatrix(R_inv_T)
        pt = np.zeros((3, 1), dtype=np.float64)
        pt[0] = world_point[0]
        pt[1] = world_point[1]
        print(world_point[2])
        print("###")
        pt[2] = 0
        world_points.append(pt.T.tolist())

    return world_points


if __name__ == '__main__':
    f = camera_parameter["f"]
    c = camera_parameter["c"]
    camera_intrinsic = np.mat(np.zeros((3, 3), dtype=np.float64))
    camera_intrinsic[0, 0] = f[0]
    camera_intrinsic[1, 1] = f[1]
    camera_intrinsic[0, 2] = c[0]
    camera_intrinsic[1, 2] = c[1]
    camera_intrinsic[2, 2] = np.float64(1)
    r = camera_parameter["R"]
    t = np.asmatrix(camera_parameter["T"]).T
    # img_points = [[100, 200],
    #               [150, 300]]
    img_points = np.array(([177, 846], [1073, 556], [1065, 672]), dtype=np.double)
    result = pixel_to_world(camera_intrinsic, r, t, img_points)
    print(result)
    print('----')

    #axis = np.float32([[7700, 73407, 0], [-66029, -605036, 0]])
    #r2 = np.asmatrix(camera_parameter["R"])
    #result2, _ = cv2.projectPoints(axis, r2, t, camera_intrinsic, 0)
    #print(result2)