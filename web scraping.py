# importing the necessary packages
import numpy as np
import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.entekhab.ir/fa/archive'
data = {
    'from_date': '1396/01/01',
    'to_date': '1399/01/01',
    'rpp':'1000000'
}
r = requests.post(url, data = data)
coverpage = r.content

soup = BeautifulSoup(coverpage, 'html5lib')

coverpage_news = soup.find_all('div', class_='linear_news')

len(coverpage_news)

for n in np.arange(0, len(coverpage_news)):
    
    # Getting the link of the article
    link = 'https://www.entekhab.ir' + coverpage_news[n].find('a')['href']
    
    id = link.split("/")[5]
    
    file = open(id + '.txt', 'w')
    
    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    file.write(title)
    file.write('\n')
    
    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='khabar-matn')
    x = body[0].find_all('p')
    
    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
        
    file.write(final_article)
    file.close()
    time.sleep(1)
