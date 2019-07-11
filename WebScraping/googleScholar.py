from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import pandas as pd


# arxiv
def inp(s):
    str = '+'.join(s)
    return 'https://arxiv.org/search/?query=' + str + '&searchtype=all&source=header'


def getblock(soup, div, clas):
    return soup.find_all(div, class_=clas)


def getpdfandother(block, clas):
    li = []
    for i in block:
        li.append(i.a[clas])
    return li


def getheading(block, div, clas):
    li = []
    for i in block:
        if clas == '':
            li.append(i.find(div).text.strip())
        else:
            li.append(i.find(div, class_=clas).text.strip())
    return li


def getauthors(block, div, clas):
    li = []
    for i in block:
        li.append(i.find(div, class_=clas).text)
    return li


def getsummary(block, div, clas):
    li = []
    for i in block:
        li.append(i.find(div, class_=clas).text.strip())
    return li


# eric
def inpe(s):
    str = '+'.join(s)
    return 'https://eric.ed.gov/?q=' + str


# arvxi
s = input('Enter name to the searched:- ')
url = inp(s.split())
html = urlopen(url)
soup = BS(html, 'lxml')
block = getblock(soup, 'li', 'arxiv-result')
heading = getheading(block, 'p', 'title is-5 mathjax')
pdfother = getpdfandother(block, 'href')
authors = getauthors(block, 'p', 'authors')
for i in range(authors.__len__()):
    authors[i] = authors[i].replace('\n', '').replace('        ', '').replace("    ", '').replace(
        'Authors:', '').replace(',', ';')
summary = getsummary(block, 'span', 'abstract-short has-text-grey-dark mathjax')
df = pd.DataFrame({'Heading': heading, 'Authors': authors, 'Summary': summary, 'Link': pdfother})

# eric
url = inpe(s.split())
html = urlopen(url)
soup = BS(html, 'lxml')
block = getblock(soup, 'div', 'r_i')
heading = getheading(block, 'a', '')
pdfother = getpdfandother(block, 'href')
for i in range(pdfother.__len__()):
    pdfother[i]='https://eric.ed.gov/'+pdfother[i]
authors = getauthors(block, 'div', 'r_a')
for i in range(authors.__len__()):
    l = authors[i].split('–')
    authors[i] = l[0]
summary = getsummary(block, 'div', 'r_d')
df1 = pd.DataFrame({'Heading': heading, 'Authors': authors, 'Summary': summary, 'Link': pdfother})
dfF = pd.concat([df, df1], ignore_index=True)
print(dfF)
dfF.to_csv('testscholar.csv')