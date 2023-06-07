import json
import requests
from bs4 import BeautifulSoup

url = "https://fireemblemwiki.org/wiki/Voice_actors_of_the_Fire_Emblem_series"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

tables = soup.find_all("table")

JapaneseFehVAs = tables[29]

rows = JapaneseFehVAs.find_all("tr")

jsonObject = {}

for row in rows:
    tds = row.find_all("td")
    if len(tds) >= 2:
        firstTdText = tds[0].text.strip()
        secondTdText = tds[1].text.strip()
        
        names = secondTdText.split(", ")
        characterArray = []
        for name in names:
            characterArray.append(name)
        jsonObject[firstTdText] = characterArray

with open("output.json", "w") as file:
    json.dump(jsonObject, file)
