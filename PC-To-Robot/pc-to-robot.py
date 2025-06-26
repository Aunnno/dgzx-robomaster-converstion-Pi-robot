import time
def conv_init():#握手
    print("start conversation")
    serial_ctrl.write_line("1001") #尝试连接，发送测试字符
    serial_ctrl.write_line("1001") 
    # serial_ctrl.write_line("1001") 
    accept=serial_ctrl.read_line(10.0) #返回连接结果
    if len(accept)==0:
        print("conversation fail")
        return False
    else:
        print("conversation start")
        return int(accept)
def heart():#心跳
    serial_ctrl.write_number(1002)#发送心跳代码
    # accept=serial_ctrl.read_line(2)#接收返回值
    # if len(accept)==0:
    #     print("dead")
    #     return False
    # else:
    #     print("heart")
    return True
        # return accept
def send(skill_num):#发送技能编号
    serial_ctrl.write_line("1003")
    serial_ctrl.write_line(int(skill_num))
    # accept=serial_ctrl.read_line(1.5)
    # if len(accept)==0:
    #     return False
    # elif int(accept)==1001:
    #     return True
    # elif int(accept)==1102:
    #     print("fail to start ski")
    #     return False
    # elif int(accept)==1103:
    #     print("技能执行失败")
    #     return False
def start():
    serial_ctrl.serial_config(115200,"cs8","even",1)#设置基本连接参数
    print("start")
    if not conv_init():#调用函数同时检验结果，下同
        print("fail to connect")
        return 0
    skill_num=0
    if not send(skill_num):
        return 0
    while heart():
        time.sleep(0.5)
        continue
# import time
# serial_ctrl.serial_config(115200,"cs8","none",1)#设置基本连接参数
# time_1=0
# time_2=0
# def conv_init():#握手
#      serial_ctrl.write_number(1001) #尝试连接，发送测试字符
#      accept=serial_ctrl.read_line(10.0) #返回连接结果
#      if len(accept)==0:
#          return False
#      else:
#          return int(accept)
     
# def heart():#心跳
#     serial_ctrl.write_number(1002)#发送心跳代码
#     time_1=time.time()
#     accept=serial_ctrl.read_line(2)#接收返回值
#     if len(accept)==0:
#         return False
#     else:
#         return accept
    
# def send(skill_num):#发送技能编号
#     serial_ctrl.write_number(skill_num)
#     accept=serial_ctrl.read_line(1.5)
#     if len(accept)==0:
#         return False
#     elif int(accept)==1001:
#         return True
#     elif int(accept)==1102:
#         print("技能启动失败")
#         return False
#     elif int(accept)==1103:
#         print("技能执行失败")
#         return False
    
# def inv(accept):
#     if accept!=False:    #为什么要写报错提示呢主要是为了方便调试
#         if accept==1001:
#             print("握手成功")
#             return 1
#         elif accept==1002:
#             print("心跳")
#             return 1
#         elif accept==1102:
#             print("技能启动失败")
#             return 0
#         elif accept==1103:
#             print("技能执行失败")
#             return 0
#         elif accept==1003:
#             print("技能启动成功")
#             return 1
#         elif accept==1004:
#             print("技能关闭")
#             return 0
#         elif accept==1005:
#             print("通信结束")
#             return 0
#     else:
#         print("连接丢失")
#         return 0
    
# def main():
#    if not conv_init():#调用函数同时检验结果，下同
#        print("连接失败")
#        return 0
#    skill_num=0
#    if not send(skill_num):
#        return 0
#    accept=heart()
#    while inv(accept):
#         time_2=time.time()
#         if time_2-time_1<=2:
#             time.sleep(time_2-time_1)
#         accept=heart()
#         continue
      