#!/usr/bin/env python
# encoding: utf-8

"""
PegInHole
use the scene：UR5PegInHole2.ttt

@Author: Zane
@Contact: ely.hzb@gmail.com
@File: forceSensor.py   
@Time: 2019-07-31 15:55
"""
import vrep
import sys
import numpy as np
import math
import matplotlib.pyplot as mpl
import time



sensorName = 'UR5_connection'


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

errorCode, returnHandle = vrep.simxGetObjectHandle(clientID, sensorName, vrep.simx_opmode_blocking)
forceSensorHandle = returnHandle

print('Handles available!') 


# 开始仿真
while vrep.simxGetConnectionId(clientID) != -1:
    errorCode,state,forceVector,torqueVector=vrep.simxReadForceSensor(clientID,forceSensorHandle,vrep.simx_opmode_streaming)
    time.sleep(2)
    errorCode,state,forceVector,torqueVector=vrep.simxReadForceSensor(clientID,forceSensorHandle,vrep.simx_opmode_buffer)
    print(forceVector)
    print(torqueVector)
