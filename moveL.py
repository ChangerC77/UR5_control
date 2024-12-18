import rtde_control

"""
6 Dof pose control
"""
# connect to UR5
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")

pose = [0.5429566900711207, 0.09506155877620812, 0.15241717904557417, -2.0500864359149493, 1.921806832795989, -0.2192187264597655]

rtde_c.moveL(pose, 0.1, 0.1, True)