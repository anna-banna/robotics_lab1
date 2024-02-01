#!/usr/bin/env python3

import rospy
#import messages that need to be used 
from turtlesim.msg import Pose
from robotics_lab1.msg import Turtlecontrol
from geometry_msgs.msg import Twist 

#create a variable with an instance of the Pose message type 
pos_msg = Pose()
def pose_callback(data):
	global pos_msg
	#store the x position data 
	pos_msg.x = data.x

#create a variable with an instance of the Turtlecontrol message type 
turtle_control_msg = Turtlecontrol()
def control_callback(data):
	global turtle_control_msg
	#store kp and xd data
	turtle_control_msg.kp = data.kp
	turtle_control_msg.xd = data.xd


if __name__ == '__main__': 
	#initialize the node 
	rospy.init_node('robotics_lab1', anonymous = True)
	
	#add a subscriber to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	#add a publisher with a new topic using the Twist message 
	pose_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	#add a subscriber to read the Turtlecontrol information 
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, control_callback)
	
	#set a 10Hz frequency for the loop
	loop_rate = rospy.Rate(10)
	# ??????????????????
	vel_cmd = Twist()
	
	while not rospy.is_shutdown():
		#set the linear velocity 
		vel_cmd.linear.x = turtle_control_msg.kp*(turtle_control_msg.xd - pos_msg.x)
		
		#publish the message
		pose_pub.publish(vel_cmd)
		#wait 0.1sec until the next loop and repeat 
		loop_rate.sleep()
		
