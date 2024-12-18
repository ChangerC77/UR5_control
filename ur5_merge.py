import rtde_control
import time
import numpy as np
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os
import sys
# 获取当前文件的绝对路径
path = os.path.abspath('/home/ros/EncoSmart/UR5/merge')
# 将该目录添加到模块搜索路径中
sys.path.append(path)
from rename import Rename
from cal_normal import SurfaceNormalCalculator

"""
GaussianGrasper获取rgbd和机械臂pose数据的代码
"""

bridge = CvBridge()

# 文件命名
date = '0228'

# 计数器
index = 1
rgb_frame_counter = index
depth_frame_counter = index

# 处理的深度法向数量
depth_num = 16

# 相机depth内参
fx, fy = 387.4676208496094, 387.4676208496094

rgbd_file = '/home/ros/EncoSmart/UR5/pcl_merge_data{}'.format(date)
hand2base_file = '{}/hand2base.txt'.format(rgbd_file, date)
rgb_file = '{}/images'.format(rgbd_file, date)
depth_file = '{}/depth'.format(rgbd_file, date)

def aliged_camera():
    rospy.init_node("UR5")
    print("开始订阅rgbd信息")
    global rgb_sub
    global depth_sub
    rgb_sub = rospy.Subscriber('/camera/color/image_raw', Image, rgb_callback)
    depth_sub = rospy.Subscriber('/camera/aligned_depth_to_color/image_raw', Image, depth_callback)

def rgb_callback(msg):
    """存储rgb信息"""
    global rgb_frame_counter
    rgb_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imwrite('{}/images/images_{}.png'.format(rgbd_file, rgb_frame_counter), rgb_image)
    print("rgb保存成功")
    rgb_frame_counter += 1
    rgb_sub.unregister()
    
def depth_callback(msg):
    """存储depth信息"""
    global depth_frame_counter
    depth_image = bridge.imgmsg_to_cv2(msg, "32FC1")
    depth = np.array(depth_image)
    np.save('{}/depth/images_{}.npy'.format(rgbd_file, depth_frame_counter), depth)
    print("depth保存成功")
    depth_frame_counter += 1
    depth_sub.unregister()

def ur5():
    global rtde_c
    rtde_c = rtde_control.RTDEControlInterface("192.168.1.254")
    i = index
    
    # 1
    print("移动到第{}个pose\n".format(i))
    # print("移动到第1个pose\n")
    rtde_c.moveJ([1.7185090780258179, -1.5271137396441858, -2.552955929433004, -0.9868724981891077, -5.274666372929708, 2.814455509185791], 0.15, 0.15, True)
    time.sleep(3)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 2
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([1.4429723024368286, -1.4453147093402308, -2.253622357045309, -1.2355063597308558, -5.3074162046061915, 2.8144075870513916], 0.15, 0.15, True)
    time.sleep(6)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 3
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([1.5703469514846802, -2.1252673308001917, -1.819416348134176, -1.2979825178729456, -5.345413331185476, 3.143738031387329], 0.15, 0.15, True)
    time.sleep(12)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 4
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([1.1343646049499512, -1.7401936689959925, -1.6322653929339808, -1.4848740736590784, -5.123782340680258, 2.843855857849121], 0.15, 0.15, True)
    time.sleep(12)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(15) 

    # pose = [0.38043770425771123, 0.47830488521957615, 0.15510945942243176, 0.04981035867086542, 2.8155190312644445, -0.7892360168141537]
    # rtde_c.moveL(pose, 0.15, 0.15, True)
    # time.sleep(10)

    # 5
    print("移动到第{}个pose\n".format(i))
    # print("移动到第5个pose\n")
    rtde_c.moveJ([1.1734538078308105, -2.995054546986715, -0.051426235829488576, -2.32638389268984, -5.165791932736532, 3.5350403785705566], 0.15, 0.15, True)
    time.sleep(17)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 6
    print("移动到第{}个pose\n".format(i))
    # 61是高视角：
    # 高视角pose: 0.6322686392486864, 0.489954447541122, 0.40112127243145496, 1.4364815190823759, 2.6931653041409116, -0.229985078527779
    # 高视角joint: 0.8083779215812683, -2.5473039785968226, -0.15508634248842412, -2.133606735860006, -4.830277744923727, 3.3664913177490234]
    # 62是低视角：
    # 低视角pose: 0.6364323135508081, 0.49428347074963247, 0.3143735480351556, 1.4286181209533002, 2.7164647359724667, -0.5245889349774693
    # 低视角joint: 0.8083659410476685, -2.5472920576678675, -0.3508809248553675, -2.133582417164938, -4.83026618162264, 3.366443395614624
    rtde_c.moveJ([0.8083659410476685, -2.5473278204547327, -0.3508685270892542, -2.1335704962359827, -4.830301705990927, 3.3664913177490234], 0.15, 0.15, True)
    time.sleep(10)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 7
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([0.6199413537979126, -2.9297030607806605, -0.014569107686178029, -2.2760022322284144, -4.7066301743136805, 3.893589735031128], 0.15, 0.15, True)
    time.sleep(8)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 8
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([0.4021598994731903, -2.777099911366598, -0.014437500630513966, -2.193270508443014, -4.6129165331469935, 4.224498748779297], 0.15, 0.15, True)
    time.sleep(5)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 9
    print("移动到第{}个pose\n".format(i))
    # print("移动到第9个pose\n")
    rtde_c.moveJ([0.2123316377401352, -3.018264118825094, 0.05966329574584961, -2.2367642561541956, -4.440553013478414, 4.388139247894287], 0.15, 0.15, True)
    time.sleep(6)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 10
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([0.004842375870794058, -2.8253710905658167, 0.05888509750366211, -2.404638115559713, -4.395784083996908, 4.692892074584961], 0.15, 0.15, True)
    time.sleep(16)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 11
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([-0.2310708204852503, -3.08205491701235, 0.05941200256347656, -2.317707363759176, -4.205175224934713, 4.604343414306641], 0.15, 0.15, True)
    time.sleep(16)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 12
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([-0.2896340529071253, -2.298774067555563, -0.94965106645693, -1.8881304899798792, -4.119175497685568, 4.9704508781433105], 0.15, 0.15, True)
    time.sleep(16)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 13
    print("移动到第{}个pose\n".format(i))
    # print("移动到第13个pose\n")
    rtde_c.moveJ([-0.5874045530902308, -2.0703333059894007, -2.0355218092547815, -0.7800105253802698, -3.9576991240130823, 4.979300498962402], 0.15, 0.15, True)
    time.sleep(12)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3)

    # 14
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([-0.7036235968219202, -1.739678208027975, -2.5291343371020716, -0.28542834917177373, -3.8384397665606897, 5.4412689208984375], 0.15, 0.15, True)
    time.sleep(12)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 15
    print("移动到第{}个pose\n".format(i))
    # print("移动到第15个pose\n")
    rtde_c.moveJ([0.12542690336704254, -1.6821325461017054, -1.6213963667498987, -1.3228886763202112, -4.522842351590292, -0.10836202303041631], 0.15, 0.15, True)
    # time.sleep(10)
    time.sleep(40)
    print("获取点云")
    aliged_camera()
    i += 1
    time.sleep(3) 

    # 16
    print("移动到第{}个pose\n".format(i))
    rtde_c.moveJ([0.36286211013793945, -1.6809571425067347, -1.6215289274798792, -1.3722685019122522, -4.714991394673483, 1.7655085325241089], 0.15, 0.15, True)
    time.sleep(16)
    print("获取点云")
    aliged_camera()
    time.sleep(3) 

if __name__ == "__main__":
    try:   
        ur5()
        # 获取rgbd数据
        # aliged_camera()
        print("UR5任务结束!")

        print("开始处理数据")
        # 处理images
        rename = Rename(rgb_file)
        # 调用 process_files 方法处理指定目录中的文件
        rename.process_files()

        # 处理depth
        rename = Rename(depth_file)
        # 调用 process_files 方法处理指定目录中的文件
        rename.process_files()

        # 处理深度法向
        calculator = SurfaceNormalCalculator(date, depth_num, hand2base_file, fx, fy, rgbd_file)
        calculator.calculate_surface_normals()
        print("数据处理完成!")
        print("任务结束!")

    except KeyboardInterrupt:
        print("Control Interrupted!")
        rtde_c.servoStop()
        rtde_c.stopScript()
        rgb_sub.unregister()
        depth_sub.unregister()