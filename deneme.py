from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.coingecko.com/tr")
soup = BeautifulSoup(r.content,"lxml")
coin = soup.find_all("a",attrs={"class":"tw-flex tw-flex-auto tw-items-start md:tw-flex-row tw-flex-col"})
for i in coin:
    links=i.a.get("href")
    print(links)