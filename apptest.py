import streamlit as st
import google.generativeai as genai
import time # Import time for potential debugging delays

# --- Configuration ---
# Use st.cache_resource for API key configuration and model loading
# This ensures they are loaded only once and reused across reruns.
@st.cache_resource
def configure_gemini():
    try:
        genai.configure(api_key=st.secrets["Gemini_api"])
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        return model
    except Exception as e:
        st.error(f"Error configuring Gemini API: {e}")
        return None

model = configure_gemini()

# --- Chat Session Initialization ---
# Initialize chat history in session state if it doesn't exist
# This will store the messages in a format suitable for the Gemini API
if "chat_session" not in st.session_state:
    if model: # Only start chat if model was configured successfully
        try:
            st.session_state.chat_session = model.start_chat(history=[])
            st.write("Chat session initialized.") # Debugging line
        except Exception as e:
            st.error(f"Error starting chat session: {e}")
            st.session_state.chat_session = None # Ensure it's None if start fails 
    else:
        st.session_state.chat_session = None

# --- Display Chat History ---
if st.session_state.chat_session:
    for message in st.session_state.chat_session.history:
        if message.role == "user":
            st.chat_message("user").markdown(message.parts[0].text)
        elif message.role == "model":
            st.chat_message("assistant").markdown(message.parts[0].text)
else:
    st.warning("Gemini model not initialized. Please check your API key and configuration.")

# --- User Input ---
user_message = st.chat_input("You:")

if user_message and st.session_state.chat_session:
    # Display user message immediately
    st.chat_message("user").markdown(user_message)

    # Send user message to Gemini and get response
    try:
        # Append user message to the current chat session and send
        # send_message modifies the session in place.
        response = st.session_state.chat_session.send_message(user_message)        

        # The response object from send_message contains the full response.        
        # We can directly get its text.
        gemini_response_text = response.text

        # Display Gemini's response
        st.chat_message("assistant").markdown(gemini_response_text)

    except Exception as e:
        st.error(f"An error occurred during API call: {e}")
        # Consider adding a line to clear the erroneous message if it caused issues
        # Or log the error for debugging.
        # time.sleep(2) # Optional: Add a small delay before the next iteration if it's truly looping

elif user_message and not st.session_state.chat_session:
    st.warning("Cannot send message: Gemini model not available.")
'''
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
st.text(st.session_state.entire_chat)'''
