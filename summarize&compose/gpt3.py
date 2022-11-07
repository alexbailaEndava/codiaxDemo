import openai
import os

from colorama import init
from termcolor import colored
from getKey import getKey

os.chdir("..")
key = getKey()
os.chdir("summarize&compose")

openai.api_key = key

# for output printing
def highlightStages(text, colour):
    init()
    print(colored(text, colour, attrs=['bold']))

highlightStages("Text to summarize:", "green")
input = open("article.txt", "r").read().replace("\n", "")
print(input)

# produce summary
summary = openai.Completion.create(
  model="text-davinci-002",
  prompt=input + "\n\nTl;dr:",
  temperature=0.7,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

resultSummary = summary.choices[0].text.replace("\n", "")

# produce rap song
highlightStages("\nSummary:", "green")
print(resultSummary)

compose = open("compose.txt", "r").read()

rapSong = openai.Completion.create(
  model="text-davinci-002",
  prompt=compose + input,
  temperature=0.7,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

resultRap = rapSong.choices[0].text

poem = ""
for index in range(1, len(resultRap)):
  char = resultRap[index]
  if char.isupper():
    poem = poem + ("\n") + char

  else:
    poem = poem + char

highlightStages("\nRap Song:", "green")
print(poem)

