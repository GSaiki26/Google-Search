## Libs
import os
from json import dumps, loads

## Methods
def CheckPath(path: str): ## Method to check if the Results path exists.
    folders = path.split('/') ## Get all the folders in the path.
    if len(folders) == 1: ## Check if the folders has no folder.
        return ## Return the code.
    path = '' ## Reset the path to use in the loop, to write the old folders.
    for index in range(len(folders)): ## Foreach folder IN INDEX.
        folder = folders[index]
        if not index == len(folders)-1: ## This if exists to prevents to write / on the file's end.
            path+=folder+'/' ## Add the folder to the path.
            if not os.path.exists(path): ## Check if the path not exist.
                os.mkdir(path) ## Create the folder.

def Write(path: str, content): ## Method to write into a file.
    CheckPath(path) ## Create the path.
    with open(path, 'w', encoding='utf-8') as file:
        ## Write on the file the soup result.
        for tag in content: ## Foreach line in the result.
            file.write(f'{tag.get_text()}\n') ## Write in the file as str.
        

def Read(path: str, output: type = str): ## Method to read a file.
    CheckPath(path) ## Create the path.
    with open(path, 'r', encoding='utf-8') as file:
        ## Read the file.
        content = '' ## Define the content.
        for line in file: ## Foreach line in file.
            content+=line ## Add the line to content.

        ## Threat the output.
        if output is dict: ## If the user wants the output as dict, return dict.
            return loads(content) ## Return the json.
        return content ## Return the content as string