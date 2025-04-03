#基本框架直接抄的大疆开发者文档
# -*- encoding: utf-8 -*-
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

while True:

        

        recv = int(ser.readline())#接受初始连接代码
        if recv==1001:#判断是否连接成功
                ser.writelines("1")
                print("Open successfully")
        else:
                print("Fail to connect")


        

# 关闭串口
ser.close()