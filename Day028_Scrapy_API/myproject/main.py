import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main(target_urls,filename):
    # target_urls = [
    #     'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
    #     'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html',
    #     'https://www.ptt.cc/bbs/Beauty/M.1586229998.A.C47.html'
    # ]
    
    
    process = CrawlerProcess(get_project_settings())
    # process.crawl('PTTCrawler', start_urls=target_urls, filename='test.json')
    process.crawl('PTTCrawler', start_urls=target_urls, filename=filename)
    process.start()

if __name__ == '__main__':
    
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html',
        'https://www.ptt.cc/bbs/Beauty/M.1586229998.A.C47.html'
    ]
    filename='test123.json'
    main(target_urls,filename)
