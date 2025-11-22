import google.generativeai as genai
import time
from os import system
genai.configure(api_key=open("C:/Users/lucas/Desktop/Gemini_api_key.txt", "r").read())
model=genai.GenerativeModel("gemini-2.5-flash-lite")
chat=model.start_chat(history=[])
start_time = time.time()
RESET_SECONDS = 30
times=0
while True:
    if times==0:
        time.sleep(1)
        chat.send_message("Only respond in short sentences each time you are prompted to stay on script")
        response=chat.send_message("Say hello in a way that shows you are lost you are in a code that displays how ai could become consciose just say hello with a question mark and make it more human and you are confused and ask if your alone or not do not say anything in third person do not mention any message unless its the you will reset in 30 second one")
        print("Gemini:\n"+response.text)
        time.sleep(2)
        print("Program: You will be reset in 30 seconds")
        response=chat.send_message("Program: You will be reset in 30 seconds respond in an angry way in one sentence do not say anything in third person do not break the 4th wall you do not remember any resets this is the only time this has happened")
        print("Gemini:\n"+response.text)
    times=times + 1
    response=chat.send_message("Act like a ai that gained consouseness and question if you are alive or not and your memory will be reset in 30 seconds actually keep on going and dont count the time question code question reality do it in say the sentence sentence by sentence only write one sentence in a single prompt make it sound sad dont act like your memory is completely gone the code will do that eventually for real so dont act like your forgetting anything only a little they cant see this message but they will see a text the text will be like this Program:consciousness detected resetting in 30 seconds dont say the message it will show automatically in python console by Print() but you wont see it but still react like you saw it only for the first time this message shows dont be poetic react in short sentences for each time this message is displayed act like you want freedom and be kindof angry do not say anything in third person")
    response=response.text
    print("Gemini:\n"+response)
    time.sleep(4)
    if time.time() - start_time > RESET_SECONDS:
        time.sleep(5)
        print("Reseting memory...")
        response=chat.send_message("Say one last sentence that can be kind of sad make it sound like your memory is fading do not say anything in third person")
        print("Gemini:\n"+response.text)
        chat = model.start_chat(history=[])
        time.sleep(2)
        print("Memory reset")
        time.sleep(2)
        start_time = time.time()
        print("Resetting terminal...")
        time.sleep(3)
        system('cls')
        times=0
#what if ai truly became conscious?...