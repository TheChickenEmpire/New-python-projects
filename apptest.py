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
chat_html = st.session_state.entire_chat.replace("\n", "<br>")
st.markdown(
    f"""
    <div style="
      height: 70vh;
      overflow: auto;
      padding: 12px;
      background: #0b0b0b;
      color: #eee;
      border-radius: 8px;
      font-family: monospace;
      white-space: pre-wrap;
    ">
      {chat_html}
    </div>
    """,
    unsafe_allow_html=True,
)
second, first = st.columns([8,1])
with second:
    message = st.chat_input("You:") 
with first:
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
