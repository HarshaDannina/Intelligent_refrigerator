from boltiot import Bolt
import credentials
import json

mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
N = True

while N:
    response = mybolt.isOnline()
    print(response)
    ldr_response = mybolt.analogRead('A0')
    pb_response = mybolt.digitalRead('1')
    data = json.loads(ldr_response)
    print(data['value'])
    print(ldr_response)
    print(pb_response)
    N = False
    
