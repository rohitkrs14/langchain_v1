import os
from dotenv import load_dotenv

load_dotenv()

assert os.environ.get("OPENAI_API_KEY"), "Missing OPENAI_API_KEY -- check your .env file, it should be in the same folder where the current file is present"

from langchain.chat_models import init_chat_model
model = init_chat_model("openai:gpt-5-nano")
print("Environment ready.")