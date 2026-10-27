from dotenv import load_dotenv
import os 
from groq import Groq

#load .env file
load_dotenv()

#create groq client
client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

#Convenstion History
messages=[{'role':'system','content':"You are a helpful AI Assistant"}]


print("+++++++++++++++++++")
print("Pro Stack - AI Chat Bot")
print("Type exit to Stop the Chat")


while True:
    user_input=input("Ask Anything.......") 

    if user_input.lower() =="exit":
        print("Good Bye!")
        break

    messages.append({'role':"user",'content':user_input})

    #send request to GROQ/Open AI/Claude  
    response=client.chat.completions.create(model="openai/gpt-oss-120b",
                                            messages=messages)

    #Get AI Response
    bot_response=response.choices[0].message.content

    print("Bot Response", bot_response)
    print()

    #store AI resonse into message
    messages.append({"role":"assistant","content":bot_response})






