#!/usr/bin/python
# -*- coding: utf-8 -*-

 
from __future__ import print_function
from curses import raw
from traceback import print_list
import numpy as np
import pickle, os
import matplotlib.pyplot as plt

PATH = "../pkl/rabit/"
sensor_point = 4

filename_list = os.listdir(PATH)
color_list = ("blue", "red", "green")


def add_graph():
    for filename in filename_list:

        with open(PATH + filename, 'rb')as f:
            raw_data = pickle.load(f)

        timesteps = raw_data.shape[0]
        data_list = []

        for timestep in range(timesteps):
            data_list.append(raw_data[timestep][sensor_point][0])
            
        print("timesteps:", timesteps)


        x = np.linspace(0, timesteps, timesteps)

        # プロット
        plt.plot(x, data_list, label=filename, color="blue")


def spread_graph():
    row = 0
    culum = 0
    sensor_points = 16
    filename = "rabit02.pkl"
    axis = ["x", "y", "z"]
    axis_num = 2

    fig, axes = plt.subplots(4,4)

    for sensor_point in range(sensor_points):

        with open(PATH + filename, 'rb')as f:
            raw_data = pickle.load(f)

        timesteps = raw_data.shape[0]
        data_list = []

        for timestep in range(timesteps):
            data_list.append(raw_data[timestep][sensor_point][axis_num])
            
        print("timesteps:", timesteps)

        x = np.linspace(0, timesteps, timesteps)

        print("row:", row)
        print("cumlu:", culum)
        # プロット
        # plt.plot(x, data_list, label=filename, color="blue")
        # plt.ylim(-100, 650)

        axes[row, culum].plot(x, data_list, label=filename+"("+axis[axis_num]+")", color="blue")
        axes[row, culum].set_ylim(-15,50)
        culum += 1

        if culum >= 4:
            culum = 0
            row += 1
            print("culum:", culum)
            continue

        else:
            continue
    print("axis:", axis[axis_num])
    print("filename:", filename)


if __name__ == "__main__":
    # add_graph()
    spread_graph()

    # 凡例の表示woodblock
    # plt.legend()

    # プロット表示(設定の反映)
    
    plt.show()
