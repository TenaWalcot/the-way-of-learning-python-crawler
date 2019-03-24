import requests
from lxml import etree
url="https://book.douban.com/subject/25826936/comments/"
r=requests.get(url).text
s=etree.HTML(r)
file=s.xpath('//*[@id="comments"]/ul[1]/li/div[2]/p/span/text()')
with open("pinglun1.txt","w",encoding="utf-8") as f:
    for i in file:
        print(i)
        f.write(i+'\n')