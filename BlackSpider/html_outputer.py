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
import requests

from BlackSpider import html_downloader

class HtmlOutputer(object):
    def __init__(self):
        # html页面下载器
        self.downloader = html_downloader.HtmlDownloader()
        self.map = {"index16": '亚洲性图', "index17": '网友自拍', 'index18': '欧美色图',
               'index19': '丰乳肥臀', 'index20': '国产模特', "index21": "唯美清纯",
               "index22": "丝袜诱惑", 'index23': '卡通漫画'}
    #param 表示类型
    def dealwith(self, big_content, sourceurl, param):
        fail_urls = set()
        path = "F:\\CopyWebInfo\\picture"
        secondpath = path + "\\" + self.map[sourceurl[-12:-5]]
        self.creatFile(secondpath)
        while len(big_content) > 0:
            url = big_content.pop()
            content = self.downloader.downloader_html(url)
            if(content == None):
                big_content.add(url)
                continue
            else:
                soup = BeautifulSoup(content,'html.parser')
                #获取图片的地址
                list = soup.find_all("img")
                img_urls = set()
                for li in list:
                    img_urls.add(li.attrs['src'])
                #img_urls =[li.attrs['src'] for li in list]
                #获取信息
                name =soup.find(class_= 'page_title')
                targetpath = secondpath+"\\"+str(name).split(">")[1].split("<")[0]
                self.creatFile(targetpath)
                # 复制图片
                fail_urls ,count =self.copy_images(img_urls, targetpath)
                print("复制图片成功",count,"张")
                self.copy_fail(fail_urls,targetpath)


        # 复制一张图片到本地 param urls（列表）  是ajax 的url地址   return fail_url（）失败的set，success_count（）成功个数
    def copy_images(self, urls, path):
        fail_urls = set()
        count = 0
        #for url in urls:
        while len(urls)>0:
            url = urls.pop()
            _str, flag =self.copy_pic(url,path)
            if flag ==1:
                count = count + 1
            # else:
            #     fail_urls.add(url)
        #print("复制失败的图片张数",len(fail_urls))
        #如果是空文件夹，删除本文件夹
        self.delete_None_files(path)
        return fail_urls, count

    # 复制一张图片到本地,请求三次，三次没有回应则不再请求 param _str链接地址   return fail_url（）失败的set，success_count（）成功个数 path 是父路径
    def copy_pic(self, _str, path):
        count =1
        flag = 0
        if _str is not None:
                pic_name = str(_str).split("/")[-1]
                absoultpath = path + '\\' + pic_name
                while count <3 and flag ==0:
                    try:
                       #此网页的图片有的加载不出来，就不将失败的的图片放进fail_urls容器去
                       #这种方法容易报错403 服务器拒绝处理 request.urlretrieve(_str, absoultpath)
                       res = requests.get(_str,timeout=4)
                       with open(absoultpath + _str[-10:], 'wb') as f:
                           f.write(res.content)
                       flag = 1
                    except:
                        flag = 1
                    count=count+1
            #else:
                #return None, 0
        return None, 1

    # 失败的继续循环复制 param set()  return None  要避免陷入死循环
    def copy_fail(self, fail_url, path):
        while len(fail_url) > 0:
            link = fail_url.pop()
            small_fail_url, success_count = self.copy_pic(link, path)
            if success_count == 0:
                fail_url.add(small_fail_url)
                success_count = 0
        return


    # 创建文件夹
    def creatFile(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        if os.path.exists(path) is False:
            os.makedirs(path)
        return True

    def delete_None_files(self,path):
        files = os.listdir(path)  # 获取路径下的子文件(夹)列表
        if len(files) == 0:
            os.rmdir(path)
            print(path, '空文件夹删除成功.......Dispose over!')
        # for file in files:
        #     if os.path.isdir(file):  # 如果是文件夹
        #         if not os.listdir(file):  # 如果子文件为空
        #             os.rmdir(file)  # 删除这个空文件夹
        #             print(path, '空文件夹删除成功.......Dispose over!')
        #     elif os.path.isfile(file):  # 如果是文件
        #         if os.path.getsize(file) == 0:  # 文件大小为0
        #             os.remove(file)  # 删除这个文件
        #             print(path, '空文件夹删除成功.......Dispose over!')
