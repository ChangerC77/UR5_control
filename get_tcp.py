import rtde_control

""" obtain current tcp pose """

# connect to UR5
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")
tcp = rtde_c.getTCPOffset()
print("current tcp pose: ", tcp)