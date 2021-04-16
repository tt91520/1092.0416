import sys
import requests
import time
from bs4 import BeautifulSoup


URL = "https://search.books.com.tw/search/query/key/{0}/cat/all"


def generate_search_url(url, keyword):
    url = url.format(keyword)
    return url


def get_resource(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
    return requests.get(url, headers = headers)


def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
    else:
        print("HTTP request error..." + url)
        soup = None
    return soup


def web_scraping_bot(urls):
    booklist = []
    print("retrive data from Internet...")
    soup = parse_html(get_resource(url))
    #print(soup)
    if soup != None:
        tag_item = soup.find_all(class_ = "box_1")
        #print(tag_item)
        for item in tag_item:
            book = []
            book.append(item.find("item")["alt"])
            [isbn, price] = get_ISBN_Price(item.find("a")["href"])
            book.append(isbn)
            book.append(price)
            print(book)
            print("wait 2 sec")
            time.sleep(2)


def get_ISBN_Price(url):
    url1 = "https:" + url
    print(url1)
    return [url1, '1000']


if __name__ =="__main__":
    if len(sys.argv) > 1:
        url = generate_search_url(URL, sys.argv[1])
        #print(get_resource(url).text)
        '''
        r=get_resource(url)
        soup=BeautifulSoup(r.text,"lxml")
        print(soup)
        '''
        booklist = web_scraping_bot(url)
        #for item in booklist:
            #print(item)
        