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
1. In the step 4. of R3LIVE repository, after run `catkin_make`  
Meet Error:
```
CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "livox_ros_driver"
  with any of the following names:

    livox_ros_driverConfig.cmake
    livox_ros_driver-config.cmake
```
To solve this, go to ~/LivoxAvia_ws/src/ws_livox, `source devel/setup.bash`

2. When installed all the dependencies and run `catkin_make`, there might be `Error: make failed -j16 -l16`.
   Just keep run `catkin_make`.

3. After first time running `catkin_make`, there might be some error related to source file.
   Run `source devel/setup.bash` under r3live_ws, then rerun `catkin_make`.

4. If some contents in CMakeLists.txt file has modified, remember to delete build and devel files and run `catkin_make` again.
5. The missing file `CustomMsg.h` can be found in r3live_ws/devel/include/livox_ros_driver/.  
Reference:  
[#107](https://github.com/Livox-SDK/livox_ros_driver/issues/107)  
[#41](https://github.com/Livox-SDK/livox_ros_driver/issues/41)

[#104](https://github.com/Livox-SDK/livox_ros_driver/issues/104)
[#125](https://github.com/Livox-SDK/livox_ros_driver/issues/125)

## Set up camera (SN:37291130)
Install nvidia driver(I'm using the latest 555 version), CUDA(12.4), ZED-SDK. 
`ZED_Explorer` and `ZED_Sensor_Viewer` should work well, the tools are under `usr/local/zed/tools/`

## record rosbag
Make sure the topics recorded have right data message type:
`/livox/lidar: livox_ros_driver/CustomMsg`
`/livox/imu: sensor_msgs/Imu`
You need to write a launch file under `r3live_ws/src/r3live/r3live/launch` file
The launch file should launch LiDAR and camera together, launch camera using `zed2i.launch`.
Launch LiDAR using `livox_lidar_msg.launch` to make sure the lidar topic message type will be `livox_ros_driver/CustomMsg`.

*Tip*: Change the xfer parameter in `livox_lidar_msg.launch` to 1 to ensure the message to be CustomMsg.

Run these:
```
`roslaunch r3live record_sensors.launch`  
`rosbag record -O mybag00.bag /livox/lidar /livox/imu /zed2i/zed_node/left/image_rect_color /zed2i/zed_node/right/image_rect_color`

`rosbag info {BAGNAME.bag}` #check bag info
`rostopic echo {TOPIC NAME}` #check topic message type
```

## Calibration
Reference:  
https://gitee.com/linClubs/lidar2cam_calibration
https://chev.me/arucogen/

### Stereo camera intrinsic calibration
Just use official calibration tool: `/usr/local/zed/tools/ZED_Calibration` to calibrate. The calibration file is in /usr/local/zed/settings.
Or download official calibration file by calling http://calib.stereolabs.com/?SN={CAMERA SERIAL NUMBER}

### LiDAR and camera extrinsic calibration

Use calibration tool: [livox_camera_calib](https://github.com/hku-mars/livox_camera_calib)




## Build workspace
