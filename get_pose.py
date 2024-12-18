import rtde_receive

"""
obtain 6 Dof Pose
"""
# connect to UR5
rtde_r = rtde_receive.RTDEReceiveInterface("192.168.1.254")

# obtain target TCP(末端位姿) pose
# pose = rtde_r.getTargetTCPPose()
# obtain acutal TCP(末端位姿) pose
pose = rtde_r.getActualTCPPose()
print("getActualTCPPose: ")
print(pose)