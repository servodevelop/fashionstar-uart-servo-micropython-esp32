'''
FashionStar Uart舵机 
> 气泵开关控制 <
--------------------------------------------------
- 作者: 阿凯
- Email: kyle.xing@fashionstar.com.hk
- 更新时间: 2021-06-04
--------------------------------------------------
'''
from machine import UART
from uservo import UartServoManager
import ustruct
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

def pump_value(uservo, value):
	param_bytes = ustruct.pack('<BhHH', 0xFE, int(value*10), int(0), int(0))
	uservo.send_request(uservo.CODE_SET_SERVO_ANGLE, param_bytes)
	
def pump_on(uservo):
	'''气泵打开'''
	pump_value(uservo, -90.0)

def pump_off(uservo):
	'''气泵关闭'''
	pump_value(uservo, 0.0) 
	time.sleep(0.1)
	pump_value(uservo, 90.0) 
	time.sleep(0.5)
	pump_value(uservo, 0.0) 

# 气泵打开
pump_on(uservo)
# 延时5s
time.sleep(5)
# 气泵关闭
pump_off(uservo)