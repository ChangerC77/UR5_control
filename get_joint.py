import rtde_receive

"""
obtain joint 
"""
# connect to UR5
rtde_r = rtde_receive.RTDEReceiveInterface("192.168.1.254")

# obtain actual joint angles
actual_q = rtde_r.getActualQ()
print("actual_q: ")
print(actual_q)