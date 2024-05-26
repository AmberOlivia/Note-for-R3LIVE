# Note-for-R3LIVE

## Set up Livox Avia LiDAR
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
   Check if SDK is correctly installed: under `build/sample/lidar`, run `./lidar_sample`.
3. Install livox_ros_driver
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
pkg-config --modversion opencv #check opencv version
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


## Set up camera

## Build workspace
