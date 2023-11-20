from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

if __name__ == "__main__":
    with open("../data/recording.mp3", "rb") as f:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=f)

    print(transcript.text)
