from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

if __name__ == "__main__":
    model_list = client.models.list()
    for model in model_list:
        print(model.id)
