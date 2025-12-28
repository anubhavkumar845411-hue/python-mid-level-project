import pyttsx3 
import speech_recognition as sr
from openai import OpenAI
import os
from dotenv import load_dotenv

# LOAD ENV VARIABLES
load_dotenv()

# it is a speak function :-
def speak(text):
    engine  =  pyttsx3.init('sapi5')
    engine.say(str(text))
    engine.runAndWait()
    # engine.stop()

speak("hi, i am agi assistance how can i help you")

def STT() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en-IN")
        print("Human said : "+query)
        
    except Exception as e :
        print(e)
        speak("Say it again please...")
        return "None" 
    return  query   

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
conversection_history = [{
    "role":"system" ,"content" :"You are a helpful AI assistant."
}]

def gpt_output(user_input):
    conversection_history.append(
        {"role":"user" , "content" : user_input}  # this help to take the input form user
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=conversection_history   # this help to get the answer of diffrent query usn=ing the openai api keys
    )


    ai_reply = response.output_text  # in thar statment it response bacck to the ai_reply

    conversection_history.append(
        {"role" : "assistant" ,"content" :ai_reply}    # Save assistant response
    )
    
    print("AI : ",ai_reply)
    speak(ai_reply)
    return conversection_history,""

# chat loop 


while True :
    user = STT()
    if user.lower() in ["exit" , "quit"]:
        break
    gpt_output(user)