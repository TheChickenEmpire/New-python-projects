import google.generativeai as genai
genai.configure(api_key=open("C:/Users/lucas/Desktop/Gemini_api_key.txt", "r").read())
model=genai.GenerativeModel("gemini-2.5-flash-lite")
chat=model.start_chat(history=[])
while True:
    try:
        response=chat.send_message(input("You:\n"))
        response=response.text
        print("Gemini:\n"+response+'\n_________________________________________')
    except ValueError:
        print('Program: Pls input content\n_________________________________________')