import rclpy
import sys
import time
from rclpy.node import Node
from std_msgs.msg import Int16

class ReaderNode(Node):

    def __init__(self):
        super().__init__("Reader")
        self.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        if msg.data == 0 :
            self.get_logger().info("One day,someone bet on Hemingway.")
        elif msg.data == 1 :
            self.get_logger().info("'If you can make a short story with 6 words,'")
        elif msg.data == 2 :
            self.get_logger().info("'And make people cry,It's your victory.'")
        elif msg.data == 3 :
            self.get_logger().info("And Hemingway won the bet.")
        elif msg.data == 4 :
            self.get_logger().info("This is it...")
        elif msg.data == 5 :
            self.get_logger().info("For sale : baby shoes, never worn")
        else :
            sys.exit("done")

rclpy.init()
rclpy.spin( ReaderNode() )
