import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_board = ['Gossiping', 'Stock']
    # target_board = ['Stock']
    process = CrawlerProcess(get_project_settings())
    
    # process.crawl('PTTCrawler', target_board)
    # process.start()
    
    
    for board in target_board:
        process.crawl('PTTCrawler', board=board)
    process.start()

if __name__ == '__main__':
    main()
