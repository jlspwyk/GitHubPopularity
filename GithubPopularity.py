from bs4 import BeautifulSoup
import urllib.request
import requests
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

GithubPopularityURL = 'https://github.com/search?p=1&q=stars%3A%3E1000&type=Repositories'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/55.0.2883.87 Safari/537.36'}
r = requests.get(GithubPopularityURL, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
htmlList = []
tags = soup.find_all(name = 'a', attrs={'class' : 'v-align-middle'})
for tag in tags:
    htmlList.append('https://github.com' + tag.get('href'))
print(htmlList)