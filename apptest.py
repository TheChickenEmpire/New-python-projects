import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["Gemini_api"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")
st.session_state.api = 0
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "entire_chat" not in st.session_state:
    st.session_state.entire_chat = ""
message = st.chat_input("You:")
if message:
    try:
        resp = st.session_state.chat.send_message(message)
        text = getattr(resp, "text", str(resp))
    except Exception as e:
        if "quota" in e:
            if st.session_state.api == 0:
                genai.configure(api_key=st.secrets["Gemini_api2"])
                st.session_state.api = 1
            else:
                genai.configure(api_key=st.secrets["Gemini_api"])
                st.session_state.api = 0
            resp = st.session_state.chat.send_message(message)
            text = getattr(resp, "text", str(resp))
        else:
            text = f"(error: {e})"

    st.session_state.entire_chat += f"You:\n{message}\nGemini:\n{text}\n_________________\n"
st.text(st.session_state.entire_chat)
'''
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["Gemini_api"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "entire_chat" not in st.session_state:
    st.session_state.entire_chat = ""
message = st.chat_input("You:")
if message:
    try:
        resp = st.session_state.chat.send_message(message)
        text = getattr(resp, "text", str(resp))
    except Exception as e:
        text = f"(error: {e})"

    st.session_state.entire_chat += f"You:\n{message}\nGemini:\n{text}\n_________________\n"
st.text(st.session_state.entire_chat)
'''