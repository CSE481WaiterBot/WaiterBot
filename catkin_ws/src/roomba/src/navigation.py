import rospy
from  geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist)
tw = Twist()

seconds = 0.7

flag = False
def on_bumper(msg):
    global flag
    if msg.state == BumperEvent.PRESSED:
	flag = True
	rospy.sleep(seconds)
	flag = False

	
def run():
    while(1):
	if flag:
	    tw.linear.x = -0.1
	    tw.angular.z = 1.0
	else:
	    tw.linear.x = 0.1
	    tw.angular.z = 0
	pub.publish(tw)
	        
		
def main():
    rospy.init_node("roomba")
    rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, on_bumper)
    run()
    rospy.spin()	

if __name__ == '__main__':
    main()
