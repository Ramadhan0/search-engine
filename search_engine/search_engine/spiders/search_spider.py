import scrapy
# from io import StringIO
# from functools import partial
# from scrapy.http import Request
# from scrapy.spiders import BaseSpider
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.item import Item


class SearchSpider(CrawlSpider):
    name = "search"

    # allowed_domains = [
    #     'https://bk.rw/',
    #     'https://rwanda.accessbankplc.com/',
    #     'https://www.ecobank.com/'
    # ]

    print('============================================')
    start_urls = [
        'https://bk.rw/',
        # 'https://rwanda.accessbankplc.com/',
        # 'https://www.ecobank.com/rw/personal-banking/countries'
    ]
    # rules = [Rule(LinkExtractor(), follow=True, callback="search_word")]

    # crawl_count = 0
    # words_found = 0

    print('============================================')

    def search_word(self, response):

        # self.__class__.crawl_count += 1
        # crawl_count = self.__class__.crawl_count

        wordlist = [
            'loan',
            # 'money transfer'
        ]

        url = response.url
        print('============', url)
        contenttype = response.headers.get(
            'content_type', '').decode('utf-8').lower()
        data = response.body.decode('utf-8')

        # print(data)

        for word in wordlist:
            substrings = find_all_substrings(data, word)
            for pos in substrings:
                ok = False
                if not ok:
                    self.__class__.words_found += 1
                    print(word + ";" + url + ";")
        print('=======================================')
        print(Item())
        print('=======================================')
        return Item()
