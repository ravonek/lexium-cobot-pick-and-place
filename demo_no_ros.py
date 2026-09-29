"""Run the Assignment #02 data flow without ROS2 installed.

This script is only a local fallback for quick presentation/demo checks.
The real ROS2 implementation is in lexium_cobot_pick_and_place/*.py.
"""

import json
import math
import time


def mock_camera_detection(step: int) -> dict:
    return {
        "sensor": "Intel RealSense D435i",
        "object": "cube",
        "x_m": round(0.31 + 0.015 * math.sin(step / 3.0), 3),
        "y_m": round(-0.08 + 0.010 * math.cos(step / 4.0), 3),
        "z_m": 0.035,
        "yaw_rad": 0.0,
        "confidence": 0.91,
    }


def subscriber_make_pick_goal(detection: dict) -> dict:
    if detection["confidence"] < 0.70:
        raise ValueError("low confidence detection")
    return {
        "frame_id": "robot_base",
        "target_object": detection["object"],
        "pick": {
            "x_m": detection["x_m"],
            "y_m": detection["y_m"],
            "z_m": detection["z_m"],
            "yaw_rad": detection["yaw_rad"],
        },
        "place": {
            "x_m": 0.45,
            "y_m": 0.12,
            "z_m": 0.04,
            "yaw_rad": 0.0,
        },
    }


def publisher_make_device_command(sequence_id: int, goal: dict) -> dict:
    return {
        "command_id": sequence_id,
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


def main() -> None:
    print("Assignment #02 fallback demo: sensor -> subscriber -> publisher -> device")
    print("Note: this is a no-ROS local check. Use ros2 launch for the real ROS2 demo.\n")
    for step in range(1, 4):
        detection = mock_camera_detection(step)
        print(f"[sensor/mock_intel_camera_node] /camera/object_pose")
        print(json.dumps(detection, indent=2))

        goal = subscriber_make_pick_goal(detection)
        print("[subscriber/vision_subscriber_node] /planner/pick_goal")
        print(json.dumps(goal, indent=2))

        command = publisher_make_device_command(step, goal)
        print("[publisher/lexium_device_publisher_node] /lexium_cobot/device_command")
        print(json.dumps(command, indent=2))
        print("-" * 80)
        time.sleep(0.3)


if __name__ == "__main__":
    main()
