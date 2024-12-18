import rtde_control
import object2hand
import time
import os
import sys
# the absolute path of the current file
path = os.path.abspath('/home/ros/EncoSmart/UR5/gripper')
# Add this directory to the module search path
sys.path.append(path)
from gripper import GripperController # import robotiq gripper controller library

if __name__ == "__main__":
    # connect to UR5
    rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")
    # Initialize the gripper
    gripper = GripperController()
    time.sleep(1)
    # activate the gripper
    gripper.activate()
    robot = object2hand.Grasp()
    time.sleep(1)

    # home position
    joint = [0.3726655840873718, -1.9479101339923304, -2.0182421843158167, -0.388007942830221, -4.712571684514181, 0.3080361485481262]
    rtde_c.moveJ(joint, 0.1, 0.1, True)
    time.sleep(7)
    print("initialization complete")

    pose = [0.50578725, -0.11622101, -0.1252573, -2.43400031, -1.78595081, -0.38446344]

    # 抓取
    print("moving to above the object")
    pose[2] += 0.2
    hand2base = robot.object_to_hand(pose)
    rtde_c.moveL(hand2base, 0.1, 0.1, True)
    time.sleep(5)

    print("open gripper")
    gripper = GripperController()
    gripper.open_gripper()

    print("start to grasp")
    pose[2] -= 0.225
    hand2base = robot.object_to_hand(pose)
    rtde_c.moveL(hand2base, 0.1, 0.1, True)
    time.sleep(5)

    print("close gripper")
    gripper = GripperController()
    gripper.close_gripper()

    # pick object
    print("pick object")
    pose[2] += 0.25
    hand2base = robot.object_to_hand(pose)
    rtde_c.moveL(hand2base, 0.1, 0.1, True)
    time.sleep(5)

    # home position
    print("back to home position")
    pose = [0.5429566900711207, 0.09506155877620812, 0.15241717904557417, -2.0500864359149493, 1.921806832795989, -0.2192187264597655]
    rtde_c.moveL(pose, 0.1, 0.1, True)
    time.sleep(10)

    print("Task finished")