#!/usr/bin/env python3
#1. subscribe to topic for position of turtle 
#2. 

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math 

x_pos = 0
y_pos = 0
def pose_callback(data):
	x_pos = data.x
	y_pos = data.y
	print(data.x, data.y)


if __name__ == '__main__': 
	rospy.init_node('robotics_lab1', anonymous = True)
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	loop_rate = rospy.Rate(10)
	vel_cmd = Twist()
	while not rospy.is_shutdown():
		loop_rate.sleep()
		
