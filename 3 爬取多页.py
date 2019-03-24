import requests
from lxml import etree
import pandas as pd
def geturl(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "False"
def pathurl(r,pinglun):
    s=etree.HTML(r)
    file=s.xpath('//*[@id="comments"]/ul[1]/li/div[2]/p/span/text()')
    pinglun+=file
    return pinglun
def saveurl(file):
    df=pd.DataFrame(file)
    df.to_csv("pinglun3.csv",encoding="utf-16")
if __name__=="__main__":
    pinglun=[]
    for i in range(1,13):
        url="https://book.douban.com/subject/25826936/comments/hot?p={}".format(i)
        r=geturl(url)
        pinglun=pathurl(r,pinglun)
    print(pinglun)
    saveurl(pinglun)