#!/usr/bin/env python3

import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Twist

rotation_direction = -1
last_marker = None

def ar_message_handler(data):
    global last_marker
    global rotation_direction
    if len(data.markers) > 0:
        for marker in data.markers:
            rospy.loginfo("Detected marker " + str(marker.id))
            if ((last_marker is None) and (marker.id == 1)) or (not(last_marker is None) and (marker.id != last_marker)) :
                last_marker = marker.id
                rotation_direction = -rotation_direction
                rospy.loginfo("Rotation direction  " + rotation_direction)
                break
                
    #else:
        #rospy.loginfo("No AR markers detected.")

def main():
    global rotation_direction
    rospy.init_node("marker_finder")
    rospy.Subscriber("ar_pose_marker", AlvarMarkers, ar_message_handler)
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
    loop_rate = rospy.Rate(200)
    
    while not rospy.is_shutdown():
        robot_vel = Twist()
        robot_vel.linear.x = 0.0
        robot_vel.linear.y = 0.0
        robot_vel.linear.z = 0.0
        robot_vel.angular.x = 0.0
        robot_vel.angular.y = 0.0
        robot_vel.angular.z = rotation_direction * 0.39
        velocity_pub.publish(robot_vel)
        loop_rate.sleep()
                        

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
