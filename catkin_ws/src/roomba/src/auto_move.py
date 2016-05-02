import roslib
import rospy
import actionlib
import math

from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose

#move_base_msgs
from move_base_msgs.msg import *

def simple_move(pose):
    targetX = pose.position.x
    targetY = pose.position.y
    targetQ = pose.orientation

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()

    #use self?
    #set goal
    goal.target_pose.pose.position.x = targetX
    goal.target_pose.pose.position.y = targetY
    goal.target_pose.pose.orientation = targetQ
    goal.target_pose.header.frame_id = 'odom'
    goal.target_pose.header.stamp = rospy.Time.now()
    print str(targetX) + " " + str(targetY)
    #start listner
    sac.wait_for_server()

    #send goal
    sac.send_goal(goal)

    #finish
    sac.wait_for_result()

    #print result
    print sac.get_result()

global sac
global targetX
global targetY

def region_move(pose):
    global sac
    global targetX
    global targetY

    print "region move"
    targetX = pose.position.x
    targetY = pose.position.y
    targetQ = pose.orientation

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()

    #use self?
    #set goal
    goal.target_pose.pose.position.x = targetX
    goal.target_pose.pose.position.y = targetY
    goal.target_pose.pose.orientation = targetQ
    goal.target_pose.header.frame_id = 'odom'
    goal.target_pose.header.stamp = rospy.Time.now()
    print str(targetX) + " " + str(targetY)
    #start listner
    sac.wait_for_server()

    #send goal
    sac.send_goal(goal, None, None, feedbackCb)

    #finish
    sac.wait_for_result()

    #print result
    print sac.get_result()

def feedbackCb(feedback):
    curPose = feedback.base_position.pose
    curx = -curPose.position.x
    cury = -curPose.position.y
    print str(curx) + ", " + str(cury)
    print str(targetX) +", " + str(targetY)

    print str(math.sqrt((curx-targetX)**2 + (cury-targetY)**2))
    print ""
    if math.sqrt((curx-targetX)**2 + (cury-targetY)**2) < 0.7:
        sac.cancel_goal()
        print "canceled"


if __name__ == '__main__':
    rospy.init_node("auto_move")

    rospy.Subscriber("/marker_pose/point", Pose, simple_move)
    rospy.Subscriber("/marker_pose/region", Pose, region_move)

    rospy.spin()
