# Download the helper library from https://www.twilio.com/docs/python/install
# import os to ensure credentials secured
import os

from twilio.rest import Client
messagebody = "hi"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=messagebody,
                     from_=os.environ['TWILIO_SMS_FROM'],
                     to='+19254781531'
                 )

print(message.sid)


