import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/Woramanot/chromedriver')
#driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
time.sleep(20)
driver.get('https://qz.com/africa/')
time.sleep(20)

elements = driver.find_elements_by_xpath("//a[@class='latest header-button']")
element = elements[0]
element.click()
time.sleep(5)

page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
articles = soup.find(id='queue')
weblinks = articles.find_all('h2', {'class':'queue-article-title'})
pagelinks = []
for link in weblinks:
    url = link.contents[0]
    pagelinks.append(url.get('href'))


authorname = []
title = []
thearticle = []
for link in pagelinks:
    # store the text for each article
    paragraphtext = []
    # get url
    url = link
    # get page text
    page = requests.get(url)
    # parse with BFS
    soup = BeautifulSoup(page.text, 'html.parser')
    # get author name, if there's a named author
    try:
        abody = soup.find(class_='author-name')
        aname = abody.get_text()
    except:
        aname = 'Anonymous'
    # get article title
    atitle = soup.find(itemprop='headline')
    thetitle = atitle.get_text()
    # get main article page
    articlebody = soup.find(class_='item-body')
    # get text
    articletext = soup.find_all('p')
    # print text
    for paragraph in articletext:
        # get the text only
        text = paragraph.get_text()
        paragraphtext.append(text)
    # combine all paragraphs into an article
    thearticle.append(paragraphtext)
    authorname.append(aname)
    title.append(thetitle)
myarticle = [' '.join(article) for article in thearticle]