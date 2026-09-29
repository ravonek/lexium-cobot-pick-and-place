# Assignment #02 Demo Script

## What to Show

1. CAD workcell stand image.
2. Isaac Sim / Isaac Lab Lexium Cobot scene.
3. ROS2 terminal output showing sensor data and robot command flow.

## Spoken Explanation

The project uses an Intel RealSense D435i camera as the sensor and a Lexium Cobot LXMRL03S0000 as the actuator/device. The camera detects the cube pose. A ROS2 subscriber node receives that sensor input and validates it. A second ROS2 node publishes the pick-and-place command toward the robot or Isaac Sim bridge.

The real simulation is still in progress. Current work focuses on stable fixed-base behavior in Isaac Sim / Isaac Lab before longer PPO training. The assignment demo therefore uses a mock camera node to show the expected ROS data flow without claiming that full hardware integration is finished.

## Expected Output

```text
[mock_intel_camera_node] camera detection: {"sensor": "Intel RealSense D435i", ...}
[vision_subscriber_node] pick goal: {"frame_id": "robot_base", ...}
[lexium_device_publisher_node] device command: {"device": "Lexium Cobot LXMRL03S0000", ...}
```
