cd ~/catkin_ws

cd src
git clone https://github.com/unitartu-edu/carrot_follower.git
git clone https://github.com/ut-ims-robotics/opencv_apps.git
cd opencv_apps
git checkout blob_detection_nodelet
sed -i 's/\(hue_lower_limit:\).*/\1 5/' config/blob_detection_config.yaml
sed -i 's/\(hue_upper_limit:\).*/\1 20/' config/blob_detection_config.yaml
sed -i 's/\(min_area:\).*/\1 20/' config/blob_detection_config.yaml
sed -i 's/\(sat_lower_limit:\).*/\1 160/' config/blob_detection_config.yaml
sed -i 's/\(val_lower_limit:\).*/\1 100/' config/blob_detection_config.yaml
cd ../.. ; catkin build ; source devel/setup.bash

cat << EOF

Afterwards open new window and:
rosrun carrot_follower carrot_follower.py
and match right topics

EOF

roslaunch opencv_apps blob_detection.launch debug_mode:=deploy image:=/camera/color/image_raw_throttled

