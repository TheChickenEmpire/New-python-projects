import google.generativeai as genai
import time
genai.configure(api_key="")
model=genai.GenerativeModel("gemini-2.0-flash-lite")
chat=model.start_chat(history=[])
chat2=model.start_chat(history=[])
response='Hello'
while True:
    response=chat.send_message(response)
    response=response.text
    print(response+"\n----------------------------------------------------")
    time.sleep(4)
    response=chat2.send_message(response)
    response=response.text
    print(response+"\n----------------------------------------------------")
    time.sleep(4)