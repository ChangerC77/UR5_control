import rtde_control

""" turn off UR5"""
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")

rtde_c.stopScript()
