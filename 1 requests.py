import requests
url="https://book.douban.com/subject/25826936/"
r=requests.get(url)
print(r)
print(r.status_code)#对象的返回状态，200/500既是正常
print(r.text)#对象的文本格式
print(r.encoding)#对象的编码格式
print(r.content)#对象的二进制格式
print(r.apparent_encoding)#备选编码