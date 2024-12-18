import rtde_control

"""
joint angle control
"""
# connect to UR5
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")

joint = [0.11099452525377274, -1.4082754294024866, -1.20119554201235, 4.240013122558594, -4.585250918065206, 0.09134938567876816]

rtde_c.moveJ(joint, 0.2, 0.2, True) # joint, linear speed, angular speed
