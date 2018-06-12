from BlackSpider import url_manager, html_downloader, html_parser, html_outputer

import time


class SpiderMain:
     #初始化对象
    def __init__(self):
        #url管理器 分别是图片，文章，视频，总数管理器
        self.Picurls = url_manager.UrlManager()
        self.Arturls = url_manager.UrlManager()
        self.Videourls = url_manager.UrlManager()
        #html页面下载器
        self.downloader = html_downloader.HtmlDownloader()
        #适配器
        self.parser  = html_parser.HtmlParser()
        # 数据处理器
        self.outputer = html_outputer.HtmlOutputer()

    def initUrl(self):
        self.Picurls.add_new_urls(['http://www.80sbs.com/html/part/index{0}.html'.format(i) for i in range(17, 23, 1)])
        #self.Arturls.add_new_urls(['http://www.80sbs.com/html/part/index{0}.html'.format(i) for i in range(24, 32)])
        #self.Videourls.add_new_urls(['http://www.80sbs.com/list/index{0}.html'.format(i) for i in range(1, 9)])

    def craw(self):
        #判断图片url管理器是否有新的url
        print("..............", self.Picurls.getLength())
        while self.Picurls.has_new_url():
                new_url = self.Picurls.get_new_url()
                #根据url 下载页面html
                html_content = self.downloader.downloader_html(new_url)
                #将所有的图片所有的条例都存起来
                big_content = self.parser.parse_datas('pic',new_url,html_content)
                #param   new_url原地址链接 "pic"表示文字
                self.outputer.dealwith(big_content,new_url,"pic")

                time.sleep(1)
                print('..........................................太累了，休息5秒....................................')



#申明主函数
if  __name__ == "__main__":
    start = time.time()
    root_url = 'http://www.80sbs.com'
    obj_spider = SpiderMain()
    obj_spider.initUrl()
    obj_spider.craw()
    print('一共耗费的时间.............', time.time() - start)