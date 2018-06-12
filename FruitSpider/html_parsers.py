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
import threading
from FruitSpider import parse_index_url, url_manager, html_downloader, html_parsers
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import random
import xlsxwriter
import xlrd
import xlutils.copy
from xlrd import open_workbook
from xlutils.copy import copy
class HtmlParser(object):
    # 设置请求时间超过6 秒就抛出异常
    socket.setdefaulttimeout(6)

    def __init__(self, indexurl, typenum):
        self.index_url =indexurl
        self.url_manager = url_manager.UrlManager()
        self.down_html = html_downloader.HtmlDownloader()
        self.type_num = typenum
    def get_all_list(self,m):
        self.url_manager.add_new_url(self.index_url)
        flag = 0
        startNum = 10057+(self.type_num*60)
        count = startNum
        flag = 1
        while self.url_manager.has_new_url():
            new_url = self.url_manager.get_new_url()
            content = self.down_html.downloader_html(new_url)
            #判断是列表页还是详情页： 1列表页，其他详情页
            if flag == 1:
                self.get_parser_url(content)
                flag = 0
                print("............列表页爬取成功........")
            else:
                self.get_data(content, count,m)
                count = count + 1

    # 获取水果列表链接url及其页码所有查询
    def get_parser_url(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all(class_="productTitle")
        for link in links:
            furl = link.find("a")
            temp = furl.attrs['href']
            self.url_manager.add_new_url('http:'+temp)
        print("获取的子链接有......", self.url_manager.getLength())
       #鉴于数据庞大，暂时不做分页 pages

    #提取详情页数据 ,m是指水果类型
    def get_data(self, content, startNum,m):
        soup = BeautifulSoup(content, 'html.parser')
        #找第一个title
        #title = soup.find("title")
        title = soup.title
        _title = title.string[0:title.string.find("-")]
        #产地，城市 如果没有城市，就匹配产地，都没有默认中国大陆其格式为 &#20013;&#22269;&#22823;&#38470;
        city = soup.find(text = re.compile("城市"))
        provience = soup.find(text=re.compile("省份"))
        chandi = soup.find(text = re.compile("产地"))
        fruit_name = ''
        if city is None or provience is None or chandi is None:
            fruit_place = '中国大陆'
            fruit_name = "中国"+ str(m)
        elif city is None and provience is None:
            fruit_place = 'f' + chandi[chandi.find(':')+2:]
            fruit_name = chandi[chandi.find(':')+2:] + str(m)
        elif city is not None or provience is not None:
            fruit_place = provience[provience.find(':')+2:] + city[city.find(':')+2:]
            fruit_name = city[city.find(':')+2:] + str(m)
        if fruit_name.find("/") > 0 :
            fruit_name = fruit_name.split("/")[0]
        # 售价
        fruit_sellprice = round(random.uniform(40, 80), 2)
        # 原价
        fruit_price = round(random.uniform(fruit_sellprice, 80), 2)
        #进价
        fruit_enterprice = round(random.uniform(40, fruit_sellprice), 2)
        #图片名
        fruit_images = startNum
        #库存数量
        fruit_amount  = 100
        #上架状态
        fruit_states = 0
        #描述信息
        fruit_info = _title
        #保鲜时间
        fruit_date = 180
        #上架时间（现在为准）
        now = datetime.datetime.now()
        fruit_time = now.strftime('%Y-%m-%d %H:%M')
        #置顶
        istop = 0
        #水果类别
        fruit_type = m
        #添加人
        addman = '爬虫抓取'
        #获取图片地址
        picDiv = soup.find(class_="tb-thumb-content")
        links = picDiv.find_all("img")
        piccount= 1
        #10057开始 图片存储
        for link in links:
            name = str(startNum) + "_ (" + str(piccount) + ").png"
            print('图片名.......', name)
            #要转化一下为.jpg_430x430q90.jpg的后缀的图片，才能得到高清图
            temp = 'http:'+ link['src']
            targetpicurl = temp[0:temp.find('jpg')]+'jpg_430x430q90.jpg'
            print(targetpicurl)
            flag = self.copypic(targetpicurl, name)
            #flag ==1 为图片复制成功 0 为成功
            if flag == 1:
                piccount = piccount+1
        # 图片数量
        fruit_imgcount = piccount-1
        #使用execl保存表格数据
        rexcel = open_workbook("fruit.xls")  # 用wlrd提供的方法读取一个excel文件
        rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
        excel = copy(rexcel)  #用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
        values = [startNum, fruit_name, fruit_sellprice, fruit_price,fruit_place,
                   startNum, piccount, fruit_amount,fruit_states,
                  _title, fruit_date,fruit_time, istop, fruit_type, fruit_enterprice, addman]
        row = rows
        num = 0
        for value in values:
            table.write(row, num, value)  # xlwt对象的写方法，参数分别是行、列、值
            num = num + 1
        excel.save("fruit.xls")

    def copypic(self, _str, pic_name):
        path = "D:\\ImprotantPictures\\images"
        count = 1
        flag = 0
        if _str is not None:
            absoultpath = path + '\\' + pic_name
            while count < 3 and flag == 0:
                try:
                    # 此网页的图片有的加载不出来，就不将失败的的图片放进fail_urls容器去
                    # 这种方法容易报错403 服务器拒绝处理 request.urlretrieve(_str, absoultpath)
                    res = requests.get(_str, timeout=4)
                    with open(absoultpath, 'wb') as f:
                        f.write(res.content)
                    flag = 1
                except:
                    flag = 0
                count = count + 1
        return flag




