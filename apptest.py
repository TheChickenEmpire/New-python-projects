import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["Gemini_api"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")
if "entire_chat" not in st.session_state:
    st.session_state.entire_chat = ""
message = st.chat_input("You:")
if message:
    chat = model.start_chat(history=[])
    try:
        resp = chat.send_message(message)
        text = getattr(resp, "text", str(resp))
    except Exception as e:
        text = f"(error: {e})"

    st.session_state.entire_chat += f"You:\n{message}\nGemini:\n{text}\n_________________\n"
st.text(st.session_state.entire_chat)