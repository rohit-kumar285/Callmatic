import os
from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_number = ""
client = Client(account_sid,auth_token)
call = client.calls.create(
    twiml=r"""<Response><Say voice="Polly.Amy">Thanks for trying our documentation. Enjoy!</Say><Play>https://7eef-2401-4900-8844-6641-d1c2-a3b6-80a5-e3a0.ngrok-free.app/audio</Play></Response>""",
    to = "",
    from_=twilio_number
)
print(call.sid)