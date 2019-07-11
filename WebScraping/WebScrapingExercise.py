from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

# URL Testing
url = input('Enter URL for Testing:- ')
try:
    urlopen(url)
except:
    print('no such url')
else:
    print('url exists')
finally:
    print('thanks for using our project')

# Robots.txt

url = 'https://en.wikipedia.org/robots.txt'
html = urlopen(url)
soup = bs(html, 'lxml')
print(soup.prettify())

# no. Of Datasets

url = 'https://catalog.data.gov/dataset'
soup = bs(urlopen(url), 'lxml')
res = soup.find('div', class_='new-results')
print(res.text.strip())

# Latest Datasets

url = 'https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAVlqhVuBYv9rqgiTnsQzVjeRZTlB9kLz2EBY26ODAved2OpRjG7LORV15e6pD_lbIsZwrb1O573r6kkru4KUA5fg5Wt9v0N37Ugq_Hwsx6QJJdFhi7mqwelmfikpnL3IV0%3D&as_fid=30fc321c15d401d32eb00cfbeebc5592f21feda8&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C8.754794702435618%2C-59.0625%2C61.77312286453146'
soup = bs(urlopen(url), 'lxml')
li = soup.find('h3', class_='dataset-heading')
print("Lastest Datasets:- ", li.text)

# Example Domain

url = 'https://example.com'
soup = bs(urlopen(url), 'lxml')
li = soup.find('h1')
print(li.text)

# Wiki Tags

url = 'https://en.wikipedia.org/wiki/Main_Page'
soup = bs(urlopen(url), 'lxml')
for i in range(1, 7):
    s = 'h' + str(i)
    li = soup.find_all(s)
    print(s, ' Tags\n')
    for j in li:
        print(j.text.strip())
    print('\n')

# Images

url = 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
soup = bs(urlopen(url), 'lxml')
li = soup.find_all('img', class_='thumbimage')
print(li.__len__())
for i in li:
    print(i['src'])

# Browser History

url = 'https://analytics.usa.gov/data/live/browsers.json'
re = urlopen(url)
resp = requests.get(url)
rr = resp.json()
print(rr['totals']['browser'])

# Get all Links Wiki
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
soup = bs(urlopen(url), 'lxml')
li = soup.find_all('a', href=True)
for i in li:
    print(i['href'])
