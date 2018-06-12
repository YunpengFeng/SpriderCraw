from bs4 import BeautifulSoup
from urllib import parse
import urllib
import re
from urllib import request
import sys
import requests
import socket
import time
import datetime
import os
from BlackSpider import html_downloader


class HtmlParser(object):
    # 设置请求时间超过6 秒就抛出异常
    socket.setdefaulttimeout(6)
    def __init__(self):
        # html页面下载器
        self.downloader = html_downloader.HtmlDownloader()


    def parse_datas(self, type, sourceurl, html_content):
        big_content = set()
        soup = BeautifulSoup(html_content, 'html.parser')
        #根据分页获取新的链接
        new_urls = self._get_new_urls(sourceurl, soup)
        #for url in new_urls:
        while len(new_urls)>0:
            url =new_urls.pop()
            small_content = self.downloader.downloader_html(url)
            #请求失败
            if small_content == None:
                new_urls.add(url)
                continue
            #请求成功匹配数据？？、？？new_urls.pop(url)
            else:
                soup = BeautifulSoup(small_content, 'html.parser')
                list = soup.find_all('a', {'href': re.compile('/html/*')}, target="_blank")
                #big_content.add([li for li in list])
                for li in list:
                    big_content.add("http://www.80sbs.com/"+li.attrs['href'])
                print(len(big_content))
        return big_content

    #获取urls
    def _get_new_urls(self, new_url, soup):
        links = soup.find('div', class_='pagination').find_all("a")[-1]
        prefix = new_url[:-5]
        # 获取当前有多少页
        pagesize = str(links)[28:31]
        #return set([prefix +'_{a}.html'.format(a =i) for i in range(1, int(pagesize)+1)])
        return set([prefix + '_{a}.html'.format(a=i) if i != 1 else prefix+".html" for i in range(1, 2)])
