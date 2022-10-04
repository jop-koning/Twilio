# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['ACf44693fbd093dc7ec262fbd20f4b3f70']
#auth_token = os.environ['26c888a4fe64eb985a9f9d86ffd169c3']
#client = Client(account_sid, auth_token)

client = Client("ACf44693fbd093dc7ec262fbd20f4b3f70", "26c888a4fe64eb985a9f9d86ffd169c3")

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+31638475605',
                        from_='+13024052418'
                    )

print(call.sid)
