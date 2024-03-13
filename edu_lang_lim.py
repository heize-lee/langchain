from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=openai_api_key)
pass