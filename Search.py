#Library
import webbrowser, os
try:
    import googlesearch
except:
    try:
        os.system("pip install googlesearch-python")
    except:
        os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        print("The pip was downloaded!\n")
        os.system("py get-pip.py")
        print("The Pip was installed!\n")
        os.remove("get-pip.py")
        os.system("pip install googlesearch-python")
try:
    from bs4 import BeautifulSoup
except:
    os.system("pip install bs4")
try:
    import requests
except:
    os.system("pip install requests")
#Data
results = 1
i = 0
#Def
def Input(text):
    while True:
        answer = input(f'{text} (y) ou (n)? ').lower()
        if answer != 'y' and answer != 'n':
            print("Please type a valid answer!")
        else:
            return answer
def SearchByInput():
    answer = input('Type what you want to search (to split the researches use ","): ')
    search = answer.split(",")
    for x in search:
        Search(x)
def Search(x):
    global results
    searchOnGoogle = googlesearch.search(x,num_results=5,lang="pt-br")
    url = requests.get(searchOnGoogle[0])
    print(f"{i}º {x}")
    print("The URLs have been saved!")
    print(url.url)
    answer = Input("Do you want another site?").lower()
    if answer == "y":
        a = 0
        for x in searchOnGoogle:
            print(f"{x} [{a}]")
            a+=1
        boolean = True
        while boolean:
            answer = input("Type the site number: ")
            try:
                url = requests.get(searchOnGoogle[int(answer)])
                boolean= False
            except:
                print("Type a valid number!!!")
    print("Url defined!")
    site = BeautifulSoup(url.content,"html.parser")
    content = site.findAll(['p', 'spam'])
    print("Content has been captured!")
    file = open(f"Results/Result {results}.txt", "w", encoding="utf-8")
    print("Archive .txt was created!")
    for x in content:
        file.write(x.get_text()+"\n")
    print(f"Content written in Results/{results}.txt!")
    file.close()
    print(f"****{results}.txt was finished!****\n")
    results+=1

#Code
print("\n")
if os.path.exists("Results/") == False:
    os.system("mkdir Results")
if os.path.exists("search.txt") == True:
    file = open("search.txt", "r", encoding="utf-8")
    for x in file:
        Search(x)
        i+=1
    file.close
else:
    file = open("search.txt", "w", encoding="utf-8")
    file.write("")
    file.close()
if i == 0:
    SearchByInput()
answer = Input("Do you want to open all the researches")
result = 1
while True:
    if answer == "s" and os.path.exists(f"Results/Result {result}.txt"):
        print(f"{result}.txt has been opened!")
        os.system(f'notepad.exe "Results/Result {result}.txt"')
        result+=1
    else:
        break
answer = Input("Do you want to remove all the researches")
result = 1
while True:
    if answer == "s" and os.path.exists(f"Results/Result {result}.txt"):
        os.remove(f"Results/Result {result}.txt")
        print(f"{result}.txt was been deleted!")
        result+=1
    else:
        break