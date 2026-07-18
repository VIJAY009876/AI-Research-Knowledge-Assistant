import streamlit as st
from src.llm.client import ask_llm
from src.memory.chat_memory import ChatMemory

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research & Knowledge Assistant")
st.write("Welcome! Ask me anything.")

if "memory" not in st.session_state:
    st.session_state.memory = ChatMemory()

for message in st.session_state.memory.get_conversation():

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_prompt =  st.chat_input("Ask anything...")



if user_prompt:
    st.session_state.memory.add_user_message(user_prompt)
    with st.chat_message("user"):
        st.markdown(user_prompt)

if user_prompt:
    response = ask_llm(user_prompt)
    st.session_state.memory.add_assistant_message(response)
    with st.chat_message("assistant"):
        st.markdown(response)
    
