#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def publisher():
    pub = rospy.Publisher('topic_name', Int32, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz
    i = 0
    while not rospy.is_shutdown():
        pub.publish(i)
        i += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
