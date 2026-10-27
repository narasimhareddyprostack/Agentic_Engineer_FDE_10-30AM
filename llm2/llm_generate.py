import os 
from dotenv import load_dotenv
from groq import Groq
#loading environment variables
load_dotenv()
client=Groq(api_key=os.getenv('GROQ_API_KEY'))
model=os.getenv('GROQ_MODEL')
prompt=input("Ask any thing!")

response=client.chat.completions.create(model=model,
                                        messages=[{"role":"user","content":prompt}],
                                        temperature=0.2,
                                        max_completion_tokens=200)



print(response.choices[0].message.content)