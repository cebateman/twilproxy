# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = '3cf415979ebd15eb846cc9224389fd14'
client = Client(account_sid, auth_token)

message_interaction = client.proxy \
    .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .sessions('KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .participants('KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .message_interactions \
    .create(body='Reply to this message to chat!')

print(message_interaction.sid)
