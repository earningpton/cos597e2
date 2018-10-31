import requests
import csv
import time
from bs4 import BeautifulSoup

# target
#<span class="domain">
#"("
#<a href="/r/datascience/">self.datascience</a>
#")"
#</span>

url = "https://old.reddit.com/r/wallstreetbets/"
# Headers to mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

# Returns a requests.models.Response object
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
domains = soup.find_all("span", class_="domain")
#soup.find_all("span", {"class": "domain", "height", "100px"})
for domain in soup.find_all("span", class_="domain"):
    if domain != soup.find_all("span", class_="domain")[10]:
        continue

    parent_div = domain.parent.parent.parent.parent
    print(parent_div.text)
print(soup.find_all("span", class_="domain")[10].parent.parent.parent.parent.text)