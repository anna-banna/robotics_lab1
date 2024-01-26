#!/usr/bin/env python3
#1. subscribe to topic for position of turtle 
#2. 

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from robotics_lab1.msg import Turtlecontrol
import math 

turtle_control_msg = Turtlecontrol()

def pose_callback(data):
	global turtle_control_msg
	turtle_control_msg.kp =
	turtle_control_msg.xd = 


if __name__ == '__main__': 
	rospy.init_node('robotics_lab1', anonymous = True)
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	loop_rate = rospy.Rate(10)
	vel_cmd = Twist()
	while not rospy.is_shutdown():
		loop_rate.sleep()
		
