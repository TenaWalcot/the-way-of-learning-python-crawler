from lxml import etree#必须写成from...import ...
import requests
url="https://book.douban.com/subject/25826936/"
r=requests.get(url).text#别忘了.text
s=etree.HTML(r)
print(s.xpath('//*[@id="link-report"]/span[1]/div/p[1]/text()'))#浏览器复制
print(s.xpath('//*[@id="link-report"]/span[1]/div/p/text()'))
print(s.xpath('//div[@class="intro"]/p/text()'))#手写
print(s.xpath('//div[@class="intro"]/p[1]/text()'))#手写