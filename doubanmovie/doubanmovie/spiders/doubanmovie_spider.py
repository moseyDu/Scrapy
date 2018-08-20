"""爬取豆瓣电影top250"""
# coding:utf-8


import scrapy
from ..items import DoubanmovieItem


class Doubanspider(scrapy.Spider):
    """抓取豆瓣数据"""

    name = 'doubanmovie'
    # 因为产生了403拒绝，所以要添加请求头：
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '53.0.2785.143 Safari/537.36', }
    allowed_domains = ['douban.com']
    n = 1

    def start_requests(self):
        url = 'https://movie.douban.com/top250?start=0&filter='
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        """分析数据"""
        # print(response.text)

        # 打印一条记录：
        # sel = response.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div')
        # for i in sel:
        #     ranking = i.xpath('./div[1]/em/text()').extract_first()
        #     title = i.xpath('./div[2]/div[1]/a/span[1]/text()').extract_first()
        #     eng_title = i.xpath('./div[2]/div[1]/a/span[2]').extract_first()
        #     act_role = i.xpath('./div[2]/div[2]/p[1]/text()').extract_first()
        #     rating_num = i.xpath('./div[2]/div[2]/div/span[2]/text()').extract_first()       # 评分
        #     evaluation_num = i.xpath('./div[2]/div[2]/div/span[4]/text()').extract_first()       # 评价人数
        #     quote = i.xpath('./div[2]/div[2]/p[2]/span/text()').extract_first()          # 条目
        #     movie_link = i.xpath('./div[1]/a/@href').extract_first()

        # 打印top250的所有记录：
        sel = response.xpath('//*[@class="item"]')
        for i in sel:
            ranking = i.xpath('./div[@class="pic"]/em/text()').extract_first()
            title = i.xpath('./div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract_first()
            eng_title = i.xpath('./div[@class="info"]/div[@class="hd"]/a/span[2]/text()').extract_first()
            act_role = i.xpath('./div[@class="info"]/div[@class="bd"]/p[1]/text()').extract_first()
            rating_num = i.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract_first()
            evaluation_num = i.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract_first()
            quote = i.xpath('./div[@class="info"]/div[@class="bd"]/p[2]/span/text()').extract_first()
            movie_link = i.xpath('./div[@class="pic"]/a/@href').extract_first()

            item = DoubanmovieItem()
            item['ranking'] = ranking
            item['title'] = title
            item['eng_title'] = eng_title
            item['act_role'] = act_role
            item['rating_num'] = rating_num
            item['evaluation_num'] = evaluation_num
            item['quote'] = quote
            item['movie_link'] = movie_link

            yield item

        if self.n < 10:
            self.n += 1
            start = str(self.n * 25 - 25)
            next_page_url = 'https://movie.douban.com/top250?start=' + start + '&filter='
            yield scrapy.Request(next_page_url, headers=self.headers)





























