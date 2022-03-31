from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging

logger = logging.getLogger(__name__)


class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'
    rules = [Rule(LinkExtractor(allow='catalogue/'),
                  process_links='filter_links',
                  callback='parse_filter_book', follow=True)]

    def filter_links(self, input_links):
        for link in input_links:
            if '/category/' in link.url:
                yield link

    def parse_filter_book(self, response):
        yield {'url': response.url}
