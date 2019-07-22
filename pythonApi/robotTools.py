def ur5MoveToJointPosition(clientID, targetPositions ):
    '''
    # ur5MoveToJointPosition Reflexes Motion Library - Joint space
    # targetPositions: 1 x 6 vector, the target joint positions
    '''
    vrep.simxPauseCommunication(clientID, 1)
    vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 11, vrep.simx_opmode_oneshot)
    for i in range(6):
        vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+int2str(i), targetPositions(i), vrep.simx_opmode_oneshot)
    vrep.simxPauseCommunication(clientID, 0)
    wait()

def ur5MoveToConfiguration(clientID,targetPosition,targetQuaternion)
    '''
    # ur5MoveToConfiguration Reflexxes Motion Library - Move by ik group
    # targetPosition: 1 x 3 vector, the target xyz position
    # targetQuaternion: 1 x 4 vector, the target quaternion
    '''

    targetQuaternion = toVREPQuat(targetQuaternion)
    vrep.simxPauseCommunication(clientID, 1)

    #??? 'ICECUBE_0'  vrep.simx_opmode_oneshot
    vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 21, vrep.simx_opmode_oneshot)

    for i in range(3):
        vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+int2str(i), targetPosition(i), vrep.simx_opmode_oneshot)

    for i in range(4,7):
        vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+int2str(i), targetQuaternion(i-3), vrep.simx_opmode_oneshot)

    vrep.simxPauseCommunication(clientID, 0)

    wait()

def ur5GetIKTipQuaternion(icecube):
    '''
    # ur5GetIKTipQuaternion Get UR5's ikTip's quaternion from the V-REP scene
    # icecube: the icecube object
    # tipQuat: the quaternion of UR5's ikTip
    '''
    # ??? handles.ur5ikTip
    res,tipQuat= vrep.simxGetObjectQuaternion(clientID, handles.ur5ikTip, -1, vrep.simx_opmode_blocking)
    vrchk(res)
    tipQuat = toMATLABQuat(tipQuat)
    return tipQuat

def rg2Action(clientID,gripperSign):
    '''
    # rg2Action Open or Close the RG2 in the vrep sence
    # icecube: the icecube object
    # gripperSign: gripperSign, true for close while false for open
    # res: the returned code
    '''

    if gripperSign:
        # Close
        res = vrep.simxSetIntegerSignal(clientID,'RG2CMD',1,vrep.simx_opmode_blocking)
    else:
        # Open
        res = vrep.simxSetIntegerSignal(clientID,'RG2CMD',0,vrep.simx_opmode_blocking)

    vrchk(res)
    time.sleep(2)

    return res


