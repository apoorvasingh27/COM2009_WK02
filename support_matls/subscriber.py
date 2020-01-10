#!/usr/bin/env python
# A simple ROS subscriber node in Python

import rospy
from std_msgs.msg import String

class Subscriber:

    def callback(self, data):
        rospy.loginfo("Subscriber obtained the following message: \"%s\"", data.data)

    def __init__(self):
        rospy.init_node('subscriber_node', anonymous=True)
        self.sub = rospy.Subscriber("chatter", String, self.callback)
        rospy.loginfo("subscriber node is active...")

    def main_loop(self):
        rospy.spin()

if __name__ == '__main__':
    subscriber_instance = Subscriber()
    subscriber_instance.main_loop()