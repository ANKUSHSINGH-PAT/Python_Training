
import requests
from bs4 import BeautifulSoup
with open(r"Day4\Index.html", "r") as html_file:
    html_content = html_file.read()
    soup_html = BeautifulSoup(html_content, "html.parser")

    links = soup_html.find_all('a', href=True)
    p_tags=soup_html.find_all('p')


    for link in links:
        abc=link.get('href')
        if abc.startswith('http://') or abc.startswith('https://'):
            print(abc)

    for tag in p_tags:
        print(tag.get_text())
        # tag1=tag.get()
        # if tag1.startswith('</p>'):
        #     print(tag1)
