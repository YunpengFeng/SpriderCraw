#url管理器
class UrlManager(object):
    def __init__(self):
        #新的管理器和旧的管理器
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self, root_url):
        #1 判断是否为空，也都不在新老管理器中 ，则增加到新的url管理器中
        if self.new_urls is None:
            return
        if root_url not in self.new_urls  and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    #要控制从外部页面获取的链接数据，当new_urls超过N时不再新增
    def add_new_urls(self, newurls):
        if newurls is None or len(newurls) == 0:
            return
        for url in newurls:
            if url is not None or len(url) > 0:
                self.new_urls.add(url)


    def has_new_url(self):
        if self.new_urls is None or  len(self.new_urls) == 0:
            return False
        if len(self.new_urls) > 0:
            return True
    #从新的url管理器取出一个url，旧的url管理器则插入这个查询的
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def getLength(self):
        return len(self.new_urls),len(self.old_urls)

