echo "ROS setup for Debian Buster for ROS algkursus https://sisu.ut.ee/rosak"

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install python3-catkin-tools python3-osrf-pycommon
sudo apt-get install ros-noetic-teleop-twist-keyboard
sudo apt-get install ros-$(rosversion -d)-turtlesim
sudo apt-get install ros-$(rosversion -d)-joy

echo "Create Catkin workspace and fetch necessary ROS packages"

cd ~
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone https://github.com/robotont/robotont_msgs.git
git clone https://github.com/robotont/robotont_driver.git
git clone https://github.com/robotont/robotont_demos.git
git clone https://github.com/robotont/robotont_description.git
git clone https://github.com/wjwwood/serial.git

echo "Build and load Catkin workspace"

cd ..
catkin build
source devel/setup.bash
