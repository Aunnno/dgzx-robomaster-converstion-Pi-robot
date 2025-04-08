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
def conv_init():#握手函数
    accept=int(ser.readline()) #选择永久堵塞，因为你树莓派在比赛的时候毕竟是一直开着的
    if accept==1001:
        print("连接成功")
        ser.write(1001)
        return 1
    
def heart(num):#心跳函数
    accept=ser.readline(1.5)#1.5秒超时
    if len(accept)!=0:
       ser.write(num)
    else:
        print("连接丢失")

def connect(num):
    conv_init()
    while heart(num):#这个num主要是给heart函数传数据，主程序定义
        continue

# 关闭串口
ser.close()