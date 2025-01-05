import streamlit as st
import requests


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json = {'input':{'topic':input_text}})
    return response.json()['output']
def get_phi3_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json = {'input':{'topic':input_text}})
    return response.json()['output']

st.title("Learning about langchain with api")
input_text1 = st.text_input("Write an essay on")
input_text2 = st.text_input("Write an poem on")

if input_text1:
    st.write(get_ollama_response(input_text1))
if input_text2:
    st.write(get_phi3_response(input_text2))