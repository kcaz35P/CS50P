import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(figlet.getFonts()))
        word = input("Enter your word: ")
        print(figlet.renderText(word))
    elif len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts() and sys.argv[1] in ["-f","--font"]:
        figlet.setFont(font = sys.argv[2])
        word = input("Enter your word: ")
        print(figlet.renderText(word))
    else:
        sys.exit("an Error")

main()
