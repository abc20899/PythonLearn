# -*- coding: utf-8 -*-
import re
import scrapy

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['python.jobbole.com']
    # start_urls = ['http://python.jobbole.com/']
    start_urls = ['http://python.jobbole.com/89012/']

    def parse(self, response):
        # chrome中提取的xpath //*[@id="post-89012"]/div[1]/h1
        # id = post-89012  动态获取
        # //div[@class='entry-header']/h1/text()
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        create_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0] \
            .strip().replace('·', "").strip()
        prize_num = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        collect_text = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        collect_nums = re.match('.*(\d+).*', collect_text)
        if collect_nums:
            collect_num = collect_nums.group(1)
            print(collect_num)
        comment_text = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        comment_nums = re.match('.*(\d+).*', comment_text)
        if comment_nums:
            comment_num = comment_nums
            print(comment_num)
        content = response.xpath('//div[@class="entry"]').extract()[0]
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        print(tag_list) #['实践项目', 'tensorflow', '图计算', '机器学习', '深度学习', '神经网络']
