import requests
from lxml import etree
import pandas as pd
url="https://book.douban.com/subject/25826936/comments/"
r=requests.get(url).text
s=etree.HTML(r)
file=s.xpath('//*[@id="comments"]/ul[1]/li/div[2]/p/span/text()')
df=pd.DataFrame(file)
df.to_csv("pinglun2.csv")