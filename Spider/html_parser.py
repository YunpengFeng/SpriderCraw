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

class HtmlParser(object):
    # 设置请求时间超过6 秒就抛出异常
    socket.setdefaulttimeout(6)
    def parse_datas(self, new_url, html_content):
        if new_url is None or html_content is None:
            return None
        soup = BeautifulSoup(html_content,'html.parser')
        new_urls = self._get_new_urls(new_url,soup)
        path = self.creatFile(new_url)
        urls = self._get_cut_str(new_url)
        fail_url, count = self.copy_data(urls,path)
        self.copy_fail(fail_url, path)
        return new_urls , urls

    # 复制一张图片到本地 param urls（列表）  是ajax 的url地址   return fail_url（）失败的set，success_count（）成功个数
    def copy_data(self, urls,path):
        fail_urls = set()
        count = 0
        for url in urls:
            wb_data = requests.get(url)
            dict = wb_data.json()
            success_count = 0,
            if 'data' in dict:
                str = dict['data']
            for k in str:
                _str = k.get('thumbURL')
                fail_url, success_count = self.copy_pic(_str,path)
                if(success_count==0):
                    fail_urls.add(fail_url)
                count = success_count + count
            print('......图片复制失败个数..', len(fail_urls))
        return fail_urls, count

    # 复制一张图片到本地 param _str链接地址   return fail_url（）失败的set，success_count（）成功个数 path 是父路径
    def copy_pic(self, _str, path):
        success_count = 0
        if _str is not None:
            if _str.endswith('.jpg') and _str.startswith('http'):
                pic_name = _str.split("/")[-1]
                absoultpath = path + '\\' + pic_name
                try:
                    request.urlretrieve(_str, absoultpath)
                    success_count = success_count + 1
                except:
                    return _str,0
            else:
                return None, 0
        return None, 1

    # 失败的继续循环复制 param set()  return None  要避免陷入死循环
    def copy_fail(self,fail_url, path):
        while len(fail_url) > 0:
            link = fail_url.pop()
            small_fail_url, success_count = self.copy_pic(link,path)
            if success_count == 0:
                fail_url.add(small_fail_url)
                success_count = 0
        return


    '''
        获取页面数据<a class="pull-rs" title="查看 少女和大叔农村实拍" target="_self" href="/search/index?ct=201326592&amp;cl=2&amp;st=-1&amp;lm=-1&amp;nc=1&amp;ie=utf-8&amp;tn=baiduimage&amp;ipn=r&amp;rps=1&amp;pv=&amp;fm=rs15&amp;word=%E5%B0%91%E5%A5%B3%E5%92%8C%E5%A4%A7%E5%8F%94%E5%86%9C%E6%9D%91%E5%AE%9E%E6%8B%8D&amp;oriquery=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&amp;ofr=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&amp;ctd=1523443894018^00_1349X637&amp;hs=2&amp;sensitive=0">少女和大叔农村实拍</a>
    '''
    #获取urls
    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all('a',class_ ='pull-rs')
        for link in  links:
            _link  =  link.get('href')
            new_full_url = 'https://image.baidu.com' + _link
            new_urls.add(new_full_url)
        return new_urls

    # 创建文件夹
    def creatFile(self, url):
        picFile = 'F:\\CopyPictrue'
        #先进行转码，截取链接从word开始的字符串,有则获取字符串，无则获取当前时间
        from urllib import parse
        var1 = parse.unquote(url)
        if var1.find("word", 0, len(var1)):
            var2 = var1.split("word")[-1]
            var3 = var2[1:len(var2)].split("&")[0]
            var4 = var3 + str(datetime.datetime.now().strftime('%H%M%S'))
            var5 =picFile+'\\'+var4
            # 去除首位空格
            path = var5.strip()
            # 去除尾部 \ 符号
            path = path.rstrip("\\")
            if os.path.exists(path) is False:
                os.makedirs(path)
            return path
        else:
            temp =datetime.datetime.now().strftime('%Y-%m-%d~%H.%M.%S')
            var5 = picFile + '\\' + temp
            # 去除首位空格
            path = var5.strip()
            # 去除尾部 \ 符号
            path = path.rstrip("\\")
            if os.path.exists(path) is False:
                os.makedirs(path)
            return path

    '''
         根据异步请求获取数据，然后进行组装url
         要模拟下拉条滚动事件
         但是模拟失败，只能看network里面的了
         '''
    #规则是搜索的word 和分页的到第几张数 比如0 30 60 90 120 参数come_url是来自原网页
    def _get_cut_str(self,come_url):
        if come_url.find("word", 0, len(come_url)):
            var2 = come_url.split("word")[-1]
            var3 = var2[1:len(var2)].split("&")[0].strip().rstrip()
            urls = set([
                'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=' + var3 + '&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn={a}&rn=30'.format(
                    a=i)
                for i in range(0, 10) if i % 30 == 0])
            return urls
        return None
