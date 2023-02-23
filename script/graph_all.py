#!/usr/bin/python
# -*- coding: utf-8 -*-

 
from __future__ import print_function
from curses import raw
from traceback import print_list
import numpy as np
import pickle, os
import matplotlib.pyplot as plt

PATH = "/root/ros_ws/hsr_environments/src/uskin_sensor/data//Tactile/"
sensor_point = 0

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


def spread_graph(axis_set=0,name="0"):
    row = 0
    culum = 0
    sensor_points = 16
    filename = name + ".pkl"
    axis = ["x", "y", "z"]
    axis_num = axis_set

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
        # axes[row, culum].set_ylim(-15,50)
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
    for num in range(3):
    # num = 2
        name = str(11)

        spread_graph(num, name)
        
        axis_list = ["x", "y", "z"]
        axis = axis_list[num]

        # 凡例の表示woodblock
        # plt.legend()

        # プロット表示(設定の反映)
        # rosrun tam_hsr_utils get_joint_states_node.py
        plt.savefig(f'{PATH}{name}_{axis}.jpg')
