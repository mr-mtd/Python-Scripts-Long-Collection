import requests
from bs4 import BeautifulSoup
import time
import unicodedata
from TriviaSet import TriviaSet
import json

def main():
    # create an empty list to store the URLs
    url_list = []
    triviaSetsMain = []

    # populate the list with 150 URLs
    for i in range(100, 129):
        url = 'https://triviachamp.com/General-Knowledge-Trivia-Questions-E' + str(i) + '.php'
        url_list.append(url)

    # open a file to write the scraped content
    with open('C:\\Users\\mason\\Desktop\\scrapedTriv.txt', 'w') as f:
        # iterate over the URLs and scrape the content
        for url in url_list:
            # send a request to the URL
            response = requests.get(url)

            # parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # find the div with class "XSP_MAIN_PANEL" and extract its text
            xsp_main_panel = soup.find('table', {'class': 'XSP_CENTER_PANEL'}).find('tr')

            text = xsp_main_panel.text
            textF = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
            print(textF)
            # write the extracted text to the file
            f.write(textF)
            time.sleep(1)
            with open('C:\\Users\\mason\\Desktop\\scrapedTrivFinal.txt', 'w') as ff:
                triviaSetsMain.extend(oranizeQuesstionsChoicesAndAnswers())
                mySetToDictJsonStr = ''
                for item in triviaSetsMain:
                    mySetToDictJsonStr +=  json.dumps(item.to_dict()) + "\n"
                print("Trivia Jason from dict is: \n" + mySetToDictJsonStr)
                ff.write(mySetToDictJsonStr);

def oranizeQuesstionsChoicesAndAnswers():

    triviaSets = []
    with open('C:\\Users\\mason\\Desktop\\scrapedTriv.txt', 'r') as f:
        my_tri_q = TriviaSet()
        for line in f:
            print("line is: " + str(line))
            if not any(c.isalnum() for c in line):
                print("line contains no alphanumeric numbers, skipping. line was: " + str(line))
                continue
            else:
                print("line contains alphanumeric numbers, continuinig. line was: " + str(line))
            if '?' in line:
                my_tri_q.questions = line.strip()
            elif line.strip().startswith('a. '):
                my_tri_q.a  = line.strip()
            elif line.strip().startswith('b. '):
                my_tri_q.b  = line.strip()
            elif line.strip().startswith('c. '):
                my_tri_q.c  = line.strip()
            elif line.strip().startswith('d. '):
                my_tri_q.d  = line.strip()
            elif ':' in line:
                my_tri_q.answer = line.strip()
                triviaSets.append(my_tri_q)
                my_tri_q = TriviaSet()

    return triviaSets

if __name__ == '__main__':
    main()