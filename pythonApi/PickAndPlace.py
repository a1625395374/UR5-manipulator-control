# Description：A simple pick-and-place demo （Python）
# use 'scenes\UR5PickAndPlace.ttt'.
# Author:Zebin Huang
# Date:2019.07.22
from __future__ import division

try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
import numpy as np
import math
import vrepToolbox
#-------------------------Init

print('Program started')

vrep.simxFinish(-1) # 关闭潜在的连接

while True:
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)# 每隔0.2s检测一次，直到连接上V-rep
    if clientID > -1:
        break
    else:
        time.sleep(0.2)
        print("Failed connecting to remote API server!")
print("Connection success!")

#-------------------------Configuration
jointNum = 6
objectNum = 2
#--------Get UR5's handles
jointNames = ('UR5_joint1','UR5_joint2','UR5_joint3','UR5_joint4','UR5_joint5','UR5_joint6')
objectNames = ('Toy1','Toy2')
HandleUr5Joints = np.zeros((jointNum,), dtype=np.int) # 注意是整型
HandleObjects = np.zeros((objectNum,), dtype=np.int) # 注意是整型

for i in range(jointNum):
    res, returnJointHandle = vrep.simxGetObjectHandle(clientID, jointNames[i], vrep.simx_opmode_blocking)
    HandleUr5Joints[i] = returnJointHandle
    vrchk(res)
end

#--------Get objects' handles
for i in range(objectNum):
    res, returnObjectHandle = vrep.simxGetObjectHandle(clientID, objectNames[i], vrep.simx_opmode_blocking)
    HandleObjects[i] = returnObjectHandle
    vrchk(res)
end


#--------Get the objects' position

#这里存在返回值与矩阵加法运算的问题
res, initPosition = vrep.simxGetObjectPosition(clientID, HandleObjects[1], obj.vrep.simx_opmode_blocking)
initPosition = initPosition + array([0,0,0.002])
vrchk(res)

res, targetPosition = vrep.simxGetObjectPosition(clientID, HandleObjects[1], obj.vrep.simx_opmode_blocking)
targetPosition = targetPosition + array([0,0,0.005])
vrchk(res)


#--------Move it

#--------Start simulation
start(clientID,timeout,step)
#！！！考虑用全局变量或者是结构体优化

#--------Move to initial configuration
initConfig = array([0, pi/8, pi/2-pi/8, 0, -pi/2, 0])
ur5MoveToJointPosition(clientID,initConfig)
tempQuat = ur5GetIKTipQuaternion(icecube)
time.sleep(1)

#--------Move to initPosition
ur5MoveToConfiguration(clientID,initPosition,tempQuat)
time.sleep(1)
toPage(clientID,1)
time.sleep(1)

#--------Close the gripper
rg2Action(clientID,true)
time.sleep(0.5)

#--------Move to targetPosition
ur5MoveToConfiguration(clientID,targetPosition,tempQuat)
time.sleep(1)

#--------Open the gripper
rg2Action(icecube,false)
time.sleep(1)
toPage(clientID,1)
time.sleep(1)

#--------Stop and delete

stop(clientID)
delete(clientID)