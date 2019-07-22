# Description：A simple pick-and-place demo （Python）
# use 'scenes\UR5PickAndPlace.ttt'.
# Author:Zebin Huang
# Date:2019.07.22


#-------------------------Init

print('Program started')

vrep.simxFinish(-1) # 关闭潜在的连接

while True:
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)# 每隔0.2s检测一次，直到连接上V-rep
    if clientID > -1:
        break
    else:
        time.sleep(0.2)
        print("Failed connecting to remote API server!")
print("Connection success!")

#-------------------------Configuration
jointNum = 6

#--------Get UR5's handles
jointNames = ('UR5_joint1','UR5_joint2','UR5_joint3','UR5_joint4','UR5_joint5','UR5_joint6')
HandleUr5Joints = np.zeros((jointNum,), dtype=np.int) # 注意是整型

for i in range(jointNum):
    res, returnJointHandle = vrep.simxGetObjectHandle(clientID, jointNames(i), vrep.simx_opmode_blocking)
    HandleUr5Joints[i] = returnJointHandle
    vrchk(res)
end




obj.handles.ur5Joints = ur5Joints;











 
% Get the objects' handles
icecube = icecube.getObjectHandle('Toy1');
icecube = icecube.getObjectHandle('Toy2');
 
% Get the objects' position
initPosition = icecube.getObjectPosition('Toy2') + [0,0,0.002];
targetPosition = icecube.getObjectPosition('Toy1') + [0,0,0.05];
 
%% Move it
 
% Start simulation
icecube.start();
 
% Move to initial configuration
initConfig = [0, pi/8, pi/2-pi/8, 0, -pi/2, 0];
ur5MoveToJointPosition(icecube,initConfig);
tempQuat = ur5GetIKTipQuaternion(icecube);
pause(1);
 
% Move to initPosition
ur5MoveToConfiguration(icecube,initPosition,tempQuat);
pause(1);
icecube.toPage(1);
pause(1);
 
% Close the gripper
rg2Action(icecube,true);
pause(0.5);
 
% Move to targetPosition
ur5MoveToConfiguration(icecube,targetPosition,tempQuat);
pause(1);
 
% Open the gripper
rg2Action(icecube,false);
pause(1);
icecube.toPage(0);
pause(1);
 
%% Stop and delete
 
icecube.stop();
icecube.delete();
 
clear ans
