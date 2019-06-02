# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

participant = client.proxy \
                    .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .sessions('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .participants \
                    .create(friendly_name='Caller1', identifier='+12537929893')

print(participant.sid)
print(participant.proxy_identifier)
