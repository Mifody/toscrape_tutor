import logging

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

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
        """
        :param input_links: list of Links object
        :return: list of Links object

        example one Link object
        00 = {Link} Link(
            url='http://books.toscrape.com/catalogue/category/books_1/index.html',
            text='\n                            \n                                Books\n                            \n                        ',
            fragment='',
            nofollow=False)

        You can modify, supplement, filter the result of the function.
        """
        for link in input_links:
            if '/category/' in link.url:
                yield link

    def parse_filter_book(self, response):
        yield {'url': response.url}
