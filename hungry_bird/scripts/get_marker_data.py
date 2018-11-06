#!/usr/bin/env python

import rospy
import roslib
import tf

from geometry_msgs.msg import PoseArray
from aruco_msgs.msg import MarkerArray


#Defining a class
class Marker_detect():

	def __init__(self):
		rospy.init_node('marker_detection',anonymous=False) # initializing a ros node with name marker_detection

		self.whycon_marker = {}	# Declaring dictionaries
		self.aruco_marker = {}

		rospy.Subscriber('/whycon/poses',PoseArray,self.whycon_data)	# Subscribing to topic
		rospy.Subscriber('/aruco_marker_publisher/markers',MarkerArray,self.aruco_data)	# Subscribing to topic
		


	# Callback for /whycon/poses
	def whycon_data(self,msg):
		temp1=[float("{0:.3f}".format(msg.poses[0].position.x)),float("{0:.3f}".format(msg.poses[0].position.y)),float("{0:.3f}".format(msg.poses[0].position.z))]
		temp2=[float("{0:.3f}".format(msg.poses[1].position.x)),float("{0:.3f}".format(msg.poses[1].position.y)),float("{0:.3f}".format(msg.poses[1].position.z))]
		temp3=[float("{0:.3f}".format(msg.poses[2].position.x)),float("{0:.3f}".format(msg.poses[2].position.y)),float("{0:.3f}".format(msg.poses[2].position.z))]
		self.whycon_marker.update({0:temp1,1:temp2,2:temp3})
		print "WhyCon_marker",self.whycon_marker
	# Callback for /aruco_marker_publisher/markers
	def aruco_data(self,msg):
		# Printing the detected markers on terminal
		temp1=[float("{0:.3f}".format(msg.markers[0].pose.pose.orientation.x)),float("{0:.3f}".format(msg.markers[0].pose.pose.orientation.y)),float("{0:.3f}".format(msg.markers[0].pose.pose.orientation.z)),float("{0:.3f}".format(msg.markers[0].pose.pose.orientation.w))]
		temp2=[float("{0:.3f}".format(msg.markers[1].pose.pose.orientation.x)),float("{0:.3f}".format(msg.markers[1].pose.pose.orientation.y)),float("{0:.3f}".format(msg.markers[1].pose.pose.orientation.z)),float("{0:.3f}".format(msg.markers[1].pose.pose.orientation.w))]
		temp3=[float("{0:.3f}".format(msg.markers[2].pose.pose.orientation.x)),float("{0:.3f}".format(msg.markers[2].pose.pose.orientation.y)),float("{0:.3f}".format(msg.markers[2].pose.pose.orientation.z)),float("{0:.3f}".format(msg.markers[2].pose.pose.orientation.w))]
		self.aruco_marker.update({0:temp1,1:temp2,2:temp3})
		print "ArUco_marker",self.aruco_marker
		print "\n"




if __name__=="__main__":

	marker = Marker_detect()

	
	while not rospy.is_shutdown():
		rospy.spin()
