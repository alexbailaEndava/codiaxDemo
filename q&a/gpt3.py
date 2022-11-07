import openai
import os
import time

# prettier output
from colorama import init
from termcolor import colored
from pathlib import Path

from getKey import getKey

# needs tensorflow > 2.0
from transformers import GPT2Tokenizer

os.chdir("..")
key = getKey()
os.chdir("q&a")

aboutBot = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will generate whatever text I think is suitable. If the generated text does not match the prompt, your input was not clear enough."

# for output printing
def highlightStages(text, colour):
    init()
    print(colored(text, colour, attrs=['bold']))

# GPT-3 mode, choose between singel inference or continuous chat
# options provided below
def chooseMode():
    highlightStages("Choose GPT3 interaction mode: Single (s) / Continuous (c) / Interview (i)", "green")
    mode = input("Choose mode: ").upper()
    return mode

def chooseMood():
    highlightStages("Choose GPT3 Engine mood: Friendly (f) / Sarcastic (s)", "green")
    mood = input("Choose mood: ").upper()
    return mood

def passInput():
    highlightStages("Human:", "green")
    prompt = input("")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokens = len(tokenizer(prompt)['input_ids'])

    return prompt, tokens

def callGPT3Bot(prompt):
    # set API key as environment variable
    openai.api_key = key

    # generate completion for input (API call)
    # 'engine = ...' can be changed to other 
    # models, including fine-tuned ones

    response = openai.Completion.create(engine = "text-davinci-002", 
                                        prompt = prompt,
                                        temperature = 0.7, 
                                        max_tokens = 256,
                                        top_p = 1,
                                        frequency_penalty=0,
                                        presence_penalty=0
                                        )
    return response.choices[0].text.replace("\n", "")

def callGPT3Friendly(prompt):
    # set API key as environment variable
    openai.api_key = key
    # generate completion for input (API call)
    # 'engine = ...' can be changed to other 
    # models, including fine-tuned ones

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(engine = "text-davinci-002", 
                                        prompt = prompt,
                                        temperature=0.9,
                                        max_tokens=150,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0.6,
                                        stop=[" Human:", " AI:"]
                                        )
    return response.choices[0].text.replace("\n", "")

def callGPT3Sarcastic(prompt):
    # set API key as environment variable
    openai.api_key = key
    # generate completion for input (API call)
    # 'engine = ...' can be changed to other 
    # models, including fine-tuned ones

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(engine = "text-davinci-002", 
                                        prompt = prompt,
                                        temperature=0.5,
                                        max_tokens=60,
                                        top_p=0.3,
                                        frequency_penalty=0.5,
                                        presence_penalty=0
                                        )
    return response.choices[0].text.replace("\n", "")

# the script's "brain"
def controller():
    aboutEngine = "The following is a conversation with an AI assistant. The assistant is "
    mode = chooseMode()

    if mode == "S":
        highlightStages("\nGPT3 Single Mode", "green")
        print(aboutBot)
        print("\n")
        prompt, tokens = passInput()
        start = time.time()
        response = callGPT3Bot(prompt)
        end = time.time() - start
        highlightStages("AI", "green")
        print(response)
        highlightStages("Execution time", "yellow")
        print(str(round(end, 2)) + " seconds for " + str(tokens) + " tokens")

    elif mode == "C":
        highlightStages("\nGPT3 Continuous Mode", "green")
        print(aboutBot)
        print("\n")
        while True:
            prompt, tokens = passInput()
            response = callGPT3Bot(prompt)
            highlightStages("AI", "green")
            print(response)

    elif mode == "I":
        file = open("interview.txt", "w")

        file.truncate(0)
        mood = chooseMood()

        if mood == "F":
            highlightStages("\nGPT3 Friendly Interview Mode\n", "green")
            interview = open("interview.txt", "w+")
            interview.write("This is your interview with a friendly AI\n\n")
            context = open("friendly.txt").read()
            prompt = context
            while True:
                prompt, tokens = passInput()
                context = context + "\nHuman: " + prompt + "\nAI: "
                response = callGPT3Friendly(context)
                highlightStages("AI", "green")
                print(response + "\n")
                context = context + "\nAI: " + response
                interview.write("Human: " + prompt)
                interview.write("\nAI:" + response + "\n")


        elif mood == "S":
            highlightStages("\nGPT3 Sarcastic Interview Mode\n", "green")
            interview = open("interview.txt", "w+")
            interview.write("This is your interview with a Marv, the sarcastic AI\n\n")
            context = open("sarcasm.txt").read()
            prompt = context
            while True:
                prompt, tokens = passInput()
                context = context + "\nYou: " + prompt + "\nMarv: "
                response = callGPT3Friendly(context)
                highlightStages("Marv", "green")
                print(response + "\n")
                context = context + "\nMarv: " + response
                interview.write("You: " + prompt)
                interview.write("\nMarv: " + response + "\n")
        else:
            highlightStages("Mood not valid. Shutting down", "red")

    else:
        highlightStages("Option not valid. Shutting down", "red")

controller()


