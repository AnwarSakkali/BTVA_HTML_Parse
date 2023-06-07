## Fire Emblem Wiki scraper
To get VAs from the Fire Emblem Wiki with a json file as output:
- Run FEWikiScraper.java or FEWikiScraper.py

## BTVA HTML Parser
To get VAs from BehindTheVoiceActors (BTVA) from (what seems to be) any game, do the following:
- Download the html of the Voice Actor page from the game you want.
- Run BTVAHTMLParser.java with as input the html file that contains the list of voice actors
- Run sortingJson.py to sort the json you've received from the parser on name or surname
- (Bonus) Run JsonToWikiFormat.py to create an printed output that supports the table structure of FireEmblemWiki.org
