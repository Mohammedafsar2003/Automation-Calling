from twilio.rest import Client
from urllib.parse import urlencode
import time
import os


fvar = open(r'phone_nums.txt','r')
phone_nums = [x.strip('\n') for x in fvar.readlines()]
fvar.close()




def callnow():

    account_sid = 'AC85c2cbf4e4b764aedb966296d1f7d901'
    auth_token = '46d249e4149b40c573179dedc66d8a4c'
    twilio_from  = '+18454098127'
    client = Client(account_sid, auth_token)

    print(phone_nums)
    
    for num in phone_nums:
        print("Num = " , num)
        call = client.calls.create(
                                twiml='<Response><Say>Practice Python well all guys</Say></Response>',
                                to=num,
                                from_=twilio_from,
                                #url = 'https://handler.twilio.com/twiml/EHfbb90737b757304c9b3cbcb81ba73770?' + urlencode({category:dict_msg[category]})
                                )

        print(call.sid)
        call_sid = call.sid

        time.sleep(30)

        call = client.calls(call_sid).fetch()
        call_status = call.status

        print(" Call status ===== > " , call_status)

        if(call_status == "completed"):
            print(" Call has been aswered by " , num)
        else:
            print(num , "dint pick the call trying the next persion in the list ")

        


callnow()






























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
