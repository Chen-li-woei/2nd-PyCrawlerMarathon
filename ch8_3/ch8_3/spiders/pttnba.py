# -*- coding: utf-8 -*-
# import scrapy


# class PttnbaSpider(scrapy.Spider):
#     name = 'pttnba'
#     allowed_domains = ['ptt.cc']
#     start_urls = ['https://www.ptt.cc/bbs/joke/index.html']
#     # scrapy.Request('https://www.ptt.cc/bbs/joke/index.html', cookies={'over18': '1'})
    
#     def parse(self, response):
#         # self.logger.info('A response from %s just arrived!', response.url)
        
        
#         # titles = response.css("div.r-ent > div.title > a::text").extract()
#         # votes = response.xpath('//div[@class="nrec"]/span/text()').extract()
#         # authors = response.xpath('//div[@class="meta"]/div[1]/text()').extract()
#         # for item in zip(titles,votes,authors):
#         #     scraped_info = {
#         #         "title" : item[0],
#         #         "vote"  : item[1],
#         #         "author": itme[2]                
#         #     }
#         #     yield scraped_info
#         # pass




import scrapy
from scrapy.exceptions import CloseSpider

class PttnbaSpider(scrapy.Spider):
    count_page = 1
    name = 'pttnba'
    allowed_domains = ['www.ptt.cc/']
    start_urls = ['https://www.ptt.cc/bbs/movie/index.html']
    def parse(self, response):
        for q in response.css('div.r-ent'):
            item = {
                'push':q.css('div.nrec > span.hl::text').extract_first(),
                'title':q.css('div.title > a::text').extract_first(),
                'href':q.css('div.title > a::attr(href)').extract_first(),
                'date':q.css('div.meta > div.date ::text').extract_first(),
                'author':q.css('div.meta > div.author ::text').extract_first(),
            }
            yield(item)
        next_page_url = response.css('div.action-bar > div.btn-group > a.btn::attr(href)')[3].extract()
        if (next_page_url) and (self.count_page < 10):
            self.count_page = self.count_page + 1 
            new = response.urljoin(next_page_url) 
        else:   
            raise  CloseSpider('close it')
        yield scrapy.Request(new, callback = self.parse, dont_filter = True)














