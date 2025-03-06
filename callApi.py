# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'AC85c2cbf4e4b764aedb966296d1f7d901'
auth_token = '46d249e4149b40c573179dedc66d8a4c'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        to='+919342359946',
                        # from_='+12567279885',
                        from_='+18454098127',
                        url = 'https://handler.twilio.com/twiml/EH1af8791565610bef02c47acb9ebce021' + urlencode({'Message': "Incident INC12345 assigned to you "})
                        
                    )

print(call.sid)
call_sid = call.sid

time.sleep(60)

call = client.calls(call_sid).fetch()
print(call.status)





# List all the call log from twilio API

'''client = Client(account_sid, auth_token)
calls = client.calls.list(limit=20)

for record in calls:
    print(record.sid)
'''

# You can also filter the results. This example only returns phone calls to the phone number "+16698001727" which had a call status of "busy" but you can filter on other call properties as well.

'''calls = client.calls.list(status='busy', to='+917411694426', limit=20)

for record in calls:
    print(record.sid)
'''

### check the status of the call for the SID ...

'''
call = client.calls('CAad384f2b2a0ca98ac8ac66211fe18334').fetch()
print(call.status)
'''

