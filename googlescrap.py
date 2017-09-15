import requests
from bs4 import BeautifulSoup as bs
url="https://www.google.co.in/search?q="
print("what you want to search")
url=url+input()
print(url)
page=requests.get(url)
soup=bs(page.content,'html.parser')
x=soup.find_all('h3',{'class':'r'})
#x=soup.find_all('div',{'class':'f kv _SWb'})
for link in x:
    print(link.a['href'].split('=')[1])
    #print(x[0].a['href'])
#print(x)
