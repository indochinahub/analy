# -*- coding: utf-8 -*-
import scrapy
import codecs

result_file = codecs.open('result.txt', mode='w',  encoding="utf-8")

class RfaSpider(scrapy.Spider):
    name = 'rfa'
    
    allowed_domains = ['rfa.org']
    start_urls = ['https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=hell-on-wheels']
    #allowed_domains = ['toscrape.com']
    #start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        seasons = response.css("div.season-episodes")
        for season in seasons :
            season_name = season.css("h3::text").extract_first()
            for  episode in season.css("a")  :
                episode_name = episode.css("a::text").extract_first()    
                episode_link  =  "https://www.springfieldspringfield.co.uk/" + episode.css("a::attr(href)").extract_first()
                result_file.write( episode_link + " \n" )