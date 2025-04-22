import os
from twilio.rest import Client

account_sid = "ACe3e7e82ff52556487ef6d26c13b1256c"
auth_token = "2a596bc72dd19687d065ea7c971d4b93"
twilio_number = "+17604770561"
client = Client(account_sid,auth_token)
call = client.calls.create(
    twiml=r"""<Response><Say voice="Polly.Amy">Thanks for trying our documentation. Enjoy!</Say><Play>https://7eef-2401-4900-8844-6641-d1c2-a3b6-80a5-e3a0.ngrok-free.app/audio</Play></Response>""",
    to = "+919759279921",
    from_=twilio_number
)
print(call.sid)