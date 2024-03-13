import streamlit as st
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain.callbacks.base import BaseCallbackHandler
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo-0125"

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

want_to = """너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
content
{}
"""

content="""    
"""

from langchain_community.document_loaders import WebBaseLoader

st.header("코인가격 및 정보 챗봇")
st.info("코인가격 및 관련 정보를 조회할 수 있는 챗봇입니다.")
st.error("죄송합니다. 현재 서버에 문제가 있어 챗봇을 실행할 수 없습니다.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [ChatMessage(role="assistant", content="안녕하세요! 춘식이네 코인챗봇입니다. 어떤 내용이 궁금하신가요?")]

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    # 프롬프트
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    if not API_KEY:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOpenAI(openai_api_key=API_KEY, streaming=True, callbacks=[stream_handler], model_name=MODEL)
        response = llm([ ChatMessage(role="system", content=want_to.format(content))]+st.session_state.messages)
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
