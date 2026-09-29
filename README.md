# Lexium Cobot Pick-and-Place Workcell

Assignment #02 technical demo for an AI-enabled pick-and-place workcell using a Schneider Electric Lexium Cobot LXMRL03S0000 and an Intel RealSense D435i RGB-D camera.

## Project Summary

The workcell uses camera input to estimate an object pose and sends a pick-and-place command to a Lexium Cobot / Isaac Sim device interface. The current diploma project progress includes a CAD workcell stand, a Lexium cobot model imported into Isaac Sim / Isaac Lab, a table-cube-target simulation scene, and the first RL training stage for reaching the cube.

For Assignment #02, the ROS2 layer is represented by a compact demo pipeline:

1. `mock_intel_camera_node` publishes sample object detections for demo/testing.
2. `vision_subscriber_node` subscribes to camera detections and converts them into a validated pick goal.
3. `lexium_device_publisher_node` publishes a robot device command for the Lexium cobot or Isaac Sim bridge.

This satisfies the assignment requirement for sensor input, actuator/device output, a subscriber node, and a publisher node.

## Components

| Component | Purpose |
|---|---|
| Lexium Cobot LXMRL03S0000 | 6-axis robot arm, 3 kg max payload, pick-and-place actuator |
| Intel RealSense D435i | RGB-D sensor for object position and depth input |
| Isaac Sim / Isaac Lab | Simulation and RL training environment |
| CAD aluminum-profile stand | Physical workcell frame and robot/camera mount |
| ROS2 Python nodes | Sensor subscriber and device command publisher |
| Vacuum or parallel gripper | End-effector for grasping the cube/box |

## ROS2 Topics

| Topic | Message | Direction | Description |
|---|---|---|---|
| `/camera/object_pose` | `std_msgs/String` JSON | Sensor output | Detected object pose from RealSense or demo camera node |
| `/planner/pick_goal` | `std_msgs/String` JSON | Planner output | Validated pick target for the robot |
| `/lexium_cobot/device_command` | `std_msgs/String` JSON | Device command | Command payload for Lexium Cobot / Isaac Sim bridge |

## Demo Run

```bash
cd lexium-cobot-pick-and-place
colcon build
source install/setup.bash
ros2 launch lexium_cobot_pick_and_place assignment02_demo.launch.py
```

Expected console flow:

```text
mock_intel_camera_node -> publishes cube pose
vision_subscriber_node -> receives sensor input and publishes pick goal
lexium_device_publisher_node -> publishes command to /lexium_cobot/device_command
```

## Current Project Status

- CAD workcell stand model is prepared.
- Aluminum profile stand components have been ordered.
- Lexium cobot USD model is imported into Isaac Sim / Isaac Lab.
- Current simulation scene includes robot, table, cube and target.
- RL setup currently uses 29 observations and 8 actions.
- Current blocker: fixed-base stability of the robot in simulation.

## Repository Notes

This folder is ready to upload to GitHub as:

```text
lexium-cobot-pick-and-place
```

After upload, add the final GitHub URL to the technical report.
