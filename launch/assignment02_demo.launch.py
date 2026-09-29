from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="lexium_cobot_pick_and_place",
                executable="mock_intel_camera_node",
                name="mock_intel_camera_node",
                output="screen",
            ),
            Node(
                package="lexium_cobot_pick_and_place",
                executable="vision_subscriber_node",
                name="vision_subscriber_node",
                output="screen",
            ),
            Node(
                package="lexium_cobot_pick_and_place",
                executable="lexium_device_publisher_node",
                name="lexium_device_publisher_node",
                output="screen",
            ),
        ]
    )
