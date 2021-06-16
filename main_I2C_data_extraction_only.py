
from IMU_I2C_class import *
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
xdata, ydata = [], []
Npts=50
OUTX_XL_dec_list = np.zeros(Npts)
OUTY_XL_dec_list = np.zeros(Npts)
OUTZ_XL_dec_list = np.zeros(Npts)
OUTX_G_dec_list = np.zeros(Npts)
OUTY_G_dec_list = np.zeros(Npts)
OUTZ_G_dec_list = np.zeros(Npts)
N=1
data=[]
for i in range(0,N):
    data.append([])
lines = [plt.plot([], [])[0] for _ in range(N)]


IMU = IMU_class()
print('List size 1..')
print(IMU.OUTX_XL_dec_list)
x = range(0,IMU.Npts)

def init():
    for line in lines:
        line.set_data([],[])
    ax.set_xlim(0, IMU.Npts)
    ax.set_ylim(-66000, 66000)
    plt.legend(['X acc','Y acc','Z acc','X ang','Y ang', 'Z ang'])
    return lines
    
def update(frame):
    start = time.time()
    IMU.updateSensorValues()
    data[0] = IMU.OUTX_XL_dec_list
    data[1] = IMU.OUTY_XL_dec_list
    data[2] = IMU.OUTZ_XL_dec_list
    data[3] = IMU.OUTX_G_dec_list
    data[4] = IMU.OUTY_G_dec_list
    data[5] = IMU.OUTZ_G_dec_list
    for j,line in enumerate(lines):
        line.set_data(x,data[j])
    end = time.time()
    print('Time elapsed: ',end='')
    print(end - start)
    return lines
    


ani = FuncAnimation(fig, update, frames=IMU.Npts,
                    init_func=init, interval=0.001, blit=True)
plt.show()

