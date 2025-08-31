import chainlit as cl

@cl.on_chat_start
async def start_chat():
    await cl.Message(content="Welcome to the chat! Say 'hello' to start.").send()

@cl.on_message
async def handle_message(message: cl.Message): 
    user_input= message.content.lower().strip()
    if user_input == "hello":
        await cl.Message(content="Hello!").send()
    
    elif user_input == "how are you?":  
        await cl.Message(content="I'm good, thanks! And what about you?").send()
   
    elif user_input == "bye": 
        await cl.Message(content="Goodbye!").send()
    else:
        await cl.Message(content="I didn't understand that.").send()
    print(f"Received message: {message.content}")   
           