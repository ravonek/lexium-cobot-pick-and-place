import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class VisionSubscriberNode(Node):
    """Subscribes to sensor input and publishes a validated pick goal."""

    def __init__(self):
        super().__init__("vision_subscriber_node")
        self.min_confidence = 0.70
        self.subscription = self.create_subscription(
            String,
            "/camera/object_pose",
            self.handle_object_pose,
            10,
        )
        self.publisher = self.create_publisher(String, "/planner/pick_goal", 10)

    def handle_object_pose(self, msg):
        try:
            detection = json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().warning("ignored invalid JSON from camera")
            return

        confidence = float(detection.get("confidence", 0.0))
        if confidence < self.min_confidence:
            self.get_logger().warning(f"ignored low confidence detection: {confidence}")
            return

        pick_goal = {
            "frame_id": "robot_base",
            "target_object": detection.get("object", "unknown"),
            "pick": {
                "x_m": detection["x_m"],
                "y_m": detection["y_m"],
                "z_m": detection["z_m"],
                "yaw_rad": detection.get("yaw_rad", 0.0),
            },
            "place": {
                "x_m": 0.45,
                "y_m": 0.12,
                "z_m": 0.04,
                "yaw_rad": 0.0,
            },
        }

        out = String()
        out.data = json.dumps(pick_goal)
        self.publisher.publish(out)
        self.get_logger().info(f"pick goal: {out.data}")


def main(args=None):
    rclpy.init(args=args)
    node = VisionSubscriberNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
