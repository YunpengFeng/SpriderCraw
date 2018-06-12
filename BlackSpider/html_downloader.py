from urllib import request
#页面下载器
class HtmlDownloader(object):
    #下载网页源代码 ，而不是审查元素的内容  网页下载超过3次跳出
    def downloader_html(self, new_url):
        flag =0
        content = ''
        count = 1
        while flag == 0 and count <4:
            if new_url is None:
                return None
            try:
                response = request.urlopen(url=new_url,timeout=10)
                code = response.getcode()
                if code != 200:
                    flag =0
                    count = count + 1
                else:
                    content = response.read()
                    flag = 1
            except:
                print("下载网页超时了")
                flag = 0
                count = count + 1
        return content

