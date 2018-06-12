from Spider import url_manager, html_downloader, html_parser, html_outputer

import time
class SpiderMain():
     #初始化对象
    def __init__(self):
        #url管理器
        self.urls = url_manager.UrlManager()
        #html页面下载器
        self.downloader = html_downloader.HtmlDownloader()
        #适配器
        self.parser  = html_parser.HtmlParser()
        # 输出器
        self .outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        #增加一个url
        self.urls.add_new_url(root_url)
        #判断url管理器是否有新的url
        count = 1
        while self.urls.has_new_url():
                #取出新的url
                new_url = self.urls.get_new_url()
                #根据url 下载页面html
                print("new_url=",new_url,'***************count=',count)
                html_content = self.downloader.downloader_html(new_url)
                #根据html匹配要取的链接和数据
                new_urls, new_data_path = self.parser.parse_datas(new_url,html_content)
                #将收集的数据和链接放到url 管理器中
                self.urls.add_new_urls(new_urls)

                # 将一些数据展示在页面上
                if (len(new_data_path) == 0):
                    print("猜的获取的ajax失败")
                self.outputer.output_path(new_data_path)
                time.sleep(5)
                print('..........................................太累了，休息5秒....................................','new_urls里的数量 ，old_urls的数量',self.urls.getLength())
                #超过一千个跳出
                if count > 20:
                    break
                count = count + 1


#申明主函数
if  __name__ == "__main__":
    start = time.time()
    root_url ="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1523715973433_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E5%9F%8E%E5%B8%82%E7%BE%8E%E5%A5%B3"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    end = time.time()
    print('一共耗费的时间.............', end - start)