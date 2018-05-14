from network import Bluetooth
from LIS2HH12 import LIS2HH12 # accelerometer
from pytrack import Pytrack
import L76GNSS
import time
import struct

ble_device_name = "MIUN_SmartCity"
manufacturer_data = "MIUN_STC"
private_UUID = b'824509384udrfi59'

service_acc_UUID = 0x00
character_acc_x_UUID=0x01
character_acc_y_UUID=0x02
character_acc_z_UUID=0x03

service_synchroize_UUID = 0x04
character_synchroize_new_UUID=0x05

class bluetooth:
    def __init__(self):
        self.bluetooth = Bluetooth()
        self.bluetooth.set_advertisement(name=ble_device_name, manufacturer_data=manufacturer_data, service_data=None, service_uuid=private_UUID)
        self.bluetooth.advertise(True)

        #service_acc
        self.service_acc = self.bluetooth.service(uuid = service_acc_UUID,isprimary=True, nbr_chars=3, start=True)
        self.character_acc_x = self.service_acc.characteristic(uuid=character_acc_x_UUID, properties=None, value=33)
        self.character_acc_y = self.service_acc.characteristic(uuid=character_acc_y_UUID, properties=None, value=34)
        self.character_acc_z = self.service_acc.characteristic(uuid=character_acc_z_UUID, properties=None, value=35)

    def updateValue(self,accelerate=None,gps=None):
        if(accelerate != None):
            float_bytes = struct.pack('f', accelerate[0])
            #print(float_bytes)
            print(accelerate[0],accelerate[1],accelerate[2])
            total_bytes = b''
            total_bytes = struct.pack('<f',accelerate[0])+struct.pack('<f',accelerate[1])+struct.pack('<f',accelerate[2])+struct.pack('<f',gps[0])+struct.pack('<f',gps[1])

            self.character_acc_x.value(total_bytes)
            self.character_acc_y.value(total_bytes)
            self.character_acc_z.value(total_bytes)

class accelerometer:
    def __init__(self):
        self.acc = LIS2HH12()

    def getAccelerate(self):
        return self.acc.acceleration()

class gps:
    def __init__(self):
        self.gps = gps = L76GNSS.L76GNSS(pytrack=Pytrack(),sda='P22', scl='P21')

    def getValue(self):
        return self.gps.coordinates(debug=True)


if __name__ == '__main__':
    ble = bluetooth()
    acc = accelerometer()
    gpsHandle = gps()
    while True:
        ble.updateValue(accelerate=acc.getAccelerate(),gps=(0,0))
        time.sleep_ms(100)
