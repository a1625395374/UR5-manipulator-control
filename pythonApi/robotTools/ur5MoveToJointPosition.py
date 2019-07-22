def ur5MoveToJointPosition(clientID, targetPositions )
# ur5MoveToJointPosition Reflexes Motion Library - Joint space
# targetPositions: 1 x 6 vector, the target joint positions

vrep.simxPauseCommunication(clientID, 1)
vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 11, vrep.simx_opmode_oneshot)
for i in range(6):
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+int2str(i), targetPositions(i), vrep.simx_opmode_oneshot)
vrep.simxPauseCommunication(clientID, 0)
wait()

