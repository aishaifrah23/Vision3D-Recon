# Project Problem

## 1. Problem Statement

Building 3D scenes and tracking motion in time are key for robotics, autonomous navigation and spatial computing.. Many current solutions are stuck in big slow scripts or depend on expensive closed hardware. There is a need for a simple, flexible and open-source Python system that can handle two tasks: generate 3D point clouds from stereo image pairs and track movement using dense optical flow from regular video inputs or webcams.

## 2. Project Scope

The **Vision3D-Recon** project solves this with a mode, modular design built using OpenCV and NumPy:

* **Stereo Reconstruction Subsystem:** Uses -Global Block Matching (`StereoSGBM`) to create disparity maps. Converts 2D pixel locations into space and saves clean point cloud data in the standard ASCII `.ply` format so it can be viewed in common tools.

* **Motion Analytics Subsystem:** Applies Farneback optical flow to detect how pixels move between frames. Shows direction and speed of motion using color mapping in the HSV space.

* **Architecture & Interface:** Designed as seven modules with a single command-line entry point (`main.py`). Works with both recorded videos and live webcam feeds.

## 3. Target Audience

* **Computer Vision Researchers & Students:** Wanting a extendable codebase to test and learn about disparity and optical flow techniques.

* **Robotics Engineers:** Seeking a software-only tool for basic 3D mapping and motion tracking, without needing powerful GPUs or CUDA support.
