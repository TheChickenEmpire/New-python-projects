import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["Gemini_api"])
model=genai.GenerativeModel("gemini-2.5-flash-lite")
chat=model.start_chat(history=[])
entire_chat=""
while True:
    try:
        message=st.chat_input("You:\n")
        entire_chat=entire_chat+"You:\n"+message
        response=chat.send_message(message)
        response=response.text
        response="Gemini:\n"+response+'\n_________________________________________\n'
        entire_chat=entire_chat+response
        st.text(entire_chat)
    except:
        pass