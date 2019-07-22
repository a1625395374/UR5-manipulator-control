def res = stop(clientID)
# stop Stop the running simulation
# res; the returned code (You can check it by vrchk())

res = vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 01, vrep.simx_opmode_blocking)
time.sleep(0.5)