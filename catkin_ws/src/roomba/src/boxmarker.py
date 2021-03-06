import rospy
import copy
import json

from interactive_markers.interactive_marker_server import *
from visualization_msgs.msg import *
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion

from interactive_markers.menu_handler import *

menu_handler = MenuHandler()

h_first_entry = 0

pub = rospy.Publisher('marker_pose/point', Pose)
pub2 = rospy.Publisher('marker_pose/region', Pose)
def processFeedback(feedback):
    p = feedback.pose.position
    q = feedback.pose.orientation
    print feedback.marker_name + " is now at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z)
    print "    " + str(q.x) + ", " + str(q.y) + ", " + str(q.z) + ", " + str(q.w)

def makeBox( msg ):
    marker = Marker()

    marker.type = Marker.CUBE
    marker.scale.x = msg.scale * 0.45
    marker.scale.y = msg.scale * 0.45
    marker.scale.z = msg.scale * 0.45
    marker.color.r = 0.5
    marker.color.g = 0.5
    marker.color.b = 0.5
    marker.color.a = 1.0

    return marker

def makeBoxControl( msg ):
    control =  InteractiveMarkerControl()
    control.always_visible = True
    marker = makeBox(msg)
    control.markers.append( marker )
    msg.controls.append( control )
    return control

def makeQuadrocopterMarker(position, orientation, name):
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "odom"

    int_marker.pose.position = position
    int_marker.pose.orientation = orientation
    int_marker.scale = 1

    int_marker.name = name
    int_marker.description = name

    makeBoxControl(int_marker)

    control = InteractiveMarkerControl()
    control.orientation.w = 1
    control.orientation.x = 0
    control.orientation.y = 1
    control.orientation.z = 0

    
    control.interaction_mode = InteractiveMarkerControl.MENU
    
    control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
    int_marker.controls.append(copy.deepcopy(control))
    control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
    control.always_visible = True
    int_marker.controls.append(control)
    
    
    server.insert(int_marker, processFeedback)

def moveTo( feedback ):
    rospy.loginfo("moving to coordinates")
    p = feedback.pose.position
    print feedback.marker_name + " is now at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z)
    pub.publish(feedback.pose)

def moveNear( feedback ):
    rospy.loginfo("moving near coordinates")
    p = feedback.pose.position
    print feedback.marker_name + " is now at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z)
    pub2.publish(feedback.pose)

if __name__=="__main__":
    rospy.init_node("simple_marker")
    menu_handler.insert( "Move To", callback=moveTo )
    menu_handler.insert( "Move Near", callback=moveNear )
    # create an interactive marker server on the topic namespace simple_marker
    server = InteractiveMarkerServer("simple_marker")
    
    jsonString = '[{"name":"table1", "px":"5.85500335693","py":"-2.50793290138", "pz":"1.0", "qx":"0.0","qy":"0.0", "qz":"-0.723147273064","qw":"0.690703570843"}, {"name":"table2", "px":"0.0", "py":"0.0", "pz":"1.0", "qx":"0.0","qy":"0.0", "qz":"0.0","qw":"1.0"}]'

    jsonParsed = json.loads(jsonString)

    for i in range(0, len(jsonParsed)):
        cur = jsonParsed[i]
        curP = Point(float(cur['px']),float(cur['py']),float(cur['pz']))
        curQ = Quaternion(float(cur['qx']),float(cur['qy']),float(cur['qz']),float(cur['qw']))
        
        makeQuadrocopterMarker(curP, curQ, cur['name'])
        menu_handler.apply(server, cur['name'])

    # 'commit' changes and send to all clients
    server.applyChanges()

    rospy.spin()

