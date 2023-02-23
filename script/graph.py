#!/usr/bin/python
# -*- coding: utf-8 -*-
 

from curses import raw
import numpy as np
import pickle
import matplotlib.pyplot as plt

PATH = "/root/ros_ws/hsr_environments/src/uskin_sensor/data/Tactile/"

DATAPATH = PATH + "7.pkl"
# DATAPATH = PATH + "test00.pkl"

with open(DATAPATH, 'rb')as f:
    raw_data = pickle.load(f)

timesteps = raw_data.shape[0]
data_list = []

for timestep in range(timesteps):
    data_list.append(raw_data[timestep][1][0])
    
print("timesteps:", timesteps)


x = np.linspace(0, timesteps, timesteps)

# プロット
plt.plot(x, data_list, label="00", color="blue")

# DATAPATH = PATH + "rabit_01.pkl"
with open(DATAPATH, 'rb')as f:
    raw_data = pickle.load(f)

timesteps = raw_data.shape[0]
data_list = []

for timestep in range(timesteps):
    data_list.append(raw_data[timestep][1][0])

# プロット
plt.plot(x, data_list, label="01", color="red")

# DATAPATH = PATH + "rabit_02.pkl"
with open(DATAPATH, 'rb')as f:
    raw_data = pickle.load(f)

timesteps = raw_data.shape[0]
data_list = []

for timestep in range(timesteps):
    data_list.append(raw_data[timestep][1][0])


# プロット
plt.plot(x, data_list, label="02", color="green")


# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.savefig(f'{PATH}a.jpg')
