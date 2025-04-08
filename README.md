## dgzx-robomaster-Pi-robot
一个*开源*的树莓派与ROBOMASTER机器人通讯的仓库
*By Team EOR from DGZX*
### 一、项目结构
#### 1.PC-To-Robot
* pc-to-robot.py
操作端代码
#### 2.Pi-And-Robot/Connect
* Connect.py
树莓派与机器人通信代码
### 二、大致思路
#### 1.机器人端
机器人端通信框架都是一样的，每个技能只需要改一下技能编码就行了
先进行握手，握手完毕后走心跳程序，由于技能开启后选手操作端能够进行的操作只有切断技能，所以写了一个心跳函数，让机器人每隔一定时间就会给树莓派发数据并检查返回代码，没返回就是似了，具体的返回代码对应表见后文
#### 2.树莓派端
和上边基本差不多，只是握手和心跳程序都是接收并返回，同时会从main()程序中读一个返回代码表示正常心跳（其他代码见下表）。目前只是写成接收一个num,后面会改成从main()中读一个值（因为Connect()函数会单独分一个线程出来）

* 为什么要写print()一些东西呢，明明比赛的时候看不见，当然是为了调试用啊
### 三、代码解析

#### 1.PC-To-Robot

  ##### /PC-To-Robot/pc-to-robot.py

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

  握手程序，等待时间10s

  (1) ``send(skill_num)``

  ```py
  def send(skill_num):#发送技能编号
    serial_ctrl.write_number(skill_num)
    accept=serial_ctrl.read_line(1.5)
    if len(accept)==0:
         return False
    elif accept==1001:
         return True
  ```

  skill_num技能编号，接着有个等待返回代码的程序，1.5s超时