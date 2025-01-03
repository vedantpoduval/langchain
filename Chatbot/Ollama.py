from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 

from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate(
    [
        ("system","you are a helpful assistant answer the general questions"),
        ("user","question:{question}")
    ]
)

st.title("Learning Langchain with OLLAMA")
input = st.text_input("Enter your question")

llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input:
    st.write(chain.invoke({'question':input}))

