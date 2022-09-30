import scrapy
import time
from scrapy.selector import Selector

class ZakvSpider(scrapy.Spider):
    cnt = 1
    name = 'ZakvSpider'
    start_urls = ['https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/']

    def parse(self, response):
        if self.cnt != 3:
            links = response.css('div.product-thumb a::attr(href)')
            for link in links:
                time.sleep(1)
                yield response.follow(link, self.parse_book)
                
            self.cnt += 1
            link = f'https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/?page={self.cnt}'
            yield response.follow(link)
        return 'Готово'



    def parse_book(self, response):
        yield {
            'name': response.css('div.col-sm-6 h1::text').get(),
            'price': response.css('span.autocalc-product-price::text').get(),
            'availability': response.css('b.outstock::text').get()
        }

