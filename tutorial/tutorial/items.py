# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class QidianItem(scrapy.Item):
    """创建Item类，定义自己要抓取的数据，前一个相当于键，爬到的数据相当于字典中的值，比如爬取小说站点"""

    name = scrapy.Field()       # 小说的名字
    author = scrapy.Field()
    category = scrapy.Field()       # 文章类别




