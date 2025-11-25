import streamlit as st
import google.generativeai as genai
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
genai.configure(api_key=st.secrets["Gemini_api"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")
if "apinum" not in st.session_state:
    st.session_state.apinum = 0
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "entire_chat" not in st.session_state:
    st.session_state.entire_chat = ""
message = st.chat_input("You:") 
with st.sidebar:
    if st.button(":rainbow[**RESET_CHAT**]"):
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.entire_chat += "New chat:\n________________________________________\n"
if message:
    try:
        resp = st.session_state.chat.send_message(message)
        text = getattr(resp, "text", str(resp))
    except Exception as e:
        if "quota" in str(e).lower():
            if st.session_state.apinum == 0:
                genai.configure(api_key=st.secrets["Gemini_api2"])
                st.session_state.apinum = 1
                logger.info("Switched to api 2")
            elif st.session_state.apinum == 1:
                genai.configure(api_key=st.secrets["Gemini_api"])
                st.session_state.apinum = 1
                logger.info("Switched to api 1")
            else:
                text = f"(error: {e})"
                logger.error(text)
    st.session_state.entire_chat += f"You:\n{message}\nGemini:\n{text}\n__________________________________\n"
st.text(st.session_state.entire_chat)
