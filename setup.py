from setuptools import setup

package_name = "lexium_cobot_pick_and_place"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", ["launch/assignment02_demo.launch.py"]),
        ("share/" + package_name + "/config", ["config/workcell_params.yaml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Adilkhan Kaldybekov",
    maintainer_email="adilkhan@example.com",
    description="ROS2 nodes for a Lexium Cobot pick-and-place Assignment 02 demo.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "mock_intel_camera_node = lexium_cobot_pick_and_place.mock_intel_camera_node:main",
            "vision_subscriber_node = lexium_cobot_pick_and_place.vision_subscriber_node:main",
            "lexium_device_publisher_node = lexium_cobot_pick_and_place.lexium_device_publisher_node:main",
        ],
    },
)
