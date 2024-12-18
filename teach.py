import rtde_control

"""
Teach Mode
"""
# connect to UR5
rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")

print("choose teach mode? ")
option = input("y/n: ")

if option == 'y':
    # Enable teach mode
    rtde_c.teachMode()
elif option == 'n':
    # Disable teach mode
    rtde_c.endTeachMode()
else:
    print("Invalid input")