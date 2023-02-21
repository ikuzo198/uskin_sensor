#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import rospy

from uskin_sensor_msgs.msg import UskinSensorValue
from uskin_sensor_msgs.msg import UskinSensorValueArray


def callback(data):
    print(data.data)
    # global count
    # preprocess_raw_data = preprocess(data.data)

    # print(count)
    # if count == time_steps:
    #     output_file(raw_data=preprocess_raw_data, output_file_path="./src/uskin_sensor_pkgs/uskin_sensor_pkg/pkl/")


def listener():
    rospy.init_node('listerner', anonymous=True)
    rospy.Subscriber(
        '/uskin_sensor_node/sensor_data',
        UskinSensorValueArray,
        callback
    )
    rospy.spin()


if __name__ == '__main__':
    # raw_input("PLEASE ENTER >>")
    listener()