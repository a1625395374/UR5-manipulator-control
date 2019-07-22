def res = start(clientID,timeout,step)
#start Start a simulation
# res; the returned code (You can check it by vrchk())

res = vrep.simxStartSimulation(clientID, vrep.simx_opmode_blocking)
vrchk(res)

i = 0
ur5ready = 0
while (i < obj.TIMEOUT and ur5ready == 0):
    i = i + 1
    [res, ur5ready] = vrep.simxGetIntegerSignal(clientID,'UR5READY',vrep.simx_opmode_blocking);
    vrchk(res)
    pause(step)


if i>= obj.TIMEOUT:
    print('An error occurred in your V-REP server')
    vrep.simxFinish(obj.clientID)
    vrep.delete()
    res = vrep.simx_error_timeout_flag
else:
    print('V-REP is started.')
    res = vrep.simx_error_noerror
