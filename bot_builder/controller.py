from initEnvironment import initEnvironment
from highlightText import highlightText

from askQuestion import askQuestion
from answerQuestion import answerQuestion

initEnvironment()

character = input("Celebrity: ")
print("\n")

while True:
    highlightText("You", "cyan")
    question = askQuestion()
    answer = answerQuestion(character, question)

    highlightText(character, "cyan")
    print(answer + "\n")
