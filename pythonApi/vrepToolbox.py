def toPage(pageNum):
    '''
    # toPage To the new VREP page
    # pageNum: the number of the page to view
    # res: the returned code
    '''
    res = vrep.simxSetIntegerParameter(clientID, vrep.sim_intparam_current_page, pageNum, vrep.simx_opmode_blocking)
    vrchk(res)
    return res

def stop(clientID):
    '''
    # stop Stop the running simulation
    # res; the returned code (You can check it by vrchk())
    '''
    #这里把数字的01改完1，是否有影响？
    res = vrep.simxSetIntegerSignal(clientID, 'ICECUBE_0', 1, vrep.simx_opmode_blocking)
    time.sleep(0.5)
    return res

def delete(clientID):
    '''
    # delete Delete the vrep service
    # res: 0 for no error
    # Never forget to use this function in the end
    '''
    vrep.simxFinish(clientID)
    vrep.delete()
    res = 0
    return res

def start(clientID,timeout,step):
    '''
    #start Start a simulation
    # res; the returned code (You can check it by vrchk())
    '''

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
    return res

def wait(clientID,timeout,step):
    '''
    # wait Wait until the task is done
    # ticks: The number of ticks counted
    '''
    j = 0
    signal = 99
    while (j <= timeout and signal != 0):
        j  = j + 1
        [res, signal] = vrep.simxGetIntegerSignal(clientID, 'ICECUBE_0', vrep.simx_opmode_blocking)
        vrchk(res)
        pause(step)

    ticks = j
    return ticks


def vrchk(res, buffer):
    '''
    # Checks VREP return code. Set buffer to 1 if you are reading from a buffered
    # call
    '''
    inputVar = func.__code__.co_argcount

    if inputVar < 2:
        buffer = false

    if inputVar < 1:
        print("error：Missing arguments.")
        return

    expl = 'Undefined error'

    if res == vrep.simx_error_noerror:
        #noting to say
        return
    elif res == vrep.simx_error_novalue_flag:
        if buffer:
            #no problem to report
            return
        else:
            expl = 'There is no command reply in the input buffer. This should not always be considered as an error, depending on the selected operation mode'
    elif res == vrep.simx_error_timeout_flag:
        expl = 'The function timed out (probably the network is down or too slow)'
    elif res == vrep.simx_error_illegal_opmode_flag:
        expl = 'The specified operation mode is not supported for the given function'
    elif res == vrep.simx_error_remote_error_flag:
        expl = 'The function caused an error on the server side (e.g. an invalid handle was specified)'
    elif res == vrep.simx_error_split_progress_flag:
        expl = 'The communication thread is still processing previous split command of the same type'
    elif res == vrep.simx_error_local_error_flag:
        expl = 'The function caused an error on the client side'
    elif res == vrep.simx_error_initialize_error_flag:
        expl = 'simxStart was not yet called'

    print('Remote API function call returned with error code: %d. Explanation: %s.\n', res, expl)


def toVREPQuat(unitQuat):
    '''
    # toVREPQuat Transform a quaternion of <s,x,y,z> to VREP form (x,y,z,s)
    # unitQuat: the <w,x,y,z> quaternion
    # VREPQuat: the quaternion <x,y,z,s>
    '''
    VREPQuat = numpy.zeros(4)
    VREPQuat(4) = unitQuat(1)
    VREPQuat(1) = unitQuat(2)
    VREPQuat(2) = unitQuat(3)
    VREPQuat(3) = unitQuat(4)
    return VREPQuat

def toMATLABQuat(vrepQuat):
    '''
    # toMATLABQuat Transform a quaternion of VREP form (x,y,z,s) to <s,x,y,z>
    # wxyzQuat: the <s,x,y,z> quaternion
    # VREPQuat: the quaternion <x,y,z,s>
    '''
    sxyzQuat = numpy.zeros(4)
    sxyzQuat(1) = vrepQuat(4)
    sxyzQuat(2) = vrepQuat(1)
    sxyzQuat(3) = vrepQuat(2)
    sxyzQuat(4) = vrepQuat(3)
    return sxyzQuat













