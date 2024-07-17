from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='temperature_monitor',
            executable='temperature_publisher',
            name='temperature_publisher'
        ),
        Node(
            package='temperature_monitor',
            executable='threshold_subscriber',
            name='threshold_subscriber'
        ),
        Node(
            package='temperature_monitor',
            executable='alert_publisher',
            name='alert_publisher'
        ),

    ])
