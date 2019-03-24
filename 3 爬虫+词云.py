import requests
from lxml import etree
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
import jieba
urls=["https://book.douban.com/subject/25826936/comments/hot?p={}".format(i) for i in range(1,12,1)]
comment=[]
for url in urls:
    r=requests.get(url).text
    s=etree.HTML(r)
    comment+=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')
d = path.dirname(__file__)
text = open(path.join(d, 'pinglun5.txt'),encoding='utf-8').read()
wordlist = jieba.cut(text, cut_all=True)
wl = " ".join(wordlist)
print(wl)
wc = WordCloud(font_path='simhei.ttf')
wc.generate(wl)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.show()