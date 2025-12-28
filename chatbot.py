from openai import OpenAI
import os
import gradio as gr
from dotenv import load_dotenv

# LOAD ENV VARIABLES
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
conversection_history = [{~
    "role":"system" ,"content" :"You are a helpful AI assistant."
}]

def gpt_output(user_input,history):
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
    
    # print("AI : ",ai_reply)
    return conversection_history,""

#chat loop 
# while True :
#     user = input("you : ")
#     if user.lower() in ["exit" , "quit"]:  # This is the chat bot loop you can ask any question while you not entered the exit 
#         break
#     gpt_output(user)


with gr.Blocks(title= "AGI AI Assistant") as demo:
    gr.Markdown("<h1 style= 'text-align : center'>AGI AI Assistant </h1>")

    chatbot = gr.Chatbot(height=350)
    textbox = gr.Textbox(
        placeholder="Type your message here...",
        label="textbox"
    )
    send = gr.Button("send")
    send.click(
        gpt_output,
        inputs=[textbox,chatbot],
        outputs=[chatbot,textbox]
    )

    demo.launch(theme=gr.themes.Soft())
