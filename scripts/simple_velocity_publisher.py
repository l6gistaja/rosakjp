#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node("velocity_publisher")
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
    rospy.sleep(2)

    robot_vel = Twist()
    robot_vel.linear.x = 0.1
    robot_vel.linear.y = 0.0
    robot_vel.linear.z = 0.0
    robot_vel.angular.x = 0.0
    robot_vel.angular.y = 0.0
    robot_vel.angular.z = 0.0

    velocity_pub.publish(robot_vel)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
