from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12184026613',
  to='+919820077642',
  body= "Test SMS",
)

print(message.sid)