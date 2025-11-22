import streamlit as st
from PIL import Image
import google.generativeai as genai
st.set_page_config(page_title='Chicken Empire', page_icon=":chicken:", layout= 'wide')
st.logo(Image.open('Chicken.png'))
with st.sidebar:
    st.subheader(':rainbow[My channel]')
    st.link_button("Channel", 'https://www.youtube.com/@TheNewChickenEmpire')
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

    
st.subheader('Welcome to')
st.header(':rainbow[**The Chicken Empire**]')
st.subheader('_website_') 
st.divider()
st.subheader('Recent News:')
st.text(None)
st.divider()
st.subheader('About Me')
st.text('Hi im a youtuber who likes coding\nwe all have dreams\nand If you Subscribe\nyou would be helping\nme fulfil mine\nplease\n\/\/\/') 
st.link_button('Click Here Plz', 'https://www.youtube.com/@TheChickenEmpire')
st.divider()
st.subheader('My Subscribers')
st.text("")
st.divider()
st.subheader('History:')
st.text('June 23:\nChicken Empire Created\n\nJuly:\nChicken Empire faces war\n\n2024:\nYoutube channel starts\n\nMarch 2024 - April 2024:\nChannel thrives\n\nApril 24 - June 24:\nChannel views and subs drop of me going back to school\n\nJune 24:\nI create this website\n\n')
st.divider()
st.subheader('Wonderful portraits:')
st.image(Image.open('Victory.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('CE Poster (Portrait).png'), width=400)
st.text('Credits: By Zxjoshua33(My Friend)')
st.image(Image.open('James.png'), width=400)
st.text('Credits: By OppositeAce8412(My Friend)')
st.image(Image.open('Standard.png'), width=400) 
st.text('Credits: By Zxjoshua33(My Friend)')
st.image(Image.open('James1.png'), width=400) 
st.text('Credits: By OppositeAce8412(My Friend)')
st.image(Image.open('Rizzkens.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Chick (1).png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Sigma.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Chicks.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('The Chicken Empire.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Burn.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Mew.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Rock.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Roost.png'), width=400)
st.text('Credits: By Me')
st.divider()
st.subheader('Credits')
st.text('Donnie(My other friend)\nZxJoshua33(You should go see his channel)\nOppositeAce8412(You should go see his channel)\nChickens\nEthan(My other friend)')