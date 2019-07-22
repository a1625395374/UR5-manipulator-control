def tipQuat= ur5GetIKTipQuaternion( icecube )
# ur5GetIKTipQuaternion Get UR5's ikTip's quaternion from the V-REP scene
# icecube: the icecube object
# tipQuat: the quaternion of UR5's ikTip


# ??? handles.ur5ikTip

res,tipQuat= vrep.simxGetObjectQuaternion(clientID, handles.ur5ikTip, -1, vrep.simx_opmode_blocking)
vrchk(res)
tipQuat = toMATLABQuat(tipQuat)