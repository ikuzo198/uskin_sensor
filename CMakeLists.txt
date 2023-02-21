cmake_minimum_required(VERSION 3.0.2)
project(uskin_sensor)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  std_srvs
  message_generation
)

add_service_files(
  FILES
  UskinSensorReset.srv
)


add_message_files(
  FILES
  UskinSensorValue.msg
  UskinSensorValueArray.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  std_srvs
)

catkin_package(
#  INCLUDE_DIRS include
 LIBRARIES uskin_sensor
 CATKIN_DEPENDS roscpp rospy std_msgs
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
