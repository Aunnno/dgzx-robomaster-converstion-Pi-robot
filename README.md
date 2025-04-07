## dgzx-robomaster-Pi-robot
一个*开源*的树莓派与ROBOMASTER机器人通讯的仓库
*By Team EOR from DGZX*
### 一、项目结构
#### 1.PC-To-Robot
* pc-to-robot.py
操作端代码
####
### 二、代码解析

#### 1.PC-To-Robot

  ##### pc-to-robot.py

  (1) ``conv_init()``

```py
def conv_init():#握手
     serial_ctrl.write_number(1001) #尝试连接，发送测试字符
     accept=serial_ctrl.read_line(10.0) #返回连接结果
     if len(accept)==0:
         return False
     else:
         return int(accept)
```