from colorama import init
from termcolor import colored

# for output printing
def highlightText(text, colour):
    init()
    print(colored(text, colour, attrs=['bold']))