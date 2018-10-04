from boltiot import Bolt
import credentials
import json, time

bright = 800
dim_min = 200
dim_max = 799
dark = 200

mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
N = True

while N:
    ldr_response = mybolt.analogRead('A0')
    pb_response = mybolt.digitalRead('1')
    ldr_data = json.loads(ldr_response)
    pb_data = json.loads(pb_response)
    print(ldr_data['value'])
    ldr_value = int(ldr_data['value'])
    print(pb_data['value'])
    pb_value = int(pb_data['value'])
    
    if ldr_value <200 and pb_value == 1:
        print("Door is Closed")
    if ldr_value > 201 and ldr_value<1000 and pb_value == 0:
        print("Door is half open")
    if ldr_value > 1000 and pb_value == 0:
        print("Door is open")
    N = False
