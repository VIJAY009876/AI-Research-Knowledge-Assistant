import streamlit as st
from src.llm.client import ask_llm

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research & Knowledge Assistant")
st.write("Welcome! Ask me anything.")

user_prompt =  st.chat_input("Ask anything...")

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

if user_prompt:
    response = ask_llm(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    
