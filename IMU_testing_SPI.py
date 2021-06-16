import spidev
from time import sleep

spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz=10
spi.threewire = False
#to_send = [0b00010000,0b00000000] #Acc. and gyro control register CTRL1_XL
#to_send = [0b00000000,0b00000000]
to_send1 = 0b00101000 #Accelerometer output register 1
to_send2 = 0b00101001 #Accelerometer output register 2
to_send3 = 0b00101010 #Accelerometer output register 3
to_send4 = 0b00101011 #Accelerometer output register 4
to_send = [to_send1,to_send2,to_send3,to_send4]
#to_send = [0b00001111,0b01101001] #Who I am ID

print(to_send)
msg=spi.xfer(to_send)
print(msg)

while True:
    msg=spi.xfer(to_send)
    print(msg)
    sleep(0.1)