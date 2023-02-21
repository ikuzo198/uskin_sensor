#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import sys
import os
import rospy
import roslib
import rosparam
import serial

from uskin_sensor.msg import UskinSensorValue
from uskin_sensor.msg import UskinSensorValueArray
from uskin_sensor.srv import UskinSensorReset

#==================================================

# グローバル

#==================================================
GP_LOOP_RATE = 30.0

class UskinSensor(object):
    #==================================================
    
    ## @fn コンストラクタ
    ## @brief
    ## @param
    ## @return

    #==================================================
    def __init__(self):

        #==================================================

        ## rosparam

        #==================================================
        self.node_name = rospy.get_name()
        self.port = rosparam.get_param( self.node_name + "/port")
        # self.port = "/dev/ttyACM0"


        #==================================================

        ## メンバ変数

        #==================================================
        self._ros_rate = rospy.Rate(GP_LOOP_RATE)
        # port には事前に権限を変更しておくこと"
        self._uskin_sensor_serial = serial.Serial(self.port, 921600)

        self.get_sensor_val()
        self._base_sensor_val = self._sensor_value

        #==================================================

        # ROSインタフェース

        #==================================================
        self._pub = rospy.Publisher(
            rospy.get_name() + "/sensor_data",
            UskinSensorValueArray,
            queue_size=1
        )

        self._sensor_reset_srv_ = rospy.Service(
            "sensor_reset_srv",
            UskinSensorReset,
            self.sensor_reset
        )
        
    def sensor_reset(self, req):
        rospy.loginfo("Reset sensor value")
        rospy.sleep(0.3)

        while not rospy.is_shutdown():
            sensor_value = self._sensor_value
            if (len(sensor_value)==48):
                break
        
        self._base_sensor_val = sensor_value
        return True

    def get_sensor_val(self):
        get_result = False
        while not(get_result) and not(rospy.is_shutdown()):
            # データ読み取り
            sensor_value = self._uskin_sensor_serial.readline()

            sensor_value = sensor_value.decode()


            # 不要な要素の削除
            sensor_value = sensor_value.strip("\rA")
            sensor_value = sensor_value.strip("B\n")

            # センサデータのリスト化
            sensor_value = sensor_value.split(",")

            if (len(sensor_value)==48):
                get_result = True

            else:
                # rospy.logwarn("uskin sensor don't work. Please check the sensor")
                rospy.loginfo("Please check `rostopic echo /uskin_sensor_node/sensor_data`")


        self._sensor_value = sensor_value
        
    def __call__(self):
        # センサデータのリスト化
        self.get_sensor_val()
        sensor_value = self._sensor_value
        

        if(not( len(sensor_value)==48)):
            rospy.logwarn("uskin sensor don't work. Please check the sensor")

        else:
            msg = UskinSensorValueArray()
            # raw_input(">>")
            for i in range( 16 ):
                a_sensor_value = UskinSensorValue()
                a_sensor_value.x = int(sensor_value[i * 3]) - int(self._base_sensor_val[i * 3])
                a_sensor_value.y = int(sensor_value[i * 3 + 1]) - int(self._base_sensor_val[i * 3 + 1])
                a_sensor_value.z = int(sensor_value[i * 3 + 2]) - int(self._base_sensor_val[i * 3 + 2])
                msg.data.append(a_sensor_value)
                # print("msg:", msg)
                print(a_sensor_value)
            self._pub.publish(msg)
            self._ros_rate.sleep()


if __name__=='__main__':
    rospy.init_node(os.path.basename(__file__).split(".")[0])

    test = UskinSensor()
    while not rospy.is_shutdown():
        test()