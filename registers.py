import time
import smbus

CTRL1_XL = 0x10 #Linear acceleration sensor control register
CTRL2_G = 0x11 #Gyro sensor control register
CTRL1_XL_settings = 0b01100000
CTRL2_G_settings = 0b01100010

OUTX_L_G = 0x22
OUTX_H_G = 0x23
OUTY_L_G = 0x24
OUTY_H_G = 0x25
OUTZ_L_G = 0x26
OUTZ_H_G = 0x27
OUTX_L_XL = 0x28
OUTX_H_XL = 0x29
OUTY_L_XL = 0x2A
OUTY_H_XL = 0x2B
OUTZ_L_XL = 0x2C
OUTZ_H_XL = 0x2D

OUTX_XL_dec_list = []
OUTY_XL_dec_list = []
OUTZ_XL_dec_list = []
OUTX_XL_dec_list = []
OUTY_G_dec_list = []
OUTZ_G_dec_list = []

bus = smbus.SMBus(1)

I2C_device_address = 0x6b #To find address, go to CMD and write sudo i2cdetect -y 1
print('I2C device address: ' + str(I2C_device_address))



