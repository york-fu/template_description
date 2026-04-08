from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    pkg_share = FindPackageShare("template_description").find("template_description")
    urdf_file = os.path.join(pkg_share, "urdf", "template_description.urdf")
    rviz_config = os.path.join(pkg_share, "rviz", "viz.rviz")

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            parameters=[{
                "robot_description": open(urdf_file).read(),
                'publish_frequency': 60.0,
            }]
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", rviz_config],
            output="screen"
        )
    ])
