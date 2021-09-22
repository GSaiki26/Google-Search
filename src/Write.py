## Libs
from termcolor import colored
import platform, os

## Local libs
from src.Time import GetTime ## Get the current time.

## Data
clear = '' ## The clear command.

## Methods
def Log(text: str, color: str = 'magenta', dated: bool = True):
    if dated: ## Check dated.
        text = f'[{GetTime()}] {text}' ## Add the time to the text.
    print(colored(text, color)) ## print colored text!!!

def Input(text:str) -> str:
    answer = input(colored(f'[{GetTime()}] {text}','magenta')); print('') ## Get the input and break the line.
    return answer

def Clear(): ## Method to clear the console.
    global clear
    if not clear: ## If clear is not defined:
        clear = 'cls' if platform.system() == 'Windows' else 'clear' ## Set the clear command
    os.system(clear) ## Clear the terminal