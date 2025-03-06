from twilio.rest import Client
from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AAC85c2cbf4e4b764aedb966296d1f7d901'
auth_token = '46d249e4149b40c573179dedc66d8a4c'
client = Client(account_sid, auth_token)

def makeCall():
    call = client.calls.create(
        to='+919342359946',
        from_='+12567279885',
        url='https://handler.twilio.com/twiml/EH1af8791565610bef02c47acb9ebce021' + urlencode(
            {'Message': "hey sorry to say that application has failed"})
        # url = 'https://www.twilio.com/console/twiml-bins/EHfbb90737b757304c9b3cbcb81ba73770'

    )

    print(call.sid)
    call_sid = call.sid

    time.sleep(30)

    call = client.calls(call_sid).fetch()
    print(call.status)


def sendSMS(msg):
    message = client.messages \
        .create(
        body=msg,
        from_='+12567279885',
        to='+919342359946'
    )

    print(message.sid)

