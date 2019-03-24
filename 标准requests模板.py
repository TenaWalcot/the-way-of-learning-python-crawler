import requests
def Geturl(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "False"
if __name__=="__main__":
    url="https://book.douban.com/subject/25826936/"
    print(Geturl(url))