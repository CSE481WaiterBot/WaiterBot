import rospy
from  geometry_msgs.msg import Twist
pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist)
tw = Twist()

def run():
    while(1):
        tw.linear.x = 0
        tw.angular.z = 1.0
        pub.publish(tw)
	rospy.sleep(0.4)

	tw.angular.z = -1.0
	pub.publish(tw)
	rospy.sleep(0.4)


def main():
    rospy.init_node("dance")
    run()
    rospy.spin()

if __name__ == '__main__':
    main()
