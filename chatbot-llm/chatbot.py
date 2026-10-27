def chatbot(user_msg):
    message=user_msg.lower()

    if "python" in message:
        return "Python is General Purpose Programming Language"
    
    elif "java" in message:
        return "Java is Object Oriented Programing Language" 
    
    elif "hello":
        return "Hi Buddy! how can i help"
    else:
        return "Good Bye"
    
while True:

    question=input("Student:")
    if question.lower() =="exit":
       print("Bot:Good Bye")
       break 

    response=chatbot(question)
    print("Bot:", response)