class HtmlOutputer(object):
    def output_path(self, new_data):
        i = 0
        print('.......................ajax路径图片路径展示.....................................')
        for url in new_data:
            print(url,end='\n')

        print('..........................展示完毕......................................')
