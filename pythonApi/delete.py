def res = delete(clientID)
# delete Delete the vrep service
# res: 0 for no error
# Never forget to use this function in the end

vrep.simxFinish(clientID)
vrep.delete()
res = 0
