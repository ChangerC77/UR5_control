import rtde_control
import numpy as np
from scipy.spatial.transform import Rotation as R # coordinate transform library

"""
calculate grasping pose based on the object's 6Dof pose
"""

class Grasp:
    def __init__(self, ip_address="192.168.1.254"):
        # Initialize the robot arm control interface
        # self.rtde_c = rtde_control.RTDEControlInterface(ip_address)
        print("Robot arm initialized")

    def object_to_hand(self, pose):
        # Convert rotation vector to rotation matrix
        r_v = R.from_rotvec(np.array(pose)[-3:]).as_matrix()

        # Create the homogeneous matrix representing the transformation from gripper to base
        gripper2base = np.zeros((4, 4))
        gripper2base[:3, :3] = r_v
        gripper2base[:3, 3] = np.array(pose)[:3]
        gripper2base[3, 3] = 1

        # Create the homogeneous matrix representing the transformation from gripper to hand
        gripper2hand = np.array([[0, -1, 0, 0],
                                 [1,  0, 0, 0],
                                 [0,  0, 1, 0.19],
                                 [0,  0, 0, 1]])
        
        # Calculate the transformation matrix from hand to base
        hand2base = np.dot(gripper2base, np.linalg.inv(gripper2hand))

        # Extract the translation vector from the homogeneous matrix
        x, y, z = hand2base[:3, 3]
        # Extract the rotation matrix from the homogeneous matrix
        hand2base_rm = hand2base[:3, :3]
        # Convert the rotation matrix to a rotation vector
        r = R.from_matrix(hand2base_rm)
        rotation_vector = R.as_rotvec(r)
        rx, ry, rz = rotation_vector[:]
        # Create a new pose vector
        hand2base = [x, y, z, rx, ry, rz]
        return hand2base

if __name__ == "__main__":
    pose = [0.37120065, 0.3290028, -0.09201958, -2.5305735, -1.46514482, -0.72384019]

    robot = Grasp()
    robot.object_to_hand(pose)
