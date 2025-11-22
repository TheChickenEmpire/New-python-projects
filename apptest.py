import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["Gemini_api"])
model=genai.GenerativeModel("gemini-2.5-flash-lite")
chat=model.start_chat(history=[])
while True:
    try:
        message=st.chat_input("You:\n")
        response=chat.send_message(message)
        response=response.text
        st.text("Gemini:\n"+response+'\n_________________________________________')
    except:
        pass