from boltiot import Bolt, Email
import credentials
import json, time
import dtree

mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
mailer = Email(credentials.MAILGUN_API_KEY, credentials.SANDBOX_URL, credentials.SENDER_EMAIL, credentials.RECIPIENT_EMAIL)
previous_state = 0
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
    
    state = dtree.MachineLearning_model(ldr_value)
    if previous_state != present_state:
            try:
                if pb_value == 1:
                    print("Door is Closed")
                    led_state = mybolt.analogWrite('0','0')
                    response = mailer.send_email("Alert","The Current door state is: CLOSE")
                    
                if present_state == 0 and pb_value == 0:
                    print("Door is half open")
                    led_state = mybolt.analogWrite('0','75')

                if present_state == 1 and pb_value == 0:
                    print("Door is open")
                    led_state = mybolt.analogWrite('0','255')
                    response = mailer.send_email("Alert","The Current door state is: OPEN")
                    
                previous_state = present_state
                
            except Exception as e:
                print("Error",e)
    time.sleep(10)
