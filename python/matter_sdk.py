import ctypes
import os
import time

class MatterDevice:
    def __init__(self, ip, port, passcode, discriminator):
        self.matter_sdk_lib = ctypes.CDLL('../build/libmatter_sdk.so')  # Path to your shared library
        self.matter_sdk_lib.initialize_device.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
        self.matter_sdk_lib.initialize_device.restype = None
        self.matter_sdk_lib.control_device.argtypes = [ctypes.c_char_p]
        self.matter_sdk_lib.control_device.restype = ctypes.c_char_p

        self.ip = ip
        self.port = port
        self.passcode = passcode
        self.discriminator = discriminator
        self.initialize()

    def initialize(self):
        self.matter_sdk_lib.initialize_device(self.ip.encode('utf-8'), self.port, self.passcode.encode('utf-8'), self.discriminator.encode('utf-8'))
        print("Device initialized.")

    def control(self, command):
        result = self.matter_sdk_lib.control_device(command.encode('utf-8'))
        print("Control result:", result.decode('utf-8'))
        
if __name__ == "__main__":
    device = MatterDevice("127.0.0.1", 5540, "20202021", "3840")
    device.control("turn_on")
