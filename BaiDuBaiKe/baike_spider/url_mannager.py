# url管理器

class URLMannager(object):

    def __init__(self):

        self.new_urls = set()   # 待爬取的url列表
        self.old_urls = set()   # 爬取过的url列表

    # 添加单个待爬取url
    def add_new_url(self, url):

        if url is None:
            return

        # 新旧url列表中都没有这个url则添加进待爬取列表
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加待爬取url
    def add_new_urls(self, urls):

        if urls is None or len(urls) == 0:
            return

        # 调用添加单个url的方法进行逐个添加
        for url in urls:
            self.add_new_url(url)

    # 判断列表中是否有待爬取的url
    def has_new_url(self):

        return len(self.new_urls) != 0

    # 获取一个待爬取的url
    def get_new_url(self):

        # 从列表中获取一个待爬取的url,并将其从待爬取列表中移除
        new_url = self.new_urls.pop()

        # 添加进已爬取列表中
        self.old_urls.add(new_url)

        return new_url

