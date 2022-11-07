import openai
import os
import time

from colorama import init
from termcolor import colored

from getKey import getKey

os.chdir("..")
key = getKey()
os.chdir("workWithCode")

openai.api_key = key

# for output printing
def highlightStages(text, colour):
    init()
    print(colored(text, colour, attrs=['bold']))

# GPT-3 mode, choose between singel inference or continuous chat
# options provided below
def chooseMode():
    highlightStages("Choose GPT3 Codex interaction mode: Code generation (g) / Code debugging (d) / Code explanation (e)", "green")
    mode = input("Choose mode: ").upper()
    return mode

print("GPT-3 Codex for Python\n\nI am highly inteligent AI that can work with code\n")
mode = chooseMode()

if mode == "G":
    while True:
        highlightStages("\nWhat code should I generate:", "green")
        instruction = input("")

        response = openai.Completion.create(
            model="code-davinci-002",
            prompt="\"\"\"\n" + instruction + "\n\"\"\"",
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            ).choices[0].text

        codeFile = open("codeToExecute.py", "w")
        codeFile.write(response)
        codeFile.close()

        highlightStages("\nCode generated:", "green")
        print(response)

        highlightStages("\nExecuting code...", "green")
        time.sleep(2)
        exec(open("codeToExecute.py").read())

elif mode == "D":

    highlightStages("Debugging code in \"buggyCode\".py", "green")
    codeFile = open("buggyCode.py", "r")
    buggyCode = codeFile.read()
    codeFile.close()

    prePrompt = "##### Fix bugs in the below function\n \n### Buggy Python\n"
    postPrompt = "\n    \n### Fixed Python"

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prePrompt + buggyCode + postPrompt,
        temperature=0,
        max_tokens=182,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
        ).choices[0].text
    
    codeFile = open("buggyCode.py", "w")
    codeFile.write("#Buggy code\n\"\"\"" + buggyCode + "\"\"\"\n\n#Debugged code:\n" + response)
    highlightStages("Code has been debugged. Check the file.", "green")

elif mode == "E":
    highlightStages("\nPython code", "green")

    codeFile = open("codeToExplain.py", "r")
    code = codeFile.read()
    codeFile.close()

    print(code)

    instruction = "\n\n# Explanation of what the code does\n"

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=code + "\n\n\"\"\"\nHere's what the above code is doing:",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\"\"\""]
        ).choices[0].text

    highlightStages("\nCode description", "green")

    print(response)

else:
    highlightStages("Option not valid. Shutting down", "red")

    