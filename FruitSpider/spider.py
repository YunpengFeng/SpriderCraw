import time

from FruitSpider import parse_index_url, url_manager, html_downloader, html_parsers


class FruitSpider(object):

    def __init__(self):
        self.index_url = parse_index_url.InItazier()

    def startSpider(self):
        indexUrl = self.index_url.initurlmap()
        i = 0
        for m in indexUrl:
            print('\n.....................爬取水果的种类是:', m, '...............')
            typeurl = indexUrl[m]
            hparser = html_parsers.HtmlParser(typeurl,i)
            hparser.get_all_list(m)
            i = i+1

if __name__  == "__main__":
    starttime = time.time()
    fspider = FruitSpider()
    fspider.startSpider()
    print("一共消耗的时间是：",  time.time()-starttime)