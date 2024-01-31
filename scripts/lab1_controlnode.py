#!/usr/bin/env python3
#1. subscribe to topic for position of turtle 
#2. 

import rospy
from turtlesim.msg import Pose
from robotics_lab1.msg import Turtlecontrol
import math 

ROTATION_SCALE = 180.0/math.pi 
pos_msg = Pose()
def pose_callback(data):
	global pos_msg
	pos_msg.x = data.x
	pos_msg.y = data.y
	pos_msg.theta = data.theta * ROTATION_SCALE


turtle_control_msg = Turtlecontrol()
def control_callback(data):
	global turtle_control_msg
	turtle_control_msg.kp =
	turtle_control_msg.xd = 


if __name__ == '__main__': 
	rospy.init_node('robotics_lab1', anonymous = True)
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	pose_pub = rospy.Publisher('/turtle1/control_params', Turtlecontrol, queue_size = 10)
	rospy.Subscriber('turtle1/control_params;', Turtlecontrol, control_callback)
	loop_rate = rospy.Rate(10)
	vel_cmd = Twist()
	while not rospy.is_shutdown():
		loop_rate.sleep()
		
