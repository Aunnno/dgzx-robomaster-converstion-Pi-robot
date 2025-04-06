serial_ctrl.serial_config(115200,"cs8","none",1)#设置基本连接参数
def conv_init():#握手
     serial_ctrl.write_number(1001) #尝试连接，发送测试字符
     accept=serial_ctrl.read_line(10.0) #返回连接结果
     if len(accept)==0:
         return False
     else:
         return int(accept)
     
def heart():#心跳
    serial_ctrl.write_number(1002)#发送心跳数据包
    accept=serial_ctrl.read_line(1.5)#接收返回值
    if len(accept)==0:
        return False
    else:
        return accept
    
def send(skill_num1,verif):#发送技能编号和校验码
    serial_ctrl.write_numbers(skill_num1,verif)
    accept=serial_ctrl.read_line(1.5)
    if len(accept)==0:
         return False
    elif accept==1001:
         return True
    
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
    
def main():
   if not conv_init():#调用函数同时检验结果，下同
       print("连接失败")
       return 0
   skill_num=0
   if not send(skill_num,1003):
       print("技能启动失败")
       return 0
   accept=heart()
   while inv(accept):
        accept=heart()
        continue
      