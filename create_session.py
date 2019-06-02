from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

session = client.proxy.services(service.sid) \
                      .sessions \
                      .create(unique_name='20 Minutes Session')

print(session.sid)
print(service.sid)
