# CVblocks
Python based CV2 for finding game objects in GRR


## About
This code is built to work with a PICam2 being run on a Raspberry Pi 4/5 running Ubuntu and ROS2. 
It is designed to use the OpenCV2 library with Python.

## Purpose
The objective for this snippet is to detect purple cube game objects as a robot picks them up. It should detect the amount of cubes present in the collection spot and report back to the robot.
It achieves this by taking a set number of photos using the PiCam attached to the robot and detecting the size of the object in the collection zone. 
