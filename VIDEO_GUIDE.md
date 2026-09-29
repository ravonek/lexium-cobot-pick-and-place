# Demo Video Guide

Use your own short screen recording for Assignment #02. The external YouTube video can be mentioned as inspiration, but the submitted demo should show our project flow.

## Recommended 45-60 second video structure

1. Show the GitHub repository and README.
2. Show the connection diagram in `docs/connection_diagram.png`.
3. Open terminal and run:

```bash
python3 demo_no_ros.py
```

4. Point to the three required parts in the output:
   - sensor data: `/camera/object_pose`
   - subscriber processing: `/planner/pick_goal`
   - publisher/device command: `/lexium_cobot/device_command`
5. Show the Isaac Sim / CAD screenshot from `docs/`.

## What to say

This is a local fallback demo because ROS2 is not installed on this presentation computer. It shows the same Assignment #02 signal flow: sensor input, subscriber processing, and publisher command to the Lexium Cobot device. On a ROS2 machine, the same logic runs through `ros2 launch`.

## Backup visual

`docs/demo_preview.gif` is a simple animated preview of the same signal flow. Use it only as supporting visual material; the strongest demo is a screen recording of the terminal run.
