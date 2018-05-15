from network import Bluetooth
import time

ble_device_name = "MIUN_SmartCity"
manufacturer_data = "MIUN_STC"
private_UUID = b'824509384udrfi59'

service_acc_UUID = 0x00
character_acc_x_UUID=0x00
character_acc_y_UUID=0x01
character_acc_z_UUID=0x02

class ble:
    def __init__(self):
        self.bluetooth = Bluetooth()
        self.bluetooth.set_advertisement(name=ble_device_name, manufacturer_data=manufacturer_data, service_data=None, service_uuid=private_UUID)
        self.bluetooth.advertise(True)

        #service
        self.service_acc = self.bluetooth.service(uuid = service_acc_UUID,isprimary=True, nbr_chars=3, start=True)
        self.character_acc_x = self.service_acc.characteristic(uuid=character_acc_x_UUID, properties=None, value=33)
        self.character_acc_y = self.service_acc.characteristic(uuid=character_acc_y_UUID, properties=None, value=34)
        self.character_acc_z = self.service_acc.characteristic(uuid=character_acc_z_UUID, properties=None, value=35)

    def updateValue(self,accelerate=None):
        if(accelerate != None):
            self.character_acc_x.value(accelerate[0])
            self.character_acc_y.value(accelerate[1])
            self.character_acc_z.value(accelerate[2])

if __name__ == '__main__':
    ble = stc_ble()
    i = 0
    while True:
        ble.updateValue(accelerate=(i,i+1,i+2))
        i = i+1
        time.sleep(2)
