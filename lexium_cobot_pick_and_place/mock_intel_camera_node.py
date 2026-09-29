import json
import math

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MockIntelCameraNode(Node):
    """Publishes a repeatable RGB-D object pose for assignment demo runs."""

    def __init__(self):
        super().__init__("mock_intel_camera_node")
        self.publisher = self.create_publisher(String, "/camera/object_pose", 10)
        self.step = 0
        self.timer = self.create_timer(1.0, self.publish_detection)

    def publish_detection(self):
        self.step += 1
        pose = {
            "sensor": "Intel RealSense D435i",
            "object": "cube",
            "x_m": round(0.31 + 0.015 * math.sin(self.step / 3.0), 3),
            "y_m": round(-0.08 + 0.010 * math.cos(self.step / 4.0), 3),
            "z_m": 0.035,
            "yaw_rad": 0.0,
            "confidence": 0.91,
        }
        msg = String()
        msg.data = json.dumps(pose)
        self.publisher.publish(msg)
        self.get_logger().info(f"camera detection: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = MockIntelCameraNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
