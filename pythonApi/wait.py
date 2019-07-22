def ticks = wait(clientID,timeout,step)
# wait Wait until the task is done
# ticks: The number of ticks counted

j = 0
signal = 99


while (j <= timeout and signal ~= 0):
    j  = j + 1
    [res, signal] = vrep.simxGetIntegerSignal(clientID, 'ICECUBE_0', vrep.simx_opmode_blocking)
    vrchk(res)
    pause(step)

ticks = j


