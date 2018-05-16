from network import LoRa
import socket
import time
import binascii

class LoRaNetwork:
    def __init__(self):
        lora = LoRa(mode=LoRa.LORAWAN, frequency=868000000)
        #lora.init(mode=LoRa.LORAWAN, frequency=868000000,sf=12)
        self.loraSocket = None

        print("MacAddress: ",[hex(x) for x in lora.mac()])

        app_eui = binascii.unhexlify('e5 e0 55 68 56 80 43 24'.replace(' ',''))
        app_key = binascii.unhexlify('a3 51 5e 56 2a 69 1e ea 50 f5 4e 18 d0 6c 54 a4'.replace(' ',''))

        if not lora.has_joined():
            while not lora.has_joined():
                lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0,dr=1)
                time.sleep(6)
                print('Not yet joined...')
        # create a LoRa socket
        self.loraSocket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # set the LoRaWAN data rate
        self.loraSocket.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)


    def send(self,sendBytes):
        self.loraSocket.send(sendBytes)

if __name__ == '__main__':
    loraNet = LoRaNetwork()
    loraNet.send('Hello World')
