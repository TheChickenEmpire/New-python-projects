import streamlit as st
import google.generativeai as genai
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
genai.configure(api_key=st.secrets["Gemini_api"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "entire_chat" not in st.session_state:
    st.session_state.entire_chat = ""
with st.columns(8,1):
    message = st.chat_input("You:") 
with st.columns(8,1):
    if st.button("RESET"):
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.entire_chat += "New chat:\n--------------------"
if message:
    try:
        resp = st.session_state.chat.send_message(message)
        text = getattr(resp, "text", str(resp))
    except Exception as e:
        text = f"(error: {e})"
        logger.error(text)
    st.session_state.entire_chat += f"You:\n{message}\nGemini:\n{text}\n_________________\n"
st.text(st.session_state.entire_chat)
