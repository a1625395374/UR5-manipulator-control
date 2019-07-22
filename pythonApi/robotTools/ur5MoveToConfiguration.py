def ur5MoveToConfiguration(clientID,targetPosition,targetQuaternion)

# ur5MoveToConfiguration Reflexxes Motion Library - Move by ik group
# targetPosition: 1 x 3 vector, the target xyz position
# targetQuaternion: 1 x 4 vector, the target quaternion

targetQuaternion = toVREPQuat(targetQuaternion)
vrep.simxPauseCommunication(clientID, 1)

#??? 'ICECUBE_0'  vrep.simx_opmode_oneshot
vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 21, vrep.simx_opmode_oneshot)

for i = 1:3:
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+int2str(i), targetPosition(i), vrep.simx_opmode_oneshot)

for i = 4:7
    vrep.simxSetFloatSignal(clientID, 'ICECUBE_'+int2str(i), targetQuaternion(i-3), vrep.simx_opmode_oneshot)

vrep.simxPauseCommunication(clientID, 0)

wait()

