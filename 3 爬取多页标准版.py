import requests
from lxml import etree
import pandas as pd
urls=["https://book.douban.com/subject/25826936/comments/hot?p={}".format(str(i)) for i in range(1,13)]
comment=[]
for url in urls:
    r=requests.get(url).text
    s=etree.HTML(r)
    comment+=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')
print(comment)
df=pd.DataFrame(comment)
df.to_csv("pinglun4.csv")