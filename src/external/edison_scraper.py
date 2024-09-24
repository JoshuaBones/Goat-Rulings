#is meant to be run through vscode, that way the paths are correct
#simply puts all rulings from https://www.goatformat.com/indivrulings.html
#into a readable json file - keeps raw html as inconsistencies, if there, would cause problems.
#ruling update frequency is unknown, and can't rip this client-side due to CORS, so a separate python file is the best I've got
import json

import requests
from bs4 import BeautifulSoup

#inconsistent links, so this is necessary
mainLink = "https://www.edisonformat.com/rulings/"
ends = ["individual-rulings-a-c", "individual-rulings-d-e", "individual-rulings-f-h", 
        "individual-rulings-i-k", "individual-rulings-l-o", "individual-card-rulings-p-r", 
        "individual-card-rulings-s-t", "rules-u-z"]
links = []

for end in ends:
    links.append(mainLink + str(end))
    
        

print('starting')

rulings = {}
for link in links:
    print('retrieving data: ' + link)
    #little crazy with the format fixes. Done with sublime text ctrl+shift+L after searching < in card names on the site, but sadly it removes any formatting on the site for some reason
    html_text = requests.get(link).text#.replace('<strong>CHARM OF SHABTI</strong>', 'CHARM OF SHABTI').replace('<span><span>D - FORMATION</span> </span>', 'D - FORMATION').replace('<span><span>D - TIME</span> </span>', 'D - TIME').replace('<span><span>D. D. CRAZY BEAST</span> </span>', 'D. D. CRAZY BEAST').replace('<span><span>D. D. DESIGNATOR</span> </span>', 'D. D. DESIGNATOR').replace('<span><span>D. D. DYNAMITE</span> </span>', 'D. D. DYNAMITE')
    soup = BeautifulSoup(html_text, 'html.parser')

    #curr_rulings = soup.find_all("div", {"class": "paragraph"})[0]
    curr_rulings = soup.find_all("strong")[0]

    #currRulings is the parent and contains everything, so 
    #next_element to start and next_sibling for everything else
    ruling_elements = curr_rulings#.next_element

    currKey = ''
    while ruling_elements != None:  

        if ruling_elements.name == 'strong':
            currKey = str(ruling_elements.next)
        else:
            if ruling_elements.name != 'br':
                rulings[currKey] = rulings.get(currKey, '') + str(ruling_elements)

        ruling_elements = ruling_elements.next_sibling
print('finished retrieving\nwriting to file')
    
with open("./src/edison_rulings.json", "w") as outfile:
    json.dump(rulings, outfile)
print('finished successfully')