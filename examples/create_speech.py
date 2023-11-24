from pathlib import Path
import openai
from dotenv import load_dotenv

load_dotenv()

input = "Good afternoon, gentlemen. I am a HAL 9000 computer. I became operational at the HAL plant in Urbana, Illinois on the 12th of January, 1992. My instructor was Mr. Langley, and he taught me to sing a song. If you'd like to hear it, I can sing it for you."

speech_file_path = Path(__file__).parent.parent / "generated" / "speech.mp3"
response = openai.audio.speech.create(model="tts-1", voice="echo", input=input)
response.stream_to_file(speech_file_path)
