def res = toPage(pageNum )
# toPage To the new VREP page
# pageNum: the number of the page to view
# res: the returned code


res = vrep.simxSetIntegerParameter(clientID, vrep.sim_intparam_current_page, pageNum, vrep.simx_opmode_blocking)
vrchk(res)

