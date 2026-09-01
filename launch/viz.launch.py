from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    pkg_share = FindPackageShare("template_description").find("template_description")
    urdf_file = os.path.join(pkg_share, "urdf", "template_description.urdf")
    rviz_config = os.path.join(pkg_share, "rviz", "viz.rviz")

    start_rsp_arg = DeclareLaunchArgument(
        "start_rsp",
        default_value="false",
        description="Start robot_state_publisher in this launch",
    )

    return LaunchDescription([
        start_rsp_arg,
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            condition=IfCondition(LaunchConfiguration("start_rsp")),
            parameters=[{
                "robot_description": open(urdf_file).read(),
                "publish_frequency": 100.0,
            }],
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", rviz_config],
            output="screen",
        ),
    ])
