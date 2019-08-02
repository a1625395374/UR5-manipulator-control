#!/usr/bin/env python
# encoding: utf-8

"""
PegInHole
use the scene：meshImport.ttt

@Author: Zane
@Contact: ely.hzb@gmail.com
@File: IKtest.py
@Time: 2019-07-29 15:55
"""
import vrep
import sys
import numpy as np
import math
import matplotlib.pyplot as mpl
import time

RAD2DEG = math.pi / 180  # 常数，弧度转度数
step = 0.005  # 定义仿真步长
TIMEOUT = 5000

# 配置关节信息
jointNum = 6

jointName = 'UR5_joint'

print('Program started')
# 关闭潜在的连接
vrep.simxFinish(-1)
# 每隔0.2s检测一次，直到连接上V-rep

clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
print("Connection success")

# 开启仿真
vrep.simxStartSimulation(clientID, vrep.simx_opmode_blocking)
print("Simulation start")

i = 0
ur5ready = 0
while i < TIMEOUT and ur5ready == 0:
    i = i + 1
    errorCode, ur5ready = vrep.simxGetIntegerSignal(clientID, 'UR5READY', vrep.simx_opmode_blocking)
    time.sleep(step)

if i >= TIMEOUT:
    print('An error occurred in your V-REP server')
    vrep.simxFinish(clientID)

jointHandle = np.zeros((jointNum,), dtype=np.int)  # 注意是整型
for i in range(jointNum):
    errorCode, returnHandle = vrep.simxGetObjectHandle(clientID, jointName + str(i + 1), vrep.simx_opmode_blocking)
    jointHandle[i] = returnHandle
    time.sleep(2)

errorCode, holeHandle = vrep.simxGetObjectHandle(clientID, 'Hole', vrep.simx_opmode_blocking)
errorCode, ikTipHandle = vrep.simxGetObjectHandle(clientID, 'UR5_ikTip', vrep.simx_opmode_blocking)
errorCode, connectionHandle = vrep.simxGetObjectHandle(clientID, 'UR5_connection', vrep.simx_opmode_blocking)

print('Handles available!')

errorCode, targetPosition = vrep.simxGetObjectPosition(clientID, holeHandle, -1, vrep.simx_opmode_streaming)
time.sleep(0.5)
errorCode, targetPosition = vrep.simxGetObjectPosition(clientID, holeHandle, -1, vrep.simx_opmode_buffer)
print('Position available!')

# 关节空间控制
initConfig = [0, 22.5 * RAD2DEG, 67.5 * RAD2DEG, 0, -90 * RAD2DEG, 0]

vrep.simxPauseCommunication(clientID, True)
for i in range(jointNum):
    vrep.simxSetJointTargetPosition(clientID, jointHandle[i], initConfig[i], vrep.simx_opmode_oneshot)
vrep.simxPauseCommunication(clientID, False)

# Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
vrep.simxGetPingTime(clientID)
time.sleep(1)

errorCode, tipQuat = vrep.simxGetObjectQuaternion(clientID, ikTipHandle, -1, vrep.simx_opmode_blocking)

# tipQuat = toMATLABQuat(tipQuat)

# tipQuat = [0,0,0,0]
#
# tipQuat[0] = tempQuat[3]
# tipQuat[1] = tempQuat[0]
# tipQuat[2] = tempQuat[1]
# tipQuat[3] = tempQuat[2]


targetPosition[2] = targetPosition[2] + 0.15

vrep.simxPauseCommunication(clientID, 1)
vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 21, vrep.simx_opmode_oneshot)
for i in range(1, 4):
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_' + str(i), targetPosition[i - 1], vrep.simx_opmode_oneshot)

for i in range(4, 8):
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_' + str(i), tipQuat[i - 4], vrep.simx_opmode_oneshot)

vrep.simxPauseCommunication(clientID, 0)

j = 0
signal = 99
while j <= TIMEOUT and signal != 0:
    j = j + 1
    errorCode, signal = vrep.simxGetIntegerSignal(clientID, 'ICECUBE_0', vrep.simx_opmode_blocking)
    # obj.vrchk(res);
    time.sleep(step)

ticks = j




targetPosition[2] = targetPosition[2] - 0.05
time.sleep(2)

vrep.simxPauseCommunication(clientID, 1)
vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 21, vrep.simx_opmode_oneshot)
for i in range(1, 4):
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_' + str(i), targetPosition[i - 1], vrep.simx_opmode_oneshot)

for i in range(4, 8):
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_' + str(i), tipQuat[i - 4], vrep.simx_opmode_oneshot)

vrep.simxPauseCommunication(clientID, 0)

j = 0
signal = 99
while j <= TIMEOUT and signal != 0:
    j = j + 1
    errorCode, signal = vrep.simxGetIntegerSignal(clientID, 'ICECUBE_0', vrep.simx_opmode_blocking)
    # obj.vrchk(res);
    time.sleep(step)

ticks = j

# Stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_blocking)

errorCode = vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 1, vrep.simx_opmode_blocking)
time.sleep(0.5)

# Close the connection to V-REP
vrep.simxFinish(clientID)

print('Program end')








