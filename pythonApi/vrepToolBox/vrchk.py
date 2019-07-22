def vrchk(res, buffer)
# Checks VREP return code. Set buffer to 1 if you are reading from a buffered
# call
inputVar = func.__code__.co_argcount

if inputVar < 2:
    buffer = false

if inputVar < 1:
    print（"error：Missing arguments."）
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