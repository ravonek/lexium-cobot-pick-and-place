import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class LexiumDevicePublisherNode(Node):
    """Publishes command data toward the Lexium Cobot or Isaac Sim bridge."""

    def __init__(self):
        super().__init__("lexium_device_publisher_node")
        self.subscription = self.create_subscription(
            String,
            "/planner/pick_goal",
            self.handle_pick_goal,
            10,
        )
        self.publisher = self.create_publisher(String, "/lexium_cobot/device_command", 10)
        self.sequence_id = 0

    def handle_pick_goal(self, msg):
        try:
            goal = json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().warning("ignored invalid pick goal JSON")
            return

        self.sequence_id += 1
        command = {
            "command_id": self.sequence_id,
            "device": "Lexium Cobot LXMRL03S0000",
            "mode": "pick_and_place",
            "motion_sequence": [
                {"step": "approach_pick", "pose": goal["pick"], "speed": "reduced"},
                {"step": "grasp", "tool": "vacuum_or_gripper", "confirm": True},
                {"step": "lift", "delta_z_m": 0.10},
                {"step": "move_to_place", "pose": goal["place"], "speed": "reduced"},
                {"step": "release", "tool": "vacuum_or_gripper"},
                {"step": "return_ready"},
            ],
        }

        out = String()
        out.data = json.dumps(command)
        self.publisher.publish(out)
        self.get_logger().info(f"device command: {out.data}")


def main(args=None):
    rclpy.init(args=args)
    node = LexiumDevicePublisherNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
