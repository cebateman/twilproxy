import sys
from twilio.rest import Client
import uuid

account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

def create_proxy():
    client = Client(account_sid, auth_token)
    service = client.proxy.services.create(unique_name='Session_Test1'+ str(uuid.uuid1()))
    session = client.proxy.services(service.sid) \
                          .sessions \
                          .create(unique_name='20 Minutes Session'+ str(uuid.uuid1()))

    print(session.sid)
    print(service.sid)
    if session.sid != None and service.sid != None:
        participant = client.proxy \
                            .services(service.sid) \
                            .sessions(session.sid) \
                            .participants \
                            .create(friendly_name='Caller1', identifier='+12537929893')
        print('created participant:')
        print(participant.sid)
        print(participant.proxy_identifier)
    else:
        print('failed to create participant homieeee')


def main(argv):
    print('yolo main')
    arg_1 = argv[0]
    arg_2 = argv[1]
    print(arg_1)
    print(arg_2)
    create_proxy()

if __name__ == '__main__':
    main(sys.argv[1:])
