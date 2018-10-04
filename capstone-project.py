from boltiot import Bolt, Email
import credentials
import json, time


mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
mailer = Email(credentials.MAILGUN_API_KEY, credentials.SANDBOX_URL, credentials.SENDER_EMAIL, credentials.RECIPIENT_EMAIL)
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
    try:
        if ldr_value <300 and pb_value == 1:
            print("Door is Closed")
            response = mailer.send_email("Alert","The Current door state is: CLOSE")
        if ldr_value > 301 and ldr_value<1000 and pb_value == 0:
            print("Door is half open")
            response = mailer.send_email("Alert","The Current door state is: HALF-OPEN")
        if ldr_value > 1000 and pb_value == 0:
            print("Door is open")
            response = mailer.send_email("Alert","The Current door state is: OPEN")
    except Exception as e:
        print("Error",e)
    time.sleep(10)
