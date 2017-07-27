'''
Created on Jun 5, 2017
@author: ZHUXIN
Version: Python3.6.1
以Python词条为入口,爬取百度百科相关词条并输出为html文件。
'''

from baike_spider import url_mannager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer

class SpiderMain(object):

    # 构造函数，初始化url管理器、下载器、解析器、输出器
    def __init__(self):
        self.urls = url_mannager.URLMannager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    # 爬取流程
    def crawl(self, root_url):
        count = 1                                                           # 记录当前url的序号
        self.urls.add_new_url(root_url)                                     # 首先把入口url添加进url管理器
        while self.urls.has_new_url():                                      # 启动爬虫循环, 当url管理器中有待爬取的url时:
            try:
                new_url = self.urls.get_new_url()                           # 获取一条新的待爬取url
                print('crawl %d: %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)               # 启动下载器下载页面,存储在html_content中
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 调用解析器解析页面数据,得到新的页面列表及新的数据

                # 分别处理new_urls和new_data
                self.urls.add_new_urls(new_urls)                            # 把url列表添加进url管理器
                self.outputer.collect_data(new_data)                        # 收集数据

                # 本程序目标是爬取100条数据
                if count == 100:
                    break

                count += 1
            except:
                print('craw faild')

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
    print('执行结束')