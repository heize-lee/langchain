
from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

#WebBaseLoader
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://www.moel.go.kr/policy/policyinfo/support/list4.do")

docs = loader.load()


#embeddings
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

