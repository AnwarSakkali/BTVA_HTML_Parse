from BTVAHtmlParser import main
from JsonToWikiFormat import run
from SortingJson import sortKeysBySurnameInJson
import os

def find_html_file():
    root_dir = os.getcwd()
    for file_name in os.listdir(root_dir):
        if file_name.endswith(".html") and os.path.isfile(file_name):
            return file_name
            
game = find_html_file()
print("-------------------------------------------")
main(game)
print("-------------------------------------------")
sortKeysBySurnameInJson(game + ".json")
print("-------------------------------------------")
run(game + ".json")
input()