import rtde_receive

"""
obtain the real-time status of UR5
"""
# connect to UR5
rtde_r = rtde_receive.RTDEControlInterface("192.168.1.254")
status = rtde_r.getRobotStatus()

print(status)