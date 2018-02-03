import pyfirmata
from time import sleep
LED=13
PORT="/dev/cu.usbmodem14421" #PORT可任意修改,Windows為COM 1/2/3...
board=pyfirmata.Arduino(PORT)


def arduino_do(par):
    if par == '開燈':
        print("啊堆妞開燈")
        board.digital[LED].write(1)
    elif par == '關燈':
        print("啊堆妞關燈")
        board.digital[LED].write(0)
    else:
        print("啊堆妞不知道要幹嘛")
        pass
