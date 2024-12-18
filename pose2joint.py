import rtde_receive
import rtde_control

"""
By obtaining the end-effector's 6-DOF pose, solve for the joint angles through inverse kinematics.
"""

# connect to UR5
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")


pose = [0.63471878, 0.54662782, -0.06191026, -0.6017871, 2.70580886, 0.11460755]
# Take the joint angles from the kinematic inverse solution
joint = rtde_c.getInverseKinematics(pose)
print("joint: ")
print(joint)