## dgzx-robomaster-Pi-robot
一个*开源*的树莓派与ROBOMASTER机器人通讯的仓库
*By Team EOR from DGZX*
***
### 一、项目结构
#### 1.PC-To-Robot
* pc-to-robot.py
操作端代码
#### 2.Pi-And-Robot/Connect
* Connect.py
树莓派与机器人通信代码
***
### 二、大致思路
#### 1.机器人端
机器人端通信框架都是一样的，每个技能只需要改一下技能编码就行了
先进行握手，握手完毕后走心跳程序，由于技能开启后选手操作端能够进行的操作只有切断技能，所以写了一个心跳函数，让机器人每隔一定时间就会给树莓派发数据并检查返回代码，没返回就是似了，具体的返回代码对应表见后文[编码对照表](#四、编码对照表)
#### 2.树莓派端
和上边基本差不多，只是握手和心跳程序都是接收并返回，同时会从main()程序中读一个返回代码表示正常心跳（其他代码见下表）。目前只是写成接收一个num,后面会改成从main()中读一个值（因为Connect()函数会单独分一个线程出来）
***
* 为什么要写print()一些东西呢，明明比赛的时候看不见，当然是为了调试用啊
***
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

  * 握手程序，等待时间10s

  (1) ``send(skill_num)``

  ```py
  def send(skill_num):#发送技能编号
    serial_ctrl.write_number(skill_num)
    accept=serial_ctrl.read_line(1.5)
    if len(accept)==0:
        return False
    elif int(accept)==1001:
        return True
    elif int(accept)==1102:
        print("技能启动失败")
        return False
    elif int(accept)==1103:
        print("技能执行失败")
        return False
  ```

* skill_num技能编号，接着有个等待返回代码的程序，1.5s超时

  (2)``inv(accept)``
  ```py
  def inv(accept):
    if accept!=False:    #为什么要写报错提示呢主要是为了方便调试
        if accept==1001:
                return 1
        elif accept==1102:
                print("技能启动失败")
                return 0
        elif accept==1103:
                print("技能执行失败")
                return 0
        elif accept==1003:
                print("技能启动成功")
                return 1
        elif accept==1004:
                print("技能关闭")
                return 0
        elif accept==1005:
                print("通信结束")
                return 0
    else:
        print("连接丢失")
        return 0
  ```
  * 编码返回bool值并打印对应提示
  ***
#### 2.Pi-And-Robot

  ##### /Pi-And-Robot/Connect/Connect.py
  (1)
```py
import serial

ser = serial.Serial()

# 配置串口 波特率 115200，数据位 8 位，1 个停止位，无校验位，超时时间 0.2 秒
ser.port = 'COM3'
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.parity = serial.PARITY_NONE
ser.timeout = 0.2

# 打开串口
ser.open()
```
* 配置串口 波特率 115200，数据位 8 位，1 个停止位，无校验位，超时时间 0.2 秒

(2)```conv_init()```

```py
def conv_init():#握手函数
    accept=int(ser.readline()) #选择永久堵塞，因为你树莓派在比赛的时候毕竟是一直开着的
    if accept==1001:
        print("连接成功")
        ser.write(1001)
        return 1
```

* 永久堵塞，因为你树比赛的时候树莓派会提前打开
* 接收握手编码并返回
(2)```heart(num)```
```py
def heart(num):#心跳函数
    accept=ser.readline(1.5)#1.5秒超时
    if len(accept)!=0:
        ser.write(num)
        return 1
    else:
        print("连接丢失")
        return 0
```
* 心跳函数，1.5s未接收到信息就超时

### 四、编码对照表
#### 通信编码
<table>
  <tr>
  <th>编码</th>
  <th>含义</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>握手</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>心跳</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>技能启动</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>技能关闭</td>
  </tr>
  <tr>
    <td>1005</td>
    <td>结束通信</td>
  </tr>
</table>

#### 错误代码
<table>
  <tr>
  <th>编码</th>
  <th>含义</th>
  </tr>
  <tr>
    <td>1100</td>
    <td>一切正常</td>
  </tr>
  <tr>
    <td>1101</td>
    <td>连接失败</td>
  </tr>
  </tr>
  <tr>
    <td>1102</td>
    <td>技能启动失败</td>
  </tr>
  <tr>
    <td>1103</td>
    <td>技能执行失败</td>
  </tr>
</table>