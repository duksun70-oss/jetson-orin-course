# ROS 2 package의 Python node 예제용 핵심 코드
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('simple_talker')
        self.pub = self.create_publisher(String, 'course_message', 10)
        self.timer = self.create_timer(0.5, self.tick)
        self.count = 0

    def tick(self):
        msg = String()
        msg.data = f'Jetson Orin ROS2 #{self.count}'
        self.pub.publish(msg)
        self.count += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
