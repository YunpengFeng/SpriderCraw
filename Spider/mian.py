import  test
import socket
import time
from urllib import request
from bs4 import BeautifulSoup
from urllib import parse
import urllib
from urllib.parse import urljoin
import re
from urllib import request
import sys

'''
start = time.time()
socket.setdefaulttimeout(6)
urll ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=270&rn=30&gsm=10e&1523530175597='
url2 ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=90&rn=30&gsm=5a&1523530003288='
url4 ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=120&rn=30&gsm=78&1523530005293='
url5 ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=150&rn=30&gsm=96&1523530172060='
url6 ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=180&rn=30&gsm=b4&1523530172942='
url7 ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=210&rn=30&gsm=d2&1523530173906='
url8 ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=240&rn=30&gsm=f0&1523530175051='
urls = {urll,url2,url4,url5,url6,url7,url8}
fail_url,count = test.copy_data(urls)
print('......图片复制成功个数..', count)
#失败也要复制不断的复制
test.copy_fail(fail_url)
end = time.time()
print ('一共耗费的时间.............',end-start)
'''


#----------------------动态加载一组数据--------------------------------
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # 引入keys类操作
import time
import os
from selenium import webdriver

class SpiderMain():
    def __init__(self):
        pass
    def oparetion_chrome(self):
        root_url = "https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs2&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&oriquery=%E5%86%9C%E6%9D%91%E7%9C%9F%E5%AE%9E%E7%BE%8E%E5%A5%B3&ofr=%E5%86%9C%E6%9D%91%E7%9C%9F%E5%AE%9E%E7%BE%8E%E5%A5%B3&hs=2&sensitive=0"
        #path ='C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\chromedriver.exe'
        # browser = webdriver.Chrome(path)
        #browser.get(root_url)
        # browser.save_screenshot("F:\\CopyPictrue\\screen.png")
        #js = "window.scrollBy(0,900)"
        #browser.find_element_by_id('imgContainer').save_screenshot("F:\\CopyPictrue\\screen4.png")
        '''
        import requests
        r = requests.get(root_url)
        r.encoding('gbk')
        print(r.text)
        '''

        urls = ([
                'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%86%9C%E6%9D%91%E6%80%A7%E6%84%9F%E5%B0%91%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn={a}&rn=30&gsm=b4&1523637279263='.format(a=i) for i in range(0,300) if i % 30 == 0])
        for url in urls :
                print(url)
        #print(browser.page_source)
        '''
        js = 'alert("打印成功")'
        browser.execute_script(js)
        
        print('begin scroll to get info page...')
        t1 = time.time()
        n = 60  # 这里可以控制网页滚动距离
        for i in range(1, n + 1):
            s = "window.scrollTo(0,document.body.scrollHeight/{0}*{1});".format(n, i)
           # 输出滚动位置，网页大小，和时间
            print(s, len(browser.page_source), time.time() - t1)
            browser.execute_script(s,None)
            '''


if  __name__ == "__main__":

    obj_spider = SpiderMain()
    obj_spider.oparetion_chrome()
    #obj_spider.oparetion_chrome()
'''
js = "window.scrollBy(0,900)"
browser.find_element_by_id('kw').send_keys('冯云鹏')
print(".....................1")
browser.execute_script(js)
print(".....................")
time.sleep(4)
js1 = "window.scrollBy(0,900)"
browser.execute_script(js1)

i= 0
while True:
    js = "window.scrollTop(0,"+str(800+i*200)+")"
    print(js)
    try:
        browser.execute_script(js)
        time.sleep(4000)
        print("下拉一次")
    except:
        print("挂掉了...................")
    if(i>10):
        break
    i = i+1
'''

