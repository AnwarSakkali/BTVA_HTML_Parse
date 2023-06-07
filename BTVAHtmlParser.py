import json
from bs4 import BeautifulSoup

def main(html):
    jsonObject = {}

    with open(html, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    body = soup.find("div", class_='credit_pics_wide')

    divs = body.find_all("div")

    for div in divs:
        if div.find("h3"):
            voiceActor = div.find("h3").text
            print(voiceActor)
            allDivs = div.find_all("div")
            
            try:
                jpDiv = allDivs[2]
                japanese = jpDiv.img['title']
                print(japanese)
            except:
                pass
            alts = div.find_all("a")
            count = 2
            characterArray = []
            for i in alts:
                try:
                    character = alts[count]['title']
                    print(character)
                    count += 1
                    characterArray.append(character)
                except:
                    pass
            jsonObject[voiceActor] = characterArray
            print("------------------------")

    with open(html + ".json", "w") as file:
        json.dump(jsonObject, file)