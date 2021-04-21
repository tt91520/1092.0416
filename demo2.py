import sys
import requests
from bs4 import BeautifulSoup
import time

URL="https://search.books.com.tw/search/query/key/{0}/cat/all"

def generate_search_url(url,keyword):
    url=url.format(keyword)
    return url

def get_resource(url):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
        "AppleWebKit/537.36 (KHTML, like Gecko)" 
        "Chrome/89.0.4389.114 Safari/537.36"
        }
    return requests.get(url,headers=headers,verify=False)

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding="utf8"
        soup=BeautifulSoup(r.text,"lxml")
    else:
        print("HTTP request error..."+url)
        
        soup=None
    return soup

def web_scraping_bot(url):
    booklist=[]
    print("retrive data from Internet...")
    soup=parse_html(get_resource(url))
    #print(soup)
    if soup!=None:
        tag_item=soup.find_all(class_="box_1")
        #print(tag_item)
        for item in tag_item:
            book=[]
            book.append(item.find("img")["alt"])
            [isbn,price]=get_ISBN_Price(item.find("a")["href"])
            book.append(isbn)
            book.append(price)
            print(book)
            
            
            print("wait 5 sec")
            time.sleep(5)

def get_ISBN_Price(url):
    url1="https:"+url
    soup=parse_html(get_resource(url1))
    inbnStr=""
    if soup!=None:
        bd=soup.find(class_="bd")
        liList=bd.find_all("li")
        print("liList \n",liList)
        price=0
        priceUl=soup.find('ul',{'class':'price'})
        for liData in liList:
            print("liData \n\n",liData.text)
            if "ISBN" in liData.text:
                isbnStr=liData.text[5:]
        price=priceUl.find('li').text[3:-1]
        return [isbnStr,price]
    else:
        return [None,None]
    
if __name__=="__main__":
    if len(sys.argv)>1:
        url=generate_search_url(URL,sys.argv[1])
        #print(url)   1
        #r=get_resource(url)   2
        #soup=BeautifulSoup(r.text,"lxml")   2
        #print(soup)   2
        booklist=web_scraping_bot(url)
        #for item in booklist:   3
            #print(item)   3