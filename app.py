## Libs
from time import sleep

## Local libs
import src.Search as Search ## Import the local lib of search.
from src.Menu import Menu ## Import the local lib to use Menus.
from src.Write import Log as log
from src.Write import Clear
## Methods

## Code
def Start():
    opt = ['[OPT] Search', '[OPT] Search (File)', '[OPT] Exit'] ## Creating a list of opt to the Menu.
    ## Get the choice.
    choice = Menu(opt, 'Please choose an option:\n')

    ## Call the choice
    if choice == '[OPT] Search':
        Search.ByPhrase()
    elif choice == '[OPT] Search (File)':
        Search.ByFile()
    else:
        return ## Break the loop.
    Menu(opt, 'The search is over. Please use me again :))')

## Code
Clear() ## Clear the console.
Start() ## Start the program.