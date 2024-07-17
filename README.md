# Rabih-Ros2-Temperature-Monitor
## Overview
This package simulates a temperature monitoring system using ROS 2. It consists of 4 nodes:
1. temperature_publisher: Simulates a temperature sensor by publishing random temperature values.
2. threshold_subscriber: Subscribes to the temperature topic and publishes an alert if the temperature exceeds a threshold.
3. alert_publisher: Subscribes to the alert_trigger topic and publishes an alert message.
4. temperature_logger: Subscribes to the temperature topic and logs the temperture over time.

The package has a launch file to launch all the nodes together to ensure communication. it is located under launch/ (launch.py).

## Installation
sh
# Clone the repository and navigate to the workspace
git clone <repository_link> ~/ros2_ws/src/temperature_monitor
cd ~/ros2_ws

# Build the package
colcon build

# Source the overlay workspace
source install/setup.bash

## Running

# Launch the nodes
ros2 launch temperature_monitor launch.py
