import pycom
from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
import time


py = Pytrack()
acc = LIS2HH12()

def getAccelerate():
    return (acc.x[0],acc.y[0],acc.z[0])

'''
while True:
    print("x:",acc.x[0],",y:",acc.y[0],",z:",acc.z[0])
    pitch = acc.pitch()
    roll = acc.roll()
    print("pitch:",pitch,",","roll:",roll)
    time.sleep_ms(100)
'''
