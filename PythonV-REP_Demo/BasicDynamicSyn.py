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

## 设置仿真步长，为了保持API端与V-rep端相同步长
#vrep.simxSetFloatingParameter(clientID, vrep.sim_floatparam_simulation_time_step, tstep, vrep.simx_opmode_oneshot)
## 然后打开同步模式
#vrep.simxSynchronous(clientID, True)
##开启仿真
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

jointHandle = np.zeros((jointNum,), dtype=np.int) # 注意是整型
for i in range(jointNum):
    errorCode, returnHandle = vrep.simxGetObjectHandle(clientID, jointName + str(i+1), vrep.simx_opmode_blocking)
    jointHandle[i] = returnHandle
    time.sleep(2)


print('Handles available!') 

# 然后首次读取关节的初始值，以streaming的形式
jointConfig = np.zeros((jointNum,))
for i in range(jointNum):
     _, jpos = vrep.simxGetJointPosition(clientID, jointHandle[i], vrep.simx_opmode_streaming)
     jointConfig[i] = jpos

lastCmdTime=vrep.simxGetLastCmdTime(clientID)  # 记录当前时间
vrep.simxSynchronousTrigger(clientID)  # 让仿真走一步

# 开始仿真
initConfig = [0, 22.5*RAD2DEG, 67.5*RAD2DEG, 0, -90*RAD2DEG, 0]


vrep.simxPauseCommunication(clientID, 1)
vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 11, vrep.simx_opmode_oneshot)
for i in range(jointNum):
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+str(i), initConfig[i], vrep.simx_opmode_oneshot)
vrep.simxPauseCommunication(clientID, 0)
    
#while vrep.simxGetConnectionId(clientID) != -1:
#
#    #保证仿真进行完成
#    currCmdTime=vrep.simxGetLastCmdTime(clientID)  # 记录当前时间
#    dt = currCmdTime - lastCmdTime # 记录时间间隔，用于控制
#    lastCmdTime=currCmdTime    # 记录当前时间
#    vrep.simxSynchronousTrigger(clientID)  # 进行下一步
#    vrep.simxGetPingTime(clientID)    # 使得该仿真步走完
#    #仿真进行完成读取状态
#    # 读取当前的状态值，之后都用buffer形式读取
#    for i in range(jointNum):
#        _, jpos = vrep.simxGetJointPosition(clientID, jointHandle[i], vrep.simx_opmode_buffer)
#        #print(round(jpos * RAD2DEG, 2))
#        jointConfig[i] = jpos



    




