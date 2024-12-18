# UR5 Control Library (ur_rtde)
## Website
https://sdurobotics.gitlab.io/ur_rtde/introduction/introduction.html

## 1. Install Dependences
```
sudo add-apt-repository ppa:sdurobotics/ur-rtde
sudo apt-get update
sudo apt install librtde librtde-dev
```
then will output the hint to install 
```
 A C++ interface for sending and receiving data to/from a UR robot using the Real-Time Data Exchange (RTDE) interface of the robot.
 更多信息： https://launchpad.net/~sdurobotics/+archive/ubuntu/ur-rtde
按 [ENTER] 继续或 Ctrl-c 取消安装
```
press [ENTER] to continue or [Ctrl-c] to cancel install

## 2. Build Instructions(from source)
- Boost
- pybind11

The pybind11 dependency is optional and are only required if ur_rtde are to be used with Python. The ur_rtde library depends on Boost for networking and threading.

## 3. Dependencies
You can install Boost on Ubuntu using:
```
sudo apt-get install libboost-all-dev
```
(Optionally) if you want to use ur_rtde with Python make sure pybind11 is checked out from the submodule before attempting to build using:
```
git submodule update --init --recursive
```
## 4.Build
```
git clone https://gitlab.com/sdurobotics/ur_rtde.git
cd ur_rtde
git submodule update --init --recursive
mkdir build
cd build
cmake ..
make
sudo make install
```
Sometimes, network issues may cause the ``sudo make install`` command to fail when downloading pybind11. In such cases, You can use the compressed package ``pybind11.zip`` or you may need to manually download it using a proxy or other methods.
### .gitmodules
```
[submodule "pybind11"]
        path = pybind11
        url = https://github.com/pybind/pybind11.git
        branch = stable
```
unzip or download this file in ur_rtde library, relative path: ``UR5_control/ur_rtde/pybind11``
# Examples
## control and receive 
```
import rtde_control
import rtde_receive

# connect to UR5
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")
rtde_r = rtde_receive.RTDEReceiveInterface("192.168.1.254")
```
## 1. control UR5 to move 
```
python moveJ.py              # joint angle control
python moveL.py              # position control
python control_feedback.py   # Continuous movement with closed-loop detection of position accuracy
```

## 2. receive data
```
python get_joint.py # obtain UR5 joint
python get_pose.py  # obtain 6 Dof pose
python get_tcp.py   # obtain TCP pose
python status.py    # obtain real-time status of UR5
```

## 3. teach mode
```
python teach.py # enable or disable teach mode
```
## 4. inverse kinematics (6 DOF pose -> joint)
```
python pose2joint.py  # inverse kinematics
```
## 5. grasp task
```
python object2hand.py    # calculate grasping pose based on the object's 6Dof pose

python pick_and_place.py # connected with gripper to pick and place object
```

## 6. turn off 
```
python power_off.py  # turn off UR5
```

## program trash
```
ur5_merge.py
```