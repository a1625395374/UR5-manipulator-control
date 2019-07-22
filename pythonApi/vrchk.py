def vrchk(vrep, res, buffer)
# Checks VREP return code. Set buffer to 1 if you are reading from a buffered
# call
inputVar = func.__code__.co_argcount

if inputVar < 3:
    buffer = false

if inputVar < 2:
    print（"error：Missing arguments."）
    return

expl = 'Undefined error'





if inputVar < 3:
    buffer = false;
  end
  if (inputVar < 2),
    error('Missing arguments.');
  end
  
  expl = 'Undefined error';
  
  if res == vrep.simx_error_noerror,
    % Nothing to say
    return;
  elseif res == vrep.simx_error_novalue_flag,
    if buffer,
      % No problem to report
      return;
    else
      expl = 'There is no command reply in the input buffer. This should not always be considered as an error, depending on the selected operation mode';
    end
  elseif res == vrep.simx_error_timeout_flag,
    expl = 'The function timed out (probably the network is down or too slow)';
  elseif res == vrep.simx_error_illegal_opmode_flag,
    expl = 'The specified operation mode is not supported for the given function';
  elseif res == vrep.simx_error_remote_error_flag,
    expl = 'The function caused an error on the server side (e.g. an invalid handle was specified)';
  elseif res == vrep.simx_error_split_progress_flag,
    expl = 'The communication thread is still processing previous split command of the same type';
  elseif res == vrep.simx_error_local_error_flag,
    expl = 'The function caused an error on the client side';
  elseif res == vrep.simx_error_initialize_error_flag,
    expl = 'simxStart was not yet called';
  end
  error(sprintf('Remote API function call returned with error code: %d. Explanation: %s.\n', res, expl));
 
end

