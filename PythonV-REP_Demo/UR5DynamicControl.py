#!/usr/bin/env python
# encoding: utf-8

"""
PegInHole
use the scene：UR5PegInHole2.ttt

@Author: Zane
@Contact: ely.hzb@gmail.com
@File: PegInHole.py
@Time: 2019-07-29 15:55
"""
import vrep
import sys
import numpy as np
import math
import matplotlib.pyplot as mpl
import time

RAD2DEG = 180 / math.pi   # 常数，弧度转度数
tstep = 0.005             # 定义仿真步长
# 配置关节信息
jointNum = 6

jointName = 'UR5_joint'


print('Program started')
# 关闭潜在的连接
vrep.simxFinish(-1)
# 每隔0.2s检测一次，直到连接上V-rep
while True:
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    if clientID > -1:
        break
    else:
        time.sleep(0.2)
        print("Failed connecting to remote API server!")
print("Connection success!")


jointHandle = np.zeros((jointNum,), dtype=np.int) # 注意是整型
for i in range(jointNum):
    errorCode, returnHandle = vrep.simxGetObjectHandle(clientID, jointName + str(i+1), vrep.simx_opmode_blocking)
    jointHandle[i] = returnHandle
    time.sleep(2)

#errorCode, baseHandle = vrep.simxGetObjectHandle(clientID, baseName, vrep.simx_opmode_blocking)

print('Handles available!') 

# 然后首次读取关节的初始值，以streaming的形式
jointConfig = np.zeros((jointNum,))
for i in range(jointNum):
     _, jpos = vrep.simxGetJointPosition(clientID, jointHandle[i], vrep.simx_opmode_streaming)
     jointConfig[i] = jpos


# 开始仿真
while vrep.simxGetConnectionId(clientID) != -1:
    #仿真进行完成读取状态
    # 读取当前的状态值，之后都用buffer形式读取
    for i in range(jointNum):
        _, jpos = vrep.simxGetJointPosition(clientID, jointHandle[i], vrep.simx_opmode_buffer)
        #print(round(jpos * RAD2DEG, 2))
        jointConfig[i] = jpos
        
    #关节空间控制
    # 控制命令需要同时方式，故暂停通信，用于存储所有控制命令一起发送
    initConfig = [0, 22.5, 67.5, 0, -90, 0]
    #vrep.simxPauseCommunication(clientID, True)
    for i in range(jointNum):
        vrep.simxSetJointTargetPosition(clientID, jointHandle[i], initConfig[i] / RAD2DEG, vrep.simx_opmode_oneshot)
    #vrep.simxPauseCommunication(clientID, False)
    #工作空间








#function sysCall_threadmain()
#    jointHandles={-1,-1,-1,-1,-1,-1}
#    for i=1,6,1 do
#        jointHandles[i]=sim.getObjectHandle('UR5_joint'..i)
#    end
#
#    -- Set-up some of the RML vectors:
#    vel=180
#    accel=40
#    jerk=80
#    currentVel={0,0,0,0,0,0,0}
#    currentAccel={0,0,0,0,0,0,0}
#    maxVel={vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180}
#    maxAccel={accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180}
#    maxJerk={jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180}
#    targetVel={0,0,0,0,0,0}
#
#    targetPos1={90*math.pi/180,90*math.pi/180,-90*math.pi/180,90*math.pi/180,90*math.pi/180,90*math.pi/180}
#    sim.rmlMoveToJointPositions(jointHandles,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,targetPos1,targetVel)
#
#    targetPos2={-90*math.pi/180,45*math.pi/180,90*math.pi/180,135*math.pi/180,90*math.pi/180,90*math.pi/180}
#    sim.rmlMoveToJointPositions(jointHandles,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,targetPos2,targetVel)
#
#    targetPos3={0,0,0,0,0,0}
#    sim.rmlMoveToJointPositions(jointHandles,-1,currentVel,currentAccel,maxVel,maxAccel,maxJerk,targetPos3,targetVel)
#end