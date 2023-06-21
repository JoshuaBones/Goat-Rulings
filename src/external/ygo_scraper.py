#is meant to be run through vscode, that way the paths are correct
#simply puts all rulings from https://www.goatformat.com/indivrulings.html
#into a readable json file - keeps raw html as inconsistencies, if there, would cause problems.
#ruling update frequency is unknown, and can't rip this client-side due to CORS, so a separate python file is the best I've got
import json

import requests
from bs4 import BeautifulSoup

firstLink = "http://www.goatformat.com/rulings"
lastLink = ".html"
links = []

for i in range(1,9):
    links.append(firstLink + str(i) + lastLink)

rulings = {}
for link in links:
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')

    curr_rulings = soup.find_all("div", {"class": "paragraph"})[0]

    #currRulings is the parent and contains everything, so 
    #next_element to start and next_sibling for everything else
    ruling_elements = curr_rulings.next_element

    currKey = ''
    while ruling_elements != None:     

        if ruling_elements.name == 'strong':
            currKey = str(ruling_elements.next)
        else:
            if ruling_elements.name != 'br':
                rulings[currKey] = rulings.get(currKey, '') + str(ruling_elements)

        ruling_elements = ruling_elements.next_sibling
    
with open("./src/rulings.json", "w") as outfile:
    json.dump(rulings, outfile)