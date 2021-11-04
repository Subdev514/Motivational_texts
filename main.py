from twilio.rest import Client
import random
# Importing module that are needed

account_sid = 'YOUR TWILIO ACOUNT.SID HERE'
auth_token = 'YOUR TWILIO AUTH_TOKEN HERE'
client = Client(account_sid, auth_token)
# Your accountsid and token goes here

with open('texts.txt') as file:
    result = file.readlines()
# Storing every line of motivatiobal_texts.txt in result

sms = str((' '.join(random.choices(result))))
# Formating sting

message = client.messages.create(
    to="REPLACE THIS WITH THE NBUMBER U WANT TO SEND MSGS TO", 
    from_="REPLACE THIS NUMBER WITH THE NUMBER U WERE GIVEN FROM TWILIO",
    body=sms)
#Sending the msg
