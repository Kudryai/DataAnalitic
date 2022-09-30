import scrapy
import time
from scrapy.selector import Selector

class GiftsSpider(scrapy.Spider):
    cnt = 1
    name = 'GiftsSpider'
    start_urls = ['https://siberia.eco/gotovye-podarki/']

    def parse(self, response):
        if self.cnt != 3:
            links = response.css('div.card-borders a::attr(href)')
            for link in links:
                time.sleep(1)
                yield response.follow(link, self.parse_book)
                



    def parse_book(self, response):
        yield {
            'name': response.css('h1.global-header__title::text').get(),
            'price': response.css('span.s-price::text').get(),
            'structure': response.css('div.s-product-desc a::text').getall()
        }

