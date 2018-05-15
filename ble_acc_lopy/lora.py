from network import LoRa
import socket
import time
import binascii

class LoRaNetwork:
    def __init__(self):
        lora = LoRa(mode=LoRa.LORAWAN, frequency=868000000)
        self.loraSocket = None

        print("MacAddress: ",[hex(x) for x in lora.mac()])

        app_eui = binascii.unhexlify('00 00 00 00 00 00 00 00'.replace(' ',''))
        app_key = binascii.unhexlify('00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'.replace(' ',''))

        if not lora.has_joined():
            while not lora.has_joined():
                lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
                time.sleep(6)
                print('Not yet joined...')
        # create a LoRa socket
        self.loraSocket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        # set the LoRaWAN data rate
        self.loraSocket.setsockopt(socket.SOL_LORA, socket.SO_DR, 2)


    def send(self):
        self.loraSocket.send(sendBytes)

if __name__ == '__main__':
    loraNet = LoRaNetwork()
    loraNet.send('Hello World')
