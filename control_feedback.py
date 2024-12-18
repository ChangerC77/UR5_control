import rtde_control
import rtde_receive
import time

"""
Multi-View closed-loop control program for UR5
"""

# connect to UR5
robot_ip = "192.168.1.254"  # IP address of UR5
rtde_c = rtde_control.RTDEControlInterface(robot_ip)
rtde_r = rtde_receive.RTDEReceiveInterface(robot_ip)

# Target joint position sequence (radians)
joints = [
    # this joint sequence not position sequence !
    [0.20186041295528412, -0.6271708647357386, -1.8644431273089808, 4.522186279296875, -4.64686364332308, 0.09137335419654846],
    [0.20186041295528412, -0.6271708647357386, -1.8644431273089808, 4.522186279296875, -4.64686364332308, 0.09137335419654846]
]

# Set a tolerance for reaching the target position
tolerance = 0.01  # radian

def check_position_reached(target_positions):
    """Check if the target joint position is reached"""
    time.sleep(0.5)
    current_joint_positions = rtde_r.getActualQ()
    position_errors = [abs(current - target) for current, target in zip(current_joint_positions, target_positions)]
    return all(error < tolerance for error in position_errors)

def move_to_positions(target_positions_list):
    """Move to a series of joint positions and provide feedback"""
    for idx, target_positions in enumerate(target_positions_list):
        print(f"Moving to target joint position {idx + 1}: {target_positions}")
        rtde_c.moveJ(target_positions, 0.2, 0.2, True)
        
        while True:
            # Check if the target position is reached
            if check_position_reached(target_positions):
                print(f"Target joint position {idx + 1} reached")
                break
            time.sleep(0.5)
        
        # After reaching the target position, generate feedback and wait for user input
        if process_feedback_signal(idx + 1):
            input("Press Enter to continue to the next joint action...")

def process_feedback_signal(position_index):
    """Process feedback signal"""
    print(f"Processing feedback signal: Joint position {position_index} reached")
    return True

try:
    move_to_positions(joints)
except KeyboardInterrupt:
    print("Program Interrupt!")
finally:
    rtde_c.stopScript()
    rtde_r.disconnect()