# Note-for-R3LIVE

## Set up Livox Avia LiDAR (Broadcast node: 3JEDM1F001V0541)
Reference:  
https://blog.csdn.net/m0_52765390/article/details/136658542  
https://blog.csdn.net/qq_38768959/article/details/123098437  
Wired connecting Livox LiDAR and laptop, keep the voltage at the range of 10~15 V.

### Laptop settings
Before powering up, changes are need in the laptop-settings-Network:
- In wired connection, add a new profile, in IPv4, change the IPv4 to manual and set below:  
   Address: 192.168.1.50    Netmask: 255.255.255.0    Gateway: 192.168.1.154 ('54'in'154' is from last two numbers of S/N number)

### Install Livox-SDK and Livox-ROS-driver
1. Create a workspace named `LivoxAvia-ws`, cd into it and `catkin_make`.  
   https://github.com/Livox-SDK/Livox-SDK 
2. Install SDK   
   ```
   cd ~/LivoxAvia_ws/src
   git clone https://github.com/Livox-SDK/Livox-SDK.git
   cd Livox-SDK/build/
   cmake ..
   make
   sudo make install
   ```
   Check if SDK is correctly installed: under `Livox-SDK/build/sample/lidar`, run `./lidar_sample`. (Use this to get broadcast code)
   
4. Install livox_ros_driver
   ```
   cd ~/LivoxAvia_ws/src
   git clone https://github.com/Livox-SDK/livox_ros_driver.git ws_livox/src
   cd ws_livox
   catkin_make
   source ./devel/setup.sh
   ```
   Run Livox-ROS-driver by running launch files, including:
   ![image](https://github.com/AmberOlivia/Note-for-R3LIVE/assets/74347715/9b563386-fbff-4165-a795-dd9d2dfeab2a)

   For example: `roslaunch livox_ros_driver livox_lidar_rviz.launch`  
   This will launch Rviz and see the LiDAR view, Fixed Frame:`livox_frame`, Topic(add **PointCloud2** topic):`/livox/lidar`, 
   
## Set up environment for R3LIVE
Following step 3,4, and 5 in https://github.com/hku-mars/r3live  
```
#-----prepare prerequisites-----
sudo apt-get install ros-noetic-cv-bridge ros-XXX-tf ros-noetic-message-filters ros-noetic-image-transport ros-noetic-image-transport*
sudo apt-get install libcgal-dev pcl-tools

#-----check opencv version-----
pkg-config --modversion opencv

#-----create workspace------
cd ~/r3live/src
git clone https://github.com/hku-mars/r3live.git
cd ../
catkin_make
source ~/r3live/devel/setup.bash

#-----run-----
roslaunch r3live r3live_bag.launch # terminal 1
rosbag play YOUR_DOWNLOADED.bag  # terminal 2
```
More in official repo.

#### Possible Error
In the step 4. of R3LIVE repository, after run `catkin_make`  
Meet Error:
```
CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "livox_ros_driver"
  with any of the following names:

    livox_ros_driverConfig.cmake
    livox_ros_driver-config.cmake
```
To solve this, go to ~/LivoxAvia_ws/src/ws_livox, `source devel/setup.bash`


## Set up camera (SN:37291130)
Install nvidia driver(I'm using the latest 555 version), CUDA(12.4), ZED-SDK. 
`ZED_Explorer` and `ZED_Sensor_Viewer` should work well, the tools are under `usr/local/zed/tools/`

## Calibration for camera and lidar
Reference:  
https://gitee.com/linClubs/lidar2cam_calibration
https://chev.me/arucogen/

### Stereo camera intrinsic calibration


### LiDAR and camera extrinsic calibration





## Build workspace
