#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
 
    
   
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    vel_msg.linear.x = 0
    
    rate=rospy.Rate(5)
    part=1
    
    
    while not rospy.is_shutdown():

	
	if part<=19:
           vel_msg.angular.z = 2
           vel_msg.linear.x = 1
           velocity_publisher.publish(vel_msg)
	   part=part+1
           print(part)
           
        elif part==20:
	     vel_msg.angular.z = 0
             vel_msg.linear.x = 10
             velocity_publisher.publish(vel_msg)
             part=part+1
	     print(part)
        elif 21<=part<=39:
             vel_msg.angular.z = 2
             vel_msg.linear.x = 1
             velocity_publisher.publish(vel_msg)
             part=part+1
             
        else:
	 
         break
        rate.sleep()
             
	
		

    

     
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
