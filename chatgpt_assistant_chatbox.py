import openai
import gradio as gr


openai.api_key="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"

message=[{ "role" : "system" , "content" : "You are a helpful and kind AI Assistant." }]

def user_input(input):
    if input:
        input_message={"role" : "user" , "content" : input}
        message.append(input_message)
        chat = openai.ChatCompletion.create( model = 'gpt-3.5-turbo' , messages=message)
        reply=chat.choices[0].message.content
        output_message={"role" : "assistant" , "content" : reply}
        message.append(output_message)

    return reply

input=gr.inputs.Textbox(lines=7 , label='Chat with AI')
output=gr.outputs.Textbox(label='replay')

interface=gr.Interface(fn=user_input, inputs=input, outputs=output, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact")

interface.launch()
