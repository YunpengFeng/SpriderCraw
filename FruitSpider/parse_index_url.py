from FruitSpider import html_downloader
from bs4 import BeautifulSoup
'''
    获取本地淘宝文件中水果种类url链接
'''


class InItazier(object):

    def initurlmap(self):
        #读取本地文件
        url = 'fruit.html'
        htmlfile = open(url, 'r', encoding='UTF-8')  #以只读的方式打开本地html文件
        content = htmlfile.read()
        soup = BeautifulSoup(content, 'html.parser')
        url_list = soup.find_all(class_='hot-word ')
        url_map = {}
        for a in url_list:
            url_map[a.string] = "http:"+ a.attrs['href']
        print(url_map.items())
        #for _li in url_map:
        #   print("键：", _li, '值：', url_map[_li])
        return url_map


