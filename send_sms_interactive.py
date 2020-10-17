# Download the helper library from https://www.twilio.com/docs/python/install
# import os to ensure credentials secured
import os

from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

phone = input("Phone as '+1##########'")

messagebody = input("What do you want to say in ''?")

message = client.messages \
                .create(
                     body=messagebody,
                     from_=os.environ['TWILIO_SMS_FROM'],
                     to=phone
                 )

print(message.sid)


