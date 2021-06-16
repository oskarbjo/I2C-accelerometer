# IMU testing I2C

# CONNECTIONS:
# RASPI VERSION 3A+

# RASPI PIN 1 --> SENSOR VDD
# RASPI PIN 3 --> SENSOR SDA
# RASPI PIN 5 --> SENSOR SCL
# RASPI PIN 17 --> SENSOR CS
# RASPI PIN 39 --> SENSOR GND

import smbus
import time
from registers import *
import numpy as np

class IMU_class:
    def __init__(self):
        print('Setup...')
        self.setupRegisters()
        self.Npts = 100
        self.OUTX_XL_dec_list = np.zeros(self.Npts)
        self.OUTY_XL_dec_list = np.zeros(self.Npts)
        self.OUTZ_XL_dec_list = np.zeros(self.Npts)
        self.OUTX_G_dec_list = np.zeros(self.Npts)
        self.OUTY_G_dec_list = np.zeros(self.Npts)
        self.OUTZ_G_dec_list = np.zeros(self.Npts)
        self.OUTX_XL_dec = 0
        self.OUTY_XL_dec = 0
        self.OUTZ_XL_dec = 0
        self.OUTX_G_dec = 0
        self.OUTY_G_dec = 0
        self.OUTZ_G_dec = 0
        
    def updateSensorValues(self):

        self.readSensorRegisters()
        self.updateValueLists()
    
        self.printValues()
    
    def updateValueLists(self):
        self.OUTX_XL_dec_list=np.roll(self.OUTX_XL_dec_list,-1)
        self.OUTY_XL_dec_list=np.roll(self.OUTY_XL_dec_list,-1)
        self.OUTZ_XL_dec_list=np.roll(self.OUTZ_XL_dec_list,-1)
        self.OUTX_G_dec_list=np.roll(self.OUTX_G_dec_list,-1)
        self.OUTY_G_dec_list=np.roll(self.OUTY_G_dec_list,-1)
        self.OUTZ_G_dec_list=np.roll(self.OUTZ_G_dec_list,-1)
        self.OUTX_XL_dec_list[-1]=(self.OUTX_XL_dec)
        self.OUTY_XL_dec_list[-1]=(self.OUTY_XL_dec)
        self.OUTZ_XL_dec_list[-1]=(self.OUTZ_XL_dec)
        self.OUTX_G_dec_list[-1]=(self.OUTX_G_dec)
        self.OUTY_G_dec_list[-1]=(self.OUTY_G_dec)
        self.OUTZ_G_dec_list[-1]=(self.OUTZ_G_dec)
        
    def readSensorRegisters(self):

        OUTX_G_dec_LSB=bus.read_byte_data(I2C_device_address,OUTX_L_G)
        OUTX_G_dec_MSB=bus.read_byte_data(I2C_device_address,OUTX_H_G)
        OUTX_G_bin = '{0:08b}'.format(OUTX_G_dec_MSB) + '{0:08b}'.format(OUTX_G_dec_LSB)
        self.OUTX_G_dec = self.twos_comp(int(OUTX_G_bin,2),len(OUTX_G_bin))
        
        OUTY_G_dec_LSB=bus.read_byte_data(I2C_device_address,OUTY_L_G)
        OUTY_G_dec_MSB=bus.read_byte_data(I2C_device_address,OUTY_H_G)
        OUTY_G_bin = '{0:08b}'.format(OUTY_G_dec_MSB) + '{0:08b}'.format(OUTY_G_dec_LSB)
        self.OUTY_G_dec = self.twos_comp(int(OUTY_G_bin,2),len(OUTY_G_bin))
        
        OUTZ_G_dec_LSB=bus.read_byte_data(I2C_device_address,OUTZ_L_G)
        OUTZ_G_dec_MSB=bus.read_byte_data(I2C_device_address,OUTZ_H_G)
        OUTZ_G_bin = '{0:08b}'.format(OUTZ_G_dec_MSB) + '{0:08b}'.format(OUTZ_G_dec_LSB)
        self.OUTZ_G_dec = self.twos_comp(int(OUTZ_G_bin,2),len(OUTZ_G_bin))
        
        OUTX_XL_dec_LSB=bus.read_byte_data(I2C_device_address,OUTX_L_XL)
        OUTX_XL_dec_MSB=bus.read_byte_data(I2C_device_address,OUTX_H_XL)
        OUTX_XL_bin = '{0:08b}'.format(OUTX_XL_dec_MSB) + '{0:08b}'.format(OUTX_XL_dec_LSB)
        self.OUTX_XL_dec = self.twos_comp(int(OUTX_XL_bin,2),len(OUTX_XL_bin))
        
        OUTY_XL_dec_LSB=bus.read_byte_data(I2C_device_address,OUTY_L_XL)
        OUTY_XL_dec_MSB=bus.read_byte_data(I2C_device_address,OUTY_H_XL)
        OUTY_XL_bin = '{0:08b}'.format(OUTY_XL_dec_MSB) + '{0:08b}'.format(OUTY_XL_dec_LSB)
        self.OUTY_XL_dec = self.twos_comp(int(OUTY_XL_bin,2),len(OUTY_XL_bin))
        
        OUTZ_XL_dec_LSB=bus.read_byte_data(I2C_device_address,OUTZ_L_XL)
        OUTZ_XL_dec_MSB=bus.read_byte_data(I2C_device_address,OUTZ_H_XL)
        OUTZ_XL_bin = '{0:08b}'.format(OUTZ_XL_dec_MSB) + '{0:08b}'.format(OUTZ_XL_dec_LSB)
        self.OUTZ_XL_dec = self.twos_comp(int(OUTZ_XL_bin,2),len(OUTZ_XL_bin))
        #self.OUTY_XL_dec
        #self.OUTZ_XL_dec
        #self.OUTX_G_dec
        #self.OUTY_G_dec
        #self.OUTZ_G_dec
        
    def setupRegisters(self):
        bus.write_byte_data(I2C_device_address,CTRL1_XL,CTRL1_XL_settings)
        bus.write_byte_data(I2C_device_address,CTRL2_G,CTRL2_G_settings)
        print('wrote settings')
        
    def printValues(self):
        print('OUTX_XL = ' + str(self.OUTX_XL_dec),end='')
        print(', OUTY_XL = ' + str(self.OUTY_XL_dec),end='')
        print(', OUTZ_XL = ' + str(self.OUTZ_XL_dec))
        print('OUTX_G = ' + str(self.OUTX_G_dec),end='')
        print(', OUTY_G = ' + str(self.OUTY_G_dec),end='')
        print(', OUTZ_G = ' + str(self.OUTZ_G_dec))
    
    def twos_comp(self,val,bits):
        if(val & (1 << (bits - 1))) != 0:
            val = val - (1<<bits)
        return val

