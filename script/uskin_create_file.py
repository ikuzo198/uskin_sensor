#!/usr/bin/python
# -*- coding: utf-8 -*-
 

import numpy as np
import rospy
import pickle

from uskin_sensor_msgs.msg import UskinSensorValue
from uskin_sensor_msgs.msg import UskinSensorValueArray


count = 0
time_steps = 200
sensor_nums = 16
data_list = [[[] for sensor_num in range(sensor_nums)] for time_step in range(time_steps)]


def preprocess(raw_data):
    """センサデータのリスト格納を行う
    list形式で保存される
    
    Parameters:
        raw_data (list): 長さ16のリスト形式センサ値
        time_step (int): 取得するタイムステップ

    Returns:
        preprocessed_data (ndarray): 整形したデータ
    """
    global sensor_nums
    global data_list
    global count
    

    for sensor_num in range(sensor_nums):
        data_list[count][sensor_num] = raw_data[sensor_num].x, raw_data[sensor_num].y, raw_data[sensor_num].z

    count += 1
    return np.array(data_list)


def output_file(raw_data, output_file_path="./", output_file_name="output", extension=".pkl"):
    """ファイルに書き出す

    Args:
        raw_data (float): 書き出すファイル
        output_file_path (string): 書き出すファイルのパス
        output_file_name (string): 書き出すファイル名
        extension (string): 書き出す拡張子名
        
    """
    print("file name:")
    output_file_name = input()
    raw_input(">>")
    
    output_name = output_file_path + output_file_name + extension
    
    with open(output_name, 'wb') as f:
        pickle.dump(raw_data, f)

    print("==FIN DUMP==")
    
    raw_input(">>")


def callback(data):
    global count
    preprocess_raw_data = preprocess(data.data)

    print(count)
    if count == time_steps:
        output_file(raw_data=preprocess_raw_data, output_file_path="./src/uskin_sensor_pkgs/uskin_sensor_pkg/pkl/")


def listener():
    rospy.init_node('listerner', anonymous=True)
    rospy.Subscriber('/uskin_sensor_node/sensor_data', UskinSensorValueArray, callback)
    rospy.spin()
    

if __name__ == '__main__':
    raw_input("PLEASE ENTER >>")
    listener()