import time
import _thread as thread
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

def read():
    while True:
        resp = ser.readline().decode()
        print(resp, end='')


thread.start_new_thread(read, ())


r = 100
g = 100
b = 100
speed = 4
idx = 0 
while True:
    msg = f'on:{idx}:{r}:{g}:{b}:200:{speed}'
    ser.write(msg.encode())
    time.sleep(3.2)
    msg = f'on:{idx}:{r}:{g}:{b}:000:{speed}'
    ser.write(msg.encode())
    time.sleep(2.2)
    # idx = (idx + 1) % 3
