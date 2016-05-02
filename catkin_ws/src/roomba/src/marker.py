import rospy
import math
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Twist, Quaternion, Pose, Point, Vector3, PoseWithCovarianceStamped
from std_msgs.msg import Header, ColorRGBA
from tf.transformations import euler_from_quaternion

pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist)
marker_publisher = rospy.Publisher('visualization_marker', Marker)
prevPoints = []
prevQuats = []
reverse = False
threshDist = 0.1

def show_text_in_rviz(text):
    global marker_publisher
    global prevPoints
    marker = Marker(type=Marker.LINE_STRIP, id=0,
                lifetime=rospy.Duration(1.5),
                pose=Pose(Point(0.0, 0.0, 0.10), Quaternion(0, 0, 0, 1)),
                scale=Vector3(0.06, 0.06, 0.06),
                header=Header(frame_id='odom'),
                color=ColorRGBA(0.0, 1.0, 0.0, 0.8), text=text,
		points = prevPoints) 
    marker_publisher.publish(marker)

def run():
    #global tfListener
    #listener = tf.TransformListener()
    #Todo: May need a callback
    global reverse
    rospy.Subscriber("/robot_pose_ekf/odom_combined", PoseWithCovarianceStamped, odomCallback)
    while(rospy.get_time()== 0):
        val = 1
    val = rospy.get_time() + 10
    while(1):
        show_text_in_rviz("foo")
        rospy.sleep(0.2)
        if rospy.get_time() >= val:
            reverse = True

firstTime = True
def odomCallback(msg):
    global firstTime
    global targetPoint
    global targetQuat
    if not reverse:
        if len(prevPoints) == 0:
            prevPoints.append(msg.pose.pose.position)
            prevQuats.append(msg.pose.pose.orientation)
        point0 = prevPoints[-1]
        point1 = msg.pose.pose.position
        dist = math.sqrt(math.pow(point0.x - point1.x, 2) + math.pow(point0.y - point1.y, 2))
        if(dist > threshDist):
            prevPoints.append(point1)
            prevQuats.append(msg.pose.pose.orientation)
    else:
        if firstTime:
            targetPoint = prevPoints.pop()
            targetQuat = prevQuats.pop()
            firstTime = False
        currPoint = msg.pose.pose.position
        currQuat = msg.pose.pose.orientation
        quaternion = (currQuat.x, currQuat.y, currQuat.z, currQuat.w)
        euler = euler_from_quaternion(quaternion)
        currYaw = euler[2]
        quaternion = (targetQuat.x, targetQuat.y, targetQuat.z, targetQuat.w)
        euler = euler_from_quaternion(quaternion)
        targetYaw = euler[2]

        tw = Twist()
        #print str(abs(currYaw - targetYaw))
        if abs(currYaw - targetYaw) < 0.1:
            if abs(targetPoint.x - currPoint.x) < 0.1 and abs(targetPoint.y - currPoint.y) < 0.1:
                if len(prevPoints) != 0:
                    targetPoint = prevPoints.pop()
                    targetQuat = prevQuats.pop()
                tw.linear.x = 0
                tw.angular.z = 0
            else:
                tw.linear.x = -0.2
                tw.angular.z = 0
        else:
            print str(radDeg(currYaw)) + ", " +  str(radDeg(targetYaw))
            # TODO fix rotation direction to rotate optimally
            if radDeg(targetYaw - currYaw) > 180.0: 
                tw.angular.z = 0.5
            else:
                tw.angular.z = -0.5
            tw.linear.x = 0
        pub.publish(tw)

def radDeg(val):
    val += math.pi
    val = 180 * val / math.pi
    return val

def main():
    rospy.init_node("marker")
    run()
    rospy.spin()


if __name__ == '__main__':
    main()

