#!/usr/bin/env python3
import json
import os
import rospy
import sys
from geometry_msgs.msg import Twist

def main():
    rospy.init_node("velocity_publisher")
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
    
    with open(os.path.dirname(os.path.realpath(__file__))+'/routes/'+sys.argv[1]+'.json') as data_file:    
        
        data = json.load(data_file)
        print(data['description'])
        
        for route in data['routes']:
            
            print('===== ',route['description'],' =====')
            rospy.sleep(route['wait_at_first'])
            loop_rate = rospy.Rate(route['rate'])
            counter = 1
            countdown = 1
            if 'cycles' in route:
                if route['cycles'] < 1:
                    countdown = -1 # eternal loop
                else:
                    countdown = route['cycles']
                    
            while 1:
                print('CYCLE ',counter)
                counter += 1
                for leg in route['legs']:
                    
                    starting_time = rospy.get_time()
                    if 'd' in leg:
                        print(leg['d'])
                    else:
                        print(leg['x'], ';', leg['y'], ';', leg['Z'], ';', leg['t'] ) 
                    
                    while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < leg['t']):
                        robot_vel = Twist()
                        robot_vel.linear.x = leg['x']
                        robot_vel.linear.y = leg['y']
                        robot_vel.linear.z = 0.0
                        robot_vel.angular.x = 0.0
                        robot_vel.angular.y = 0.0
                        robot_vel.angular.z = leg['Z']
                        velocity_pub.publish(robot_vel)
                        loop_rate.sleep()
                        
                if countdown > 0:
                    countdown -= 1
                if countdown == 0 or rospy.is_shutdown():
                    break
                
            if rospy.is_shutdown():
                break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: velocity_publisher.py route_from_routes_dir_without_extension")
    else:
        try:
            main()
        except rospy.ROSInterruptException:
            pass
