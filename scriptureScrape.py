#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import pandas as pd

def pullScrip(work, book, ch):
    """
    Pulls the given chapter of a book from churchofjesuschrist.org
    work: specific work its found in i.e. ot for old testament.  See website for name
    book: specific book its found in i.e. gen for genesis.  See website for specific name
    ch: chapter to pull
    Returns the body of the scripture with tags stripped out
    """
    url = f"https://www.churchofjesuschrist.org/study/scriptures/{work}/{book}/{ch}?lang=eng"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    body = soup.find('div', class_ = 'body-block')

    for sup in body.find_all('sup'):
        body.sup.decompose()

    for verses in body.find_all('p'):
        for links in verses.find_all('a'):
            links.unwrap()
    return body

# Iterate through books pulling verses of each chapter and appending them to pandas df
bookList = pd.read_csv("data/")
scriptures = pd.DataFrame([["Book","Work", "Chapter", "Verse"]])

work = "bofm"
book = "1-ne"
ch = 1

body = pullScrip(work, book, ch)

for verse in body.find_all('p'):
    ver = ''
    for string in verse.strings:
        ver += string
    print(ver + '\n')
    scriptures.loc[len(scriptures.index)] = [, 3, 4]
    


