# -*- coding: utf-8 -*-
import scrapy


class VietjackSpider(scrapy.Spider):
    name = 'vietjack'
    allowed_domains = ['vietjack.com']
    start_urls = ['https://vietjack.com/ngu-phap-tieng-anh/index.jsp']

    def parse(self, response):
        for url in response.css("ul.list a::attr(href)") :
            link = url.extract()
            link = 'https://vietjack.com/' + link.replace("../", "")
            yield scrapy.Request(url=link, callback=self.parse_detail)
            
    def parse_detail(self, response):
        self.log("I just visited :: " + response.url )
        i = 0
        for text in response.css('pre.prettyprint::text') :
            text = text.extract()
            text = response.url + text 
            items = {
                'something'  : text
            }
            
            yield items            