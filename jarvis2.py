import pyttsx3 # pip install pyttsx3 == it is used to convert the text to speech
import datetime
import  speech_recognition as sr #pip install speechrecognition  == speech  date from mic to text 
import smtplib 
from newvoice2 import speak
from secreate import senderemail,epwd,to 
from email.message import EmailMessage 
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os 
import pyjokes
import string
import random
from nltk.tokenize import word_tokenize


from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv

# def speak(text):
#     engine  =  pyttsx3.init('sapi5')
#     engine.say(str(text))
#     engine.runAndWait()
#     # engine.stop()

# ----------------- GPT MEMORY -----------------
# LOAD ENV VARIABLES
load_dotenv()

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


# ----------------- BASIC FUNCTIONS -----------------
def time():
    now  = datetime.datetime.now()
    Time =  f"{now.hour}:{now.minute}:{now.second}"
    print("The current time is :  \t")
    print(Time)
    speak(Time)

# time()

def tell_date():
    now  = datetime.datetime.now()
    year  = now.year  
    month  = now.month  
    day  = now.day  
    sentence = f"The current date is {day} {month} {year}"
    speak("The current date is :  \t")
    print(sentence)
    speak(sentence)

# date()

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <=12:
        speak("Good morning sir!")
    elif hour >=12 and hour <=18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour <=24:
        speak("Good Evening sir!")
    else:
        speak("Good night sir!")

# greeting()

def wishme():
    speak("Welcome Back sir! \n")
    # time()
    # tell_date()
    # greeting()
    speak("Jarvis at your service, please tell me how can i help you! \n")

# wishme()    

def takecommandcmd():
    query =input("please tell me how can i help you! \n")
    return query

def takecommandmic():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogining...")  
        query = r.recognize_google(audio,language = "en-IN")
        print("user said :"+query)
        return query
    except Exception as e:
        print(e)
        speak("say it again please....")
        return "none"    

# ----------------- EMAIL -----------------
def sendEmail(receiver , subject , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail , epwd)
    email = EmailMessage()
    email['from'] = senderemail
    email['To'] = receiver
    email['subject'] = subject
    email.set_content (content)
    server.send_message(email)
    server.close()
 
# sendEmail()

def sendwhatsmsg(phone_no,message):
    message = message
    wb.open(f'https://web.whatsapp.com/send?phone={phone_no}&text={message}')
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search for?')    
    search = takecommandmic()
    wb.open(f'https://www.google.com/search?q='+search)

def chatgpt():
    speak('Opening ChatGPT... ')
    wb.open('https://chatgpt.com')

def news():
    newsapi = NewsApiClient(api_key = '61aed091d2524e5c8a6e400d049ff9ba')
    data = newsapi.get_top_headlines(country='us',
                                    language = 'en',
                                    page_size = 5)    
    
    newsdata = data['articles']
    if not newsdata:
        speak("No news found")
        return
    
    for x,y in enumerate(newsdata ,start=1):
        print(f"{x}. {y['description']}")   
        speak(f"{x}. {y['description']}")

    speak("That's it for now i'll update you in some time")    

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    url = "https://disease.sh/v3/covid-19/all"
    r = requests.get(url)

    data = r.json()
    covid_data = (
    f"Confirmed cases: {data['cases']}\n"
    f"Deaths: {data['deaths']}\n"
    f"Recovered: {data['recovered']}"
    )
    print(covid_data)
    speak(covid_data)

def screen_shot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name_img = f"C:\\new jarvise\\screenshot_{timestamp}.png"
    img = pyautogui.screenshot(name_img)
    img.show()
    speak("Screenshot taken successfully")

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = 8

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass = ("".join (s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("okay sir, fliping a coin?")
    coin = ['head' ,'tails']
    toss= []
    toss.extend(coin)
    random.shuffle(toss)
    toss= ("".join(toss[0]))
    speak("i flipped the coin and you got"+toss)
    print(toss)

def rolladie():
    speak("okay sir, rooling a die for you")
    die = ['1','2','3','4','5','6']
    roll=[]
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print(roll)
    speak("i rooled a die and you get "+roll)    


# ----------------- MAIN LOOP -----------------
if __name__ == "__main__":
    wishme()
    email_list = {
        'anubhav kumar' : 'anubhavkumar845411@gmail.com'
        }
    weakword=  "jarvis"
    while True:
        query = takecommandmic().lower()
        # query = word_tokenize(query)
        # query1 = " ".join(query)
        query1  = query
        print(query)
        if weakword in query:

            if query == "none":
                continue
            if 'time' in query:
                time()
            elif 'date' in query:
                tell_date()    
            elif 'email' in query:
                try:
                    speak("To whom should I send the email?")
                    name = takecommandmic().lower()
                    receiver = email_list[name]

                    speak("what is the subject of the mail?")
                    subject = takecommandmic() 

                    speak('what should i say?')
                    content = takecommandmic()

                    sendEmail(receiver , subject , content)
                    speak("email has bean send")

                except Exception as e :
                    print ("error message : ",e) 
                    speak("unable too send the email")  

            elif 'message' in query:
                user_name = {
                    'anubhav': '+91 9661867002',
                    'sumit' :'+91 7209696347',
                    'abhinav':'+91 8210708350',
                    'anubhav kumar':'+91 7970797683'
                }
                try:
                    speak("To whom should I send the whatsapp message?")
                    name = takecommandmic().lower()
                    phone_no = user_name[name]

                    speak("what is the message?")
                    message = takecommandmic() 

                    sendwhatsmsg(phone_no,message)
                    speak("message has been send")

                except Exception as e :
                    print ("error message : ",e) 
                    speak("unable too send the message")  

            elif 'wikipedia' in query:
                speak('searching on wikipedia...')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result) 
            elif 'google' in query:
                searchgoogle()
            elif 'ai' in query:
                chatgpt()    
            elif 'youtube' in query:
                speak('what should i search for on youtube?')
                topic = takecommandmic()
                pywhatkit.playonyt(topic)
            elif 'weather' in query:
                city = 'new york'
                api_key = '8acb2c7e8a591cd57d2315993f5ec9ab'
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'
                res = requests.get(url)
                data = res.json()
                weather =data['weather'][0]['main']
                temp = data['main']['temp']
                desp = data['weather'][0]['description']  
                temp = round((temp -32)*5/9)
                print(weather)
                print(temp)
                print(desp)  
                speak(f'whether in {city} city')
                speak('Temperature : {} degree celcious'.format(temp))
                speak('weather is {}'.format(desp))

            elif 'news' in query:
                news()    
            elif 'read' in query:
                text2speech()    
            elif 'covid' in query:
                covid()    
            elif 'open code' in query:
                codepath = r'C:\Windows.old\Users\Anubhav\AppData\Local\Programs\Microsoft VS Code\Code.exe'    
                os.startfile(codepath)

            elif 'open document' in query:
                os.system('explorer c:// {}'.format(query.replace('open','')))   
            elif'jokes' in query :
                speak(pyjokes.get_joke())  
            elif 'screenshot' in query:
                screen_shot()    
            elif 'remember' in query and 'that' in query:
                speak("what should i remember?")
                data = takecommandmic()
                speak("you said me to remember that "+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'do you know anything' in query:
                remember = open('data.txt','r')
                speak("you told me to remember that"+remember.read())    

            elif 'password' in query :
                passwordgen()
            elif 'toss' in query:
                flip()       
            elif 'roll' in query :
                rolladie()  
            elif 'offline' in query:
                quit()
            else :
                gpt_output(query1)    
