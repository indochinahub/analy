import scrapy
import codecs
import time

result_file = codecs.open('result.txt', mode='w' )
link_file  = open('link.txt', mode='r')


class QuotesSpider(scrapy.Spider):
    name = "hell_on_wheel"

    def start_requests(self) :
         urls = [ 'https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=hell-on-wheels&episode=s01e01'] 
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        texts =  response.css("div.scrolling-script-container::text")
        for text in texts :
            result_file.write(  text.extract()  + " \n")
