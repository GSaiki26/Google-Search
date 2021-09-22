## Libs
from termcolor import colored

## Local Libs
from src.Write import Log as log ## lib to write colored and "dated".

## Methods
def Menu(lis: list, topMessage: str): # Do a looped Menu, until the user choice some options.
    print(colored('--------------------------------------------------','magenta'))
    ## lis: list of choices | topMessages = message to be showed on the top of the menu.
    ## Define another topMessage in case of error.
    log(topMessage, 'magenta', False) ## Write the current top message.
    topMessage = ['The answer in invalid.\n', 'red'] ## Recursive to get another answer until its a valid one.

    ## Write the menu.
    for index in range(len(lis)): ## Foreach item in lis (INDEX).
        item = lis[index] ## get the current item, using the current index.
        log(f'{item} [{index}]', 'yellow', False)

    ## Threat the answer.
    answer = input(colored(f'\nYour answer[0/{len(lis)-1}]: ','cyan')) ## get the user input to analysis.
    print(colored('\n--------------------------------------------------','magenta'))
    try:
        answer = int(answer) ## Get the answer as int.
    except:
        return Menu(lis, topMessage) ## Be recursive.
    if answer < 0 or answer >= len(lis): ## If the answer is invalid.
        return Menu(lis, topMessage) ## Be recursive
    return lis[answer]