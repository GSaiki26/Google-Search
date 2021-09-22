## Libs
import os ## Idk.
import googlesearch ## Search on google.
import requests as r ## Requests to get content.
from bs4 import BeautifulSoup as bs ## Get the content of the website.
from termcolor import colored

## Local libs
from src.Menu import Menu ## Get the menu.
from src.Write import Log as log
from src.Write import Input
import src.Files as f

## Sup Methods.
def DoReq(url: str, method: str = 'GET') -> str: ## Method to do a request and return the body.
    req = r.request(method, url) ## Get the request.
    return req.text ## Return the site's body.

## Methods
def TextWrapper(websiteBody: str) -> str: ## Method to wrapper the "main" content of the site.
    soup = bs(websiteBody,'html.parser') ## Do the soup.
    content = soup.findAll(['p', 'spam']) ## Get all the content.
    log('The main content of the site has been wrapped.')
    return content ## Return the content.

def GetWebsiteBody(phrase: str) -> str: ## Method to get the website to wrap.
    log(f'Searching on the google by: '+colored(phrase,'white'))

    ## Get the Google's result;
    results = googlesearch.search(phrase, num_results=10, lang='pt-br') ## Get the google results.

    ## Call the Menu.
    lis = [f'[URL] {result}' for result in results] ## Define the list(menu) to a null list, and add each URL to results.
    url = Menu(lis, f'Phrase: {colored(phrase,"white")}\n{colored("Choose a website to get the content:", "magenta")}\n') ## Get the choice.

    ## Threat the website.
    log('Getting the website\'s body...'); websiteBody = DoReq(url[5:]) ## Get the website's body.
    return f'<spam>{url}</spam>\n{websiteBody}'

def ByPhrase(): ## Method to search on the google using a phrase.
    phrase = Input('Type what you want to search: ') ## Get the user's phrase.
    body = GetWebsiteBody(phrase) ## get the body.
    log('Threating the website\'s content...'); content = TextWrapper(body) ##Get the website content.
    path = 'Results/Result_0.txt'
    f.Write(path, content) ## Write on the file the content.
    log(f'The result was written on the file: "{path}".', 'cyan')

def ByFile(): ## Method to search multiples phrases into a file.
    while True: ## Loop until the user choice a valid path.
        try:
            fileName = input('Type the file\'s name [Leave empty to use content.txt]: ') ## Get the users path.
            if not fileName: ## threat the path.
                fileName = 'content'
            phrases = f.Read(f'{fileName}.txt').split('\n') ##Try to get the files names.
            break ## Break the loop
        except Exception as e:
            print(e)
            log('The file could\'t be founded. Please try again.\n', 'red')
    for index in range(len(phrases)): ## Foreach phrase IN INDEX.
        phrase = phrases[index] ## Get the current phrase.
        log(f'Checking the phrase:"{phrase}" [{index}/{len(phrases)}]...')
        body = GetWebsiteBody(phrase) ## Get the website's body.
        log('Threating the website\'s content...'); content = TextWrapper(body) ##Get the website content.
        path = f'Results/Result_{index}.txt'
        f.Write(path, content) ## Write on the text.
        log(f'The result was written on the file: "{path}".', 'cyan')