from pydub import AudioSegment
import whisper

def convert_ulaw_to_wav(ulaw_file, wav_file):
    audio = AudioSegment.from_file(ulaw_file, format="ulaw", codec="pcm_mulaw")
    audio.export(wav_file, format="wav")
    print(f"Converted to {wav_file}")


def transcribe_audio(wav_file):
    model = whisper.load_model("base")
    result = model.transcribe(wav_file)
    print("Transcription:")
    print(result["text"])