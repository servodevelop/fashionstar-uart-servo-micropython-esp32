'''
FashionStar Uart舵机 
> Python SDK舵机角度查询 Example <
--------------------------------------------------
- 作者: 阿凯
- Email: kyle.xing@fashionstar.com.hk
- 更新时间: 2021-06-04
--------------------------------------------------
'''
from machine import UART
from uservo import UartServoManager
import time

# 舵机个数
# 注：舵机ID编号 假定是依次递增的
# 例: [0, 1, 2, ..., srv_num-1]
servo_num = 1
# 要测试的舵机ID
servo_id = 0

# 创建串口对象 使用串口2作为控制对象
# 波特率: 115200
# RX: gpio 16
# TX: gpio 17
uart = UART(2, baudrate=115200)
# 创建舵机管理器
uservo = UartServoManager(uart, srv_num=servo_num)

# 设置舵机为阻尼模式
uservo.set_damping(servo_id, 500)

# 舵机角度查询
while True:
    angle = uservo.query_servo_angle(servo_id)
    print("当前舵机角度: {:4.1f} °".format(angle), end='\r')
    time.sleep(1)

