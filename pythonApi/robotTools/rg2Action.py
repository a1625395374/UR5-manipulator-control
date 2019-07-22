res = rg2Action(clientID,gripperSign )
# rg2Action Open or Close the RG2 in the vrep sence
# icecube: the icecube object
# gripperSign: gripperSign, true for close while false for open
# res: the returned code

if gripperSign
    # Close
    res = vrep.simxSetIntegerSignal(clientID,'RG2CMD',1,vrep.simx_opmode_blocking)
else
    # Open
    res = vrep.simxSetIntegerSignal(clientID,'RG2CMD',0,vrep.simx_opmode_blocking)

vrchk(res)
time.sleep(2)




