# -*- coding: utf-8 -*-
import scrapy
import codecs

result_file = codecs.open('result.txt', mode='w',  encoding="utf-8")

class RfaSpider(scrapy.Spider):
    name = 'rfa'
    
    allowed_domains = ['rfa.org']
    start_urls = ['https://www.rfa.org/khmer/news/history/story_archive?b_start:int=60']
    #allowed_domains = ['toscrape.com']
    #start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        stories = response.css("div.sectionteaser")
        for story in stories :
            result_file.write( story.css("h2 span::text").extract()[0] + '\t' + story.css("a::attr(href)").extract()[0]+ '\n' )

