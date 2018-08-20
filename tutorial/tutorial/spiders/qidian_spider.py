"""Spider是用户编写用于从单个网站或一些网站爬取数据的类；
构建完字段后，编写爬虫(爬取起点网排行榜完本榜总榜的500本小说)"""
# coding:utf-8


import scrapy
import re
from ..items import QidianItem


class Qidianspider(scrapy.Spider):
    """抓取数据"""

    # 这个name就是entrypoint中的第三个参数，此name的名字在整个项目中有且只有一个，不可重复！
    name = 'qidian'
    # 设置allowed_domains的含义是过滤爬取的域名，它只会跟进存在于allowed_domains中的URL，不存在的url会被忽略：
    allowed_domains = ['qidian.com']
    # 包含了spider在启动时进行爬取的url列表：
    start_urls = ['https://www.qidian.com/rank/fin?style=1&dateType=3']
    n = 1   # 第一页

    def parse(self, response):
        """调用该函数，每个初始url完成下载后生产的response对象会作为唯一的参数传递给该函数
        该方法负责解析返回的数据（response data），提取数据以及生成需要进一步处理的url的request对象"""

        # 进行页面分析，可以利用XPath或者css提取数据(选择该页面中所有包含该XPath的元素)：
        sel = response.xpath('//*[@class="book-mid-info"]')
        for i in sel:
            # 拼接XPath来进一步获取某些节点：
            name = i.xpath('./h4/a/text()').extract_first()      # 获取小说名字
            author = i.xpath('./p[@class="author"]/a[1]/text()').extract_first()
            category = i.xpath('./p[@class="author"]/a[last()]/text()').extract_first()
            item = QidianItem()
            item['name'] = name
            item['author'] = author
            item['category'] = category
            yield item

        if self.n < 25:
            self.n += 1     # n表示页码
            next_url = 'https://www.qidian.com/rank/fin?style=1&dateType=3&page=%d' % self.n
            yield scrapy.Request(next_url)


# name://*[@id="rank-view-list"]/div/ul/li[1]/div[2]/h4/a
# author://*[@id="rank-view-list"]/div/ul/li[2]/div[2]/p[1]/a[1]
# category://*[@id="rank-view-list"]/div/ul/li[1]/div[2]/p[1]/a[2]




































