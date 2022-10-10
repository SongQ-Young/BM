import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'fishbot_description'
    urdf_name = "mobile_manipulator.urdf"

    ld = LaunchDescription()
    pkg_share = FindPackageShare(package=package_name).find(package_name) 
    urdf_model_path = os.path.join(pkg_share, f'urdf/{urdf_name}')

    rviz_config_dir = os.path.join(
        get_package_share_directory('fishbot_description'),
        'rviz',
        'model.rviz')
        
  #  gazebo_world_path = os.path.join(pkg_share, 'world/fishbot.world')
    
        # Start Gazebo server
   # start_gazebo_cmd = ExecuteProcess(
   #     cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', gazebo_world_path],
   #     output='screen')
        
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        arguments=[urdf_model_path]
        )

    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        arguments=[urdf_model_path]
        )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_dir],
        output='screen',
        )

    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_node)
    ld.add_action(rviz2_node)

    return ld

