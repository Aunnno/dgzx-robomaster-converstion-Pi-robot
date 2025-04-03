def conv_init():#初始化连接函数
     serial_ctrl.serial_config(115200,"cs8","none",1)#设置基本连接参数
     serial_ctrl.write_number(1001) #尝试连接，发送测试字符
     return bool(serial_ctrl.read_line()) #返回连接结果
def send(skill_num1,verif):#发送技能编号和校验码
    serial_ctrl.write_numbers(skill_num1,verif)
    return bool(serial_ctrl.read_line())#返回发送结果
def main():
   if not conv_init():#调用函数同时检验结果，下同
       print("fail")
       return 0
   skill_num=0
   if not send(skill_num,1):
       print("fail")
       return 0