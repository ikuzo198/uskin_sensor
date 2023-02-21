#!/usr/bin/python
# -*- coding: utf-8 -*-



import numpy as np
import rospy, smach
import pickle

from uskin_sensor_msgs.msg import UskinSensorValue
from uskin_sensor_msgs.msg import UskinSensorValueArray

from pymycobot.mycobot import MyCobot

import uskin_create_file

mycobot = MyCobot("/dev/ttyUSB0")

class State1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done','exit'])
        self.counter = 0


    def execute(self, userdata):
        rospy.loginfo('Init')
        # rospy.sleep(2.0)
        mycobot.set_gripper_ini()
        
        return "done"
        


class State2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])


    def execute(self, userdata):
        rospy.loginfo('Grasp_REC')
        rospy.sleep(2.0)
        uskin_create_file
        
        return 'done'


def main():
    rospy.init_node('smach_somple1')

    sm_top = smach.StateMachine(outcomes=['succeeded'])
    with sm_top:
        smach.StateMachine.add('STATE1', State1(), transitions={'done':'STATE2', 'exit':'succeeded'})
        smach.StateMachine.add('STATE2', State2(), transitions={'done':'STATE1'})

    outcome = sm_top.execute()


if __name__ == '__main__':
    main()