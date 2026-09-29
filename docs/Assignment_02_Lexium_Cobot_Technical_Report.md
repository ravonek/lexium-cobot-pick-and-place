# Assignment #02 Technical Report: AI-Enabled Pick-and-Place Workcell

Team: Adilkhan Kaldybekov, Tair Jumashev, Yerassyl Maitan, Ratmir  
Supervisor: Tolengutov Rasul  
Submitted to: Prof. Ilyas Muhammad  
Due: 29 Sept 2026

## Project Description
The project develops a compact robotic workcell for pick-and-place tasks using a Schneider Electric Lexium Cobot LXMRL03S0000 as the actuator/device. An Intel RealSense D435i RGB-D camera is selected as the sensor input. The camera detects the object pose, ROS2 nodes convert the sensor data into a pick goal, and a publisher node sends a robot command to the Lexium Cobot / Isaac Sim bridge.

## Components
- Lexium Cobot LXMRL03S0000: 6-axis robot arm, 3 kg payload, 626 mm reach.
- Intel RealSense D435i: RGB-D sensor for object pose input.
- ROS2 Python nodes: subscriber for sensor input and publisher for device command.
- Isaac Sim / Isaac Lab: simulation, physics scene and PPO/RL training.
- CAD aluminum stand: robot/camera/workspace frame.

## Connection
Sensor input is published on `/camera/object_pose`, received by `vision_subscriber_node`, converted to `/planner/pick_goal`, and sent as `/lexium_cobot/device_command` by `lexium_device_publisher_node`.

## Results
CAD stand is prepared; Lexium Cobot is imported in Isaac Sim; the task scene includes table, cube and target; the RL setup uses 29 observations and 8 actions. Main blocker: fixed-base stability must be solved before further PPO training. For Assignment #02, the ROS2 demo publishes sample camera data and shows the subscriber/publisher command flow.

## GitHub / Code
Prepared local repository: `lexium-cobot-pick-and-place`. Public GitHub link should be added after upload: `https://github.com/ravonek/lexium-cobot-pick-and-place`.
