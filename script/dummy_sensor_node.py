#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import random
import numpy as np
from uskin_sensor.msg import UskinSensorValue, UskinSensorValueArray

if __name__ == "__main__":
    rospy.init_node("dummy_sensor_node")
    rate = rospy.Rate(10)
    pub = rospy.Publisher("/dummy_sensor", UskinSensorValueArray)
    while not rospy.is_shutdown():
        pub_array = UskinSensorValueArray()
        pub_array.header.stamp = rospy.Time.now()
        for _ in range(16):
            dummy_value = UskinSensorValue(random.randint(1,100), random.randint(1,100), random.randint(1,100))
            pub_array.data.append(dummy_value)
        pub.publish(pub_array)
        rate.sleep()