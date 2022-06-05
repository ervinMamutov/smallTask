from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())

print('\n')

titles = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print([title for title in titles])

print('\n')

all_Text = bs.find_all('span', {'class': {'green', 'red'}})
print([text for text in all_Text])

print('\n')

nameList2 = bs.find_all(text='the prince')
print(len(nameList2))

print('\n')

