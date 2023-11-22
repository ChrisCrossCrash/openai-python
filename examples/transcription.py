from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

client = OpenAI()

if __name__ == "__main__":
    with open(f"{Path(__file__).parent}/../data/recording.mp3", "rb") as f:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=f)

    print(transcript.text)
