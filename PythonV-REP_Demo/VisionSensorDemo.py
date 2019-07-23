#!/usr/bin/env python
# encoding: utf-8

"""
Enable the vision sensor in V-REP,Python
use the scene：VisionSensorDemo.ttt

@Author: Zane
@Contact: ely.hzb@gmail.com
@File: VisionSensorDemo.py
@Time: 2019-07-23 15:55
"""
import vrep
import sys
import numpy as np
import math
import matplotlib.pyplot as mpl


def main():
    PI = math.pi

    #Python connect to the V-REP client
    vrep.simxFinish(-1)

    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

    if clientID != -1:
        print("Connected to remote API server")
    else:
        print("Connection not successful")
        sys.exit("Connected failed,program ended!")

    #Get the handle of vision sensor
    errorCode,visionSensorHandle=vrep.simxGetObjectHandle(clientID,'Vision_sensor',vrep.simx_opmode_oneshot_wait)

    #Get the image of vision sensor
    image=vrep.simxGetVisionSensorImage(clientID,visionSensorHandle,1,vrep.simx_opmode_streaming)

    #Process the image to the format (64,64,3)
    sensorImage=[]
    sensorImage=np.array(image,dtype=np.uint8)
    sensorImage.resize([resolution[0],resolution[1],3])

    #Use matplotlib.imshow to show the image
    mpl.imshow(sensorImage,origin='lower')


if __name__ == '__main__':
    main()