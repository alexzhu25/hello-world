#!/usr/bin/python
#Get website input from user. Scans website and outputs text to file with name related to website

import os
import codecs
import requests
from bs4 import BeautifulSoup


website = input("Please input a website (include http): ")
websitename = website.split('/')
filename = websitename[2] + "-samplepage.txt"

#Creates new file or accesses and overwrites file in current directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
websitetext = open(os.path.join(__location__, filename), 'w')

r = requests.get(website)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
html_text_body = soup.find_all(["h1", "p"])
for html_text in html_text_body:
    line = html_text.get_text()
    try:
        print(line)
        websitetext.write(line + "\n")
    except Exception: 
        print(str(line.encode("utf-8",'ignore')) + "\n")

websitetext.close()