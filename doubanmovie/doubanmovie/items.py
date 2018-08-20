# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ranking = scrapy.Field()        # 排名
    title = scrapy.Field()      # 电影名字
    eng_title = scrapy.Field()      # 英文名
    act_role = scrapy.Field()       # 主演
    rating_num = scrapy.Field()     # 评分
    evaluation_num = scrapy.Field()     # 评价人数
    quote = scrapy.Field()      # 条目
    movie_link = scrapy.Field()     # 电影链接

