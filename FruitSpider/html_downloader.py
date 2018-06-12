from urllib import request
import requests

# 页面下载器
class HtmlDownloader(object):

    # 下载网页源代码 ，而不是审查元素的内容  网页下载超过3次跳出
    def downloader_html(self, new_url):
        flag = 0
        content = ''
        count = 1
        while flag == 0 and count <4:
            if new_url is None:
                return None
            try:
               # tcookie = 'tk_trace=1; cna=fm10EzmWJEECAT2EOzIdBTnM; t=daf24a7611a81a201847a1800772baf5; _tb_token_=db8731fe7ee3; cookie2=1fd7d95b3a47a8ddbd8619152d0225cf; hng=""; cq=ccp%3D0; _m_h5_tk=64580eeed7f3bab7b0638750b5012ac3_1525681001738; _m_h5_tk_enc=ba64e0200c757c73b158b7ba6cafc83c; enc=QiNIfnFnZ3qM7Rk%2Bq1D1jO7khOjIT2cdfWQCp6GI5qeWDzLHgvQgshRDbIV89N0xEXHCyplVq%2BBUwSRhnsPrcA%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; whl=-1%260%260%260; isg=BP7-BPbkKFmAV3xiNW3ToAySTxRKNcnqxpqNt6gHdcE8S54lEM8SySQhxxeH87rR; uc1=cookie14=UoTeO8touBobNw%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; uc3=nk2=qBSx3uCh%2FsZMOg%3D%3D&id2=UUtJZ%2BqLGLwgPg%3D%3D&vt3=F8dBz44lKrypJzAufy4%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu601D%5Cu60F3%5Cu9053%5Cu5FB7%5Cu89C2; _l_g_=Ug%3D%3D; ck1=""; unb=2320132161; lgc=%5Cu601D%5Cu60F3%5Cu9053%5Cu5FB7%5Cu89C2; cookie1=W5iQAkAh48S0kVH%2BD3XgirUEZs4%2Fx37H3avqjW9j8Rk%3D; login=true; cookie17=UUtJZ%2BqLGLwgPg%3D%3D; _nk_=%5Cu601D%5Cu60F3%5Cu9053%5Cu5FB7%5Cu89C2; uss=""; csg=3a6c2f1c; skt=480dff4e7b8805ce'
                head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
                response = requests.get(new_url, headers=head)
                code = response.status_code
                if code != 200:
                    flag =0
                    count = count + 1
                else:
                    content = response.text
                    flag = 1
            except:
                print("下载网页超时了")
                flag = 0
                count = count + 1
        return content

