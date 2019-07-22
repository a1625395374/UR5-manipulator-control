# -*- coding:utf-8 -*-
import vrep

vrep.simxFinish(-1)  # 关掉之前的连接
clientId = vrep.simxStart("127.0.0.1", 19999, True, True, 5000, 5)  # 建立和服务器的连接
if clientId != -1:  # 连接成功
    print('connect successfully')
else:
    print('connect failed')
vrep.simxFinish(clientId)
print('program ended')