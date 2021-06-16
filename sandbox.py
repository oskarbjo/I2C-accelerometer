from IMU_I2C_class import *
import smbus
import time
from registers import *
import numpy as np
#a=127
#b='{0:08b}'.format(a)
#print(b)

#def twos_comp(val,bits):
#    if(val & (1 << (bits - 1))) != 0:
#        val = val - (1<<bits)
#    return val

#value=twos_comp(int(b,2),len(b))
#print(value)
msg1 = bus.read_byte_data(I2C_device_address,CTRL1_XL)
print(msg1)
bus.write_byte_data(I2C_device_address,CTRL1_XL,CTRL1_XL_settings)
bus.write_byte_data(I2C_device_address,CTRL2_G,CTRL2_G_settings)
msg1 = bus.read_byte_data(I2C_device_address,CTRL1_XL)
print(msg1)
OUTX_G_dec_LSB=bus.read_byte_data(I2C_device_address,OUTX_L_G)
print(OUTX_G_dec_LSB)
