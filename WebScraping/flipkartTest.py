from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import pandas as pd

url = 'https://www.flipkart.com/mens-watches-store?otracker=nmenu_sub_Men_0_Watches'
html = urlopen(url)
soup = BS(html, 'lxml')
print(soup.title)
nameT = soup.find_all('a', class_='_2cLu-l')
test= soup.find_all('div',class_='_3liAhj _2Vsm67')
name = []
rate = []
price = []
orgPrice = []
discount = []
ct = 0
for i in nameT:
    n = i.text
    name.append(n)
for i in test:
    r = i.find('div', class_='hGSR34')
    p = i.find('div', class_='_1vC4OE')
    o = i.find('div', class_='_3auQ3N')
    d = i.find('div', class_='VGWI6T')
    if r is None:
        rate.append('NaN')
    else:
        rate.append(r.text)
    if p is None:
        price.append('NaN')
    else:
        price.append(p.text)
    if o is None:
        orgPrice.append('NaN')
    else:
        orgPrice.append(o.text)
    if d is None:
        discount.append('NaN')
    else:
        discount.append(d.text)
    ct += 1
print(ct)
print(tes.text)
print(name)
print(rate)
print(price)
print(orgPrice.__len__())
print(discount)
df = pd.DataFrame({'name': name, 'rate': rate, 'price': price, 'original price': orgPrice, 'discount': discount})
df.to_csv('FlipKart.csv', index=False)
print(df)
