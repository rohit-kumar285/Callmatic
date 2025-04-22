from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import PlainTextResponse
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Start, Stream,Say
from dotenv import load_dotenv
import base64
import json
import os

load_dotenv()

ngrok_url = os.environ["ngrok_url"]
app = FastAPI()

# Replace these with your actual Twilio credentials and numbers
ACCOUNT_SID = "ACe3e7e82ff52556487ef6d26c13b1256c"
AUTH_TOKEN = "2a596bc72dd19687d065ea7c971d4b93"
TWILIO_NUMBER = "+17604770561"
TO_NUMBER = "+919759279921"  # Your number to test the call

client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.get("/make-call")
def make_call():
    call = client.calls.create(
        to=TO_NUMBER,
        from_=TWILIO_NUMBER,
        url=f"{ngrok_url}/voice"
    )
    return {"status": "calling", "sid": call.sid}


@app.post("/voice", response_class=PlainTextResponse)
async def voice_handler():
    response = VoiceResponse()

    start = Start()
    stream = Stream(url=f"wss://{ngrok_url}/transcript")
    start.append(stream)
    response.append(start)

    response.say("Hello! I am your assistant. How can I help you?")
    
    return PlainTextResponse(str(response), media_type="application/xml")

@app.post("/transcript")
async def transcript_listener(request: Request):
    data = await request.json()
    print("🔠 Transcript Event:", data)

    transcript = data.get("transcription", {}).get("text", "")
    if transcript:
        print("🧠 USER SAID:", transcript)

        # TODO: Feed to LLM and respond

    return {"status": "received"}
