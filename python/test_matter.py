from matter_sdk import MatterDevice
from matter_sdk import *

# Initialize the Matter device
device = MatterDevice("127.0.0.1", 5540, "20202021", "3840")

# Test the control function
response = device.control("turn_on")
print("Response:", response)
