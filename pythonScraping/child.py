from urllib.request import urlopen

from bs4 import BeautifulSoup

import re


html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

print('2 \n')

for sibling in bs.find('table',{'id': 'giftList'}).tr.next_siblings:
    print(sibling)

print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())


print('3 \n')

images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

print('4 \n')

images = bs.find_all((lambda tag: len(tag.attrs) == 2))
print(images)
