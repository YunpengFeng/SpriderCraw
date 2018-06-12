from urllib import request
#页面下载器
class HtmlDownloader(object):
    #下载网页源代码 ，而不是审查元素的内容
    def downloader_html(self, new_url):
        if new_url is None:
            return None
        response = request.urlopen(new_url)
        code = response.getcode()
        if code != 200:
            return None
        return response.read().decode()

